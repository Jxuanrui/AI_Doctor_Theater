# 主角人设表 v5（2026-10-09：灰虎斑白短毛猫医生）

> 方向变更记录：v4 系橘白长毛方向经用户目视后被否（2026-10-09 用户拍板："我觉得还是灰虎斑白短毛猫"），
> v4/v4b 全部候选与 raw 原图、Seedance 隔离衍生物已删除（台账见 docs/governance.md §1）。
> 参考锚点：抖音某头部 AI 萌宠账号封面猫（**白底+灰黑虎斑、短毛、圆脸大眼**；该账号作品为 AI 生成）。
> 设计原则"取神不取形"：只取品种气质，不复刻安全帽/荧光背心/电钻/白鹅等标志元素，名称亦不复用。

## 角色档案

- 角色名：**待定**（"Dr.咪"因与参考账号名混淆已弃用；灰猫候选名：Dr.灰 / 灰灰 / 毛毛 / Dr.Tabby，待用户选）
- 物种/品种：短毛灰虎斑白猫（头部/背部/两侧灰黑虎斑纹，白胸白口鼻白爪）
- 体型年龄：圆脸微胖成年猫，短毛紧密
- 性格：温吞可靠、话痨科普、偶尔犯困（口头禅候选："别慌，听喵说"，定妆后共创）
- 音色：**待用户拍板**（候选 tongtong / xiaochen，GLM-TTS 已实测，见 data/api_probe/）
- 记忆点：圆脸大眼 / 灰白虎斑配色 / 白大褂+薄荷绿听诊器（自然系记忆点，弱于标志物；如需强化后续加固定配饰，如小圆眼镜/名牌）

## 视觉 DNA（v5 官定锚点块，英文，逐字复用）

`a short-haired gray tabby cat with a chubby round face, gray and black tabby stripes on the head, back and sides, solid white chest, white muzzle and white paws, big round amber eyes with gentle sparkle, pink nose, wearing a crisp white doctor coat, and a mint-green binaural stethoscope draped around the neck with earpiece tubes on one side and a single chest piece on the other side`

- 质感配方（v4b 验证有效，沿用）：sitting at a wooden clinic desk looking straight at camera, candid amateur DSLR photograph, 50mm lens, shallow depth of field, soft natural window light from the left, warm white balance, visible film grain, authentic natural texture, imperfect fur clumps, slightly wrinkled fabric, photorealistic real photo
- 场景块：cozy clinic interior with blurred shelf of medical books and a potted plant in uneven natural bokeh
- 服装细节（v6 新增，用户 2026-10-09 要求）：白大褂左胸印中文"**猫猫医院**"四字；胸前口袋**夹一支笔**。提示词写法：`wearing a crisp white doctor coat with the Chinese characters 猫猫医院 clearly printed on the left chest, a pen clipped in the chest pocket`
- 负向：cartoon, 3d render, illustration, chibi drawing, **long-haired cat, fluffy neck ruff, orange cat, ginger fur, calico, tan nose bridge, orange patch on face**, skinny cat, kitten proportions, **watermark, garbled text, misspelled characters, extra Chinese characters**（v6 起不再用 any text——与想要的印字冲突，改为防乱码/防多余字）, deformed paws, extra limbs, two cats, oversmoothed fur, plastic texture, **two chest pieces**, duplicated stethoscope heads, stethoscope on both sides, **hard hat, safety vest**
- 关键负向：orange/ginger（防 CogView 对 tabby 默认串橘色）；tan nose bridge（v5 _3/_4 鼻梁橙斑教训）；two chest pieces（v4/v5_6 听诊器畸形教训）；hard hat/safety vest（防参考账号标志元素串入）；garbled text（v6 印字核心风险）
- 检查纪律（监工 v5 轮 P1#7 + v6 事故修订）：候选图一律**逐张全检**，硬性检查项：①胸口文字逐字正确（须裁剪放大对照）②"一端耳件、一端单听头"③灰黑虎斑无串橘④口袋元素如实核对；**视觉质检串行单图单调用+文件名与 sha256 前 8 位回带校验**，执行方结论须监工看图复核方可放行

## 候选与质检记录（主观目测属 candidate_research，以用户目视为准）

### v6"猫猫医院"升级轮（2026-10-09，v5_tabby_5 底板 + 白大褂印字 + 口袋夹笔，用户指令）——**全批不合格（监工打回）**

监工逐张看图结论（以监工报告 docs/reviews/phase0/supervisor-v6-text-fail-reject.md 为准；执行方初检因结果错位全部作废）：

