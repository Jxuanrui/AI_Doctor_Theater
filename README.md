# AI_Doctor_Theater

AI-generated comic-drama platform for medical science popularization, starring **Dr.咪**
（医学科普 AI 漫剧生产平台，主角：灰虎斑白短毛猫医生 Dr.咪，配音=有节奏猫叫+全字幕）.
Built on vetted open-source upstreams; own code stays minimal.

Status: **Phase 1 首集样片进行中**（计划 v3.5：`docs/reviews/plan-v3.5-supervisor.md`；关口 1 已过，自研轻管线底座，LMD 已关停清 key）。
Plans & audit trail: [`docs/reviews/plan-phase0-draft.md`](docs/reviews/plan-phase0-draft.md)（批准版 v3.2）与
[`docs/reviews/plan-v3.1.md`](docs/reviews/plan-v3.1.md)（前一版，历史留档）；治理纪律见
[`docs/governance.md`](docs/governance.md)（AI 标识/监工/钥匙/素材合规/字幕硬门禁）。

> Rename note: the working name during gate review was `medtoon`; renamed to `AI_Doctor_Theater` per owner decision (2026-10-07).
> Archived documents under `docs/reviews/` still mention `medtoon` verbatim in their bodies — read it as this repo's former name.

## Layout

| path | purpose | tracked |
|---|---|---|
| `docs/persona/` | 主角人设表（官定形象/DNA/配音/资产清单） | yes |
| `docs/governance.md` | 治理纪律（AI 标识、监工、钥匙、素材合规、字幕门禁、delogo 台账） | yes |
| `docs/reviews/` | supervisor audit records + evidence + asset snapshots（`phase0/asset-snapshots/` 清理前快照纪律） | yes |
| `upstream/` | vendored third-party platforms, pinned commits below | no |
| `data/` | runtime data: `persona/`（官定形象资产）、`sfx/`（CC0 猫叫音效+许可台账）、`api_probe/`、`lmd/`、`lumenx/`、`phase0/`、`seedance/` | no |
| `scripts/` | our own scripts: `phase0_env.sh`、`persona_badge_text.py`、`i2v_template.py`、`compose_episode.py`（合成，扩展中）、`t0_c2_glm_json_test.py`、`iris_gate.py`（虹膜色相闸门） | yes |
| `patches/` | local patches to upstream, one file per change | yes |
| `app/` | our own pipeline code (from Phase 1) | yes |

Any manual edit inside `upstream/` MUST be mirrored as a patch file here, or it silently disappears on re-clone.

Secrets never enter this repo. They live at `/data/AI_Video/.secrets/AI_Doctor_Theater/` (0700/0600); the repo keeps only `.env.example` templates.

## Upstream pins

| repo | commit (full) | license |
|---|---|---|
| alibaba/lumenx | `f2a02e23171447c939e7d8e1386b24d17049bbf1` | MIT |
| xuanyustudio/LocalMiniDrama | `755192a70517fa392e034c58f2e92da41e7fc56a` | MIT |

Re-clone: `git clone <url> upstream/<name> && git -C upstream/<name> checkout <commit>`
Apply our patches: `git -C upstream/<name> apply ../../patches/<repo>-<desc>.patch`

## Migrated paths (old -> new)

| old | new |
|---|---|
| `/tmp/supervisor_review/ai_manga_drama_plan.md` | `docs/reviews/plan-v3.1.md` |
| `/tmp/supervisor_review/server_probe_evidence.txt` | `docs/reviews/server-probe-evidence.txt` |
| `/tmp/supervisor_review/path_proposal.md` | `docs/reviews/path-proposal.md` |
| (session stdout / transcript, 2026-10-06/07) | `docs/reviews/supervisor-review-v2.md` / `-v3.md` / `-path-gate.md` |
| `medtoon` (working name, incl. `/data/AI_Video/medtoon/`, `.secrets/medtoon/`) | `AI_Doctor_Theater` |

Texts inside migrated docs still reference the old paths verbatim; this table is the authoritative mapping.
