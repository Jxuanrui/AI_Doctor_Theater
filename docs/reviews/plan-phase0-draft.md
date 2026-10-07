> [监工规划草案] 2026-10-07 由监工（supervisor agent）应用户指派梳理，原文存档自 claude -p 会话输出（/tmp/supervisor_review/plan_draft_output.md）。状态：待用户审核，批准后升级为 plan-v3.2。

# 监工审核报告

> 本次是规划建议（方向级，只有建议权），最后由用户拍板。
> 用户要求的"二、Phase 0 执行计划"和"三、Phase 1–3 骨架"按监工固定格式放在下面第三节，编号为 3.1 和 3.2。

## 一、裁决：沿用"有条件通过"，只批 Phase 0；开工前要并入 v3.2 增补

- **4 条开工条件全部继续有效**：dev 双端口、只监听本机 127.0.0.1、数据进 /data、密钥卫生。
- **这次复扫代码发现 7 处新事实**（见第二节）：
  - 2 处是条件 4 的具体化：TLS 证书校验被全局关掉；LMD 的配置接口会把明文 key 返回给任何访问者。
  - 1 处是条件 2 的延伸：前端 3008 端口默认也对所有网卡开放。
  - 其余 4 处是部署事实，不改会卡住冒烟或违反条件 3。
- 这些都不改变技术路线，所以**不打回**。处理方式：
  - **现在就能开工的**：公共前置 S0，以及所有不需要 key 的步骤（A1–A3、B1–B4、B6、C4、D1）。
  - **要等 v3.2 增补入库后才能做的**：凡是要用 key 的步骤。
- **没有核实到的部分**：
  - 执行方说"仓库 main@0cd2184 已就绪、.secrets 权限为 600"，我读 `/data/AI_Video/AI_Doctor_Theater` 被拒（工具报错），这条**未经独立验证**。
  - 关口 1 之前，需要你授权我读这个仓库（见第四节 #9）。

## 二、证据（新增事实，排程直接依赖这些）

| # | 事实 | 证据 | 对计划的影响 |
|---|---|---|---|
| N1 | LMD 默认配置 `insecure_tls: true`，启动后会把 `NODE_TLS_REJECT_UNAUTHORIZED` 设为 0，也就是全局不再校验 TLS 证书 | `LocalMiniDrama/backend-node/configs/config.yaml:13`；`src/server.js:4-12` | 带着 key 的请求不校验证书，属于安全底线问题，必须改成 false |
| N2 | LMD 的 `GET /api/v1/ai-configs` 不用登录，原样返回 api_key 明文 | `routes/index.js:94` → `routes/aiConfig.js:6-7` → `services/aiConfigService.js:226` | 同机任何用户执行一次 `curl 127.0.0.1:5679/api/v1/ai-configs` 就能拿到 key。比 v3 里说的"日志打印"更严重 |
| N3 | LMD 读配置时优先找"当前目录/configs/config.yaml"，前端打包目录可以用 `WEB_DIST_PATH` 指定，数据库和存储路径都相对当前目录 | `src/config/index.js:5-9`；`src/app.js:46-50,69`；`config.yaml:16,21` | **不用改上游文件**就能满足条件 2 和条件 3：在 `data/lmd/` 下启动，配置副本也放那里 |
| N4 | lumenx 前端开发服务由脚本透传参数，默认端口 3008；LMD 的 vite dev 写死监听 `0.0.0.0:3013` | `frontend/scripts/run-next-dev.mjs:39-41`；`frontweb/vite.config.js:13-14` | 3008 启动时必须加 `-H 127.0.0.1`，并用 `ss` 实测确认；LMD **禁止用 vite dev**，只用生产构建 |
| N5 | lumenx 的 LLM 调用即使走 DashScope 也要 `openai` 包，但 `requirements-docker.txt` 里没有 | `src/apps/comic_gen/llm_adapter.py:41-46,53-58`；`requirements-docker.txt:1-23` | A1 要额外装 `openai`，否则写剧本这一步直接报错 |
| N6 | lumenx 的 OSS 上传默认开启，可显式关闭后改用本地文件；出图有 base64 回退 | `src/utils/oss_utils.py:38-41,157-158`；`src/models/image.py:538-540` | 必须设 `OSS_ENABLE=false`，阿里云 AK 和 OSS 都不申请 |
| N7 | 在 lumenx 设置页填的 key 会写进上游根目录的 `.env`，启动时还会以 `override=True` 加载这个文件；产物目录 `output/` 相对当前目录 | `api.py:63-67,1163-1166,1208-1210`；`pipeline.py:82`；`api.py:96-108` | key 只通过环境变量注入，**不在设置页填**；在 `data/lumenx/` 下启动 |

