import json, time, re, uuid, urllib.request, urllib.error, pathlib, subprocess
def load_env(p):
    d={}
    for line in open(p):
        if '=' in line: k,_,v=line.strip().partition('='); d[k.strip()]=v.strip()
    return d
GLM=load_env('/data/AI_Video/.secrets/AI_Doctor_Theater/glm.env')['BIGMODEL_API_KEY']
NT=load_env('/data/AI_Video/.secrets/AI_Doctor_Theater/notoken.env')
NTKEY,NTBASE=NT['NOTOKEN_API_KEY'],NT['NOTOKEN_BASE']
BASE=pathlib.Path('/data/AI_Video/AI_Doctor_Theater/data/persona')
DNA='a short-haired gray tabby cat with a chubby round face, gray and black tabby stripes on the head, back and sides, solid white chest, white muzzle and white paws, big round amber eyes with gentle sparkle, pink nose, wearing a crisp white doctor coat with a small blank white name badge clipped on the chest pocket, the badge is plain and completely empty, and a mint-green binaural stethoscope draped around the neck with earpiece tubes on one side and a single chest piece on the other side'
TEX='candid photo taken on a smartphone, slightly off-center framing, mixed indoor lighting with warm desk lamp and cool daylight window, harsh light falloff, visible sensor noise, slight chromatic aberration at frame edges, slightly missed focus on fur tips, realistic skin and fabric texture, wrinkled coat, imperfect fur clumps, authentic amateur snapshot, not retouched'
NEG='cartoon, 3d render, illustration, chibi drawing, long-haired cat, fluffy neck ruff, orange cat, ginger fur, calico, tan nose bridge, orange patch on face, skinny cat, kitten proportions, any text, watermark, garbled text, printed characters, Chinese characters, letters, numbers, handwriting, logo, pen, studio lighting, perfect symmetry, oversmoothed fur, plastic texture, airbrushed, flawless skin, professional retouching, two chest pieces, duplicated stethoscope heads, stethoscope on both sides, hard hat, safety vest, deformed paws, extra limbs, two cats'
SCENES={
 'd3_s1':'sitting at the wooden clinic desk holding a clipboard in one paw, looking at the camera, clipboard partially visible',
 'd3_s2':'standing on the desk beside a shelf of medical books, one paw raised pointing at an anatomy poster on the wall behind',
 'd3_s3':'close-up portrait from chest up, gentle relaxed expression, soft window light on the face',
}
# ---- A) D3 三场景 ----
for tag,sc in SCENES.items():
    body={'model':'cogview-4','prompt':f'{DNA}, {sc}, {TEX}. avoid: {NEG}','size':'1024x1024'}
    req=urllib.request.Request('https://open.bigmodel.cn/api/paas/v4/images/generations',
        data=json.dumps(body).encode(), headers={'Content-Type':'application/json','Authorization':f'Bearer {GLM}'})
    with urllib.request.urlopen(req,timeout=180) as r: j=json.loads(r.read())
    url=(j.get('data') or [{}])[0].get('url')
    with urllib.request.urlopen(url,timeout=120) as r: raw=r.read()
    (BASE/f'raw_{tag}.png').write_bytes(raw)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(BASE/f'raw_{tag}.png'),
                    '-vf','delogo=x=730:y=930:w=284:h=88',str(BASE/f'{tag}.png')],check=True)
    print(f'D3 {tag} OK', flush=True)
# ---- B) Seedance i2v 动态验证（official_persona） ----
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(BASE/'official_persona.png'),
                '-vf','scale=768:768','-q:v','7','/tmp/official_768.jpg'],check=True)
def nt(method,path,body=None,file=None):
    headers={'Authorization':f'Bearer {NTKEY}','Connection':'close'}; data=None
    if file is not None:
        b=uuid.uuid4().hex; headers['Content-Type']=f'multipart/form-data; boundary={b}'
        data=(f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="up.jpg"\r\nContent-Type: image/jpeg\r\n\r\n').encode()+file+f'\r\n--{b}--\r\n'.encode()
    elif body is not None:
        headers['Content-Type']='application/json'; data=json.dumps(body).encode()
    req=urllib.request.Request(f'{NTBASE}{path}',data=data,headers=headers,method=method)
    try:
        with urllib.request.urlopen(req,timeout=120) as r: return r.status,json.loads(r.read())
    except urllib.error.HTTPError as e: return e.code,json.loads(e.read() or b'{}')
c,j=nt('POST','/api/v3/files/uploads',file=open('/tmp/official_768.jpg','rb').read())
img_main=j.get('url'); print('i2v uploaded:',img_main is not None)
body={'model':'doubao-seedance-2.0-mini','duration':4,'ratio':'1:1','content':[
  {'type':'image_url','image_url':{'url':img_main}},
  {'type':'text','text':'画面中这只穿白大褂的灰虎斑猫医生保持原样：灰黑虎斑毛色与白色胸毛完全不变，胸前胸牌与薄荷绿听诊器形状保持，它坐在诊室桌前微笑看镜头，缓慢眨眼，头部轻微自然摆动，像被手机随手拍摄的真实猫，温暖室内光'}]}
c,j=nt('POST','/api/v3/contents/generations/tasks',body)
tid=j.get('id'); print('i2v task:',tid)
t0=time.time()
while time.time()-t0<360 and tid:
    time.sleep(15)
    c,k=nt('GET',f'/api/v3/contents/generations/tasks/{tid}')
    st=k.get('status','?')
    if st in ('succeeded','failed'):
        raw=json.dumps(k,ensure_ascii=False); print('i2v status:',st)
        if st=='succeeded':
            urls=re.findall(r'https?://[^"\']+?\.mp4[^"\']*',raw)
            if urls:
                with urllib.request.urlopen(urls[0],timeout=120) as r: vid=r.read()
                out=BASE/'official_i2v_test.mp4'; out.write_bytes(vid)
                print('i2v saved:',out,len(vid)//1024,'KB')
        break
print('ALL DONE')
