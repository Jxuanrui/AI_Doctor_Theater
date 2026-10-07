> [已脱敏存档] 原件位于 /data/AI_Video/.secrets/AI_Docter_Theater/supervisor-review-path-gate.orig.md（0600，不入库）。脱敏项：IP/用户名/主机名/同事服务端口 → <REDACTED:*>，其余与原件一致。
> 原件来源：2026-10-07 会话 transcript 恢复 + stdout（原件 .secrets/AI_Docter_Theater/supervisor-review-path-gate.orig.md）


# 监工审核报告

## 一、裁决：有条件通过

可以创建 `/data/AI_Video/medtoon/` 这个目录。但在完成下面 4 项 P0 之前，不得执行 `git init` 后的首次提交。

结构本身满足用户要求，也满足 v3.1 的 4 条开工条件：数据目录放在 /data 上，`secrets/` 和 `data/` 不入库，`upstream/` 不入库。问题在于首次提交的内容和 `.gitignore`，有 3 处会让敏感信息或不实材料永久进入 git 历史，另有 1 处会让开工条件 4 要求的补丁登记无处落地。

前提说明：我没有 `/data/AI_Video` 读取权限，第 1 节盘点数据（大小、"无本地改动"）只能采信执行方的转述，属于未独立验证。

## 二、证据

| # | 证据 | 结论 |
|---|---|---|
| E1 | `/tmp/supervisor_review/server_probe_evidence.txt:18-20` 写有同事用户名 <REDACTED:colleague-1>、<REDACTED:colleague-2> 和 <REDACTED:user>，以及各自的公网登录 IP（<REDACTED:client-ip-1>/69、<REDACTED:client-ip-3>）；`:10-15` 写有内网 IP、出口公网 IP、同事服务的开放端口、"ufw ENABLED=no" | 这已经不只是提案 §5-1 说的"服务器 IP"，而是**第三方个人信息加上一张攻击面清单**。提案只说建私有仓库，低估了风险 |
| E2 | `ai_manga_drama_plan.md:17,21` 再次写出 <REDACTED:internal-ip> 和 <REDACTED:egress-ip>；`:7` 写出上游未鉴权接口的位置（api.py:1258） | 计划书也需要脱敏 |
| E3 | `path_proposal.md:22` 说"可上传 GitHub"，`:72` 说"未来转 public 需先清洗 IP" | 矛盾：信息一旦提交，以后转公开就得改写 git 历史（filter-repo），成本高且容易漏。应该在**首次提交前**脱敏，而不是事后清洗 |
| E4 | `path_proposal.md:30-31` 说 `supervisor-review-v2.md` 和 `supervisor-review-v3.md` "从 /tmp 迁入"。但 `/tmp/supervisor_review/` 下只有 3 个文件（path_proposal.md、ai_manga_drama_plan.md、server_probe_evidence.txt），按 `/tmp/*/*review*v*` 搜索没有结果，`.claude/reviews/` 里也没有相关记录 | **两份监工报告的原文来源不明**。如果是根据记忆或摘要重写的，就不是原样存档，不能当作治理记录入库 |
| E5 | `.gitignore` 草案 `path_proposal.md:51-52` 只有 `*.env` 和 `.env` | `*.env` **匹配不到** `.env.local`、`.env.production`、`.env.development` 这类常见变体；也没有覆盖 `*.key`、`*.pem`、`.secrets/`、`*.db`、`*.sqlite`、音视频和图片产物、`.cache/`、`.npm/`，以及 agent 配置目录（`.zcode/`、`.claude/`） |
| E6 | `ai_manga_drama_plan.md:4,5,7` 要求：①在上游目录外写启动脚本；②修改 LocalMiniDrama 的 `config.yaml` 中的 server.host；③给 LMD 打本地补丁并"登记"。而 `path_proposal.md:33` 规定 `upstream/` 整体不入库，`:38` 规定不预建其他目录 | 补丁和 host 修改都在被忽略的 `upstream/` 里，**重新克隆就会丢**。开工条件 4 的"登记"和条件 1 的"上游目录外脚本"在新结构里没有可入库的落点 |
| E7 | `path_proposal.md:35` 新建 `secrets/`；`:12` 根目录已有 `.secrets/`（700） | 两个密钥目录并存。另外密钥放在 git 工作树内，只靠 `.gitignore` 这一层防护，`git add -f` 就能绕过 |
| E8 | `path_proposal.md:17` 称三个克隆"无本地改动，可按提交号重克隆" | 我无法核验，提案也没给出各克隆的完整提交号和 `git status` 输出 |
| E9 | `ai_manga_drama_plan.md:80` 要求 venv/npm 缓存指向 /data | 如果缓存指向 medtoon 目录内部，而 `.gitignore` 没有对应条目，就会被提交 |

## 三、改进方案

### P0（必须在首次提交前完成）

1. **脱敏后入库**（涉及 `docs/reviews/server-probe-evidence.txt`、`plan-v3.1.md`）
   - 用户名、登录 IP、内外网 IP、同事服务端口一律替换为 `<REDACTED:xxx>` 占位符。
   - 未脱敏的原件放在被忽略的私有位置（如 `secrets/` 或仓库外 `.secrets/`），权限 600。
   - 每份脱敏文件开头加一行说明："本文件已脱敏，原件位于 <路径>"。
   - 提交前 grep 校验：IPv4 正则和上述用户名的命中数应为 0。
