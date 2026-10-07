# Kling / Vidu 官方价目与 lumenx 对接要点（Phase 0 / C4，案头）

> 全部为公开网页信息，价格随时变动，申请前以官方页面为准；标【candidate_research】者为转述未二次核实。

## ① Kling（可灵开放平台）

计价：1 积分 = ¥1（国内）；海外 $0.14/Unit。来源：https://klingai.com/dev/pricing 、https://klingai.com/document-api/pricing/base/video

| 模型 | 方式 | 720P | 1080P | 4K |
|---|---|---|---|---|
| Kling 3.0 | 无声 | 0.6/s | 0.8/s | 3.0/s |
| Kling 3.0 | 有声未指定音色 | 0.9/s | 1.2/s | 3.0/s |
| Kling 3.0 Turbo | 有声 | 0.8/s | 1.0/s | - |
| Kling 3.0 Omni | 无参考·无声 | 0.6/s | 0.8/s | - |
| Kling 3.0 Omni | 有参考·无声 | 0.9/s | 1.2/s | - |
| Kling 2.6 | 无声/有声 | 0.7 / 1.0 | 1.0 / 1.4 | - |
| Kling 2.5 Turbo | 无声 | 0.35/s | 0.5/s | - |

- 图片 API：¥0.025/积分（Kling Image 3.0 约 ¥0.2/张）；动作控制 ¥0.9–1.2/s
- 多参考：官方"多图参考生视频"最多 4 张选主体（2026-06 上线，官方更新公告）；图生视频首尾帧 image/image_tail、element_list ≤3、voice_list ≤2
- 【candidate_research】旧模型（2.1/2.1 Master/2.0/1.6）价格页已下架，第三方转述 v2.1 Master 约 $1.70/5s

## ② Vidu（platform.vidu.cn）

计价：1 积分 = ¥0.03125（¥100=3200 积分）；**错峰 off_peak 一律 5 折**。来源：https://platform.vidu.cn/docs/pricing

| 模型 | 规格 | 标准 | 错峰 |
|---|---|---|---|
| Vidu Q3 Pro | 720p 5s | 30（≈¥0.94/条） | 15 |
| Vidu Q3 Pro | 1080p 5s | 40 | 20 |
| Vidu Q3 Turbo | 720p 5s | 20 | 10 |
| Vidu Q3 | 1080p 8s | 48 | 24 |
| Vidu Q2 Pro | 720p/1080p 5s | 15 / 20 | 7.5 / 10 |
| Vidu Q2 | 720p/1080p 5s | 10 / 15 | 5 / 7.5 |
| Vidu 2.0 | 720p 4s | 8（=¥0.25/条） | 4 |

- R2V 专长：参考生视频接口**主体最多 7 个、每主体最多 3 张图**（Q2 Pro 另支持视频主体）；prompt 用 @主体名 引用。来源：https://platform.vidu.cn/docs/reference-to-video
- 普通 img2video 仅 1 张首帧图（≤50MB）

## ③ lumenx 对接要点（/tmp/research_base/lumenx 只读核对）

- 文档：docs/1-api-reference/kling-i2v.md、vidu-i2v.md；catalog：config/model_catalog/families/{kling,vidu}.yaml
- Kling：POST /v1/videos/image2video（api-beijing.klingai.com/v1）；鉴权 JWT HS256（KLING_ACCESS_KEY+KLING_SECRET_KEY，kling.py）；也支持 dashscope 代理模式（KLING_PROVIDER_MODE 切换）
- Vidu：POST https://api.vidu.cn/ent/v2/img2video；鉴权 Token {VIDU_API_KEY}（vidu.py）；dashscope 代理同上
- **缺口**：lumenx vendor 直连只实现了单图 img2video；多图参考/R2V 依赖 dashscope 网关路由（bailian-kling-proxy / bailian-vidu-proxy）。直连 R2V 需补抓 Vidu /ent/v2/reference2video 与 Kling 多图参考文档【待 Phase 1 决策】

## 对 Phase 0 的意义

- Phase 0 不买视频 key（¥0）的决策不变；此表供 Phase 1 关口对比：Q版动态化若开视频模型，Vidu Q2 720p 错峰 ≈¥0.16/条最低；Kling 2.5 Turbo 720p ≈¥1.75/5s 条
- "DashScope 一把钥匙"可通过其 Kling/Vidu 代理获得 R2V 能力（lumenx catalog 已声明 supported_modalities 含 r2v）