| 图 | 胸前文字 | 夹笔 | 听诊器 | 结论 |
|---|---|---|---|---|
| v6_tabby_1 | 两行乱码 | 无 | 看不到听头 | **不合格** |
| v6_tabby_2 | 只有两字笔画错缺"医院" | 无 | 正常 | **不合格** |
| v6_tabby_3 | 形近"福猫"+杂符 | 无 | 正常 | **不合格** |
| v6_tabby_4 | 四字全变形 | 无 | 两端耳件无听头 | **不合格** |
| v6_tabby_5 | **"猫医院"三字（少一"猫"），字形基本正确** | 无 | 正常 | 不合格（缺字），**最接近** |
| v6_tabby_6 | 乱码（被听诊器遮挡） | 无 | 两端圆盘听头无耳件 | **不合格** |
| v6_tabby_7 | 四字都有但"猫""院"变形 | 口袋无笔 | 正常 | 不合格，**最接近四字** |
| v6_tabby_8 | 上行像"**狗**"字 | 无法确认 | 正常 | **不合格** |

结论：扩散模型写中文字实测 0/8 命中，抽卡路线否决；待用户在"后期贴字/局部重绘"与"继续抽卡"间拍板（监工强烈建议前者）；若走后期贴字，可用 _5/_7 作底图修字。

### 质检机制修订（2026-10-09，v6 事故后）

- 事故：执行方单条消息**并行调用 4 个视觉模型**，返回数组顺序与调用顺序不对应 → 结论与文件编号错位（给 _6 的描述实为 _5 的画面）；且视觉模型对乱码宽容（把乱码"转录"成正确字）。连续第三轮质检失真（v4 评分高估 → v5 抽样漏检 → v6 全批错位）。
- 修订：
  1. 视觉质检一律**串行单图单调用**（一次一张，URL 与文件一一对应）；
  2. 每次送检请求带**文件名 + sha256 前 8 位**，回报原样带回才有效，对不上即作废重检；
  3. 文字类检查须**裁剪放大胸口区域后逐字对照**（猫/猫/医/院），"文字清晰"不算过；
  4. 执行方"全过"结论不能单独作为放行依据，须监工直接看图复核。

### 历史：v5 灰虎斑首轮（已删）

_1 合格 / _2 听诊器存疑 / _3 _4 鼻梁橙棕斑 / _5 六张最优（用户选为 v6 底板）/ _6 听诊器双听头+口袋红牌带字不合格。全批已按用户指令删除（v6 升级替代），详见 archive-manifest.md。

### 历史：v4/v4b 橘白长毛（已删）

v4 听诊器双听头畸形+插画感；v4b 修复轮合格但方向被用户否决。全批已删。

## 资产清单

- 定妆候选：v5_tabby_1~6.png（1024x1024，delogo 后；raw_v5_* 原图留档溯源）
- 参考材料：data/persona/ref/ref_cover1~2.jpg（仅供内部对照，禁止上传任何外部模型接口；官定图选出后删除改存来源链接）
- sha256 清单：data/persona/ASSETS.sha256

## 待用户拍板

1. **官定图**：可选范围 **_1 / _3 / _4 / _5**（_2 存疑、_6 不合格已排除）；监工目视推荐 **_5**（听诊器结构最标准、嘴鼻纯白）或 _1；_3/_4 有鼻梁橙棕斑小瑕疵
2. **专属记忆点**（监工新增）：纯"灰白猫穿白大褂"与参考账号同品种同类内容，易被当模仿号——是否加固定小配饰（小圆眼镜/固定名牌等）进 DNA，**建议在定官定图前决定**
3. **角色名**：Dr.灰 / 灰灰 / 毛毛 / Dr.Tabby / 其他（避开与参考账号谐音）
4. 音色 tongtong / xiaochen；口头禅共创
5. 定妆后：重跑 D3（3 场景一致性）+ Seedance i2v 动态验证（**逐帧检查毛色条纹是否保住**，监工风险预警 #2/#3）；参考封面随即删除改存来源链接

## AI 标识纪律

见 docs/governance.md §1（素材层原图留档、成片层显式标识、delogo 台账）。

## 历史版本

v1 人类女医生 / v2 短毛写实小猫 / v3 短毛幼猫 / v4~v4b 橘白长毛（用户否决，已删）→ **v5 灰虎斑白短毛（当前，用户拍板方向）**。旧文档 persona-v4.md 已随方向废弃删除，见 git 历史。
