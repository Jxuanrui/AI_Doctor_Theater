#!/usr/bin/env python3
"""i2v_template.py — Seedance 图生视频调用模板（2026-10-09 依监工要求由一次性脚本精简为模板）

纪律（源自 docs/persona/persona-v5.md"视频生成纪律"，违反会重演字崩/眼色漂移）：
1. 输入图默认用空白牌底图 data/persona/official_persona_blank.png（**不要**用带"住院猫医"贴字的
   official_persona.png——i2v 会把中文在第 1 帧起崩成伪英文）；
2. 运动提示词自动追加锚定句（毛色/黄琥珀眼/空白胸牌/听诊器）——注意：锚定句不能阻止眼色漂移（E5 实证），S2 试点须做虹膜色相数值闸门；
3. DNA/负向以 persona-v5.md v8 官定锚点块为准，勿用旧版；
4. 密钥从 /data/AI_Video/.secrets/AI_Doctor_Theater/notoken.env 注入（本文件无硬编码密钥）；
5. 生成 URL 10 分钟过期，成功后立即下载。
"""
import json, time, re, uuid, urllib.request, urllib.error, pathlib, subprocess, sys

def load_env(p):
    d = {}
    for line in open(p):
        if '=' in line:
            k, _, v = line.strip().partition('='); d[k.strip()] = v.strip()
    return d

NT = load_env('/data/AI_Video/.secrets/AI_Doctor_Theater/notoken.env')
NTKEY, NTBASE = NT['NOTOKEN_API_KEY'], NT['NOTOKEN_BASE']
IMG_DEFAULT = '/data/AI_Video/AI_Doctor_Theater/data/persona/official_persona_blank.png'

def nt(method, path, body=None, file=None):
    headers = {'Authorization': f'Bearer {NTKEY}', 'Connection': 'close'}; data = None
    if file is not None:
        b = uuid.uuid4().hex; headers['Content-Type'] = f'multipart/form-data; boundary={b}'
        data = (f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="up.jpg"\r\n'
                f'Content-Type: image/jpeg\r\n\r\n').encode() + file + f'\r\n--{b}--\r\n'.encode()
    elif body is not None:
        headers['Content-Type'] = 'application/json'; data = json.dumps(body).encode()
    req = urllib.request.Request(f'{NTBASE}{path}', data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b'{}')

def i2v(img_path=IMG_DEFAULT, duration=4, ratio='9:16',
        motion='坐在诊室桌前看镜头缓慢眨眼，头部轻微自然摆动，温暖室内自然光',
        out='out_i2v.mp4'):
    """图生视频：压缩上传 → 建任务 → 轮询 → 立即下载。运动提示词自动追加锚定纪律句。"""
    anchored = (motion + '，灰黑虎斑毛色与白胸完全不变，眼睛始终保持黄琥珀色不变，'
                '胸前空白胸牌保持纯白空白无任何文字，薄荷绿听诊器形状保持，像手机随手拍的真实猫')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', img_path,
                    '-vf', 'scale=768:768', '-q:v', '7', '/data/AI_Video/.tmp/i2v_in.jpg'], check=True)
    c, j = nt('POST', '/api/v3/files/uploads', file=open('/data/AI_Video/.tmp/i2v_in.jpg', 'rb').read())
    assert j.get('url'), f'upload failed: {j}'
    body = {'model': 'doubao-seedance-2.0-mini', 'duration': duration, 'ratio': ratio, 'content': [
        {'type': 'image_url', 'image_url': {'url': j['url']}},
        {'type': 'text', 'text': anchored}]}
    c, j = nt('POST', '/api/v3/contents/generations/tasks', body)
    tid = j.get('id'); assert tid, f'task failed: {j}'
    print('i2v task_id:', tid)  # Phase 1 纪律：每镜保留 task id
    t0 = time.time()
    while time.time() - t0 < 600:
        time.sleep(15)
        c, k = nt('GET', f'/api/v3/contents/generations/tasks/{tid}')
        if k.get('status') == 'succeeded':
            urls = re.findall(r'https?://[^"\']+?\.mp4[^"\']*', json.dumps(k, ensure_ascii=False))
            with urllib.request.urlopen(urls[0], timeout=180) as r:
                pathlib.Path(out).write_bytes(r.read())
            return out
        if k.get('status') == 'failed':
            sys.exit(f'i2v failed: {k}')
    sys.exit('i2v timeout')

if __name__ == '__main__':
    print('saved:', i2v())
