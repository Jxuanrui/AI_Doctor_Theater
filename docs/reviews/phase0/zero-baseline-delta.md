# 零号基线改造点清单（Phase 0 / B6，案头分析）

> 分析对象：/data/AI_Video/anything2explainer（只读）。用途：底座选型的"不引新平台"对照项。
> 结论先行：总改造量 **M（约 2–4 人日）**；唯一框架级代码改动是 Footage.tsx 加图片分支（S 级）；
> 工时大头是 QC 判据校准与抽卡流程，不是代码。

## 一、现有流水线事实

- 八阶段 skill 编排（SKILL.md）；画面"全部代码绘制"是硬性原则（SKILL.md:15）
- 分镜链路：narration.txt → tts_build.py → timeline.json/src/common/timeline.ts → storyboard_src.md（时间令牌）→ render_storyboard.py（:21 正则替换令牌）→ 分镜表.md
- 分镜表 7 列格式（reference/narration-storyboard.md:77）；**selfcheck.py:16-17、frame_metrics.py:62-65、motion_check.py 都用正则 `^\| (SC\d\d)[^|]*\| (\d+)–(\d+) \|` 解析帧区间**——新列必须插在"帧"列之后
- 镜头组件：一镜一文件 src/shots/Gn/SCxx.tsx；组 index.ts 导出 SHOTS/BG/FOOTAGE 三表；Main.tsx:40-43 聚合
- **已有外部素材通道**：src/common/Footage.tsx 的 FootageSpec（:9-18，from/to/src/zoom/pan/blur/opacity/grade）+ FootageTrack（:45-53），z 序在幕底之上覆盖层之下（Main.tsx:17,24）；但只渲染 <OffthreadVideo>（Footage.tsx:38），**不支持静态图**
- 图片必须落 public/assets/<slug>/ 下才会进 bundle（staticFile 机制）；stills/ 只是自检截图目录、不进 bundle

## 二、插入 AI 出图的最小改动清单

**A. 出图通道（唯一必需的 common 层改动）**
- A1 Footage.tsx:38：按 spec.src 扩展名分支，png/jpg/webp 走 <Img src={staticFile()}>（复用 objectFit/zoom/pan/DarkGrade），视频维持 OffthreadVideo（约 10–15 行，S 级）
- A2 Footage.tsx:9-18：srcFrom 对图片标注忽略；可选加 fit 字段
- A3 备选：各组 SCxx.tsx 内直接 <Img> 半幅嵌入（保"幕底常驻"风格约束时用）

**B. 分镜表协议**
- B1 narration-storyboard.md:77 加第 8 列"底图"（必须插在"帧"列之后，否则三个 QC 工具全断）
- B2 :78 全局约束加"AI 底图清单"（文件名/镜头/提示词/负向词/seed/模型/重试），图内禁文字
- B3 render_storyboard.py **零改动**（令牌正则与图片字段正交）
- B4 new_project.sh:19 顺带建 public/assets/$SLUG/img（一行）

**C. QC 判据放宽（最大工时项，M 级）**
- C1 frame_metrics.py:83,94-96,97-106,108-110,143-151：碎屑/柔光/主角尺度判据按矢量黑底调参，照片底图必误报 → 需逐镜头豁免机制 + 真实样片校准
- C2 agent-qc-rules.md:14：允许底图镜头全幅（DarkGrade 融入黑底）
- C3 motion_check.py:17-20 + agent-qc-rules.md:18-19：底图镜头强制保留代码层动词动作（保持"持续动作"硬原则）
- C4 selfcheck.py:90-105：assets/ 前缀豁免画面字面量扫描
- C5 agent-build-rules.md:19 措辞修订 + :18 补 <Img> 用法

**D. 政策文档**
- D1 SKILL.md:15/README_ZH.md:208：AI 生成底图合法来源条款（MANIFEST 字段扩为 模型+提示词+seed+重试）
- D2 SKILL.md:46,48：阶段 3 末圈定底图镜头；阶段 4 插入出图脚本环节
- D3 SKILL.md:58：交付说明加底图来源清单
- D4 prompts.md/agent-build-rules.md：构建与 QC prompt 同步
- D5 template/.gitignore：public/assets/*/img/ 取舍

**胶水件**：gen_images.py（DashScope 异步出图+落盘+MANIFEST，约 100–150 行，S）；抽卡重试循环（S–M）；seed/提示词管理就放分镜表文本（S，零代码改动）。

## 三、定位与风险（对比 lumenx / LocalMiniDrama）

1. 只换底、不换能力：产出仍是 MG 片，无视频化运镜/叙事分镜能力
2. 风格漂移结构性风险：黑底白线+紫重点+幕底常驻（SKILL.md:82-92）AI 图难以稳定复现；FootageTrack 为偶发 B-roll 设计，不是主画面通道
3. QC 工具链全线失真需重校准（C1）
4. 事实/文字风险：图内文字必乱码，提示词须禁文字、文字全部代码层画
5. "零新平台"打折扣：仍引入 DashScope 云依赖与阶段间人工抽卡环节
6. 优势：seed 全落盘可复现；改造量小于引入新平台的整合成本

**结论**：零号基线是最低成本对照锚点（S 级代码改动 + M 级流程/QC 修订即可验证真实成本），不宜作为最终形态。
