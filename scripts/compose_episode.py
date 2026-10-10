#!/usr/bin/env python3
"""compose_episode.py — 自研轻管线合成器（B5 实战命令固化，2026-10-09）

输入：视频段列表（每段：mp4 路径 + 字幕文本 + 时长）+ 猫叫 wav → 输出成片（字幕≤14字/条自动拆行、全程「AI生成」水印、猫叫轨替换原声）。
依赖：ffmpeg（subtitles 滤镜 + wqy 字体；本机 ffmpeg 无 drawtext，水印用第二字幕轨等效实现）。
用法：python compose_episode.py <segments.json> <out.mp4>，segments.json 形如
[{"video":"a.mp4","subtitle":"清晨咖啡馆内Dr.咪向你介绍今天聊聊咖啡","meow":"rhythm_demo.wav"}]
"""
import json, subprocess, sys, pathlib, re

FONT_DIR = '/usr/share/fonts/truetype/wqy'
SRT_SAFE = 14  # 每条字幕最多 14 字（P2/P8 规格）


def split_lines(text, width=SRT_SAFE):
    return [text[i:i + width] for i in range(0, len(text), width)] or ['']


def ts(sec):
    h = int(sec // 3600); m = int(sec % 3600 // 60); s = sec % 60
    return f'{h:02d}:{m:02d}:{s:06.3f}'.replace('.', ',')


def main(segments_path, out_path):
    segs = json.load(open(segments_path))
    work = pathlib.Path('/data/AI_Video/.tmp/compose'); work.mkdir(parents=True, exist_ok=True)
    srt, wm = [], ['1\n00:00:00,000 --> 00:59:59,000\nAI生成\n']  # 水印：force_style Alignment=7 在 libass 实测呈现右上（2026-10-10 抽帧核对），以实测为准
    t = 0.0
    srt_idx = 1
    parts = []
    for i, s in enumerate(segs):
        dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                                    '-of', 'csv=p=0', s['video']], capture_output=True, text=True).stdout.strip())
        lines = split_lines(re.sub(r'\s', '', s['subtitle']))
        per = dur / len(lines)
        for j, ln in enumerate(lines):
            idx = srt_idx
            srt_idx += 1
            srt.append(f'{idx}\n{ts(t+j*per)} --> {ts(t+(j+1)*per)}\n{ln}\n')
        parts.append(s['video'])
        t += dur
    (work / 'cap.srt').write_text('\n'.join(srt), encoding='utf-8')
    (work / 'wm.srt').write_text('\n'.join(wm), encoding='utf-8')
    concat = work / 'list.txt'
    concat.write_text('\n'.join(f"file '{p}'" for p in parts))
    meow = segs[0]['meow']
    vf = (f"subtitles={work}/cap.srt:charenc=UTF-8:fontsdir={FONT_DIR}:force_style='FontName=WenQuanYi Micro Hei,"
          f"FontSize=14,PrimaryColour=&H00FFFFFF,OutlineColour=&H90000000,BorderStyle=1,Outline=2,MarginV=50',"
          f"subtitles={work}/wm.srt:charenc=UTF-8:fontsdir={FONT_DIR}:force_style='FontName=WenQuanYi Micro Hei,"
          f"FontSize=13,PrimaryColour=&H00FFFFFF,OutlineColour=&H90000000,BorderStyle=1,Outline=1,Alignment=7,MarginV=20,MarginL=20'")
    # 视频段拼接 → 猫叫轨替换原声（循环铺满）→ 烧字幕+水印
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error',
                    '-f', 'concat', '-safe', '0', '-i', str(concat), '-stream_loop', '-1', '-i', meow,
                    '-map', '0:v', '-map', '1:a', '-vf', vf, '-c:v', 'libx264', '-preset', 'medium', '-crf', '20',
                    '-c:a', 'aac', '-b:a', '128k', '-shortest', out_path], check=True)
    print('saved', out_path)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
