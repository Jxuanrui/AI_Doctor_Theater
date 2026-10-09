# NoToken 中转站（Seedance 2.0 API）文档审计（2026-10-08）

> 审计对象 https://notokenpro.apifox.cn/（44 页全量抓取，slug 溯源见各节）。控制台 notoken.pro/console。
> 用途：评估作为本项目 Seedance 2.0 视频生成通道的可行性与风险。全部运营主体信息为【candidate_research】。

## 模型清单（Seedance 2.0 档位，1 创作点=¥1）
| 模型代码 | 模式 | 单价(点/秒) |
|---|---|---|
| seedance-2.0-i2v-audio-720p | 图生视频+音频，兼容t2v，4/8/12s | 0.2 |
| seedance-2.0-i2v-audio-1080p | 图生视频+音频 4/8/12s | 0.5 |
| seedance-2.0-i2v-audio-4k | 仅i2v+音频，仅8s | 0.7（5.3页另写1.2，文档自相矛盾） |
| seedance-2.0-t2v-audio-720p/1080p | 文生视频+音频 | 0.2/0.5 |
| seedance-2.0-t2v-noaudio-720p/1080p | 文生视频无音频 | 0.2/0.5 |
| seedance-2.0-r2v-audio-720p/1080p | 多参考图生视频 | 0.2/0.5 |
| 首尾帧（各档位内） | 首帧+尾帧自动过渡 | 同档位 |
其他：Seedream 4.0（/v1/images/generations 生图，支持垫图）；GPT-5o/Claude Opus 4.5（chat，仅提及）。另有视频编辑/续接接口。

## 调用方式
- 鉴权：Authorization: Bearer <令牌>（控制台创建，每令牌独立额度可设上限）
- 形态：火山原生异步任务制——POST /api/v3/contents/generations/tasks（model/content[]/duration/ratio/seed/camera_fixed）→ GET .../tasks/{id} 轮询（queued/running/succeeded/failed），无回调
- 图片先传 POST /api/v3/files/uploads → file_id → GET /api/v3/files/{id} 取 url
- OpenAI 兼容另有 /v1/chat/completions 与 /v1/images/generations

## 计费与限制
- 应扣点数=ceil(秒×单价)；示例1080p 5s=2.5点（与ceil公式矛盾，实测为准）；失败自动全额返还；**内容审核不通过不返还**
- 充值：支付宝/微信/对公(1000点起)；提现8%手续费；新用户送10点
- **视频文件生成后10分钟删除、任务记录24小时删除、控制台仅存最近10条 → 管线必须即时自动下载**
- 未公布并发/QPS；无SLA/退款政策/用户协议/备案主体

## 审计结论
1. 价格显著低于官方刊例（火山约1元/秒、企业限定；本站1080p约5折、720p约2折）——典型池化企业额度转售，上游风控则服务整体中断【candidate_research】
2. 无主体/备案/协议 → 预充值余额有损失风险，仅建议小额
3. 全部prompt/图片/视频经其中转服务器，无隐私条款
4. 协议为火山原生 → 与 LocalMiniDrama 的 volces 通道同构，若其 base_url 可配则可配置级接入；独立脚本直调亦可

## 接入实测记录（2026-10-09）
- 令牌验证：/v1/models 200（列表为空）；billing 端点正常，usage=0
- 图片上传通道：1.1MB PNG 会断流（Broken pipe），压至 80KB JPEG 后 200，返回平铺 id/url（无需二次取 url）
- 任务创建：seedance 全档位 + gpt-5o + seedream-4.0 全部 503 "No available channel ... under group default (distributor)"——**令牌分组未绑定任何模型渠道**（服务侧账号配置问题）
- 待办：用户在控制台检查令牌分组/模型开通（或联系客服 snake2118，request id 202610090116001082529118268d9d6XUyqdLn2）；已花费 0 点

## Seedance 实测结果（2026-10-09，doubao-seedance-2.0-mini，本分组唯一可用模型）
| 试片 | 参数 | 耗时 | 大小 | 结果 |
|---|---|---|---|---|
| M1 i2v 720p 1:1 讲课 | 4s 官定图 | 92s | 1.5MB | ✅ 形象高度保真（担心眉/蓝眼/呆毛/急救箱全保留），举爪讲课+嘴部动作自然，轻微推镜，带音频 |
| M2 i2v 720p 9:16 奔跑 | 4s 官定图 | 168s | 1.6MB | ✅ 竖屏适配良好（背景自动延展），奔跑动作成立，mini 档快速动作略软 |
| M3 r2v 双参考图 讲台 | 4s 官定图+讲台图 | 91s | 1.4MB | ✅ **多参考图一致性成立**：主体=官定形象、场景=讲台参考，两张参考都被采纳 |
- 工程要点：多图必须带 `role: reference_image`；视频 URL 在返回包 content 数组内（火山原生结构）；生成后须立即下载
- 计费实测：每条 4s 片 usage=38800 tokens；billing 端点 2 条后 total_usage=110（约 $1.10≈¥7.8，**折合约 1 创作点/秒**）——显著高于文档档位表 0.2 点/秒（档位表对应聚合命名模型，本分组未开放，mini 按 token 计费折算更贵）【以控制台钱包实际扣点为准】
- 结论：mini 档"形象保真+多参考一致性"达标，适合动作验证；**量产经济性取决于能否开通 0.2点/秒的聚合档位**