**补充：**
- 两个 40 位锁定提交号：lumenx 为 `f2a02e23171447c939e7d8e1386b24d17049bbf1`（`lumenx/.git/refs/heads/main:1`），LMD 为 `755192a70517fa392e034c58f2e92da41e7fc56a`（`LocalMiniDrama/.git/refs/heads/main:1`）。
- 两个上游仓库地址：`.git/config:7`。
- lumenx 的 TTS 默认模型是 `cosyvoice-v3-flash`（`src/audio/tts.py:117`）。
- 两个前端都有 `package-lock.json`，可以用 `npm ci` 按锁定版本安装。

## 三、改进方案

### 3.0 v3.2 增补（P0：要用 key 的步骤开工前必须写进计划并入库）

| # | 增补内容 | 涉及文件 |
|---|---|---|
| P0-a | LMD 运行配置三处改动：`server.host: 127.0.0.1`、`insecure_tls: false`、`image_proxy.use_for_video: false`。配置副本放在 `data/lmd/configs/`；和上游的差异存成 `patches/LocalMiniDrama-config-localhost.diff` 入库 | patches/、plan-v3.2 |
| P0-b | 先打 `ttsService.js:148` 的注释补丁（存为 `patches/LocalMiniDrama-tts-no-key-log.patch`），**之后才允许**往 LMD 录入任何 TTS key | patches/ |
| P0-c | lumenx 前端必须带 `-H 127.0.0.1` 启动。验收：`ss -tlnp` 里 3008、17177、5679 三个端口都只出现 127.0.0.1 | plan-v3.2 A 线 |
| P0-d | 密钥传递纪律：<br>① key 只放在 `.secrets/AI_Doctor_Theater/*.env`（权限 600），用 `set -a; . file; set +a` 注入环境；<br>② **key 不能出现在命令行参数里**：同机用户能通过 `/proc/<pid>/cmdline` 读到，所以 curl 要用 `-H @文件` 的写法或改用 SDK；<br>③ 不在 lumenx 设置页填 key；<br>④ key 由用户本人写进服务器上的文件，不经过聊天记录或 agent 对话 | plan-v3.2 C 线 |
| P0-e | 把 N2 写进风险：LMD 的 key 只能靠"消费上限 + 用的时候才开服务 + 独立 key"兜底。Phase 1 如果选 LMD，必须先加鉴权 | plan-v3.2 §7 |
| P0-f | 缓存和临时目录都指向 /data：`TMPDIR`、`npm_config_cache`、`PIP_CACHE_DIR`、`UV_CACHE_DIR`、`XDG_CACHE_HOME`，全部放在 `/data/AI_Video/.cache` 和 `.tmp`（仓库外）。原因：/tmp 在根分区，根分区已用 89% | scripts/phase0_env.sh |

**P1：**
- lumenx 后端可选加固：用 uvicorn 的 `--uds` 改监听 unix socket，再用 `ssh -L 17177:/路径/lumenx.sock` 转发，同机用户就连不上这个端口了。代价有两个：会破坏 Next 的 `/api-proxy` 文件下载；VS Code 端口转发不支持这种方式。Phase 0 默认不做，列入拍板 #11。

**P2：**
- v3.1 §2 里"8259CL 推断 AWS"这句仍建议删除。

---

### 3.1 Phase 0 高效并行执行计划（核心）

**通用约定**

| 名称 | 路径 | 说明 |
|---|---|---|
| `ROOT` | `/data/AI_Video/AI_Doctor_Theater` | 仓库根目录 |
| `SEC` | `/data/AI_Video/.secrets/AI_Doctor_Theater` | 密钥目录，目录权限 700，文件权限 600 |
| `EVD` | `$ROOT/data/phase0/evidence/` | 证据原件（不入库）；关口 1 时出脱敏副本，放进 `docs/reviews/phase0/` |
| 工具链 | `/data/AI_Video/.tools/` | venv、node、python、ffmpeg 都放这里 |

