# Q版人设表 v0（Phase 0 / D1）

> 绑定第一条科普主题：《肠道菌群》（复用 `projects/microbiome` 题材与事实清单）。
> 纯文字版，不附图片；图片产物落 `data/persona/`（不入库），manifest 记录模型/seed/费用。
> ⚠️ lumenx 自带风格预设把 chibi/Q版放进了**负向提示词**（style_presets.json:118,133，v2 审核已核实）——
> 出图一律走自定义风格（custom_styles / custom preset），不得套用官方预设。

## 通用画风（全局锁定，每个提示词都要带）

- 中文：Q版三头身比例，圆润软萌，厚描边扁平插画风，柔和糖果色，干净浅色背景，儿童医学科普绘本风格，无阴影渐变
- 英文（positive）：chibi style, 3-head-body proportion, soft round shapes, thick clean outlines, flat pastel candy colors, children's medical picture-book illustration, simple light background, no gradients
- 反向（negative）：写实, 恐怖, 血腥, 暴露, 阴暗, 复杂纹理, 3D 渲染, 照片质感, 文字, 水印, 长手指 / realistic, horror, gore, nsfw, dark, 3d render, photorealistic, text, watermark, complex textures
- **硬规则：图内禁止出现任何文字/数字/字母**（文字全部由代码层绘制——QC 第 3 优先级要求逐字核对）

## 角色一：豆豆医生（Dr. Doudou）—— 主讲人

| 项 | 设定 |
|---|---|
| 身份 | 年轻女医生，白大褂，讲科普的"团长" |
| 配色 | 白大褂 + 薄荷绿听诊器 + 蜜桃粉腮红；头发深棕双丸子头 |
| 标志物 | 胸前听诊器（薄荷绿）；左胸口袋插一支橙色体温笔 |
| 比例 | 三头身；大圆脸、大眼睛、小短手 |
| 性格镜头语言 | 讲解时单手比"OK"，惊讶时头发丸子会翘起 |
| 中文提示词 | Q版三头身年轻女医生豆豆医生，深棕双丸子头，白大褂，薄荷绿听诊器挂在胸前，左胸口袋橙色体温笔，大眼睛圆脸腮红，糖果色扁平插画风，儿童医学科普绘本风格，浅色干净背景，全身像 |
| 英文提示词 | chibi 3-head-body young female doctor, dark brown double bun hair, white coat, mint-green stethoscope, orange thermometer pen in chest pocket, big round eyes, blush, flat pastel illustration, children's medical picture-book, clean light background, full body |

## 角色二：菌小宝（Bacto）—— 肠道菌群拟人（ Beneficial gut flora ）

| 项 | 设定 |
|---|---|
| 身份 | 益生菌拟人，豆豆医生的"小跟班"，一队出现时同款不同色 |
| 配色 | 奶黄色胶囊形身体 + 奶白肚皮；腮红蜜桃粉；小手小脚奶白 |
| 标志物 | 头顶一片小绿叶（"好菌"徽章）；开心时头顶绿叶会发亮 |
| 比例 | 二头身胶囊形，无脖颈 |
| 性格镜头语言 | 得意时叉腰，委屈时缩成一颗胶囊 |
| 中文提示词 | Q版二头身益生菌拟人菌小宝，奶黄色胶囊形身体奶白肚皮，头顶一片小绿叶徽章，大眼睛蜜桃粉腮红，小短手小短脚，糖果色扁平插画风，儿童医学科普绘本风格，浅色干净背景，全身像 |
| 英文提示词 | chibi 2-head-body probiotic mascot, cream-yellow capsule body with white belly, small green leaf badge on head, big eyes, peach blush, tiny arms and legs, flat pastel illustration, children's medical picture-book, clean light background, full body |

## 角色三：球球（Suga）—— 糖分/坏习惯拟人（反派担当）

| 项 | 设定 |
|---|---|
| 身份 | 多余糖分拟人，圆滚滚的捣蛋鬼（不恐怖化，只"贪吃贪玩"） |
| 配色 | 棉花糖粉身体 + 深粉描边；嘴角常挂糖渍 |
| 标志物 | 怀里抱一颗比自己脸还大的棒棒糖 |
| 比例 | 二头身圆球 |
| 性格镜头语言 | 得意打滚；被教育后瘪嘴 |
| 中文提示词 | Q版二头身糖分拟人球球，棉花糖粉色圆球身体深粉描边，抱着超大棒棒糖，坏笑大眼睛，糖果色扁平插画风，儿童医学科普绘本风格，浅色干净背景，全身像 |
| 英文提示词 | chibi 2-head-body sugar mascot, cotton-candy pink round body with darker pink outline, hugging an oversized lollipop, mischievous grin, big eyes, flat pastel illustration, children's medical picture-book, clean light background, full body |

## 出图计划（D2 预告，待 C1 钥匙到位）

- 每角色 5–10 张：提示词固定、只换 seed；总量 ≤ 40 张（监工止损线）
- 模型：DashScope qwen-image（C1 实测通过后）
- 产物：`data/persona/<角色>/seed_<n>.png` + `data/persona/manifest.csv`（文件、模型、提示词哈希、seed、延迟、费用）
- 一致性测试（D3）：每角色选 1 张定妆 → lumenx 三视图 / LMD 参考图各出 3 姿态 → 评分表（角色辨识度/配色一致/比例一致/医学形象不失真/无恐怖谷，1–5 分）

## 合规红线（写进提示词生成器的硬约束，v3.1 计划 §2.4）

- 不出现具体药品商品名/医疗器械品牌；不做疗效承诺；不贩卖医疗焦虑
- 形象明显虚构非真人（Q版卡通），不扮演"数字真人医生"输出诊疗建议
- 成片须带"本内容为健康科普，不能替代诊疗意见"角标 + AI 生成标识（Phase 2 落地）
