# AI_Doctor_Theater

AI-generated chibi-style comic-drama platform for medical science popularization
（医学科普 Q版 AI 漫剧生产平台）. Built on vetted open-source upstreams; own code stays minimal.

Status: pre-Phase 0 (path skeleton created under supervisor gate review).
Plan & audit trail: [`docs/reviews/plan-v3.1.md`](docs/reviews/plan-v3.1.md) (redacted; originals kept privately outside the repo).

> Rename note: the working name during gate review was `medtoon`; renamed to `AI_Doctor_Theater` per owner decision (2026-10-07).
> Archived documents under `docs/reviews/` still mention `medtoon` verbatim in their bodies — read it as this repo's former name.

## Layout

| path | purpose | tracked |
|---|---|---|
| `docs/reviews/` | governance: plan + supervisor audit records (redacted) | yes |
| `upstream/` | vendored third-party platforms, pinned commits below | no |
| `data/` | runtime data / logs (`LUMENX_DATA_DIR`, `LUMENX_LOG_DIR`, storage dirs point here) | no |
| `scripts/` | our own launch scripts — created when first needed; always OUTSIDE `upstream/` | yes |
| `patches/` | local patches to upstream, one file per change: `<repo>-<desc>.patch` | yes |
| `app/` | our own code (adapters, presets, Remotion composition components; from Phase 1) | yes |

`scripts/` and `patches/` do not exist yet — they are created with the first script/patch (Ponytail: no empty scaffolding).
Any manual edit inside `upstream/` (e.g. LocalMiniDrama `config.yaml` host change, `ttsService.js:148` log-line fix)
MUST be mirrored as a patch file here, or it silently disappears on re-clone.

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

Texts inside migrated docs still reference the old paths verbatim (originals are preserved unmodified, apart from the mechanical `medtoon` → `AI_Doctor_Theater` path renames listed above); this table is the authoritative mapping.