- 不使用 Maxmetagenome 的 miniforge3：那是另一个项目的禁改路径。
- 服务一律放在 tmux 会话里运行，会话名 `adt-lx-be`、`adt-lx-fe`、`adt-lmd`。
- 服务的 stdout 重定向到对应 `data/*/logs/`（目录权限 700）。
- **服务只在测试时开着**，每次会话结束就关掉。

#### S0 公共前置（串行，约 45 分钟，不需要 key，现在就能做）

| 步骤 | 做什么 | 产物 | 验收判据 |
|---|---|---|---|
| S0-1 | 收紧权限：`umask 077`；`chmod 700 $ROOT/data $SEC`；`chmod 600 $SEC/*` | — | `stat -c '%a %n' $ROOT/data $SEC $SEC/*` 显示 700/700/600，输出存为 `EVD/S0_perm.txt` |
| S0-2 | 新建 `scripts/phase0_env.sh`（约 15 行，不含任何密钥）。内容：umask 077；P0-f 的各项缓存和临时目录变量；`LUMENX_DATA_DIR=$ROOT/data/lumenx/home`；`LUMENX_LOG_DIR=$ROOT/data/lumenx/logs`；`OSS_ENABLE=false`；`NO_PROXY=*.aliyuncs.com,localhost,127.0.0.1` | 入库文件 | 文件存在，`grep -ci key` 结果为 0 |
| S0-3 | 摸清工具链：`python3.11 -V; python3.12 -V; uv --version; node -v; which ffmpeg ffprobe gcc make` | `EVD/S0_toolchain.txt` | 按结果补装：<br>· 没有 3.11/3.12 → 用 `uv python install 3.11` 装到 .tools；<br>· Node 改用 20/22 LTS（nvm，`NVM_DIR` 指向 .tools）——Node 24 下 better-sqlite3 11 能否直接用预编译包未核实【candidate_research】；<br>· 没有 ffmpeg → 装静态版到 .tools/bin |
| S0-4 | 查端口和残留进程：`ss -tlnp \| grep -E ':(3008\|17177\|5679\|18080)\b'`；`df -h / /data` | `EVD/S0_ports.txt` | 输出为空，同时证实之前 18080 的临时测试服务已关闭（关掉 v3 审核留下的 P1 项）；记录根分区占用基线 |
| S0-5 | 克隆上游：`git clone https://github.com/alibaba/lumenx.git upstream/lumenx`，然后 `checkout f2a02e23171447c939e7d8e1386b24d17049bbf1`；LMD 同样做（仓库 `xuanyustudio/LocalMiniDrama`，提交 `755192a70517fa392e034c58f2e92da41e7fc56a`） | `EVD/S0_upstream.txt`（`rev-parse HEAD` 和 `status --porcelain` 的输出）；README 记录两个 40 位提交号 | HEAD 与上面两个提交号一致，porcelain 输出为空 |

#### A 线：lumenx 冒烟（dev 双端口，依赖 S0）

| 步骤 | 命令要点 | 产物 | 验收判据 |
|---|---|---|---|
| A1 | `python3.11 -m venv /data/AI_Video/.tools/venvs/lumenx`；`pip install -r upstream/lumenx/requirements-docker.txt openai`（N5）。**禁止**装 `requirements.txt`，里面的 demucs 会带进 torch，pywebview 需要图形界面 | `EVD/A1_pip.txt` | `python -c "import fastapi,dashscope,openai,oss2"` 返回码为 0；`pip list \| grep -Ei 'torch\|demucs\|webview'` 输出为空 |
| A2 | tmux `adt-lx-be` 里：`source scripts/phase0_env.sh && cd $ROOT/data/lumenx && PYTHONPATH=$ROOT/upstream/lumenx python -m uvicorn src.apps.comic_gen.api:app --host 127.0.0.1 --port 17177`。**不加 --reload；禁止用 main.py 和 start_backend.sh** | `data/lumenx/logs/app.log` | ① `ss` 只看到 `127.0.0.1:17177`；<br>② `curl -s 127.0.0.1:17177/config/info` 返回 JSON；<br>③ `data/lumenx/output/` 已生成，且 `upstream/lumenx/output` 不存在；<br>④ `~/.lumen-x` 不存在（核查条件 3）；<br>⑤ 日志里关于 htdemucs 的报错只到 warning 级别 |
| A3 | `cd upstream/lumenx/frontend && npm ci`，然后在 tmux `adt-lx-fe` 里执行 `npm run dev -- -H 127.0.0.1` | `EVD/A3_ss.txt` | `ss` 只看到 `127.0.0.1:3008`；如果出现 `*:3008` 或 `0.0.0.0:3008`，**立即停止服务**，记为不满足条件 2；`curl -sI 127.0.0.1:3008` 返回 200 |
| A4（需要 C0） | 本机开隧道（见 U3）后打开 `localhost:3008`。key 只经环境变量注入。建 1 个测试项目，依次做：剧本解析（DashScope qwen）→ 1 个角色的三视图定妆 → 1 张分镜图 → 1 句 TTS | 截图 4 张；`data/lumenx/output/` 下的产物；成本台账加 1 行 | 4 步都有对应产物文件和日志行；完成后 `upstream/lumenx/.env` **不存在**；如果存在，其中 `_BASE_URL` 的行数必须为 0 |
| A5（需要 C2 通过） | 设 `LLM_PROVIDER=openai`、`OPENAI_BASE_URL=https://open.bigmodel.cn/api/paas/v4`，模型名由执行方按账户可用型号填写，重做一次剧本解析 | 截图和日志 | 剧本 JSON 能正常解析成分镜，这是 GLM 在真实平台里的端到端验证 |
| A6 | 测试结束后停掉两个服务 | `EVD/A6_ss.txt` | 3008 和 17177 都不在监听 |

