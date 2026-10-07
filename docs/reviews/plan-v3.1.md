> [已脱敏存档] 原件位于 /data/AI_Video/.secrets/AI_Doctor_Theater/plan-v3.1.orig.md（0600，不入库）。脱敏项：IP/用户名/主机名/同事服务端口 → <REDACTED:*>，其余与原件一致。
> 原件来源：执行方 2026-10-07 送审材料（/tmp 易失，原件已存 .secrets/AI_Doctor_Theater/plan-v3.1.orig.md）

# 送审材料 v3.1：医学科普 Q版 AI 漫剧平台 — 服务器画像 + 复扫修正 + 执行计划

2026-10-07 监工复审裁决：**有条件通过，批准进入 Phase 0**。以下 4 项条件已并入 §4（开工版）：
1. lumenx 无头启动二选一：冒烟期用 dev 双端口（3008+17177 各一条隧道，零代码改动）；或后续在上游目录外写 ~10 行启动脚本补挂 /static（禁止跑 main.py，pywebview 无头必挂；api.py 本身不挂 /static）
2. 监听地址一律 127.0.0.1：lumenx 禁用 start_backend.sh（0.0.0.0+--reload）；LocalMiniDrama 改 config.yaml server.host
3. 数据目录进 /data：设 LUMENX_DATA_DIR/LUMENX_LOG_DIR，工作目录在 /data 下启动（根分区已用 89%）
4. 密钥卫生（安全底线）：多用户共机前提成立；lumenx POST /config/env 无鉴权可改 key（api.py:1258）、LMD 明文打印 TTS key（ttsService.js:148）→ Phase 0 密钥必须设消费上限、文件权限 600、日志不落公共可读位置、LMD 本地补丁注释该行并登记

修订：2026-10-07。v2→v3 变更：①新增服务器实测画像与网页可达性甄别；②按代码复扫修正两处候选事实（lumenx 视频多厂商 / LocalMiniDrama 无 edge-tts）；③新增候选 huobao-drama、排除 BigBanana；④补充 /data/AI_Video 资产摘录（满足 v2 审核放行条件 3）。
代码基线：lumenx@f2a02e2（8-11 后停更，HEAD 复核无新提交）；LocalMiniDrama@755192a（10-02，1949★）。

---

## 1. 服务器画像（实测，证据见 /tmp/supervisor_review/server_probe_evidence.txt）

- 西柚云租用的 VMware 虚机 <REDACTED:hostname>：Xeon Platinum 8259CL（AWS 定制款【candidate_research：推断宿主为 AWS 裸金属】）48 vCPU / 755GB 内存 / /data 20TB（用 18%）/ Ubuntu 22.04.2，已运行 154 天
- **内网 NAT 形态**：ens160 仅私网 <REDACTED:internal-ip>/16，出口公网 <REDACTED:egress-ip>；本机 ufw 关闭
- 同事已在跑多个 web 服务（<REDACTED:port>/<REDACTED:port>/<REDACTED:port>/<REDACTED:port>/<REDACTED:port>），SSH 登录来源均为公网宽带 IP → SSH 通路存在（映射端口/VPN 机制待用户在西柚云控制台确认）
- **网页打开甄别结论**：
  - 服务器→外网：畅通（GitHub/各 API 可达）
  - 外网→服务器：**高位端口不可达**（18080 四国节点全超时；22 在出口 IP 上被拒；<REDACTED:port> 混合超时/拒绝）→ **无法直接 http://<REDACTED:egress-ip>:端口 访问**
  - 可用替代：A) SSH 隧道 `ssh -L 5679:127.0.0.1:5679`（零新增依赖，推荐）；B) VS Code Remote 端口转发（用户已在用 VS Code Remote，服务器上有 code 进程佐证）；C) 西柚云控制台申请端口映射（能力未知【candidate_research】）；D) frp/Tailscale（引入外部依赖，备选）

## 2. 候选事实修正（复扫代码级证据）

