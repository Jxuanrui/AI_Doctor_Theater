#!/usr/bin/env python3
"""persona_badge_text.py — 形象定妆图贴字+做旧管线（v8，2026-10-09 固化）

流程：OpenCV inpaint 修水印 → PIL 贴字（multiply 正片叠底随卡片明暗）→ 全图做旧后期 → 佐证件输出。
用法：python persona_badge_text.py <raw_png> <out_dir> [light|medium]
坐标参数（水印区/卡片中心/采样点/字区）仅适用 raw_v8_4 底板；换底板必须按监工测绘重填 CONFIG。
颜色纪律：后期全程 RGB 域；与 cv2 交界处必须 [::-1] 转 BGR（历史上两次通道互换事故）。
"""
import sys, pathlib
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

PRESETS = {  # 做旧三档（监工 P2）：light=当前轻档, medium=更像手机随手拍
    'light':  dict(soften=0.25, noise_sigma=2.2, vignette=0.05, jpeg_q=85, seed=7),
    'medium': dict(soften=0.35, noise_sigma=3.5, vignette=0.10, jpeg_q=78, seed=7),
}
CONFIG = dict(
    inpaint_mask=(828, 930, 1020, 1020),   # raw 右下"AI生成"水印区（监工测绘）
    text='住院猫医',                        # 用户 2026-10-09 指定
    text_px=15, text_rgb=(38, 58, 100),    # 深藏蓝印刷
    text_center=(674, 723),                # 监工测绘卡片中心
    text_rotate=13,                        # 卡片上沿倾角，字随卡片
    text_blur=0.4,
    zoom_box=(560, 640, 760, 800),         # 胸口 4x 放大区
    samples={'眼睛': (560, 330), '桌面': (200, 900), '大褂': (400, 600)},  # 颜色门禁采样点
    text_zone=(706, 742, 648, 704),        # 字区（y1,y2,x1,x2）可辨性检查
)

