# 主角人设表 v5（2026-10-09：灰虎斑白短毛猫医生 · v8 官定）

> **官定（2026-10-09，用户"按照监工的建议执行"）**：形象 = data/persona/official_persona.png（= v8_final_5/final.png，**轻档做旧**——监工建议：定妆图复用到视频选轻档；不加 heavy 档）；胸牌文字"住院猫医"；品牌名是否兼用待用户定。角色名与音色（tongtong/xiaochen）仍待用户拍板，不阻塞定妆。
> 参考封面 ref/ 已按 governance §4 于官定后删除（来源：抖音头部 AI 萌宠账号封面，2026-10-09 抓取；当时未归档分享链接——疏漏记录于 archive-manifest.md；设计已与参考脱钩，删除无影响）。
> 方向沿革：v4 橘白长毛（否）→ v5 灰虎斑方向 → v6 印字失败 → v7 空白牌+贴字 → v8 写实增强+做旧（官定）。

## 角色档案

- 角色名：**待定**（候选：Dr.灰 / 灰灰 / 毛毛 / Dr.Tabby；避开与参考账号谐音）
- 物种/品种：短毛灰虎斑白猫（头部/背部/两侧灰黑虎斑纹，白胸白口鼻白爪）
- 体型年龄：圆脸微胖成年猫
- 性格：温吞可靠、话痨科普、偶尔犯困（口头禅候选："别慌，听喵说"）
- 音色：**待用户拍板**（tongtong / xiaochen，GLM-TTS 已实测 data/api_probe/）
- 记忆点：圆脸大眼 / 灰白虎斑 / 白大褂+薄荷绿听诊器+**"猫猫医院"工作胸牌**（胸牌文字即记忆点之一）

## 视觉 DNA（v7 官定锚点块，英文，逐字复用）

`a short-haired gray tabby cat with a chubby round face, gray and black tabby stripes on the head, back and sides, solid white chest, white muzzle and white paws, big round yellow-amber eyes with gentle sparkle, pink nose, wearing a crisp white doctor coat with a small blank white name badge clipped on the chest pocket, the badge is plain and completely empty, and a mint-green binaural stethoscope draped around the neck with earpiece tubes on one side and a single chest piece on the other side`

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

## v8 写实增强轮（2026-10-09，用户"去 AI 痕迹"指令，当前官定候选）

- 底板：raw_v8_4（8 张中唯一空白卡正对镜头，监工看图选定）→ OpenCV TELEA inpaint 修水印（delogo 版 v8_real_1~8 有修补痕迹，已归档 data/persona/archive_v8_delogo/）
- 贴字：**"住院猫医"**（用户指令）连续单行完整贴字——管子与卡片无重叠（≥40px），"被听诊器挡字"在该底板物理上不存在（监工确认放弃，未编造坐标）；multiply 正片叠底随卡片明暗 + rotate(13°) 随卡片倾角 + blur 0.4
- **做旧后期管线**（去 AI 痕迹核心，光靠提示词不够）：降锐 0.25→R/B 微色差 1px→传感器噪点 σ2.2→暗角 5%→JPEG q85 往返；预设 light/medium 两档（脚本 PRESETS）
- 成品：data/persona/v8_final_5/final.png（轻档）/ final_medium.png（中档）+ 佐证件（zoom/inpaint_compare/compare_face/desk）
- 固化脚本：scripts/persona_badge_text.py（含通道互换相关系数门禁、采样色相门禁、边缘黑楔门禁、字可辨门禁，全部失败即退出；坐标仅适用 raw_v8_4）
- 管线教训入档：黑楔（rotate 空角必须填白）、通道互换（PIL/cv2 交界必须显式转 BGR）——见 supervisor-v8-4rounds-pass.md
- v7_final_6（猫猫医院版）保留为历史候选；胸牌文字以用户最新指令"住院猫医"为准

## 资产清单

