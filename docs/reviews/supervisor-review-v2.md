> [已脱敏存档] 原件位于 /data/AI_Video/.secrets/AI_Doctor_Theater/supervisor-review-v2.orig.md（0600，不入库）。脱敏项：IP/用户名/主机名/同事服务端口 → <REDACTED:*>，其余与原件一致。
> 原件来源：2026-10-06 claude -p --agent supervisor 会话 stdout（原件 .secrets/AI_Doctor_Theater/supervisor-review-v2.orig.md）


# 监工审核报告

一、裁决【有条件通过】

方向可行：lumenx 作生成端底座站得住，无 GPU、无 Docker 两条硬约束均满足。但送审材料有 4 处与代码事实不符或自相矛盾，直接影响第 3 项（买哪家 API）和工作量估算。因此只放行 Phase 0，Phase 1–3 待关口 1 复审后再批。

放行条件：
1. 按第三节 P0-1 至 P0-4 修订送审材料后，再呈报用户拍板。
2. Phase 0 限时 1 天，只做部署和冒烟，不写适配器或转换器。
3. `/data/AI_Video` 我无读取权限（工具被拒），"合成端已有资产"这根支柱本次**未经监工验证**；关口 1 前须授权复核或提供摘录。

二、证据

**核实属实**

| 声明 | 证据 |
|---|---|
| lumenx 为 MIT | `lumenx/LICENSE:1-3` |
| LLM 支持 openai 分支并读 `OPENAI_BASE_URL` | `src/apps/comic_gen/llm_adapter.py:28,48-52` |
| `doubao.py` 存在但未接入 | 全仓搜索 `DoubaoModel|doubao` 仅命中 `src/models/doubao.py` 自身 |
| catalog 共 8 个家族 | `config/model_catalog/families/` 下 8 个 YAML |
| TTS 含 Momo / Mochi / Bunny 音色 | `src/audio/tts.py:62,71,74` |
| 15 个风格预设，无 Q版预设 | `style_presets.json`；chibi 仅出现在 negative_prompt（:118,:133） |
| 字幕参数收了未实现 | `api.py:3519-3521` |
| 无数据库、无 Redis | `src/` 搜索 sqlite/redis/sqlalchemy 等 0 命中 |
| 可免 Docker 原生启动 | `start_backend.sh:19`（uvicorn） |
| drama-skills 用 Remotion 渲透明 VP8+alpha 叠层 | `short-drama-edit/assets/remotion/README.md:35` |
| dramaclaw 为 Elastic 2.0 且须保留 "Powered by" | `dramaclaw/README.md:51-53,459` |
| ai_story 有 2026-10-30 时间锁 | `research_aistory/backend/apps/agent/views.py:25` |
| LocalMiniDrama 为 MIT，含字幕后处理与 TTS 服务 | `LICENSE:1-3`；`mergedEpisodePostProcess.js`、`ttsService.js` 存在 |

**与文件事实冲突（以文件为准）**

1. **"Seedance 注册只需 1 行 + 1 YAML"不成立。**
   - `factory.py` 的 `ModelFactory` 全仓无任何调用方，是死代码。
   - 真实视频路由硬编码在 `pipeline.py:3264-3334`，只有 mulerouter、kling、vidu 和默认 wanx 四个分支。
   - 后端白名单固定为 `("dashscope","vendor","mulerouter")`（`provider_registry.py:7`），catalog 校验会拒绝新后端（`model_catalog.py:85,126`）。
   - `doubao.py` 是半成品：写死 720p/5 秒（:71），轮询无超时（:86-111）。

2. **"唯一缺口是字幕烧录"与材料自身风险 1 矛盾，也与代码矛盾。**
   - 出图只有 DashScope（`models/image.py:9-10,50`）；全仓无 Seedream 适配器，仅设计稿 HTML 提及。
   - TTS 只有 DashScope（`tts.py:128-132`，`audio.py:148`）；无豆包 TTS。
   - 按材料首选的火山方舟，出图、视频、配音三条链路都要新写适配器，而自研清单只列了视频那"1 行"。

3. **"requirements.txt 无 torch"有误导。**
   - `requirements.txt:28` 含 `demucs>=4.0.0`，它会传递安装 torch【candidate_research，未查 PyPI 元数据】。
   - 后端启动即起线程下载 htdemucs 权重（`pipeline.py:109,2516-2526`），失败只记 warning。
   - CPU 可跑的结论大概率仍成立。`requirements-docker.txt` 不含 demucs 和 pywebview，可作精简安装基线（待 Phase 0 实证）。

4. **备案日期表述错乱。** 今天是 2026-10-06。§2.4 写"2026-04-01 起先备案后上线"，§5 第 4 项却写"需 2026-04-01 前备案"，风险 4 又称"有时间风险"。若新规属实，它已生效半年，是现行门槛而非未来风险。

**未验证（不得当作已核实呈报）**

- `/data/AI_Video/` 下的 anything2explainer、`分镜表.md`、`glm_call.py`：读取被拒。
- Python 3.12 是否已装：`/usr/bin` 读取被拒。材料只称本机有 3.13.13，lumenx 目标是 3.11（`pyproject.toml:3`）。
- GLM "配置级接入"是否真通：
  - `openai` 包在 `requirements.txt:35` 被注释，需手动安装。
  - 现有密钥是 Anthropic 兼容端点，lumenx 需要 OpenAI 兼容端点，同一 token 能否通用未测。
  - `response_format` JSON 约束（`llm_adapter.py:136-137`）GLM 是否支持未测。
  - `qwen_vl.py:47` 仍直连 DashScope。
