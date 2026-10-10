【关口 1 补件复审（简报）】（仓库根=/data/AI_Video/AI_Doctor_Theater，commit 0f11393 已推送回读一致）

P0 五项落实：
1. 加权改正（gate1-materials.md）：式子分=表格分，成本维补分——LMD 6.30 / lumenx 5.40 / 自研 7.20；你的复核表（4.75/4.45/6.80）并列成表；底座结论改为"两种口径下自研均不低于 LMD"；前版算术错误声明作废。
2. 摩擦⑤按你原文改正（evidence+materials）：字幕与 TTS 绑死/猫叫与水印不依赖 TTS/缺 drawtext 为环境问题；并按你 P0-2 补跑 ¥0 验证（merge_id=3，burn_dialogue_audio=true 无字幕无水印）：后处理成功不跳过，但音轨身份不明（corr vs rhythm=0.0465 / vs 原声=0.0000 / RMS 3360，root cause 未深挖如实记摩擦）——LMD 猫叫轨路径实测未达可用；"Phase 1 零新代码"已删改。
3. 证据入 git：docs/reviews/phase0/gate1_evidence_v2.txt（相关性代码+结果 0.999663/v2 ffprobe/关服后 ss 无监听/stat 权限/泄露扫描工作区与全历史均 0 命中/上游 rev-parse 两哈希/补丁 md5/segments.json+cap.srt+wm.srt）；git add -f 已入提交。
4. ASSETS.sha256 登记至 26 项（含 b5/b5v2/vg_4），快照 persona-2026-10-10-v3.sha256 入库。
5. v3.3:10 改"待 U-A 追认"；哈希链补 governance 提交 5a9b4aa 与回读；materials 未销项清单更新。
P1：compose 序号改递增；水印 Alignment=7 实测呈现右上已注明；evidence 相关性改 0.999663 引用 raw。

请简报复核并给最终裁决一行：关口 1 PASS（呈报 U-A）或打回（理由）。