- 定妆候选：v8_final_5/final.png（轻档）+ final_medium.png（中档）+ 佐证件 4 张
- 底板与留档：raw_v8_1~8（原图溯源）、v8_base_clean 在 v8_final_5/ 内、v7_badge_1~8 + v7_final_6（历史）、archive_v8_delogo/（delogo 弃稿）
- 参考材料：data/persona/ref/ref_cover1~2.jpg（官定后删除改存来源链接）
- sha256：data/persona/ASSETS.sha256（重算后为准）
- 音频：data/api_probe/voice_{tongtong,xiaochen}.{wav,mp3}（2026-10-09 修复：原文件为裸 PCM 假 mp3，已转 wav+标准 mp3 双格式）


## i2v 动态验证已知局限（2026-10-09 实测，监工看帧认定）

1. **胸牌中文必崩**：输入图已贴的"住院猫医"在第 1 帧起即崩成伪英文（"BERNAX/BERNVA"），全程无一帧保住。
   → **策略升格为正式纪律：视频生成阶段一律空白胸牌，身份用字幕/角标表达（默认）；仅定妆特写镜头用后期跟踪合成贴字**。
2. **眼色漂移**：琥珀眼随时间偏黄绿/橄榄绿（DNA 级特征漂移，多镜头会累积"不是同一只猫"感）——多镜头时每镜头抽帧对照官定图；i2v 提示词加 amber eyes 锚定。
3. **分辨率**：mini 档输出 640×640（低于 1024 输入）——Phase 0 冒烟继续用 mini 控成本，Phase 1 前做正式档对比再定。
4. 其他实测：毛色虎斑全程保持（未串橘/未变长毛）✓；动作自然无肢体畸形✓；D3 生成图中"指海报"类构图动作不可靠（s2 未达成）；s3 胸牌呈彩条不合格（胸牌道具统一为"口袋上的白色空白卡"）。

## DNA 补充硬约束（2026-10-09 监工 P1，防漂移）

- **眼色标准以官定图实测为准**：DNA 中 amber eyes 改为 **yellow-amber eyes**；每镜头抽帧须对照色卡 data/persona/eyecolor_card.png（官定图眼部裁图）比对，不得用抽象"琥珀"越推越暖
- 白色鼻梁纹贯通到口吻（solid white blaze extending from nose bridge to muzzle）
- 禁止耳缘出现暖橙色（负向加 warm orange ear rims, orange ear edges）
- 爪垫红斑入负向（red paw pads）防误读为伤口
- i2v 运动提示词须含 yellow-amber eyes 锚定

## 视频用空白牌底图（2026-10-09 新增资产，监工 P1-2）

- **official_persona_blank.png**：raw_v8_4 → TELEA 修水印 → 轻档做旧（参数同官定），**未贴字**——"视频一律空白胸牌"纪律的可执行输入图
- 空白牌保持性实测（official_blank_i2v.mp4 + blank_f0/1/2/3_9 帧）：程序检测胸牌区暗像素 0.2%→14.7%→21%→5%（首帧干净，后续出现暗区），系伪文字或阴影/管移动待监工看帧判定（结论见审核存档）

## 待用户拍板

1. **角色名**：Dr.灰 / 灰灰 / 毛毛 / Dr.Tabby / 其他（"住院猫医"是否兼作账号/品牌名也请一并定）
2. **音色**：tongtong / xiaochen（试听 data/api_probe/voice_*.{wav,mp3}，已修复可播）
3. **视频文字策略确认**（监工建议默认）：视频统一空白胸牌+字幕/角标表达身份，特写镜头后期跟踪贴字——请确认或改选
4. Phase 1 前做 Seedance 正式档（非 mini）画质对比，再定成片档位

## AI 标识纪律

见 docs/governance.md §1（素材层原图留档、成片层显式标识、delogo 台账）。

## 版本沿革

v1 人类女医生 / v2 短毛写实小猫 / v3 短毛幼猫 / v4-v4b 橘白长毛（否） / v5 灰虎斑方向 / v6 印字失败轮 / v7 空白胸牌+后期贴字 / **v8 写实增强+做旧（官定 official_persona.png，轻档）**。
