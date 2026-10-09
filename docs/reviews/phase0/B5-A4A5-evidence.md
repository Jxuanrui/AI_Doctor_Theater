# B5 / A4 / A5 执行证据与摩擦记录（2026-10-09，Phase 0 收尾）

## B5：LMD 平台内 Dr.咪第一个分镜全链路（咖啡选题，用户拍板）

### 跑通环节（按链路顺序）

| 环节 | 结果 | 证据 |
|---|---|---|
| AI 配置（text=GLM/image=CogView/video=NoToken） | ✓ | ai-configs id=1/2/3；**N2 证实：GET /ai-configs 明文返回 api_key** |
| 剧集创建 | ✓ | drama_id=1「Dr.咪科普·喝咖啡的作用与危害」 |
| 剧本生成（GLM） | ✓（glm-4-flash） | episode 1「咖啡真相」436 字；任务 ab0c2a0d/86f1ee9a completed |
| 分镜生成（GLM） | ✓ | 6 个分镜（narration+image_prompt 齐全），任务 f271ee9f completed |
| 首帧图 | **摩擦②绕行**：手工上传官定 blank 底图 | image_gen id=4 绑定 storyboard 1 |
| i2v（NoToken 火山协议） | ✓（第 4 次尝试） | video_gen id=4 completed；本地 vg_4_382ab040.mp4（1440×2560/h264+aac/5.09s）；NoToken task cgt-20261009162308-eyolp |
| 猫叫音频挂载 | ✓ | rhythm_demo.wav → storage audio/sb1_meow.wav；PUT storyboards/1 audio_local_path |
| 合成导出（字幕+AI 标识+猫叫轨） | **摩擦⑤绕行**：自研 ffmpeg（命令已固化 scripts/compose_episode.py；v2 成品 b5_final_meow_v2.mp4 字幕≤14字拆条修复） | b5_final_meow.mp4：视频+音频流、5.1s、**音轨与 rhythm_demo 相关性 1.000**（猫叫轨替换原声）、字幕+「AI生成」水印抽帧见 t0-frames/b5_final_f*.png |

### 摩擦清单（关口 1 对比关键数据）

1. **摩擦①（text）**：LMD aiClient 不发 thinking:disabled，glm-4.7 思考烧 token 返回空（T0 预警命中）；换 glm-4-flash 后 content 曾为数组（.trim 报错），改"连续叙述"措辞后通过。**glm-4.7 在 LMD 内不可用**。
2. **摩擦②（image）**：LMD 内置 aspectRatioToSize 尺寸表全部 ≥368 万像素（为其他网关设计），CogView 上限 2^21≈209 万 → **平台内出图 400 必败**（imageService.js:395 硬编码，无配置出口）。
3. **摩擦③（video 入口）**：POST /videos/image/:id 只建任务不触发处理（半成品端点）；POST /videos 才是完整入口。
4. **摩擦④（video 协议）**：火山路径默认 /video/generations（旧中转），需手动 endpoint=/api/v3/contents/generations/tasks + query_endpoint 带 {taskId} 占位符（配置可解）；**NoToken 拒收 base64 首帧**（要求公网 URL），LMD 对本地/localhost 图转 base64 → 绕行=先传 NoToken files/uploads 拿公网 URL 再回填 LMD（零代码，多一步手工）。
5. **摩擦⑤（合成）**：LMD 后处理把"旁白字幕烧录"与"旁白 TTS"绑死——无 TTS 配置则**整个后处理跳过**（猫叫烧入/字幕/水印全不执行）；且本机 ffmpeg 无 drawtext（LMD 水印在此机亦会挂）。绕行=自研 ffmpeg 单命令（双 subtitles 滤镜：字幕+全程「AI生成」水印）。
6. 崩溃一次：video_gen2 轮询 404 循环中后端进程退出（无栈日志），重启后数据无损（sqlite）。

### B5 成本

GLM 文本 6 次 ≈¥0.05；CogView 失败 2 次 ¥0；i2v：vg2 任务丢失 ~4 点 + vg4 成功 ~4-5 点 ≈ **¥8-9**（预算 ≤¥8 贴线，超因 vg2 端点试错损失，如实记录）。累计 Phase 0 收尾（T0+B5+A4/A5）≈ ¥13。

## A4/A5：lumenx 冒烟

- **A5（剧本→分镜）✓**：后端以 env 注入 GLM（LLM_PROVIDER=openai/OPENAI_*，tmux adt-lx-be 重启，env 验证 pid 2303348）；POST /projects + /projects/{id}/storyboard/analyze → **7 帧结构化分镜**（action_description/dialogue/visual_atmosphere 等字段齐全），glm-4-flash 直接调用无空内容问题（lumenx llm.py 自带剥围栏）。
- **A4（出图）**：如实记录——**lumenx 无 CogView/智谱接入**（src grep 0 命中，监工 E2 复核一致），出图需 DashScope key 或适配器；零代码验证，按计划不写代码。
- 注：lumenx env 注入的 key 位于进程环境（ps 不可见），不入 git。

## 时间台账（Phase 0 收尾全程）

T0 约 40 分钟（含 E5 重生成与判定）；B5 约 90 分钟（含 3 次失败试错与 1 次重启）；A4/A5 约 15 分钟。合计 ≈2.5 小时（监工预估 ≤1 天）。

## 补档（关口 1 复审补件，2026-10-09）

- 全部原始输出（ffprobe/音轨相关性 corr=0.999663 计算代码/LMD 后处理跳过原日志行/ss 仅 127.0.0.1/df 89%/git 哈希）→ data/phase0/evidence/B5_raw_outputs.txt
- 首中末三帧色卡对照：监工看帧判定（gate1_verdict.md）——0.5s/2.5s 虹膜黄橄榄未保持琥珀（与 E5 一致，预期内）；空白胸牌保持 ✓；4.8s 闭眼帧
- 服务关闭：LMD/lumenx 前后端全部 tmux 关闭，ss 无 5679/17177/3008 监听（用时才开纪律）；LMD sqlite 中明文 key 待 U-A 拍板后清除
- 成本实扣：GLM/NoToken 控制台截图执行方无权限获取（key 属用户账户），以估算 ¥15.7 呈报，请用户在控制台核对
