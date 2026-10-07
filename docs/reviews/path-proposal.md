> [已脱敏存档] 原件位于 /data/AI_Video/.secrets/AI_Docter_Theater/path-proposal.orig.md（0600，不入库）。脱敏项：IP/用户名/主机名/同事服务端口 → <REDACTED:*>，其余与原件一致。
> 原件来源：执行方 2026-10-07 新路径创建提案（原件 .secrets/AI_Docter_Theater/path-proposal.orig.md）

# 送审提案：新建独立子路径承载 AI 漫剧系统（关口类型：③新路径创建前）

2026-10-07。决策依据：用户指示——当前 /data/AI_Video 根目录内容为以前探索的结果，需创建独立、干净、整洁、可上传 GitHub 的子路径承载并部署新系统。

## 1. 现状盘点（2026-10-07 实测）

| 路径 | 大小 | 性质 | 处置建议 |
|---|---|---|---|
| anything2explainer/ | 310M，含 .git | Remotion 科普视频 skill（未来"合成端"支柱资产） | **保留原地** |
| projects/（microbiome+smoke） | 1.9G | Remotion 成片工程（分镜表协议参考、合成端素材） | **保留原地** |
| research/ | 48K | 既有调研笔记（anything2explainer.md） | 保留原地 |
| tools/、glm-claude.sh、.secrets/、.agents/ | 小 | 工具与密钥（.secrets 权限 700） | 保留原地 |
| **ai-fusion-video/** | 38M | **调研期克隆**（已排除的候选：Java+MySQL 栈） | **移入 archive/** |
| **drama-skills/** | 9.2M | **调研期克隆**（MIT 工艺层借鉴，架构已摘录进计划书） | **移入 archive/** |
| **Kinema/** | 172M | **调研期克隆**（已排除：AGPL） | **移入 archive/** |

注：三个调研克隆为公开仓库原样克隆（无本地改动），archive 后仍可随时按提交号重克隆；/tmp/research_base/ 的 8 仓库克隆与此并行存在（易失，Phase 0 起按需转入新路径 upstream/）。

## 2. 新路径结构提案

路径名：`/data/AI_Video/medtoon/`（medical+toon；用户可一键改名，创建前告知即可）

```
medtoon/                        # 独立 git 仓库（git init，可上传 GitHub）
├── .gitignore                  # 见 §3 草案
├── README.md                   # 极简占位：项目名+一句话+指向 docs/reviews/（不超过 10 行）
├── docs/
│   └── reviews/                # 治理记录（从 /tmp 迁入并纳入版本管理）：
│       ├── plan-v3.1.md        #   计划书（含监工 4 条开工条件）
│       ├── supervisor-review-v2.md   # 10-06 监工首审报告（有条件通过）
│       ├── supervisor-review-v3.md   # 10-07 监工复审报告（有条件通过 Phase 0）
│       └── server-probe-evidence.txt # 服务器实测证据
├── upstream/                   # 第三方平台部署区（.gitignore 不入库；Phase 0 起 lumenx@f2a02e2、LocalMiniDrama@755192a）
├── data/                       # 运行数据/日志（.gitignore；LUMENX_DATA_DIR/LUMENX_LOG_DIR/存储目录指向此处）
└── secrets/                    # API keys（.gitignore；Phase 0 C 线创建，chmod 700/600）
```

自研代码目录（app/ 等）：**不预建**——Phase 1 有实际代码时再建（Ponytail：不创建未明确需要的空样板）。upstream 固定提交号记录在 README。

## 3. .gitignore 草案

```
# 第三方上游（按提交号重克隆，不入库）
upstream/
# 运行数据与日志
data/
logs/
*.log
# 密钥
secrets/
*.env
.env
# Python
__pycache__/
*.pyc
.venv/
venv/
# Node
node_modules/
dist/
.next/
# OS/编辑器
.DS_Store
```

## 4. 首次提交内容

.gitignore、README.md、docs/reviews/ 四份治理文件。分支 main，单次 initial commit（英文提交信息）。不设远程、不加 LICENSE（许可证选择待用户拍板，涉及商用定位）。

## 5. 风险与说明

1. docs/reviews/ 含服务器内外网 IP 等信息：**建议 GitHub 仓库建为 private**（推送时机与可见性由用户决定；如未来转 public 需先清洗 IP）
2. archive/ 为非破坏性处置（不删数据）；用户如确认不需要可后续删除，本次不动
3. 根目录其余旧资产（anything2explainer/projects/research）不动——它们是合成端支柱与参考，且不属于本次"新路径"范围
4. 新路径创建后，此前 /tmp 中的送审材料同步迁移完成，履行 v2 审核 P1"证据挪稳定路径"

## 6. 请监工裁决

a) 结构与命名是否满足"独立、干净、可上传 GitHub"；b) 根目录三个调研克隆的 archive 处置是否恰当；c) .gitignore 是否有遗漏导致敏感/大文件入库的风险；d) 首次提交范围是否合适；e) 其他 P0/P1。
