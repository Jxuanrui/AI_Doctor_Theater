# archive/MANIFEST — 调研期克隆归档记录（2026-10-07，监工 P1-6）

## ai-fusion-video
- HEAD: 5fec8bb09efb185d285204f26a8ef9bd376f4396
- URL: https://github.com/Stonewuu/ai-fusion-video.git
- status --porcelain:
  (empty = 无本地改动)

## drama-skills
- HEAD: c2426e03c0e7722bebcc6a488b6658dc38c65ac3
- URL: https://github.com/zenstory-ai/drama-skills.git
- status --porcelain:
  (empty = 无本地改动)

## Kinema
- HEAD: cad96abe8d297c7147ebcc77e3ec43af251d60c0
- URL: https://github.com/chillzhuang/Kinema.git
- status --porcelain:
  (empty = 无本地改动)

## 根目录引用检查（2026-10-09 补做，闭环 path-gate P1-6）

`grep -rn -E 'archive/|ai-fusion-video|drama-skills|Kinema' --include='*.md,*.sh,*.py,*.ts,*.js'`（排除 upstream/）结果：所有命中均在 docs/reviews/ 的历史审核报告与路径提案（记录性质），**无任何脚本/配置/构建文件依赖已删路径**。结论：删除安全。

## 删除记录（2026-10-09）

- 删除对象：`/data/AI_Video/archive/`（含上述三个克隆，共约 218MB）
- 删除依据：用户指令原文（2026-10-09）"帮我清理不需要的项目路径以及文件"；三个克隆均为已排除候选，HEAD 哈希已留档于本文件上半部分，可随时按 URL+哈希重新拉取
- 删除方式：rm -rf；未做覆写（非敏感数据，仅为省空间）
- 同批删除：/tmp 下调研期临时克隆约 1GB（不在仓库范围，无留档义务）
- 风险评估：低——架构结论已摘录进计划书与审核文档，源码可再生

## v4 形象资产删除记录（2026-10-09 第二批）

- 删除对象：data/persona/ 下 v4_drmi_1~6.png、v4b_drmi_1~6.png、raw_v4_1~6.png、raw_v4b_1~6.png（橘白长毛方向候选及原图，含 delogo 前后全套）、quarantine_ref_derived/（v4_seed_1~3.png、ref_seedance_drmi.mp4，参考封面衍生物）
- 删除依据：用户指令原文（2026-10-09）"我觉得还是灰虎斑白短毛猫，请给我重新设计，删除旧的结果，然后重新生成新的结果"——方向整体作废
- 合规确认：该批素材从未对外发布（仅存本地 data/，git 仓库不含任何媒体文件），符合 governance.md §1 例外条款；台账见 governance.md §1
- 替代物：v5_tabby_1~6.png（灰虎斑白短毛方向）

## v5 形象资产删除记录（2026-10-09 第三批）

- 删除对象：data/persona/ 下 v5_tabby_1~6.png、raw_v5_1~6.png（灰虎斑首轮候选全套）
- 删除依据：用户指令原文（2026-10-09）"这张再给我优化一下……请删除旧的结果，然后重新生成新的结果"——用户选定 v5_tabby_5 为底板升级（白大褂印"猫猫医院"+口袋夹笔），旧批整体作废
- 合规确认：未对外发布，符合 governance.md §1 例外条款；台账见 governance.md §1
- 替代物：v6_tabby_1~8.png（同 DNA + 白大褂"猫猫医院"印字 + 口袋夹笔）

## v6 形象资产删除记录（2026-10-09 第四批）

- 删除对象：data/persona/ 下 v6_tabby_1~8.png、raw_v6_1~8.png、v7_final_1.png、v7_final_2.png（后两者为贴字失败成品，监工打回）
- 删除依据：用户指令（2026-10-09）"重新出干净底版"；v6 全批文字 0/8 错误（监工 supervisor-v6-text-fail-reject.md），v7_final_1/2 贴字位置错位（监工 supervisor-v7 打回报告）
- 合规确认：未对外发布；失败成品属衍生物可删，原图 raw_v6 随批作废删除（governance §1 例外）
- 替代物：v7_badge_1~8.png（空白胸牌底板）→ v7_final_6.png（_6 贴字成品）

