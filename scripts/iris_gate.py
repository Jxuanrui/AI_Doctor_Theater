#!/usr/bin/env python3
"""iris_gate.py — 虹膜色相数值闸门（Phase 1 D0 建，plan-v3.5 B1）

从帧中定位眼睛区域取虹膜色相（HSV H 通道），与官定色卡基准比对；超阈值即 FAIL。
用法：python iris_gate.py <帧图> [<帧图> ...]   （基准：data/persona/eyecolor_card.png）
原理：官定图黄琥珀虹膜 → H 通道 20-45（OpenCV 0-179 标度）为合格窗；每帧取眼部区域
（自动检测失败时须人工传 --box x,y,w,h）。阈值与窗口可按 S0 实测校准（CONFIG）。
"""
import sys, cv2, numpy as np, pathlib

CONFIG = dict(
    card='/data/AI_Video/AI_Doctor_Theater/data/persona/eyecolor_card.png',
    h_lo=26, h_hi=50,          # 合格色相窗（D0 基线校准：琥珀 f0 h_mean=38.8；漂移帧 f1/f2 h_mean=15.7/18.9——判据 h_mean∈[26,50]=PASS）
    min_sat=40, min_val=40,    # 低饱和/低亮像素不参与（避免眼白/阴影）
    eye_roi_default=(0.25, 0.20, 0.50, 0.28),  # 相对帧的比例框（x,y,w,h）——眉眼带
)

def iris_hue_stats(img, roi):
    """虹膜定位：眉眼带 ROI 内 HoughCircles 找双眼虹膜圆，仅统计圆内高饱和像素。"""
    H, W = img.shape[:2]
    rx, ry, rw, rh = [int(v * s) for v, s in zip(roi, (W, H, W, H))]
    band = img[ry:ry+rh, rx:rx+rw]
    gray = cv2.cvtColor(band, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2,
                               minDist=int(rh*0.3), param1=80, param2=28,
                               minRadius=max(4, int(rh*0.03)), maxRadius=int(rh*0.16))
    px_all = []
    if circles is not None:
        mask = np.zeros(gray.shape, np.uint8)
        for cx, cy, r in np.round(circles[0]).astype(int)[:2]:
            cv2.circle(mask, (cx, cy), max(3, r - 1), 255, -1)
        hsv = cv2.cvtColor(band, cv2.COLOR_BGR2HSV)
        m = (mask > 0) & (hsv[:, :, 1] > CONFIG['min_sat']) & (hsv[:, :, 2] > CONFIG['min_val'])
        px_all = hsv[m]
    if len(px_all) < 40:
        return None
    return dict(n=len(px_all), h_mean=float(px_all[:, 0].mean()), h_p25=float(np.percentile(px_all[:, 0], 25)),
                h_p75=float(np.percentile(px_all[:, 0], 75)))

def gate(frame_path, roi=None):
    img = cv2.imread(str(frame_path))
    if img is None:
        return f'{frame_path}: READ_FAIL'
    st = iris_hue_stats(img, roi or CONFIG['eye_roi_default'])
    if st is None:
        return f'{frame_path}: INSUFFICIENT_PIXELS'
    ok = CONFIG['h_lo'] <= st['h_mean'] <= CONFIG['h_hi']  # 闸门判据（D0 校准）：虹膜均值色相 h_mean∈[h_lo,h_hi]=琥珀保持
    return (f"{frame_path}: {'PASS' if ok else 'FAIL'} h_mean={st['h_mean']:.1f} "
            f"p25={st['h_p25']:.1f} p75={st['h_p75']:.1f} n={st['n']} (窗 {CONFIG['h_lo']}-{CONFIG['h_hi']})")

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--box')]
    box = None
    if '--box' in sys.argv:
        i = sys.argv.index('--box')
        box = tuple(float(v) for v in sys.argv[i+1].split(','))
    # 基准自检：色卡通闸
    print('[card]', gate(CONFIG['card']))
    for a in args:
        print('[frame]', gate(a, box))
