# 主角人设表 v5（2026-10-09：灰虎斑白短毛猫医生 · v7 贴字版）

> 方向沿革：v4 系橘白长毛被用户否 → 用户拍板灰虎斑白短毛（v5）→ v5_5 选为底板，"猫猫医院"印字+夹笔（v6）因扩散模型写中文字 0/8 全错被监工打回 → 用户拍板 B 路线（后期贴字）+ 夹笔换胸牌 + 重出干净底板（v7，空白胸牌）→ **v7_final_6.png = 当前定妆候选**（_6 底板 + PIL 贴"猫猫医院"）。
> 参考锚点：抖音某头部 AI 萌宠账号封面猫（白底灰黑虎斑、短毛、圆脸大眼，AI 生成）。"取神不取形"：只取品种气质，不复刻安全帽/背心/电钻/白鹅等标志元素。

## 角色档案

- 角色名：**待定**（候选：Dr.灰 / 灰灰 / 毛毛 / Dr.Tabby；避开与参考账号谐音）
- 物种/品种：短毛灰虎斑白猫（头部/背部/两侧灰黑虎斑纹，白胸白口鼻白爪）
- 体型年龄：圆脸微胖成年猫
- 性格：温吞可靠、话痨科普、偶尔犯困（口头禅候选："别慌，听喵说"）
- 音色：**待用户拍板**（tongtong / xiaochen，GLM-TTS 已实测 data/api_probe/）
- 记忆点：圆脸大眼 / 灰白虎斑 / 白大褂+薄荷绿听诊器+**"猫猫医院"工作胸牌**（胸牌文字即记忆点之一）

## 视觉 DNA（v7 官定锚点块，英文，逐字复用）

`a short-haired gray tabby cat with a chubby round face, gray and black tabby stripes on the head, back and sides, solid white chest, white muzzle and white paws, big round amber eyes with gentle sparkle, pink nose, wearing a crisp white doctor coat with a small blank white name badge clipped on the chest pocket, the badge is plain and completely empty, and a mint-green binaural stethoscope draped around the neck with earpiece tubes on one side and a single chest piece on the other side`

- 质感配方（沿用）：sitting at a wooden clinic desk looking straight at camera, candid amateur DSLR photograph, 50mm lens, shallow depth of field, soft natural window light from the left, warm white balance, visible film grain, authentic natural texture, imperfect fur clumps, slightly wrinkled fabric, photorealistic real photo
- 场景块：cozy clinic interior with blurred shelf of medical books and a potted plant in uneven natural bokeh
- 负向：cartoon, 3d render, illustration, chibi drawing, long-haired cat, fluffy neck ruff, orange cat, ginger fur, calico, tan nose bridge, orange patch on face, skinny cat, kitten proportions, **any text, watermark, garbled text, printed characters, Chinese characters, letters, numbers, handwriting, logo, pen**, deformed paws, extra limbs, two cats, oversmoothed fur, plastic texture, **two chest pieces**, duplicated stethoscope heads, stethoscope on both sides, hard hat, safety vest
- **服装文字纪律（v6 教训，2026-10-09 定）**：AI 出图一律**不含任何文字**；"猫猫医院"四字由 **PIL + 文泉驿微米黑**后期贴在胸牌上（深藏蓝 #23375F、带轻阴影），字号按牌面自适应。~~v6 的"图内印字"提示词写法已作废，禁止再用~~。
- 检查纪律（v4-v7 四轮失真教训，2026-10-09 定）：
  1. 视觉模型仅作辅助描述，**位置/文字/标志物判断一律以像素坐标 + 裁剪放大截图（≥3x）核对为准**，监工看图复核是放行唯一依据；
  2. 视觉质检串行单图单调用，请求带文件名+sha256 前 8 位并要求回带，日志落盘 docs/reviews/phase0/qc-v7-log.md；
  3. 凡判"有胸牌/无文字"必须附放大截图佐证。

## 候选与质检记录（权威结论以监工看图报告为准）

### v7 空白胸牌底板轮（2026-10-09，监工逐张结论）

