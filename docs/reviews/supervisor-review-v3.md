> [已脱敏存档] 原件位于 /data/AI_Video/.secrets/medtoon/supervisor-review-v3.orig.md（0600，不入库）。脱敏项：IP/用户名/主机名/同事服务端口 → <REDACTED:*>，其余与原件一致。
> 原件来源：2026-10-07 会话 transcript + stdout 拼合（原件 .secrets/medtoon/supervisor-review-v3.orig.md）


# 监工审核报告

**审核对象**：送审材料 v3（`/tmp/supervisor_review/ai_manga_drama_plan.md`）及服务器实测证据（`server_probe_evidence.txt`）
**审核性质**：方向级事项只提建议；Phase 0 计划本身的质量问题，监工有否决权。

## 一、裁决

**有条件通过：批准进入 Phase 0，前提是下面 4 项开工前写进计划。**

两处事实修正经代码核验成立。服务器画像整体自洽。但核验中发现 v3 有 1 处事实缺口和 3 处计划漏洞。这几处不改，A 线会卡在启动，系统盘可能写满，密钥可能泄露。

- **条件 1（事实缺口）**：v3 说 lumenx 是"单端口 17177 伺服静态页面"，这只在官方入口 `main.py` 下成立。而 `main.py` 第 5 行就加载了 pywebview（图形窗口组件），无界面服务器上会直接报错。计划 A 线说的"用 uvicorn 起 17177 + 静态导出"不会把前端页面挂上去，打开网页只会 404。必须二选一写进计划：
  - (a) 开发模式双端口：3008 前端 + 17177 后端，开两条 SSH 隧道。不用改任何代码，**冒烟阶段推荐这个**；
  - (b) 在上游目录外另写一个约 10 行的极简启动脚本，补上 `/static` 挂载。
- **条件 2（监听地址）**：B 线没要求 LocalMiniDrama 只监听本机。它默认监听 0.0.0.0（对所有网卡开放），会暴露给 <REDACTED:internal-cidr> 整个私网。同时禁止直接用 lumenx 自带的 `start_backend.sh`，它也是 0.0.0.0 加热重载。
- **条件 3（数据目录）**：lumenx 的日志和用户数据默认写到 `~/.lumen-x`，生成产物写到"当前所在目录"下。根分区已用 89%，必须设置 `LUMENX_DATA_DIR`、`LUMENX_LOG_DIR` 指向 /data，并且在 /data 下启动。
- **条件 4（密钥卫生，安全底线不可删减）**：
  - 修正 v3 第 2 节"SSH 隧道内可接受裸奔"的前提。这台机器是多用户共用的，127.0.0.1 上的端口同机每个用户都能访问。
  - lumenx 修改配置的接口不用登录，任何人都能改写 API 密钥和接口地址。
  - LocalMiniDrama 会把 TTS 密钥明文打印到日志。
  - Phase 0 必须用设了消费上限的密钥，密钥文件权限设为 600，日志不要落到别人能读的位置。

## 二、证据

### 1. 事实修正核验（`/tmp/research_base/`）

**版本基线（成立）**
- lumenx 当前 commit 为 `f2a02e23…`（`lumenx/.git/refs/heads/main:1`），与材料一致。
- LocalMiniDrama 当前 commit 为 `755192a7…`（`LocalMiniDrama/.git/refs/heads/main:1`），与材料一致。
- 两者许可证均为 MIT（各自 `LICENSE:1`）。

**lumenx 视频支持多家厂商（成立）**
- `pipeline.py:3271-3279`：按模型名前缀分流到 Vidu 和 MuleRouter（Seedance）；Kling、Vidu 只在 `backend == "vendor"` 时启用。
- `pipeline.py:3281-3333`：分别调用 MuleRouter、Kling、Vidu 三个视频模型。
- `playground/service.py:279-290`：试验场同样按 seedance / kling / vidu 分流，其余走 wanx。
- `utils/endpoints.py:4-21`：四家厂商的接口地址都可以用 `{PROVIDER}_BASE_URL` 环境变量覆盖。

**lumenx 出图与 TTS（成立）**
- `assets.py:56-63`：`gpt-image` 开头的模型走 MuleRouter，其余走 Wanx。
- `tts.py:111-132`：`TTSProcessor` 只用 dashscope。全文件导入只有 dashscope 和 requests（第 128、198、262-263 行），没有其他 TTS 厂商。