| 事项 | v2 说法 | v3 修正（证据） |
|---|---|---|
| lumenx 视频通道 | 仅 DashScope/mulerouter | **Kling/Vidu/MuleRouter(Seedance2.0) 均原生支持**（pipeline.py:3283-3320；playground/service.py:280-290；utils/endpoints.py:4-8 有各厂 BASE_URL env 覆盖） |
| lumenx 出图 | 仅 DashScope | 主路径 DashScope，gpt-image* 走 MuleRouter（assets.py:56-63）；TTS 仍仅 DashScope（tts.py:111-132） |
| LocalMiniDrama TTS | "最全，含 edge-tts 免费兜底" | **edge-tts 是虚假注释，未实现**：实际仅 minimax 与 openai 兼容 HTTP（ttsService.js:3 注释 vs 139-160 dispatch，else 直接抛错） |
| LocalMiniDrama 远程访问 | 未查 | 最优：纯相对路径 API（request.js:4-5 baseURL='/api/v1'），生产单端口 5679 同源伺服（app.js:69-85, server.js:20-21）；坑：storage.base_url 拼绝对 URL 需保持端口 5679（drama.js:25,153） |
| lumenx 远程访问 | 未查 | 生产=FastAPI 单端口 17177 伺服静态导出（main.py:80-82, next.config.mjs:12-15）；dev 双端口 3008+17177；坑：transport.ts:45,82 硬编码 localhost:17177，隧道须保持原端口号 |
| 两者鉴权 | 未查 | **均无登录/鉴权/多用户**（lumenx api.py 4863 行无 auth 中间件；LMD 无 login 路由）→ SSH 隧道内小团队可用，属可接受裸奔 |
| BigBanana-AI-Director | 候选之一 | **排除**：仓库无源码，仅 docker-compose 拉预构建镜像；我们无 Docker，且闭源不可审计 |
| huobao-drama（新） | 未评估 | 15.8k★，Nuxt3+Hono+SQLite，唯一显式支持远程部署（.env PUBLIC_BASE_URL）；**CC BY-NC-SA 禁商用** + 引流自家 API 中转（api.firemux.com）→ 仅当项目确认非商用时才值得深查 |

## 3. 选型与架构（v3，仍待 Phase 0 并排冒烟定案）

- 底座仍倾向 **lumenx**（三视图定妆/资产锁定/共享资产池仍是最贴合"Q版一致性"的差异化；视频多厂商支持恢复加分；停更 2 个月是减分项），LocalMiniDrama 次之（字幕烧录完成度、远程访问形态最干净；TTS 需接 minimax 或 openai 兼容端），零号基线（现有 Remotion + 出图步骤）作对照组
- **访问形态统一为 SSH 隧道/VS Code 端口转发单端口模式**：lumenx 走 17177（生产静态导出），LMD 走 5679（生产构建），端口保持原值
- API：DashScope key 仍是最小钥匙（lumenx 出图主路径 + 全部 TTS）；视频可按需另配 Kling/Vidu key（lumenx 原生支持）；LLM 外移 GLM（三验证不变：openai 包/v4 端点/response_format）
- 合规与医学科普红线：同 v2（AI 标识、资质、事实回链，不再展开）

## 4. Phase 0 执行计划（v3，四线并行 1 天，全部适配隧道访问）

- A线 lumenx 冒烟：Python 3.11/3.12 venv + `requirements-docker.txt` 精简安装；**不用 main.py**（pywebview 会拉 GUI，headless 必挂，agent 复扫描证实），用 uvicorn 起 17177 + 前端构建静态导出（或 dev 双端口）；改绑 127.0.0.1（不再 0.0.0.0，因公网不可达且无鉴权）
- B线 LocalMiniDrama 冒烟：Node + better-sqlite3 + sharp 原生装；生产构建单端口 5679；顺手验证 ffmpeg 走系统 PATH（utils/ffmpegPath.js 支持）；零号基线改造点清单
- C线 API 实测：DashScope（出图+TTS 各一次，记价格延迟）；GLM 三验证；如 lumenx 路线要视频再试 Kling/Vidu 官方 key（可不申请，先用文档评估）
- D线 Q版人设草案：Q版医生 + 2-3 器官拟人，DashScope qwen-image 各出 5-10 张候选
- 验收：四线产物 + 一页对比表（部署摩擦/GLM 接入/定妆入口/远程访问/许可）→ 🚦关口 1 送监工复审 → 定底座批 Phase 1

