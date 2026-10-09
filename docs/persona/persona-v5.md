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
- 负向：cartoon, 3d render, illustration, chibi drawing, **long-haired cat, fluffy neck ruff, orange cat, ginger fur, calico, tan nose bridge, orange patch on face**, skinny cat, kitten proportions, any text, watermark, logo, **name tag, badge, pocket label**, deformed paws, extra limbs, two cats, oversmoothed fur, plastic texture, **two chest pieces**, duplicated stethoscope heads, stethoscope on both sides, **hard hat, safety vest**
- 关键负向：orange/ginger（防 CogView 对 tabby 默认串橘色）；tan nose bridge（v5 _3/_4 鼻梁橙斑教训）；two chest pieces（v4/v5_6 听诊器畸形教训）；hard hat/safety vest（防参考账号标志元素串入）；name tag/badge（v5_6 口袋红牌带字教训）
- 检查纪律（监工 v5 轮 P1#7）：候选图一律**逐张全检**，"一端耳件、一端单听头"为每张硬性检查项

## 候选与质检记录（主观目测属 candidate_research，以用户目视为准）

| 批次 | 文件 | 逐张质检（监工+执行方联合目测，2026-10-09；主观判断以用户目视为准） |
|---|---|---|
| v5（用户拍板灰虎斑首轮） | v5_tabby_1.png | **合格**：灰黑虎斑+白无串橘、听诊器结构可认（左听头右耳件）、白大褂完整、四肢正常 |
| | v5_tabby_2.png | **存疑**：听诊器绿管绕成圆环疑似第二听头，结构不清 |
| | v5_tabby_3.png | 小瑕疵：**鼻梁有一块橙棕色斑**；听诊器结构正确（Y 形分叉+双耳塞） |
| | v5_tabby_4.png | 小瑕疵：**鼻梁有一块橙棕色斑**；听诊器耳件呈横杆状可认 |
| | v5_tabby_5.png | **合格（六张最优）**：嘴鼻纯白、听诊器结构最标准（金属双管+黑色耳塞+单听头） |
| | v5_tabby_6.png | **不合格**：听诊器两端都是听头无耳件（v4 同款畸形）；口袋红色小牌疑似带字 |

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