- Toonflow、ai-fusion-video、Kinema、shuohao、LingGuo、CineGen 各项声明：未抽查。
- 全部价格、音色效果、Vidu 口碑、广电与四部门规定：维持 candidate_research。

三、改进方案

**P0 必改（均针对 `/tmp/supervisor_review/ai_manga_drama_plan.md`）**

- **P0-1** 重写 §3 自研清单与 §4 工时。删去"1 行 + 1 YAML"，如实列出火山路线需新增的图像、视频、TTS 三个适配器及路由和白名单改动，或改走 P0-2。
- **P0-2** §5 第 3 项补一条"DashScope 优先"备选并比较。lumenx 原生一把 `DASHSCOPE_API_KEY` 即覆盖出图、视频、TTS，适配器零自研（`README.md:158`）。材料自称 Q版口碑最佳的 Vidu 也能经 DashScope 代理调用（`provider_registry.py:161-204`）。这才符合"优先成熟轮子"。
- **P0-3** 修正 §2.2 "无 torch"表述，修正 §2.4、§5、§7 的备案日期逻辑。
- **P0-4** §3 "lumenx 是唯一同时满足五项"缺少对 LocalMiniDrama 的反证。材料自己的表格显示后者"无明显缺口、0 代码接 GLM"。须补它在"三视图定妆/资产锁定"和"声明式风格"两项上的代码级证据，或在 Phase 0 并排冒烟。

**P1 强烈建议**

- **P1-1** 增设"零号候选"基线：现有 anything2explainer 加一个出图步骤，不引入新平台。若默认走 Remotion 有限动画而不出视频，lumenx 的视频、时间线、合成、配音分离能力基本闲置；需说明它的 GUI、资产锁定、抽卡值不值得引入整个平台。
- **P1-2** "口型档位/眨眼贴图"是未验证的关键假设。AI 出的分镜图是扁平位图，逐镜姿态不同，贴图需要逐镜人脸定位和风格匹配。Phase 1 先做半天验证；退路是整帧表情变体加镜头推拉。
- **P1-3** 部署细节：
  - 无头机不要用 `npm run dev`（`package.json:7` 带 open-browser 和 `--kill-others-on-fail`），应分别启动前后端。
  - `start_backend.sh:19` 绑定 `0.0.0.0` 且带 `--reload`，共享主机上建议改绑 127.0.0.1。
  - Settings 页会写 `~/.lumen-x/config.json`（`README.md:169`），属于项目路径外写入，须告知用户。
- **P1-4** 决策记录固定 lumenx 提交号 `f2a02e2`（`.git/packed-refs:2`）。`/tmp` 易失，关键证据须摘录到稳定路径。

**P2 建议**

- Q版风格先试界面自定义风格（`api.py:3556` 的 `custom_styles`），不行再往 `style_presets.json` 加条目。措辞应为"新增一条 preset"而非"新增一个 JSON"，且需配缩略图。
- 合规关键词过滤只是辅助，不能当作医学事实正确性的保障写进验收标准。

四、待用户拍板

| # | 事项 | 通俗解释 | 监工建议 |
|---|---|---|---|
| 1 | 底座选 lumenx 还是 LocalMiniDrama | 用哪个开源项目当平台骨架 | 倾向 lumenx，但先补 P0-4 对比证据；同时把"现有 Remotion 流水线加出图步骤、不引新平台"列为零号基线，关口 1 用实跑结果定 |
| 2 | lumenx 克隆进 `/data/AI_Video` 的路径 | 上游代码放哪 | 上游仓库自带测试和文档，与"不污染项目路径"有张力。建议放独立的第三方目录（如 `vendor/lumenx` 或 `/data` 下同级目录），固定提交号。目录现状我未能读取，名称由用户定 |
| 3 | API 供应商与预算 | 花钱买哪家的生图、视频、配音 | 建议改为 DashScope 优先：一把 key 全覆盖、零适配器。火山方舟降为备选，仅当 Q版一致性抽样证明不够用时再投入。价格均未核实，申请前请看官方价目 |
| 4 | 内容形态：剧集式还是单条科普 | 做连续剧还是独立小视频 | 建议先做单条。备案新规未经官方核实，若属实则已生效，剧集化前须自行查广电总局原文 |
| 5 | 医学事实审校 | AI 写的科普谁把关 | 建议设为对外发布的硬门槛：无医学专业人士复核则仅限内部演示 |
| 6（新增） | 发布主体资质 | 用什么账号、什么资质发 | 材料引述"无医疗资质不得发专业医疗科普"【candidate_research】。若属实，资质决定平台能否实际使用，应在 Phase 1 前确认 |
| 7（新增） | 批准范围 | 一次批四阶段还是只批第一步 | 建议只批 Phase 0（1 天），关口 1 后再批后续。10–14 人日的估算依据已被 P0-1 动摇 |
| 8（新增） | Remotion 商业授权 | 合成工具对公司使用可能收费 | `drama-skills/.../remotion/README.md:75` 称超出个人或小团队规模需商业授权【candidate_research】。若以机构名义运营，请先核对官方条款 |

五、下一阶段风险预警

1. **供应商错配导致工时失控。** 若坚持火山方舟，lumenx 的"配置级接入"优势基本作废，三个适配器加路由改造才是主要工作量，1–2 人日的估计明显偏低。
2. **有限动画路线未经验证。** 口型和眨眼贴图在 AI 生成的扁平分镜图上能否稳定对位，决定默认路线成立与否。失败则要回退到按秒计费的视频模型，成本结构随之改变。
3. **平台做成但发不出去。** 备案、医疗资质、医学审校三项都是外部依赖且均未核实。Phase 2–3 的合规工程应在第 4、5、6 项拍板后再启动。