def main(raw_path, out_dir, grade='light'):
    out = pathlib.Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    raw_bgr = cv2.imread(str(raw_path)); assert raw_bgr is not None, raw_path
    raw = raw_bgr[:, :, ::-1]  # RGB
    x1, y1, x2, y2 = CONFIG['inpaint_mask']
    mask = np.zeros(raw.shape[:2], np.uint8); mask[y1:y2, x1:x2] = 255
    clean_rgb = cv2.inpaint(raw_bgr, mask, 7, cv2.INPAINT_TELEA)[:, :, ::-1]
    base = Image.fromarray(clean_rgb)  # 干净底板

    tl = Image.new('RGB', base.size, (255, 255, 255))
    d = ImageDraw.Draw(tl)
    f = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', CONFIG['text_px'])
    tw = d.textlength(CONFIG['text'], font=f); asc, desc = f.getmetrics()
    cx, cy = CONFIG['text_center']
    d.text((cx - tw / 2, cy - (asc + desc) / 2), CONFIG['text'], font=f, fill=CONFIG['text_rgb'])
    tl = tl.rotate(CONFIG['text_rotate'], center=(cx, cy), resample=Image.BICUBIC,
                   fillcolor=(255, 255, 255))  # 空角必须填白：multiply 后不变黑（黑楔事故）
    img = ImageChops.multiply(base, tl).filter(ImageFilter.GaussianBlur(CONFIG['text_blur']))

    p = PRESETS[grade]; arr = np.array(img).astype(np.float32)
    arr = cv2.GaussianBlur(arr, (0, 0), p['soften'])
    r, b = arr[:, :, 0].copy(), arr[:, :, 2].copy()
    arr[1:, 1:, 0] = r[:-1, :-1]; arr[:-1, :-1, 2] = b[1:, 1:]
    arr += np.random.default_rng(p['seed']).normal(0, p['noise_sigma'], arr.shape)
    h, w = arr.shape[:2]; yy, xx = np.mgrid[0:h, 0:w]
    dd = ((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2
    arr *= (1 - p['vignette'] * dd)[:, :, None]
    arr = np.clip(arr, 0, 255).astype(np.uint8)
    _, enc = cv2.imencode('.jpg', arr[:, :, ::-1], [cv2.IMWRITE_JPEG_QUALITY, p['jpeg_q']])
    final = cv2.imdecode(enc, cv2.IMREAD_COLOR)[:, :, ::-1]  # RGB
    suffix = '' if grade == 'light' else f'_{grade}'
    cv2.imwrite(str(out / f'final{suffix}.png'), final[:, :, ::-1])
    Image.fromarray(final).save(out / f'final{suffix}_view.png')  # RGB 直存副本

    # ---- 佐证件 ----
    fim = Image.fromarray(final)
    crop = fim.crop(CONFIG['zoom_box'])
    crop.resize((crop.width * 4, crop.height * 4), Image.LANCZOS).save(out / f'final{suffix}_zoom.png')
    if grade == 'light':
        comp = np.hstack([raw[y1:y2, x1:x2], clean_rgb[y1:y2, x1:x2]])
        Image.fromarray(comp).save(out / 'inpaint_compare.png')  # 左右均 RGB
        for tag, box in [('face', (330, 130, 650, 450)), ('desk', (60, 760, 520, 1010))]:
            Image.fromarray(np.hstack([np.array(base.crop(box)), np.array(fim.crop(box))])).save(out / f'compare_{tag}.png')

    # ---- 门禁（失败即退出，不放行）----
    bf = np.array(base).astype(float); ff = final.astype(float)
    # 1) 通道互换检测：corr(final.R, base.R) 必须 > corr(final.R, base.B) 且 > 0.98
    def corr(a, b):
        a = a.ravel() - a.mean(); b = b.ravel() - b.mean()
        return float((a * b).sum() / np.sqrt((a * a).sum() * (b * b).sum()))
    cRR, cRB = corr(ff[:, :, 0], bf[:, :, 0]), corr(ff[:, :, 0], bf[:, :, 2])
    print(f'[{grade}] 通道互换门禁: corr(R,R)={cRR:.4f} corr(R,B)={cRB:.4f}', end=' ')
    if not (cRR > 0.98 and cRR - cRB > 0.01):
        print('FAIL'); sys.exit(1)
    print('PASS')
    # 2) 采样点 5x5 邻域均值对照（色相结构须保持）
    for tag, (sx, sy) in CONFIG['samples'].items():
        b5 = bf[sy-2:sy+3, sx-2:sx+3].mean(axis=(0, 1)); f5 = ff[sy-2:sy+3, sx-2:sx+3].mean(axis=(0, 1))
        ok = (np.argmax(b5) == np.argmax(f5)) and (np.argsort(b5).tolist() == np.argsort(f5).tolist())
        print(f'  采样 {tag}: base {b5.round(0).tolist()} -> final {f5.round(0).tolist()} {"PASS" if ok else "FAIL"}')
        if not ok: sys.exit(1)
    # 3) 边缘黑楔检查（成品 vs 底板，暗占比差须 <3 个百分点）
    for name, im in [('base', bf), ('final', ff)]:
        L = im.mean(axis=2)
        parts = {s: float((sl < 40).mean()) for s, sl in
                 [('top', L[:20]), ('bottom', L[-20:]), ('left', L[:, :20]), ('right', L[:, -20:])]}
        if name == 'base': base_edges = parts
        else:
            bad = [s for s in parts if parts[s] - base_edges[s] > 0.03]
            print(f'  边缘检查 final: {parts} {"FAIL:"+str(bad) if bad else "PASS"}')
            if bad: sys.exit(1)
    # 4) 字可辨性
    ty1, ty2, tx1, tx2 = CONFIG['text_zone']
    std = float(ff[ty1:ty2, tx1:tx2].std())
    print(f'  字区标准差 {std:.1f}（>20 可辨）{"PASS" if std > 20 else "FAIL"}')
    if std <= 20: sys.exit(1)
    print(f'[{grade}] ALL GATES PASS ->', out)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 'light')
