# 主角人设表 v4（2026-10-09：长毛蓬松橘白猫医生，参考抖音"妙角维修猫"气质）

> 用户反馈：短毛幼猫版不满意；参考对象=抖音@咪的妙脆角（272.7万粉头部 AI 萌宠账号）的"妙角维修猫"
> （长毛蓬松橘白猫、大腮毛围脖、圆脸、穿工装做维修剧情，作者声明 AI 生成）。
> **设计原则：取神不取形**——吸收"长毛蓬松橘白+圆脸围脖"的品种气质（自然猫型，非该账号独创），
> 职业设定为我们自己的"医生"（白大褂+薄荷绿听诊器），不复刻其工装/工具袋等标志元素，规避 IP 纠纷。

## 视觉 DNA（v4 官定锚点块，英文，逐字复用）

`a fluffy long-haired orange tabby cat with a chubby round face, full cheek fur and thick fluffy neck ruff, white chest and muzzle fur, big round amber eyes with gentle sparkle, wearing a crisp white doctor coat and a mint-green stethoscope around the neck`

- 质感配方（沿用 v2 实拍配方）：candid snapshot, soft natural window light from the left, shallow depth of field, warm white balance, subtle film grain, authentic texture, natural imperfect fur clumps, photorealistic, ultra-detailed fur
- 场景块：cozy clinic interior with blurred shelf of medical books and a potted plant in uneven natural bokeh
- 负向：cartoon, 3d render, illustration, chibi drawing, **short-haired cat**, skinny cat, kitten proportions, any text, watermark, logo, deformed paws, extra limbs, two cats, oversmoothed fur, plastic texture
- 关键负向新增：**short-haired cat**（v3 失败根因就是短毛）

## 双生产线实测结论（2026-10-09）

| 生产线 | 产物 | 视觉质检 | 结论 |
|---|---|---|---|
| A：CogView-4 + DNA 提示词 | v4_drmi_1~6.png（1024²，delogo 去水印） | **v4_drmi_2 = 4.9/5**（围脖腮毛/白大褂/听诊器/职业气质全满，无畸形无水印） | ✅ **形象设计主力** |
| B：Seedance-mini r2v（参考封面真猫→医生装） | ref_seedance_drmi.mp4 + 抽帧 v4_seed_1~3 | 2/5：**长毛基因丢失**（出成短毛），mini 档保不住毛发 DNA | ⚠️ 只用于动作/分镜，不用于形象定妆 |

参考材料：data/persona/ref/ref_cover1~2.jpg（抖音封面，抓取自分享页；仅供内部设计参考）。

## 待用户拍板

1. 官定图：从 v4_drmi_1~6 挑 1 张（执行方推荐 **v4_drmi_2**，质检 4.9/5）
2. 角色名沿用 Dr.咪 或改
3. 定妆后重跑 D3（3 场景一致性）+ Seedance 动态验证（CogView 定妆 → Seedance i2v 动起来，检验跨引擎一致性）

## 历史版本

v1 人类女医生 / v2 短毛写实小猫 / v3 短毛幼猫（担心眉）——均已删除，见 git 历史。v3 的"记忆点方法论"仍有效，v4 起记忆点=长毛围脖+橘白配色+医生装（自然系记忆点，弱于 v3 的八字眉；若需强化可后续加固定配饰）。