**A 线止损：** 满足任一条就停，记为"部署摩擦高"，直接进入关口 1 对比：
- 累计投入超过 1 个工作日；
- 要改上游代码（已登记的补丁除外）才能启动；
- 必须装 torch 或 demucs；
- 3008 无法绑定到 127.0.0.1。

#### B 线：LocalMiniDrama 冒烟 + 零号基线（依赖 S0，与 A 线完全并行）

| 步骤 | 命令要点 | 产物 | 验收判据 |
|---|---|---|---|
| B1 | `cd upstream/LocalMiniDrama/backend-node && npm ci`；再进 `../frontweb` 执行 `npm ci && npm run build`（**禁止 vite dev**） | `frontweb/dist/` | `node -e "require('better-sqlite3');require('sharp')"` 返回码为 0；`dist/index.html` 存在 |
| B2 | 把上游 `configs/config.yaml` 拷到 `$ROOT/data/lmd/configs/`，改 P0-a 的三项；端口 5679 和 `base_url` 保持原值；用 `diff -u` 生成差异文件存入 `patches/` | patches/ 下的 diff 文件 | 上游配置文件 `git status` 无改动；diff 正好 3 处改动 |
| B3 | 注释掉 `ttsService.js:148`，执行 `git -C upstream/LocalMiniDrama diff > patches/LocalMiniDrama-tts-no-key-log.patch` | patch 文件入库 | `grep -n "synthesizeWithOpenai'," ttsService.js` 显示该行已注释；**必须先于 B5 的 TTS 步骤完成** |
| B4 | tmux `adt-lmd` 里：`cd $ROOT/data/lmd && WEB_DIST_PATH=$ROOT/upstream/LocalMiniDrama/frontweb/dist node $ROOT/upstream/LocalMiniDrama/backend-node/src/server.js` | `data/lmd/logs/` | ① `ss` 只看到 `127.0.0.1:5679`；<br>② `curl -s 127.0.0.1:5679/health` 返回 `"status":"ok"`；<br>③ `curl -s 127.0.0.1:5679/ \| grep -c 'id="app"'` 至少为 1；<br>④ 日志里**没有** `insecure_tls 已启用` 字样（证明 N1 已修，对应 server.js:12）；<br>⑤ `stat -c %a data/lmd/data/drama_generator.db` 为 600 |
| B5（需要 C0；TTS 部分需要 C3） | 在"AI 配置"里加 DashScope 出图（`imageClient.js:93`）和文本模型（GLM v4 或 DashScope compatible-mode）。建 1 部剧 → 1 张角色图 → 1 张分镜图。TTS 分情况：C3 通过才测；不通过就记"需要 MiniMax key，Phase 0 不买"。字幕烧录：没有视频素材就记为"未测"，不硬凑 | 截图；`data/lmd/data/storage/` 下的产物 | 产物文件存在；测试结束停服务，确认 `ss` 里 5679 已不在 |
| B6（纯案头，任何时候都可做） | 列出零号基线的改造点：在 anything2explainer 里插一个"出图步骤"需要改哪些位置，**只列清单不写代码**（沿用 v2 的条件 2） | `docs/reviews/phase0/zero-baseline-delta.md` | 每个改造点都写明 `文件:行号`；工时按 S/M/L 三档估 |

