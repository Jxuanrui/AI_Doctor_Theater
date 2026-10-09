#!/usr/bin/env python3
"""t0_c2_glm_json_test.py — T0-C2 GLM JSON 可解析性测试（2026-10-09，监工放行条件#2）

重跑 1 次：完整响应 JSON 落盘（含 model/usage/finish_reason/request_id）+ 去密钥请求体。
配置（thinking disabled + max_tokens 4096）即本脚本 body 所示；结论：裸 json.loads 失败（```json 围栏），
剥围栏后可解析。平台内（lumenx/LMD）是否等价未验证（两平台主解析路径自带剥围栏：LMD safeJson.js:196-199；
lumenx llm.py:14-20）。
"""
import json, re, urllib.request, pathlib

def load_env(p):
    d = {}
    for line in open(p):
        if '=' in line:
            k, _, v = line.strip().partition('='); d[k.strip()] = v.strip()
    return d

GLM = load_env('/data/AI_Video/.secrets/AI_Doctor_Theater/glm.env')['BIGMODEL_API_KEY']
OUT = pathlib.Path('/data/AI_Video/AI_Doctor_Theater/data/phase0/evidence/T0_c2_full_response.json')

SYS = ('你是医学科普短视频编剧。只输出 JSON，不要任何解释文字。'
       '格式：{"title":str, "scenes":[{"id":int, "subtitle":str(≤14字), "visual":str, "duration_s":int}]}')
body = {'model': 'glm-4.7',
        'messages': [{'role': 'system', 'content': SYS},
                     {'role': 'user', 'content': '主题：喝咖啡的作用与危害。写 6 个镜头的分镜剧本草稿，每镜字幕一行不超过14字。'}],
        'thinking': {'type': 'disabled'}, 'max_tokens': 4096, 'temperature': 0.7}
req = urllib.request.Request('https://open.bigmodel.cn/api/paas/v4/chat/completions',
                             data=json.dumps(body).encode(),
                             headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {GLM}'})
with urllib.request.urlopen(req, timeout=120) as r:
    resp = json.loads(r.read())

evidence = {'request_body_sanitized': body, 'response': resp,
            'notes': {'raw_parse': None, 'stripped_parse': None}}
content = resp['choices'][0]['message'].get('content') or ''
try:
    json.loads(content); evidence['notes']['raw_parse'] = 'OK'
except Exception as e:
    evidence['notes']['raw_parse'] = f'FAIL: {str(e)[:60]}'
try:
    json.loads(re.sub(r'^```(json)?\s*\n?|\n?```\s*$', '', content.strip()))
    evidence['notes']['stripped_parse'] = 'OK'
except Exception as e:
    evidence['notes']['stripped_parse'] = f'FAIL: {str(e)[:60]}'
OUT.write_text(json.dumps(evidence, ensure_ascii=False, indent=2))
print('saved', OUT, '| raw:', evidence['notes']['raw_parse'], '| stripped:', evidence['notes']['stripped_parse'],
      '| finish:', resp['choices'][0].get('finish_reason'), '| usage:', resp.get('usage'))