**静态页面挂载（条件 1 的依据）**
- `main.py:80-81`：挂载 `/static` 的代码写在 `run_server()` 函数里面。
- `main.py:5`：文件开头直接加载 `webview`，无界面服务器上导入即报错。
- `api.py:103-113`：后端主程序只挂载了各个 `/files*` 路径，**没有挂 `/static`**。
- `next.config.mjs:14`：生产构建的页面路径前缀是 `/static`。
- `transport.ts:45,82`：前端写死后端地址为 `http://localhost:17177`。所以只要隧道两端端口号保持一致，双端口开发模式可以直接用。

**lumenx 鉴权与密钥（成立，并有新增风险）**
- `api.py` 共 4863 行，这一点属实。
- 全文件搜索 auth / Depends / token，只命中日志关键词和 mulerun 的 OAuth 登录，没有任何鉴权中间件。
- **新发现**：`api.py:1258` 的 `POST /config/env` 不用登录就能改写密钥和接口地址；`api.py:65-67` 从项目根目录的 `.env` 读取密钥并覆盖已有环境变量（`override=True`）。

**lumenx 数据目录（条件 3 的依据）**
- `utils/__init__.py:22-25`：默认数据目录是 `~/.lumen-x`。
- `api.py:96-113`：产物目录 `output/` 是相对当前所在目录的路径。

**lumenx 自带启动脚本（条件 2 的依据）**
- `start_backend.sh:19`：启动参数为 `--reload --host 0.0.0.0`。

**LocalMiniDrama 没有 edge-tts（成立）**
- `ttsService.js:3`：注释里写了支持 edge-tts。
- `ttsService.js:139-159`：实际只处理 minimax 和 openai 兼容接口，其他情况直接报错。
- 全仓搜索 "edge"，没有 edge-tts 的实现。

**LocalMiniDrama 密钥泄露（新发现）**
- `ttsService.js:148`：`console.log` 把 `ttsConfig.api_key` 明文打印出来。

**LocalMiniDrama 单端口、相对路径（成立）**
- `request.js:5`：前端请求地址为 `baseURL: '/api/v1'`（相对路径）。
- `app.js:66-85`：后端在同一端口同时提供页面和 API。
- `server.js:20`：默认端口 5679。

**LocalMiniDrama 监听地址（条件 2 的依据）**
- `server.js:21`：默认监听 `'0.0.0.0'`。
- `configs/config.yaml:8`：`host: 0.0.0.0`。
- `configs/config.yaml:22`：`base_url: http://localhost:5679/static`。这印证了 v3 说的"隧道必须保持 5679 端口"。

**LocalMiniDrama 的 ffmpeg 查找（成立）**
- `ffmpegPath.js:2-8,47`：最后会退回到系统 PATH 里找 ffmpeg。

### 2. 服务器画像是否自洽

**自洽的部分**
- 网卡 `ens160` 只有私网地址 <REDACTED:internal-ip>/16，出口 IP 为 <REDACTED:egress-ip>，确实是内网转换（NAT）形态（证据 §2）。
- 18080 端口四个外部节点全部超时，"无法用 http://出口IP:端口 直接打开网页"这个结论成立（证据 §5）。
- 推荐 SSH 隧道或 VS Code 端口转发，与以上事实一致。

**结论推得偏宽的地方（不影响最终结论）**
- 只测了 18080 和 <REDACTED:port> 两个高位端口，就推广为"高位端口不可达"。
- 出口 IP 不一定就是入口 IP。"SSH 经其他映射端口进入"只是推测，没有核实。
- 推荐方案不依赖这两点，所以不影响结论。

**没有被计划吸收的事实**
- **多用户共用**：同一台机器上有 3 个用户登录（证据 §4）。127.0.0.1 无法把同机用户隔开，这一点没有反映到安全前提里。
- **根分区占用**：根分区 89%（证据 §1）已列入风险 5，但没有落实到 lumenx 默认写 `~/.lumen-x` 这个具体位置上。
- **临时测试服务**：实测时临时开的 `python3 -m http.server 18080`，材料没说已经关掉。
- **端口冲突**：17177、5679、3008 三个端口不在现有监听列表里，**没有冲突**（证据 §3）。

### 3. v2 三条放行条件的履行情况

我找不到 v2 审核报告原文（`/tmp/supervisor_review/` 只有两个文件，`.claude/` 里搜不到相关记录），下面以你转述的三条为准。

| 条件 | 情况 | 判定 |
|---|---|---|
| 修订材料 | v3 第 3 行列出变更清单，第 2 节表格逐条修正 | ✅ 已履行 |
| Phase 0 限时 | 第 38 行写了"1 天"，但没写超时怎么止损，也没写费用上限 | ⚠️ 部分履行 |
| 资产摘录 | 第 6 节给了 3 段摘录，但我读取 `/data/AI_Video` 被拒，无法核对原文 | ⚠️ 已提供，未核验 |

