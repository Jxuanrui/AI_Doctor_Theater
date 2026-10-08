# 主角人设表 v3（Phase 0 / D1-D3，2026-10-08：主角专版）

> 用户拍板：只要主角、更可爱、有记忆点特征；配角暂缓，逐角色设计。
> 设计方法论来源：GitHub 调研（Awesome-Nano-Banana-Prompts 结构化锚点范式、
> AI-Art-Prompt-Collection-for-Anthro-Characters 一致性双路线、chibi-sticker-generator-skill 表情动作库；
> 案例：不爽猫"出厂表情"、Venus 双面猫"稀有身体特征"、谢菲尔德儿童医院"创可贴小熊"）。
> 引擎：CogView-4 + 实拍质感配方 v2（验收 4.5/5）。素材水印 delogo 去除，AI 标识成片层统一履行。

## 官定记录（2026-10-08 用户拍板）

- **官定形象**：`data/persona/C_naiju_2.png`（副本 `official_dr_mi.png`）
- **角色名**：**Dr.咪**（Dr. Mi）
- **人设一句话**：Dr.咪——眉间自带"担心八字纹"的奶橘实习医生，认真又冒失，抱着红十字急救箱到处科普
- **官定锚点块**（后续所有分镜 prompt 逐字复用，只换场景/动作）：
  `Photorealistic photo of a baby-faced kitten doctor, cream-orange fur with soft kitten-fluff texture, very round face with a short nose and oversized glossy sky-blue eyes, two dark ginger worried-eyebrow marks above the eyes, a single cowlick ahoge on top of the head, tiny white lab coat with one sleeve rolled up, small red first-aid cross-body kit with a white cross, four white sock paws, a tiny band-aid on the left front paw`
- **质感配方**（与锚点块拼用）：candid snapshot, soft natural window light, shallow depth of field, warm white balance, subtle film grain, authentic texture, natural imperfect fur clumps, photorealistic, ultra-detailed fur
- **负向**：cartoon, 3d render, illustration, chibi drawing, amber or golden eyes, adult cat proportions, long muzzle, missing eyebrow markings, extra toes, deformed paws, any text, watermark, logo, oversmoothed fur, plastic texture, two cats
- **固定表情包动作位**：举巨大指针/图表讲课、抱急救箱奔跑、歪头听诊（IP 传播资产）

## 三路线设计验证记录（D2，12 张候选）

| 路线 | 概念与记忆点 | 视觉质检（GLM-4.6V） | 结论 |
|---|---|---|---|
| A 胡橘医生（暖心全科） | 胸前心形白斑=医者仁心；琥珀眼+M字纹+白尾尖；oversize 白大褂+挂脖听诊器 | 8.5/10，心形白斑清晰命中，全锚点在 | ✅ 备选池保留 |
| B 阴阳脸神医（怪咖专科） | 嵌合体阴阳脸+金蓝异色瞳+额镜呆毛+橘针织马甲 | 4.5/10：异色瞳未出、脸无分界、出现两只猫 | ❌ 放弃——**锚点过多超出纯文生图能力（重要技术边界）** |
| C 奶橘小医师（幼态实习） | 眉间八字担心纹（永久操心脸）；蓝眼+呆毛+单袖卷起+红十字急救箱+左前爪创可贴 | 全锚点命中，记忆点评 5/5 | ✅ **官定（C_naiju_2）** |

## D3 跨镜一致性验证（3 场景，同锚点块）

- 场景：诊室问诊（d3_clinic）/ 讲台讲课（d3_lecture，举爪指图=固定动作位）/ 上门出诊（d3_housecall，叼急救箱）
- 产物：data/persona/d3_*.png（+raw/）；锚点命中率与"同一只猫"主观一致性评分见关口 1 材料
- 已知边界：写实风格下锚点块保证"同一角色设计"，但不保证像素级同脸——严格锁脸需参考图生成（Nano Banana 多参考/Omnichar refmode）或云端 LoRA（liblib 胖橘写实系打底 0.6-0.8），Phase 1 选型项

## 量产一致性纪律（调研共识）

1. 锚点块逐字复用，绝不临场改写；2. 只替换 [场景/动作] 与镜头语言；3. 每批抽检锚点命中率（GLM-4.6V 判据）；4. 角色库沉淀于 docs/persona/，图片资产在 data/persona/（不入库）