## 5. 待用户拍板（v3，10 项）

| # | 事项 | 监工建议栏 |
|---|---|---|
| 1 | 底座：lumenx / LocalMiniDrama / 零号基线（huobao-drama 仅当确认非商用才加入） | |
| 2 | 上游代码放置路径（新路径创建） | |
| 3 | API 钥匙：DashScope 为主 + 按需 Kling/Vidu；GLM 当剧本大脑 | |
| 4 | 内容形态：剧集式（备案门槛）vs 单条科普 | |
| 5 | 医学事实审校资源 | |
| 6 | 发布主体资质 | |
| 7 | 批准范围：仅 Phase 0 | |
| 8 | Remotion 商业授权核对 | |
| 9 | **网页访问方式**：SSH 隧道（推荐）/ VS Code 端口转发 / 西柚云控制台申请端口映射（需你在控制台确认有无此功能）/ Tailscale | |
| 10 | 服务器上已有同事的服务在跑（<REDACTED:ports> 等），部署新平台需避开端口冲突并告知团队——是否需要打招呼 | |

## 6. /data/AI_Video 资产摘录（履行 v2 审核放行条件 3）

- anything2explainer/README_ZH.md 摘录：「给一个主题，产出一条带配音的科普讲解视频……画面全部由 Remotion（React + TypeScript）代码绘制……agent 先做带出处的调研，写解说词，生成配音和帧级时间轴，逐镜头写分镜，再派多个构建 agent 并行写 Remotion 组件……渲染后由 QC agent 按书面判据逐帧检查」——具备分镜协议/TTS对齐/QC判据/多agent协议
- projects/microbiome/分镜表.md 摘录（表头）：「《肠道菌群》v2 分镜源表（3–5 分钟 / 3 章 / 38 镜头 / 8 构建组）……总帧数 7991 = 266.4s，1280×720@30fps，1186 字，5.16 字/s」——帧级时间轴协议在用
- tools/glm_call.py 摘录：「GLM 客户端（Anthropic 兼容端点），供 anything2explainer 流水线调用……支持 --image 视觉 QC」
- 结论：合成端支柱（Remotion 分镜/QC/TTS 对齐）真实存在，v2 材料第 2.3 节架构依据成立

## 7. 风险（v3）

1. 平台无鉴权 + 公网不可达：SSH 隧道内可用，但若未来要给更多人用需加 auth 或 Tailscale ACL
2. 西柚云端口映射能力未知：若控制台支持映射，公网直开网页仍需加鉴权 + HTTPS，否则拒绝暴露
3. lumenx 停更 2 个月：选它意味着"接手维护"，Phase 1 起的改造都要自己扛
4. DashScope 出图的 Q版一致性未实测（D 线验证）；不行则升级 Seedream（火山）需自研适配器（v2 已明示成本）
5. 根分区 89% 用量：部署一律进 /data，venv/npm 缓存指向 /data，避免写满根分区

## 8. 监工可核验路径

- 证据文件：/tmp/supervisor_review/server_probe_evidence.txt（本材料第 1 节来源）
- 代码克隆：/tmp/research_base/{lumenx, LocalMiniDrama, ...}（本材料第 2 节修正的核验点：lumenx pipeline.py:3283-3320 / tts.py:111-132 / main.py:80-82；LMD ttsService.js:139-160 / app.js:69-85 / server.js:20-21 / request.js:4-5 / utils/ffmpegPath.js）
- /data/AI_Video 资产：监工仍无读取权限，摘录见第 6 节；如需原文复核请用户授权
