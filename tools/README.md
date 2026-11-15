# tools：生成网站的脚本

所有页面都是静态 HTML，由 `src/` 里的内容源生成。修改内容只需改 `src/`，再运行 `build.py`。

## 依赖

```bash
pip install pymupdf lxml opencc-python-reimplemented fonttools brotli playwright
python3 -m playwright install chromium   # 只在截图检查时需要
```

## 内容源（src/）

| 文件 | 内容 | 怎么来的 |
| --- | --- | --- |
| `wanzi.json` | 《俱舍万字》按章、节、段落拆分的原文 | `extract.py` 从合订稿 PDF 第 10–37 页提取 |
| `baixia.json` | 《英译百瑕》100 条的页码、品、英译出处与原文 | `extract.py`（PDF 第 44–229 页） |
| `lijiao.json` | 《理校百例》106 条的页码、论典、卷次、CBETA 位置 | `extract.py`（PDF 第 265–466 页） |
| `song.json` | 《俱舍论颂》八品全部颂文 | `extract.py` 从 CBETA XML（T29n1560.xml）提取 |
| `wanzi_en.py` | 《万字》逐段英译，与 `wanzi.json` 段落一一对应 | 手写 |
| `concepts.py` | 概念地图：89 个概念的品属、重要性、释义、颂文定位、去处 | 手写；释义多引用 `wanzi.json` 段落 |
| `baixia_en.py` | 《百瑕》英文提要、个别条目的中文要旨、对应概念 | 手写 |
| `jiuti.py` | 《九题》九个问题、各节标题与页码、入门测验 | 手写（标题与页码取自 PDF） |

## 运行顺序

```bash
# 1. （仅在 PDF 或颂文来源变化时）重新提取 JSON
#    CBETA XML 可从 https://github.com/cbeta-org/xml-p5 获取 T/T29/T29n1560.xml
python3 tools/extract.py PATH/TO/T29n1560.xml

# 2. 生成全部页面
python3 tools/build.py

# 3. 按页面实际用字裁剪字体（内容有新字时运行）
#    NOTO_DIR：notofonts/noto-cjk 的 Serif/SubsetOTF/SC；GENTIUM_DIR：google/fonts 的 ofl/gentiumplus
python3 tools/fonts.py NOTO_DIR GENTIUM_DIR

# 4. 截图检查（先在仓库根目录运行 python3 -m http.server 8765）
python3 tools/shoot.py http://localhost:8765 /tmp/shots index.html map.html --lang=zh
python3 tools/shoot.py http://localhost:8765 /tmp/shots index.html --mobile --lang=en
```

## 文件说明

- `common.py`：页面外壳（导航、语言切换、页脚）与共用函数。
- `data.py`：读取全部内容源并交叉链接（概念↔颂文↔《万字》↔《九题》↔《百瑕》）。
- `figures.py`：九品结构图、三界九地、因缘果、四向四果、十二缘起等图表，以及七十五法、九十八随眠、二十二根表。
- `build.py`：生成十个页面。
- `charset-*.txt`：`fonts.py` 生成的用字表。
