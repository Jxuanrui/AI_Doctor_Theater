【T0 清障销项请求】C2/E4/E5（仓库根=/data/AI_Video/AI_Doctor_Theater）

1. C2（GLM JSON 重测）→ 3/3 可解析（围栏剥离后）：原始输出已落盘 data/phase0/evidence/T0_c2_glm_json.txt（v1 裸解析 0/3，展示围栏问题）与 T0_c2_glm_json_v2.txt（剥离后 3/3，scenes=6/3/2）。结论：glm-4.7 + thinking disabled + max_tokens 4096 + 剥离 ```json 围栏，剧本环节解锁。
2. E4（空白牌判定补归档）→ 从 official_blank_i2v.mp4 重抽 4 帧：data/persona/e4_blank_f0/1/2/3_9.png。请看帧出判定原文（伪文字有无、空白牌保持与否）——此判定将作为 E15 要求的"监工原文"归档。
3. E5（眼色稳定性）→ 8s 样本已随精简删除（如实披露，不可再审）；改用 scripts/i2v_template.py 重生成 4s 眼色锚定样本 data/persona/e5_eye_i2v.mp4（模板自动追加 yellow-amber 锚定句），抽帧 e5_eye_f0/1/2/3_9.png。请判定：眼色琥珀是否全程保持、漂移四项（眼色/脸型/鼻梁纹/头身比）程度。
4. r2v 重测：按你 3.1"Phase 1 不用 r2v 可跳过"跳过（P5 默认官定底图+CogView 场景图路线），在关口 1 材料中如实记"r2v 未验证"。
裁决：T0 是否销项放行（B5 ∥ A4/A5 开工）。按标准格式输出（判定原文将入 phase0 存档）。