## 三、改进方案

**P0 必改（即第一节的 4 个条件）**

| # | 整改内容 | 涉及文件 |
|---|---|---|
| P0-1 | §3 第 34 行、§4 A 线改写启动方式：二选一，(a) 开发模式双端口加两条隧道，或 (b) 在上游目录外另写启动脚本补挂 `/static` | v3 §3/§4 |
| P0-2 | B 线把 `config.yaml` 的 `server.host` 改为 `127.0.0.1`；A 线注明禁止用 `start_backend.sh` | v3 §4 |
| P0-3 | A 线写明 `LUMENX_DATA_DIR`、`LUMENX_LOG_DIR` 指向 /data，并在 /data 下启动；B 线确认存储目录在 /data | v3 §4 / 风险 5 |
| P0-4 | 改写 §2"可接受裸奔"表述，明确多用户本地暴露；密钥设消费上限；`.env` 和配置文件权限 600；LocalMiniDrama 日志不落公共可读位置，或在本地注释掉 `ttsService.js:148`（作为本地补丁登记） | v3 §2/§7 |

**P1 强烈建议**
- Phase 0 补充止损规则：单线超过 1 天就停止并记为"部署摩擦高"；同时给出总费用上限。
- C 线补一项核查：DashScope 的 TTS 能否接 LocalMiniDrama 的 openai 兼容通道（`ttsService.js:147`）【candidate_research】。不能接的话，LocalMiniDrama 路线还需要 MiniMax 密钥，"DashScope 一把钥匙走通"的说法要改。
- 证据和审核记录挪到稳定路径（跟拍板 #2 一起定）。`/tmp` 内容不稳定，v2 报告已经找不到了。
- 确认 18080 临时测试服务已关闭。

**P2 建议**
- 删掉"8259CL → 推断宿主为 AWS 裸金属"这句。它和本计划无关，还是未核实的说法。
- 第 6 节摘录需要原文复核时，请你授权监工读取 `/data/AI_Video`。

## 四、待用户拍板

| # | 事项 | 通俗解释 | 监工建议 |
|---|---|---|---|
| 1 | 底座选型 | 在哪个开源项目上改 | **Phase 0 跑完再定**，三方并排比。huobao-drama 默认排除：CC BY-NC-SA 许可禁止商用，还会引流到它家的 API 中转【candidate_research】 |
| 2 | 上游代码放哪 | 克隆下来的代码放哪个目录 | 放 `/data/AI_Video/upstream/` 一类位置。**不进 Maxmetagenome 仓库，也不长期留在 /tmp** |
| 3 | API 钥匙 | 用哪些付费接口 | 同意以 DashScope 为主、GLM 写剧本。Kling、Vidu 在 Phase 0 先不申请。**所有钥匙都设消费上限** |
| 4 | 内容形态 | 连续剧，还是一条一条的科普短片 | 先做单条科普，剧集化放到后面。剧集备案门槛【candidate_research】 |
| 5 | 医学审校 | 谁来把关医学事实 | 不卡 Phase 0，但**首条内容发布前必须有具名审校人** |
| 6 | 发布主体资质 | 用谁的名义发布 | 同上，发布前必须落实 |
| 7 | 批准范围 | 这次批准到哪一步 | **只批 Phase 0**：1 天、有止损规则、有费用上限 |
| 8 | Remotion 授权 | 现有视频合成工具的商用授权 | 发布前核对授权门槛【candidate_research】，不卡 Phase 0 |
| 9 | 网页访问方式 | 怎么在自己电脑上打开平台 | SSH 隧道或 VS Code 端口转发，两者效果一样。不建议开公网映射或 Tailscale，除非以后多人使用并且加了鉴权 |
| 10 | 告知同事 | 要不要跟同机同事打招呼 | **要**。这台机器多人共用，平台没有登录机制，本机端口同事都能访问。经核查 17177、5679、3008 目前没有端口冲突 |

## 五、下一阶段风险预警

1. **lumenx 无界面启动不是官方支持路径**：官方入口绑定了图形窗口组件，A 线很可能在启动方式上耗掉半天。先按 P0-1 的方案 (a) 双端口跑通，再考虑别的。
2. **多人共用机器 + 平台无登录 + 密钥明文**：同机用户能改写密钥或接口地址（`api.py:1258`），密钥也会打印进日志（`ttsService.js:148`）。必须靠消费上限兜底。
3. **根分区 89%**：lumenx 默认往家目录写。一旦写满，同事正在跑的服务会一起出故障。
