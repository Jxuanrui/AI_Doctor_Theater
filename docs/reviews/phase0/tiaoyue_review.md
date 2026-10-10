【方向审核请求】对标跳跃视界成片效果的优化方案（仓库根=/data/AI_Video/AI_Doctor_Theater）

用户指令：参考 tiaoyue.com（跳跃视界）设计逻辑，实现其成片效果；用户判断对方是 harness（模型同源）。
执行方产出：docs/reviews/phase0/tiaoyue-benchmark.md（调研结论+七项差距分解+A/B/C 三级复刻方案+验证方式）。
调研局限如实披露：对方产品信息仅来自 2026-08 凤凰网新闻稿（软文，单一来源 candidate_research），官网域名待售无法核实；差距清单基于通用 AI 短剧成片特征与 B5 实测推断。
方案要点：A 级零成本（运镜提示词库/B-roll 空镜+Ken Burns/BGM+猫叫混音/花字字幕/叠化转场/2-3s 节奏）；B 级小额（画质补偿+正式档 1 镜对比/片头片尾模板）；C 级工程（make_episode.py 一键流串联；转绘/画布明确不做——Ponytail）。验证：咖啡第一集重做新旧同框对比。

请审：A. 用户"对方=harness"判断与调研结论是否成立；B. 差距分解是否完整（有无漏项）；C. 三级方案是否合理（A 级并入 Phase 1 现有 P4/P6/P7/P8/P9 环节是否可行）；D. candidate_research 标注与单一来源局限是否如实；E. 是否放行呈报用户。按标准格式输出。
