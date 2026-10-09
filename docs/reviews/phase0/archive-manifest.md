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