| 图 | 监工结论 |
|---|---|
| v7_badge_1 | 不合格：根本没有胸牌（无牌元素） |
| v7_badge_2 | 不合格：牌上有伪文字（绿色抬头+灰线条）；听诊器左管可疑 |
| v7_badge_3 | 不合格：无胸牌；口袋乱码字母"FXALIT"；两侧耳件畸形 |
| v7_badge_4 | 不合格：牌上伪英文多行；左侧无听头只有圆环 |
| v7_badge_5 | 不合格：红黑伪文字；双听头畸形 |
| **v7_badge_6** | **基本合格（唯一）**：口袋处夹子+空白卡片（监工坐标 575-665, 680-740）；听诊器正常；鼻梁上方轻微棕调（可接受） |
| v7_badge_7 | 不合格：卡片上有小字 |
| v7_badge_8 | 不合格：牌上多行伪文字 |

### 贴字记录

- v7_final_1 / v7_final_2：**失败已删**——视觉模型返回的胸牌 bbox 是幻觉（_1 无牌、_2 字牌错位），监工打回（2026-10-09）。
- **v7_final_6.png（当前定妆候选）**：v7_badge_6 底板 + **分排贴字**（监工建议排法）："猫猫医"（14px，x583-621）+ 听诊管区空开（x626-650）+ "院"（13px，x650-659）；管子保持底图原样、字只印卡面，遮挡关系天然正确；字层 rotate(+5°) 与卡片上沿平行（卡片右高，监工目测换算 5.4°）、blur 0.4px、深藏蓝+轻阴影。自查证据 v7_final_6_zoom.png（4x 放大）+ 程序实测（diff 568 字像素、管区仅 24 个 aa 边像素且落卡面，见 qc-v7-log.md §五）。
- 贴字参数（复现用）：文泉驿微米黑，左组"猫猫医"14px @x579-627 中心线、右组"院"13px @x646-663，#23375F α242 / 阴影 +1px 灰 α85 / rotate +5° 绕卡片中心 (620,710) / GaussianBlur 0.4px。
- **贴字遮挡纪律**：贴字/叠加前必查前景遮挡物（管/爪/领口）；能避开就分排避开（优于遮罩回贴）；必须遮挡时按物体形状做遮罩（矩形竖条会切断斜穿元素——v7 两次返工教训）。

### 历史（全部已删，详见 archive-manifest.md）

- v6 印字轮：8 张文字 0/8 全错（乱码/缺字/"狗"字），抽卡路线否决。
- v5 首轮：_5 最优被选为底板；v4/v4b 橘白长毛：方向被否。

## 资产清单

- 定妆候选：v7_final_6.png（+zoom 自查件）；备选底板 v7_badge_6.png；其余 v7_badge_1~8 留档对照
- 原图：raw_v7_1~8.png（delogo 前留档溯源）
- 参考材料：data/persona/ref/ref_cover1~2.jpg（官定后删除改存来源链接）
- sha256：data/persona/ASSETS.sha256（20 项）

## 待用户拍板

1. **官定图终审**：v7_final_6.png（看大图 + 放大截图）；监工提示：卡片偏小四字偏小（18px），如不满意可走"专门大号空白胸牌抽卡轮"或局部重绘
2. **角色名**：Dr.灰 / 灰灰 / 毛毛 / Dr.Tabby / 其他
3. **音色**：tongtong / xiaochen
4. 定妆后：删参考封面；D3 三场景一致性（贴字环节纳入管线）+ Seedance i2v 动态验证（**逐帧盯胸牌文字是否变形漂移**——监工风险预警）

## AI 标识纪律

见 docs/governance.md §1（素材层原图留档、成片层显式标识、delogo 台账）。

## 版本沿革

v1 人类女医生 / v2 短毛写实小猫 / v3 短毛幼猫 / v4-v4b 橘白长毛（否） / v5 灰虎斑方向 / v6 印字失败轮 / **v7 空白胸牌+后期贴字（当前）**。
