# 主角人设表（灰虎斑白短毛猫医生 · 2026-10-09 官定）

> **官定**：形象 = data/persona/official_persona.png（= v8_final_5/final.png 的副本，两份均留作溯源；轻档做旧——监工建议定妆图复用到视频选轻档，不加 heavy 档）；视频用空白牌底图 data/persona/official_persona_blank.png；胸牌文字"住院猫医"（静态特写贴字用）。
> 方向沿革：v4 橘白长毛（用户否）→ v5 灰虎斑方向 → v6 AI 印字失败（中文 0/8）→ v7 空白牌+后期贴字 → v8 写实增强+做旧（官定）。历史批次资产均已按用户指令删除（记录见 archive-manifest.md 第七批，不可恢复声明同文件）。

## 角色档案（2026-10-09 用户拍板）

- **角色名：Dr.咪**（监工曾建议改名规避与外部参考账号的混淆风险，已如实转达，用户决定采用——异议记录在案；上线前建议查主要平台重名/商标）
- 物种/品种：短毛灰虎斑白猫（头部/背部/两侧灰黑虎斑纹，白胸白口鼻白爪）
- 体型年龄：圆脸微胖成年猫
- 性格：温吞可靠、话痨科普、偶尔犯困（口头禅候选："别慌，听喵说"）
- **配音：有节奏的猫咪叫声 + 全字幕表达**（用户拍板弃人声 TTS）；音效库 data/sfx/（10 份 CC0，许可台账 SOURCES.md + 页面证据存私有目录）；节奏样听 data/sfx/rhythm_demo.{wav,mp3}；管线不写死，保留将来加回人声可能（监工建议）
- 记忆点：圆脸大眼 / 灰白虎斑 / 白大褂+薄荷绿听诊器+空白胸牌（视频中身份靠字幕/角标）

## 视觉 DNA（v8 官定锚点块，英文，逐字复用）

`a short-haired gray tabby cat with a chubby round face, gray and black tabby stripes on the head, back and sides, solid white chest, white muzzle and white paws, solid white blaze extending from nose bridge to muzzle, big round yellow-amber eyes with gentle sparkle, pink nose, no warm orange on ear rims, wearing a crisp white doctor coat with a small blank white name badge clipped on the chest pocket, the badge is plain and completely empty, and a mint-green binaural stethoscope draped around the neck with earpiece tubes on one side and a single chest piece on the other side`

- 眼色标准：以官定图实测**黄琥珀**为准，每镜头抽帧对照色卡 data/persona/eyecolor_card.png
- 白鼻梁纹贯通到口吻（防 s1 型漂移）；耳缘禁暖橙；爪垫红斑入负向
- 质感配方（做旧前）：candid photo taken on a smartphone, slightly off-center framing, mixed indoor lighting with warm desk lamp and cool daylight window, harsh light falloff, visible sensor noise, slight chromatic aberration at frame edges, slightly missed focus on fur tips, wrinkled coat, imperfect fur clumps, authentic amateur snapshot, not retouched
- 场景块：cozy cluttered clinic interior, blurred shelf of medical books, a potted plant and scattered papers in uneven natural bokeh
- 负向：cartoon, 3d render, illustration, chibi drawing, long-haired cat, fluffy neck ruff, orange cat, ginger fur, calico, tan nose bridge, orange patch on face, warm orange ear rims, red paw pads, skinny cat, kitten proportions, any text, watermark, garbled text, printed characters, Chinese characters, letters, numbers, handwriting, logo, pen, studio lighting, perfect symmetry, oversmoothed fur, plastic texture, airbrushed, flawless skin, professional retouching, two chest pieces, duplicated stethoscope heads, stethoscope on both sides, hard hat, safety vest, deformed paws, extra limbs, two cats
- **服装文字纪律**：AI 出图一律不含文字；"住院猫医"由 scripts/persona_badge_text.py 贴字（参数已固化）或成片层字幕表达
- 检查纪律：视觉模型仅辅助，位置/文字/标志物以像素坐标+放大截图核对，监工看图复核是放行唯一依据；逐张全检（硬检查项：无文字/听诊器结构/毛色/胸牌状态）

## 视频生成纪律（i2v 实测结论，2026-10-09）

- **胸牌中文必崩**（第 1 帧起成伪英文）→ 视频一律空白胸牌（official_persona_blank.png），身份用字幕/角标；仅定妆特写后期贴字
- 漂移观察项（人工审片）：眼色（琥珀→黄绿）、脸型、白鼻梁宽度、头身比；多镜头逐镜头抽帧对照官定图+色卡
- **锚定句不能阻止眼色漂移（E5 实证，2026-10-09 监工判定：f0 琥珀金→f1 黄橄榄→f3_9 暗橄榄，全程未回琥珀；锚定有效性无对照实验证明）**：样片阶段接受轻度漂移，镜头压 2–3 秒或在漂移前切走；S2 试点做虹膜色相数值化闸门后再定终策略（用户 2026-10-09 采纳监工建议）
- E4 判定（监工原文见 T0_verdict.md）：空白牌 4 帧全部保持无伪文字 ✓；E5 样本 task id 未记录（模板缺陷，已补打印），费用按 ~1 点/秒估算 4 点
- mini 档输出 640×640；Phase 1 前做正式档画质对比再定成片档位
- i2v 调用模板：scripts/i2v_template.py（NoToken，密钥从 .secrets 注入，无硬编码）

## 资产清单（= data/persona/ASSETS.sha256，19 项（2026-10-10 v3 快照）；快照 docs/reviews/phase0/asset-snapshots/persona-2026-10-09.sha256）

| 文件 | 用途 |
|---|---|
| official_persona.png | 官定形象（含"住院猫医"贴字+轻档做旧） |
| official_persona_blank.png | 视频用空白牌底图（同工艺未贴字） |
| raw_v8_4.png | 官定底板原图（水印溯源，governance §1 留档） |
| eyecolor_card.png | 眼色色卡（审片比对） |
| official_blank_i2v.mp4 | 空白牌保持性证据视频（4s） |
| v8_final_5/final.png | 官定原件（与 official 哈希一致） |
| v8_final_5/final_zoom.png | 胸口 4x 放大（贴字参照） |

（v7 全系/v8 弃稿/D3/抽帧等已删——见 archive-manifest.md 第七批；T0 新增 e5_eye_i2v.mp4 + e4/e5 判定帧 8 张，判定帧已复制 docs/reviews/phase0/t0-frames/ 入 git）

## 待用户拍板

1. Phase 1 前做 Seedance 正式档（非 mini）画质对比，再定成片档位
2. 动态贴字小样（特写"字跟胸牌动"成本验证，可选）
3. 猫叫音源升级（量产前考虑自录/付费授权库——当前 8 段为 OGA 自标 CC0，监工建议内部样片可用、对外发布前评估）

## AI 标识与合规

见 docs/governance.md §1（素材层原图留档、成片层显式标识、delogo/删除台账）；§4（素材合规）；字幕医学校对为成片导出前硬门禁（§5）。
