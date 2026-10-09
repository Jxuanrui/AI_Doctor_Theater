# 主角人设表 v4（2026-10-09：长毛蓬松橘白猫医生）

> 参考背景（如实记录，2026-10-09 监工纠偏）：用户提供抖音某头部 AI 萌宠账号（272.7万粉）作参考。抓取到的两张封面
> 里是**灰棕虎斑+白短毛猫**（黄安全帽、荧光背心、电钻，作者声明 AI 生成），**不是**橘白长毛猫。
> "长毛蓬松橘白"是**本项目自己的设计取向**（用户原话"当然网红可爱橘猫也可以"），与参考角色脱钩，不复刻其工装/道具/名称等标志元素。
> 用户最终取向（橘白长毛 vs 虎斑白短毛）待拍板确认，见下方"待用户拍板"。

## 角色档案

- 角色名：**待定**（原"Dr.咪"与参考账号名有混淆风险，监工建议改名，如以"橘/毛"为主字）
- 物种/品种：长毛橘白猫（橘虎斑+白胸白口鼻白爪）
- 体型年龄：微胖成年猫，圆脸，大体型围脖
- 性格：温吞可靠、话痨科普、偶尔犯困（口头禅待定妆后与用户共创，候选："别慌，听喵说"）
- 音色：**待用户拍板**（候选 tongtong / xiaochen，GLM-TTS 已实测，见 data/api_probe/）
- 记忆点：长毛围脖+大腮毛 / 橘白配色 / 白大褂+薄荷绿听诊器（自然系记忆点，弱于标志物；如需强化后续加固定配饰）

## 视觉 DNA（v4b 官定锚点块，英文，逐字复用）

`a fluffy long-haired orange tabby cat with a chubby round face, full cheek fur and thick fluffy neck ruff, white chest and muzzle fur, big round amber eyes with gentle sparkle, wearing a crisp white doctor coat, and a mint-green binaural stethoscope draped around the neck with earpiece tubes on one side and a single chest piece on the other side`

- 质感配方：sitting at a wooden clinic desk looking straight at camera, candid amateur DSLR photograph, 50mm lens, shallow depth of field, soft natural window light from the left, warm white balance, visible film grain, authentic natural texture, imperfect fur clumps, slightly wrinkled fabric, photorealistic real photo
- 场景块：cozy clinic interior with blurred shelf of medical books and a potted plant in uneven natural bokeh
- 负向：cartoon, 3d render, illustration, chibi drawing, **short-haired cat**, skinny cat, kitten proportions, any text, watermark, logo, deformed paws, extra limbs, two cats, oversmoothed fur, plastic texture, **two chest pieces**, duplicated stethoscope heads, stethoscope on both sides
- 关键负向：short-haired cat（v3 失败根因）；two chest pieces（v4 轮听诊器双听头畸形教训）

## 候选与质检记录（主观目测，均属 candidate_research，以用户目视为准）

| 批次 | 文件 | 质检结论（缺陷如实列出） |
|---|---|---|
| v4（2026-10-09 晨） | data/persona/v4_drmi_1~6.png（原图 raw_v4_1~6） | 长毛围脖/橘白/白大褂达标；**缺陷：听诊器双听头无耳件畸形（_2/_5 确认），画风偏数字插画非写实照片**。降级为备选 |
| v4b（2026-10-09 修复轮） | data/persona/v4b_drmi_1~6.png（原图 raw_v4b_1~6） | **听诊器结构修复（一端耳件+单听头，_1/_3 抽验通过）；写实度提升（毛发层次/蓬松感/真实光感）**；小瑕疵：口鼻毛发轻微粘连、背景虚化偏强。**执行方推荐从此批选官定图**（推荐 v4b_drmi_1 / _3） |
| ~~Seedance r2v~~ | data/persona/quarantine_ref_derived/（v4_seed_1~3 + ref_seedance_drmi.mp4） | **受污染衍生物，已隔离**：因参考封面（第三方版权素材）被上传到外部接口生成，禁止用于定妆/训练/发布，定妆后删除。教训已固化为 governance.md §4 |

## 资产清单（完整 sha256 见 data/persona/ASSETS.sha256，30 项）

- 定妆候选：v4b_drmi_1~6.png、v4_drmi_1~6.png（1024x1024，delogo 后；原图 raw_v4*/raw_v4b* 同目录保留作溯源）
- 参考材料：ref/ref_cover1~2.jpg（仅供内部参考，**禁止再上传到任何外部模型接口**；定妆后删除或改为仅存来源链接）
- 隔离区：quarantine_ref_derived/（定妆后删除）

## 待用户拍板

1. **设计方向**：橘白长毛（现候选）还是灰虎斑白短毛（更贴参考封面）？
2. **官定图**：从 v4b_drmi_1~6 挑 1 张（执行方推荐 _1 或 _3）；画风取向（毛茸茸可爱插画感 vs 实拍质感）一并确认
3. **角色名**：沿用 Dr.咪（有混淆风险）还是改名
4. 音色 tongtong / xiaochen；性格口头禅共创
5. 定妆后：重跑 D3（3 场景一致性）+ Seedance i2v 动态验证（**重点：i2v 是否会把长毛拉回短毛**，监工风险预警 #3）

## AI 标识纪律

见 docs/governance.md §1（素材层原图留档、成片层显式标识、delogo 台账）。

## 历史版本

v1 人类女医生 / v2 短毛写实小猫 / v3 短毛幼猫 / v4 橘白长毛（听诊器畸形+插画感）→ **v4b 修复轮（当前）**。均已删除或替换，见 git 历史。