**B 线止损：**
- 原生模块（better-sqlite3、sharp）换一次 Node LTS 后仍然编译失败 → 停；
- 投入超过 1 个工作日 → 停。

#### C 线：API 实测（关键路径在 U1，也就是拿到 key）

| 步骤 | 要点 | 产物 | 验收判据 |
|---|---|---|---|
| C0 | 用户本人把 key 写入 `$SEC/dashscope.env` 和 `$SEC/glm.env`，权限 600 | — | `stat` 显示 600；执行方不打印、不回显文件内容 |
| C1 | 在 lumenx 的 venv 里用 dashscope SDK 从环境变量读 key，各测一次：出图（qwen-image 或 wanx）、TTS（`cosyvoice-v3-flash`）、LLM（qwen-plus） | `data/api_probe/C1_*.json`，只记模型名、request_id、HTTP 状态和延迟（ms），不含 key；成本台账 | 三项都是 2xx；台账里的费用用控制台实扣金额回填 |
| C2 | GLM 三项验证：① `openai` 包的版本；② 调 v4 端点的 chat completion 成功；③ `response_format={"type":"json_object"}` 返回结果能被 `json.loads` 正常解析 | `C2_glm.json` | 三项全部通过才放行 A5 |
| C3 | 检查 DashScope 能否接 LMD 的 TTS 通道：向 `{DASHSCOPE}/compatible-mode/v1/audio/speech` 发一个最小请求 | `C3_tts_compat.json` | 2xx 且返回音频 → "一把钥匙走通 LMD"成立；404 或 400 → 改写结论为"LMD 的 TTS 需要 MiniMax"【candidate_research，以实测为准】 |
| C4（案头） | 看 Kling 和 Vidu 的官方价目，结合 `lumenx/docs/1-api-reference/*.md` 做评估，**不申请 key** | 价目摘录 | 每条都标 candidate_research 和来源 URL |

**C 线止损：** 累计花费达到上限的 80%，所有生成任务立即停止并上报。

#### D 线：Q版人设

| 步骤 | 要点 | 依赖 | 验收判据 |
|---|---|---|---|
| D1（现在就能做） | 写人设表：1 个 Q版医生和 2–3 个拟人器官（建议跟第一条科普的主题绑定，例如肠道菌群，可复用 `projects/microbiome` 的题材）。每个角色写固定外观描述（配色、比例、标志物），中英两版提示词，加反向提示词。<br>**注意**：lumenx 的风格预设把 chibi（Q版）放在反向提示词里（v2 已核实 `style_presets.json:118,133`），所以 D3 必须用自定义风格 | 无 | `docs/persona/persona-v0.md` 入库，只放文字，不放图片 |
| D2 | 用 DashScope qwen-image 给每个角色出 5–10 张：提示词固定，只换 seed；**总量不超过 40 张** | C1 | `data/persona/` 下的图片，加一份 manifest.csv（文件、模型、提示词哈希、seed、延迟、费用） |
| D3 | 一致性测试：每个角色挑最好的 1 张，分别用 (a) lumenx 三视图定妆、(b) LMD 带参考图出图，各出 3 种姿态或表情。按书面评分表打 1–5 分，评 5 项：角色辨识度、配色一致、比例一致、医学形象不失真、无恐怖谷 | A4、B5 | 每个角色一张对比拼图，外加评分表（用户和执行方各打一份）；最后结论写"一致性够用"或"不够（转 Seedream 备选，在 Phase 1 议）" |

**D 线止损：** 改两轮提示词后仍没有任何候选达到 3 分，记"不足"并停止。

#### 依赖与并行关系

```
t0 ─┬─ S0（串行）─┬─ A1→A2→A3 ──────────┬─ A4 → A5 → A6
    │             └─ B1→B2→B3→B4 ───────┼─ B5（TTS 部分等 C3）
    ├─ D1 / B6 / C4（纯案头，随时可做）    │
    └─ 用户动作 U1–U4 ─→ C0 → C1 ─┬─ C2 ──┘（A5 等 C2）
                                   ├─ C3
                                   └─ D2 ─→ D3（还要等 A4 和 B5）
                                                    └→ 关口 1 材料包
```