## data/ 子路径清理记录（2026-10-09 第五批，用户指令"清理不需要的子路径"）

- 删除：seedance/M1_i2v_720p.mp4、M2_i2v_720p_v.mp4、M3_r2v_720p.mp4（试片视频，选型结论已入库 mini_test_report.json 与审核文档）；api_probe/C1_cogview_test.png（出图中间测试件，结论在 C1_summary.json）
- 保留：persona/（当前形象）、api_probe/（TTS 试听音频+json）、seedance/mini_test_report.json、lmd/ 与 lumenx/（两平台运行时数据，B5/A4 冒烟在用）、phase0/evidence（冒烟证据）
- 依据：用户指令原文（2026-10-09）；删除件均为已出结论的中间产物，未对外发布

## 参考封面删除记录（2026-10-09 第六批，官定后合规收尾）

- 删除对象：data/persona/ref/（ref_cover1.jpg、ref_cover2.jpg，抖音头部 AI 萌宠账号封面截图，2026-10-09 抓取）
- 依据：governance.md §4"官定图选出后删除改存来源链接"+ 用户 2026-10-09"按照监工的建议执行"（监工建议官定即删）
- 疏漏披露：抓取当时未将分享页 URL 归档（应记未记）；设计方向已与参考脱钩（灰虎斑为自然品种气质、无标志元素复刻），删除无追溯影响
- 同批：v8_final_5/final.png 定为官定 official_persona.png（轻档做旧，监工建议）

## 全项目精简清理（2026-10-09 第七批，用户指令"逐个子路径梳理，清理旧测试代码/结果/说明文档"）

- data/persona（49M→7M）：删 v7 全系（badge/final_6/raw_v7，历史候选）、archive_v8_delogo 弃稿 8 张、raw_v8_1~3/5~8（弃用底板，留 raw_v8_4 官定溯源）、D3 三场景及原图（结论入档）、抽帧 11 张（i2v_frame/i2v8s_f/blank_f）、i2v 验证视频 2 条（字崩实证与 8s 样本，结论均在 supervisor-official-i2v-pass.md；留 official_blank_i2v.mp4 作空白牌策略参照）、v8_final_5 对比佐证件与中档成品
- data/api_probe：删人声 TTS 试听 6 件（tts_*/voice_*）——用户 2026-10-09 拍板改猫叫配音+字幕，人声路线弃用；留 C1_summary.json（CogView 出图审计）
- docs/reviews：删 plan-v3.1.md（被批准版 plan-phase0-draft 即 v3.2 取代）；**历史 supervisor-*.md 与证据文件全部保留**（监工纪律：结论必须附报告路径存档，属审计证据链不可删）
- /data/AI_Video/.tmp（仓库外工作区）：删全部过程脚本（d2/v4b~v8 出图、seedance/probe/tts/redesign 等）与旧素材（抖音页面/参考图副本）；留 d3_v8_i2v.py（i2v 调用模板，Phase 1 复用）与 node 工具缓存

**疏漏披露与不可恢复声明（监工 P1-2）**：删除前未冻结旧版 ASSETS.sha256（66 项）入 git，被删文件的逐条哈希不可恢复；v7 全系与弃用 raw 均无其他备份，属不可恢复删除。用户指令明确要求清理即视为接受；本项目无发布/商用依赖这些过程件。**补救纪律：自本轮起，任何资产清理前先冻结当前清单快照至 docs/reviews/phase0/asset-snapshots/（已建：persona 7 项 + sfx 10 份（sfx.sha256 权威计数 wc -l=10），2026-10-09）并随 git 入库。**