2. **说明两份监工报告的来源**（涉及 `supervisor-review-v2.md`、`supervisor-review-v3.md`）
   - 有原文（如会话 stdout 的落盘文件）：给出原始路径后原样复制。
   - 拿不到原文：不得重新撰写冒充原文。改为在 `plan-v3.1.md` 开头的裁决摘要中注明"监工原报告原文缺失"，或只入库可证实的部分。这一项若隐瞒，按"报喜不报忧"打回。
3. **补全 `.gitignore`**（涉及 `.gitignore`），至少追加：
   ```
   .env.*
   !.env.example
   .secrets/
   *.key
   *.pem
   *.p12
   id_rsa*
   *credentials*.json
   *.db
   *.sqlite
   *.sqlite3
   *.db-journal
   *.mp4
   *.mov
   *.wav
   *.mp3
   *.m4a
   out/
   renders/
   .cache/
   .npm/
   .pnpm-store/
   .zcode/
   .claude/settings.local.json
   tmp/
   ```
   如果以后确实要入库某张示例图，再用 `!` 规则单独放行。
4. **给开工条件 1 和 4 安排入库落点**（只登记，不预建）
   - 在提案里写明：第一个本地补丁或启动脚本出现时，分别存入 `patches/<repo>-<desc>.patch` 和 `scripts/`，并纳入版本管理。
   - LMD 的 `config.yaml` host 修改和 ttsService.js:148 的注释补丁都按这个方式登记。
   - README 记录 upstream 的**完整 40 位**提交号，以及如何对 upstream 打补丁。

### P1（强烈建议）

5. **密钥放到 git 工作树之外**，统一到 `/data/AI_Video/.secrets/AI_Docter_Theater/`（700/600），仓库内只保留 `.env.example`。如果坚持放在仓库内，`medtoon/` 整个目录要设为 750 或更严，因为这是多用户共用的机器。
6. **archive 搬迁前留存证据**：对三个克隆各记录一次 `git rev-parse HEAD` 和 `git status --porcelain` 的输出，写入 `archive/MANIFEST.md`。还要全文 grep 根目录（`tools/`、`glm-claude.sh`、`projects/`、`research/`），确认没有引用这三个绝对路径，以吸取 A-4 漏查引用的教训。
7. **把本次关口材料一并入库**：`path_proposal.md` 和本报告（建议命名为 `docs/reviews/supervisor-review-path-gate.md`），使关口③在仓库里可追溯。
8. **提交前设置仓库级 `git config user.name/user.email`**，避免共享服务器上的全局身份或私人邮箱进入历史。

### P2（建议）

9. 迁入的治理文件里还有指向 `/tmp/...` 的路径。不要改动原文，只在 README 里加一张"旧路径 → 新路径"对照表。
10. 首次提交前人工执行一次 `git status --ignored` 和 `git diff --cached --stat`，与第 4 节声明的 6 个文件逐项核对（沿用 §15.6 提交纪律，禁止 `git add -A`）。

## 四、待用户拍板

| # | 事项 | 通俗解释 | 监工建议 |
|---|---|---|---|
| 1 | 路径命名 `medtoon` | 将来 GitHub 仓库的名字，改名越早越省事 | 可以用；GitHub 上是否重名属 candidate_research，推送前自查 |
| 2 | 三个调研克隆移入 `archive/` | 只挪位置不删除，目的是让根目录看着更整洁；不搬也不影响新路径干净 | 不是本次必需。要搬就先完成 P1-6 的留存证据；嫌麻烦可以先不动 |
| 3 | GitHub 仓库可见性 | 私有只有受邀者能看；公开所有人都能看 | 先建私有。完成 P0-1 脱敏后，日后转公开就不用改写历史 |
| 4 | 密钥目录放仓库内还是仓库外 | 仓库内迁移方便，但一个误操作就可能被提交；仓库外更安全 | 放仓库外（P1-5） |
| 5 | LICENSE 选择 | 不放许可证等于保留全部权利；会影响以后开源和商用 | 等底座选定后再定。若用 lumenx 等上游，需与其许可证兼容；Remotion 商业授权见 v3.1 待拍板第 8 项 |
| 6 | 是否告知同事 | 脱敏针对的就是同事的登录 IP 和服务端口；仓库将来共享时会涉及他们 | 脱敏后可以不告知；如果坚持保留原文入库，建议先征得同意 |

## 五、下一阶段风险预警

1. **上游补丁漂移**：`upstream/` 不入库，lumenx 已停更，Phase 0 的 host 修改、密钥日志补丁、启动脚本如果没按 P0-4 入库，重建环境后就会悄悄失效。其中密钥打印问题会直接复发。
2. **运行产物误入库**：D 线出图、冒烟视频、SQLite 库的默认输出位置可能不在 `data/`。Phase 0 结束前要用 `git status --ignored` 做一次实测，确认没有大文件或数据库落在被跟踪的路径下。
3. **多用户共机的权限**：`/data` 对同事可见。`data/` 下可能存放上游写入的 `.env` 和日志（含 key）。目录 umask 和权限若不收紧，"密钥 600"就形同虚设，Phase 0 验收时需附上 `ls -la` 的输出作为证据。
