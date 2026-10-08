# Q版人设表 v1（Phase 0 / D1，2026-10-08 重设计）

> 用户拍板：主角改为**可爱橘猫医生**（可爱橘猫 × 猫咪医生）。v0（人类女医生版）已删除，历史见 git。
> 绑定主题：《肠道菌群》。图片产物落 `data/persona/`（不入库）。
> **素材级水印处理**：CogView-4 出图自带右下角"AI生成"水印，流水线内统一裁除；
> AI 标识义务在**成片层**履行（发布作品统一标注，Phase 2 落实显式+元数据双标识）。
> lumenx 官方风格预设将 chibi 列入负向词（style_presets.json:118,133）——一律走自定义风格。

## 通用画风（全局锁定）

- 中文：Q版二到三头身，圆润软萌，厚描边扁平插画风，柔和糖果色，干净浅色背景，儿童医学科普绘本风格，无阴影渐变
- 英文（positive）：chibi style, 2-3 head-body proportion, soft round shapes, thick clean outlines, flat pastel candy colors, children's medical picture-book illustration, simple light background, no gradients
- 反向（negative）：写实, 恐怖, 血腥, 暴露, 阴暗, 复杂纹理, 3D 渲染, 照片质感, 文字, 水印, 长手指 / realistic, horror, gore, nsfw, dark, 3d render, photorealistic, text, watermark, letters, numbers, complex textures
- 硬规则：图内禁止任何文字/数字/字母（文字全部代码层绘制）

## 角色一：橘医生 Dr. Mikan（みかん=蜜柑）—— 主讲人（C位）

| 项 | 设定 |
|---|---|
| 身份 | 可爱橘猫医生，讲科普的"团长" |
| 体貌 | 橘色虎斑猫：橘色被毛 + 奶油色口鼻/肚皮/爪尖，耳尖与尾巴有深橘虎斑条纹；圆脸大眼（琥珀色大瞳）；三头身 |
| 服装/标志物 | 迷你白大褂 + 薄荷绿听诊器；左口袋插橙色体温笔；尾巴翘起带一个白色尾巴尖 |
| 性格镜头语言 | 讲解时竖起一根肉垫爪"敲黑板"；惊讶时耳朵竖直、尾巴炸毛成瓶刷；得意时眯眼微笑（^ω^） |
| 中文提示词 | Q版三头身可爱橘猫医生橘医生，橘色虎斑猫毛色奶油色口鼻肚皮，耳尖尾巴深橘条纹，琥珀色大眼睛圆脸腮红，穿迷你白大褂薄荷绿听诊器，左口袋橙色体温笔，尾巴上翘白尾尖，糖果色扁平插画风，儿童医学科普绘本风格，浅色干净背景，全身像 |
| 英文提示词 | chibi 3-head-body cute orange tabby cat doctor, orange tabby fur with cream muzzle and belly, darker orange stripes on ear tips and tail, big round amber eyes, blush, wearing a tiny white doctor coat with mint-green stethoscope, orange thermometer pen in pocket, upright tail with white tip, flat pastel illustration, children's medical picture-book, clean light background, full body |

## 角色二：菌小宝（Bacto）—— 肠道菌群拟人（跟班）

| 项 | 设定（沿用 v0，与橘医生同画风） |
|---|---|
| 体貌 | 二头身胶囊形：奶黄色身体 + 奶白肚皮；头顶小绿叶徽章；蜜桃粉腮红 |
| 性格镜头语言 | 得意叉腰；委屈缩成一颗胶囊；常趴在橘医生头顶 |
| 英文提示词 | chibi 2-head-body probiotic mascot, cream-yellow capsule body with white belly, small green leaf badge on head, big eyes, peach blush, tiny arms and legs, flat pastel illustration, children's medical picture-book, clean light background, full body |

## 角色三：球球（Suga）—— 糖分拟人（反派担当，不恐怖化）

| 项 | 设定（沿用 v0） |
|---|---|
| 体貌 | 二头身圆球：棉花糖粉身体 + 深粉描边；抱超大棒棒糖；坏笑 |
| 英文提示词 | chibi 2-head-body sugar mascot, cotton-candy pink round body with darker pink outline, hugging an oversized lollipop, mischievous grin, big eyes, flat pastel illustration, children's medical picture-book, clean light background, full body |

## 出图计划（D2 v1）

- 橘医生 6 张、菌小宝 3 张、球球 3 张（共 12，≤40 限额内；CogView-4，约 10s/张）
- 每张下载后 ffmpeg 裁除底部水印条（1024×1024 → 1024×976）；原图留 data/persona/raw/ 备查
- manifest.csv 记录：文件/角色/模型/耗时/尺寸/状态
- D3 一致性测试（定妆后 3 姿态）沿用评分表五维（辨识度/配色/比例/医学形象不失真/无恐怖谷）

## 合规红线（不变）

- 不出现药品商品名/器械品牌；无疗效承诺；不贩卖医疗焦虑
- 形象明显虚构（Q版橘猫），不扮演"数字真人医生"
- **成片发布必须统一 AI 标识**（用户已承诺）：画面显著标注 + 元数据（GB 45438-2025），Phase 2 管线落地
