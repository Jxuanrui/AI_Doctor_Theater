# Q版人设表 v2（Phase 0 / D1，2026-10-08 第二次重设计）

> 用户拍板：风格改为**照片级写实软萌小猫**（用户提供参考图：奶油橘白小猫、超大琥珀圆眼、
> 大光圈浅景深、绒毛质感、柔光虚化背景）——即"AI 写实宠物短剧"风格，弃用扁平插画。
> v1（扁平插画风）已删除，历史见 git。
> 医生元素以"写实小猫穿迷你白大褂+薄荷绿听诊器"呈现。
> 素材级水印（CogView 右下角"AI生成"）流水线内 ffmpeg delogo 去除；
> AI 标识义务在成片层履行（发布统一标注，Phase 2 落实显式+元数据）。

## 通用画风锚点（每条提示词必带，源自参考图逆向）

- 英文（positive）：photorealistic, professional pet photography, 85mm lens, f/1.8 shallow depth of field, creamy bokeh background, soft natural lighting, ultra detailed fluffy fur, huge round sparkling amber eyes, adorable expression, high detail, 8k quality
- 反向（negative）：cartoon, flat illustration, chibi, 2d, anime, 3d render, cgi look, scary, dark, any text, letters, numbers, watermark, deformed paws, extra limbs
- 硬规则：图内禁止任何文字/数字（文字全部代码层绘制）

## 角色一：橘医生 Dr. Mikan —— 主讲人（C位）

| 项 | 设定 |
|---|---|
| 身份 | 照片级写实橘白小猫医生（参考图同款软萌感） |
| 体貌 | 奶油橘白：橘色虎斑纹（头顶/耳/尾）+ 白色口鼻/胸口/爪尖；超大琥珀圆眼带水光；绒毛质感带逆光轮廓光 |
| 服装/标志物 | 迷你白大褂（带纽扣细节）+ 薄荷绿听诊器绕颈（金属听头反光） |
| 性格镜头语言 | 微歪头看镜头；竖起一只肉垫爪"敲黑板"；惊讶时耳朵前倾、圆眼瞪更大 |
| 英文提示词 | super cute orange tabby kitten doctor, cream and orange fluffy fur with white chest and muzzle, darker orange tabby stripes on head and tail, wearing a tiny white doctor coat and a mint-green stethoscope around neck, sitting upright, head tilted up looking at camera with big sparkling eyes + 通用画风锚点 |

## 角色二：菌小宝（Bacto）—— 肠道菌群拟人（跟班）

| 项 | 设定 |
|---|---|
| 体貌 | 奶黄色圆滚滚绒毛小团子（软 plush 质感），头顶一片小绿叶，大圆眼 |
| 英文提示词 | super cute tiny cream-yellow round fluffy mascot creature like a soft plush capsule with a small green leaf on head, big sparkling eyes, adorable + 通用画风锚点 |

## 角色三：球球（Suga）—— 糖分拟人（反派担当，不恐怖化）

| 项 | 设定 |
|---|---|
| 体貌 | 棉花糖粉色绒毛圆团子，抱超大棒棒糖，坏笑 |
| 英文提示词 | super cute cotton-candy pink round fluffy mascot creature hugging an oversized lollipop, big sparkling eyes, mischievous sweet smile + 通用画风锚点 |

## 实拍质感配方 v2（2026-10-08 验收 4.5/5，当前生产配方）

- 增强锚点：wrinkled cotton coat with visible fabric weave / slightly dusty stethoscope with uneven tube reflections / cozy slightly messy clinic / cluttered edges in uneven natural bokeh / single cat only
- 反向增补：pristine uniform background / two cats
- 逆向来源：GLM-4.6V 对用户参考图（写实工装猫）的提示词逆向；参考图实为"安全帽+反光背心工装猫"写实风
- 验收记录（mikan_r2）：4.5/5 网红工装猫匹配度；毛发层次/眼神光/布料褶皱/景深全过；无水印无畸形

## 已知质量边界（验收记录 2026-10-08）

- 首批 12/12 成功 + 精修 4 张（mikan_r1~r4）；CogView-4 写实档天花板约 4.5/5，如需 5/5 级可后续测 Seedream 4（火山，约¥0.06/张）或 Nano Banana（Gemini，约¥0.5/张）
- 视觉验收（mikan_2）：风格匹配 4.5/5；已知瑕疵：听诊器管线走向偶有不合理、袖口毛发过渡略生硬——写实风格的常态，抽卡+后期选优可解
- 配角为"写实绒毛团子"路线（与主角同质感）；若用户想要配角也是真实动物（如仓鼠/兔子），改提示词即可

## 出图与一致性（沿用）

- 原图留 `data/persona/raw/` 备查；成品经 delogo 去水印；manifest.csv 记录
- D3：定妆后 3 姿态×评分五维（辨识度/配色/比例/医学形象不失真/无恐怖谷——写实风格下"恐怖谷"维度改为"解剖合理性"）