- **必须串行的**：S0 在所有安装之前；B3 在 B5 的 TTS 之前；C0 在所有调用 key 的步骤之前。
- **完全并行的**：A 线和 B 线；所有案头步骤；用户动作。

#### 需要用户动作的事项

| # | 动作 | 预计耗时 |
|---|---|---|
| U1 | 开通 DashScope（百炼），完成实名认证，创建 key：建议给 lumenx 和 LMD 各建 1 个，泄露时可以单独作废。预充值 ¥100 作为硬上限，能设费用预警就设在 ¥50。然后**本人**登录服务器把 key 写进 `$SEC/dashscope.env` | 实名审核时长未知【candidate_research】，**这是整个 Phase 0 的关键路径** |
| U2 | 在智谱为本项目单独建一个 key，**不复用** Maxmetagenome 的 `~/.glm_router_api_key`；写进 `$SEC/glm.env` | 10 分钟 |
| U3 | 在西柚云控制台确认 SSH 的入口地址和端口（**不申请公网端口映射**）。确认后，本机用一条命令建三条隧道：`ssh -N -L 3008:127.0.0.1:3008 -L 17177:127.0.0.1:17177 -L 5679:127.0.0.1:5679 -p <入口端口> <用户>@<入口>` | 10 分钟 |
| U4 | 给同事打招呼。话术示例："测试期间本机 3008、17177、5679 只监听本机，没有登录机制，请勿访问；只在测试时段开启，预计 X 天" | 5 分钟 |
| U5 | 授权监工只读访问 `/data/AI_Video/AI_Doctor_Theater` | 关口 1 前完成 |
| U6 | 参加 D3 评分 | 15 分钟 |

#### 时间线与费用上限建议

**时间线：**
- **第 1 天上午**：S0，同时用户做 U1–U4；D1、B6、C4 并行。
- **第 1 天下午**：A1–A3 和 B1–B4 并行。key 到位就接着做 C1–C3。
- **第 2 天**：A4、A5、B5、D2、D3，然后整理关口 1 材料包。
- **硬上限**：每条线投入不超过 1 个工作日；Phase 0 总共不超过 2 个工作日。
- **超时冻结**：第 2 天结束 key 还没到位，就冻结 Phase 0 并上报，不延期硬做。

**费用上限：**

| 项目 | 上限 |
|---|---|
| DashScope | ¥100（用预充值余额作为硬上限） |
| GLM | ¥20 |
| 视频、MiniMax | ¥0，不购买 |

- 单价全部是 candidate_research；台账一律以控制台实扣金额为准。

---

### 3.2 Phase 1–3 骨架与关口定义

- **Phase 1：底座落地 + 单条科普 MVP。**
  - 用关口 1 选定的底座，接入 GLM 作为剧本大脑，锁定 Q版人设。
  - 产出 1 条 60–90 秒的科普片，端到端跑通，仅限内部演示。
  - 先花半天验证口型和眨眼贴图（v2 遗留的 P1-2）。
  - 所有上游改动都在 `patches/` 登记。
  - 如果服务要长期运行，必须先加鉴权或改用 unix socket。
- **Phase 2：合成与合规工程。**
  - 用 anything2explainer 的 Remotion 分镜协议做合成和 QC。
  - 做字幕烧录。
  - AI 标识要两层：画面上显式标注，文件元数据里隐式标注。
  - 医学事实要回链到出处，并保留审校签字记录。
- **Phase 3：小规模发布与迭代。**
  - 做多主题模板和批量生产。
  - 如果用 lumenx，需要自己维护 fork。
  - 要给多人使用，就必须先加鉴权和 HTTPS。

**关口定义：**

| 关口 | 时点 | 判定内容 |
|---|---|---|
| 关口 1 | Phase 0 → Phase 1 | 定底座；批准 Phase 1 的范围和预算 |
| 关口 2 | Phase 1 结束 | 内部样片过审；批准 Phase 2 |
| 关口 3 | 首次对外发布前 | 具名医学审校人、发布主体资质、Remotion 授权、AI 标识合规四项全部落实，**缺一项就否决发布** |

（新路径或新数据源的创建，继续走既有的"关口③"规则。）

**关口 1 复审输入物清单**（每一项都要能对应到 `文件:行号` 或命令输出）：

