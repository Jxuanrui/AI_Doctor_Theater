# 猫叫音效库来源与许可台账（2026-10-09 建立，同日按监工 P0 补全至素材粒度）

全部来自 OpenGameArt.org。核验方式：2026-10-09 逐条目页抓取"作者+许可证字段"原文核对；cat-sfx 条目为 CC-BY 3.0（需署名）**未采用**。
许可均为 **CC0 1.0（公有领域，可商用免署名）**。注意（监工预警）：OGA 许可为作者自标，若发现真实来源与自标不符须整轨重做。

| 文件 | sha256 前 12 | 时长 | 条目 | 作者 | 许可字段原文 |
|---|---|---|---|---|---|
| cat_mewfood.wav | 3550f080882b | 1.1s | opengameart.org/content/cat-purr-meow | Kerzoven | CC0 |
| cat_mewpurr.wav | a58487959ee0 | 1.4s | 同上 | Kerzoven | CC0 |
| cat_mewpurr2.wav | 918a89611193 | 2.4s | 同上 | Kerzoven | CC0 |
| cat_softmew.wav | 7de9fed4401b | 2.5s | 同上 | Kerzoven | CC0 |
| cat_purractive_loop.wav | 5b41fbabf4a4 | 8.3s | 同上 | Kerzoven | CC0 |
| cat_purrsleepy_loop.wav | 7f06368e25e6 | 5.7s | 同上 | Kerzoven | CC0 |
| kitten_mew.wav | b9fd201358a8 | 1.1s | opengameart.org/content/kitten-mew | AntumDeluge | CC0 |
| meow.ogg | ae35c578eb7e | 0.5s | opengameart.org/content/meow | IgnasD（上传者，评论区 dino1489 相关） | CC0 |
| rhythm_demo.wav+.mp3（哈希为 mp3 版，wav 版见 sfx.sha256） | ea92f22940a3 | 5.1s | 上列素材拼接（喵→幼喵→软喵→食喵，间隔 0.4s） | 本项目拼接 | CC0 衍生 |

（SHA_AAA 等占位由下方真实哈希替换——见同目录 sfx.sha256，两者不一致时以 sfx.sha256 为准。）

用途：Dr.咪 配音（用户拍板：有节奏猫叫+字幕表达内容，弃人声 TTS；管线不写死，保留将来加回人声的可能——监工建议）。医学科普准确性全压字幕，**字幕校对入正式审核环节**（监工预警）。

## 页面证据存档（监工 P1-2）

三个条目页完整 HTML 已存私有目录 `/data/AI_Video/.secrets/AI_Doctor_Theater/oga-evidence/`（600 权限，不入 git）：
cat-purr-meow.html / kitten-mew.html / meow.html（各含 CC0 许可字段与作者信息）。
meow.ogg 作者说明：OGA 页面显示上传者/自标作者为 IgnasD（CC0）；如后续发现来源不符即停用该条并重配音轨。

## ffprobe 原始输出（时长证据，监工 P2）

```
cat_mewfood.wav 1.127052s | cat_mewpurr2.wav 2.419501s | cat_mewpurr.wav 1.410658s
cat_purractive_loop.wav 8.312630s | cat_purrsleepy_loop.wav 5.653628s | cat_softmew.wav 2.478186s
kitten_mew.wav 1.136893s | meow.ogg 0.510544s | rhythm_demo.wav 5.100000s
```