1. 一页对比表：lumenx、LMD、零号基线三方，比较 6 项：部署摩擦（实际耗时）、GLM 接入（C2/A5 的结果）、定妆和一致性（D3 评分）、远程访问、许可证、安全缺口（N2/N7）。
2. `EVD/` 下全部证据的脱敏副本，放在 `docs/reviews/phase0/`。
3. 两次 `ss -tlnp` 输出：一次是服务运行时（只能出现 127.0.0.1），一次是关闭后（3008、17177、5679 都不在）。
4. `stat` 或 `ls -la` 输出，覆盖 `$SEC`、`data/`、两个 sqlite 和 `.env` 文件，验证权限 600/700。
5. 泄露扫描结果（**只输出计数，不输出内容**）：`grep -rlF -f <(cut -d= -f2- $SEC/dashscope.env) $ROOT/data $ROOT/upstream | wc -l`，结果应为 0。说明：这里用进程替换读文件，key 不会出现在命令行参数里。
6. 上游两个仓库的 `rev-parse HEAD` 输出，以及 `patches/` 文件清单，要和 README 记录一致。
7. 成本台账，附控制台账单截图；时间台账，写明每条线是否触发止损。
8. 仓库提交纪律检查：`git status --ignored` 和 `git diff --cached --stat`；`df -h /` 与 S0 的基线对比。
9. C3 的结论，以及据此修订后的"一把钥匙"表述。

## 四、待用户拍板

| # | 事项 | 通俗解释 | 监工建议（默认值） |
|---|---|---|---|
| 1 | 底座选型 | 在哪个开源项目上改 | 关口 1 用实跑数据定；目前仍倾向 lumenx，但 N7 的密钥写入问题要计入代价 |
| 2 | API 与预算 | 买哪家接口、花多少钱 | DashScope 为主，预充值 ¥100 作硬上限；GLM ¥20；视频 key 和 MiniMax **都不买** |
| 3 | GLM 专用 key | 要不要和另一个项目共用一把钥匙 | **不共用**，单独新建一个，泄露时互不影响 |
| 4 | 内容形态 | 连续剧还是单条科普 | 单条科普 |
| 5 | 医学审校 | 谁把关医学事实 | 不卡 Phase 0；关口 3 必须有具名审校人 |
| 6 | 发布主体资质 | 用谁的名义发布 | 同上，关口 3 落实 |
| 7 | 告知同事 | 要不要打招呼 | **要**，用 U4 的话术 |
| 8 | 批准范围 | 这次批到哪一步 | 只批 Phase 0：不超过 2 个工作日，有止损规则，有费用上限 |
| 9 | 监工读取授权 | 让监工能看新仓库 | 授权只读，否则关口 1 的证据我无法独立核验 |
| 10 | 接受 LMD 的 key 明文风险（N2） | 同机用户可以直接读到 key | Phase 0 接受，兜底靠上限、用时才开、独立 key；Phase 1 如果选 LMD，必须先加鉴权 |
| 11 | lumenx 后端改用 unix socket | 让同事连不上这个端口 | Phase 0 不做；Phase 1 如果要常驻运行再做 |
| 12 | Remotion 商业授权 | 合成工具商用可能收费 | 关口 3 前核对【candidate_research】 |

## 五、下一阶段风险预警

1. **多用户共机下 key 失窃**：
   - LMD 的接口会把 key 明文返回（N2）；
   - lumenx 的配置接口允许任何人改 `*_BASE_URL`，key 会被发到别人指定的地址（`api.py:1258,1289-1294`）；
   - 命令行参数里的 key 同机用户都能看到。
   - 能做的只有：消费上限、两个平台用不同的 key、服务只在用时开启、关口 1 的泄露扫描。**少一项都不能放行。**
2. **key 申请是关键路径**：实名或充值一卡住，C、D 两线和 A4、B5 全部停摆。所以不需要 key 的步骤要先做完；超过 2 天就冻结，不能拿"没有 key 的冒烟"冒充完成。
3. **工具链摩擦**：本机可能没有 Python 3.11 和 ffmpeg；Node 24 下原生模块可能装不上；npm 和 Next 默认往根分区（已用 89%）的 /tmp 写。应对：S0-3 先摸清再补装，P0-f 把临时目录和缓存全部改到 /data，各线按止损规则执行；超时就记为"部署摩擦高"，作为关口 1 的比较数据，不要硬啃。
