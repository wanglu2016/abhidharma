"""Subset fonts to the characters actually used on the site.
Inputs (not in the repo, fetched separately):
  NOTO_DIR  — notofonts/noto-cjk  Serif/SubsetOTF/SC  (NotoSerifSC-Regular.otf, NotoSerifSC-SemiBold.otf)
  GENTIUM_DIR — google/fonts ofl/gentiumplus (GentiumPlus-*.ttf)
Run after build.py:  python3 tools/fonts.py NOTO_DIR GENTIUM_DIR
"""
import glob, os, subprocess, sys
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "fonts")
noto_dir, gentium_dir = sys.argv[1], sys.argv[2]

text = ""
for pat in ["*.html", "assets/js/*.js"]:
    for f in glob.glob(os.path.join(ROOT, pat)):
        text += open(f, encoding="utf-8").read()
chars = sorted(set(text) | set(" ·—–…“”‘’「」『』《》〈〉（）、，。：；？！0123456789"))
cjk = "".join(c for c in chars if ord(c) > 0x2E7F or c in "·—–…“”‘’")
latin = "".join(c for c in chars if ord(c) < 0x2E80)
os.makedirs(OUT, exist_ok=True)
open(os.path.join(ROOT, "tools", "charset-cjk.txt"), "w", encoding="utf-8").write(cjk)
open(os.path.join(ROOT, "tools", "charset-latin.txt"), "w", encoding="utf-8").write(latin)

def subset(src, dst, txtfile):
    subprocess.run(["pyftsubset", src, f"--text-file={txtfile}", "--flavor=woff2", "--layout-features=*",
                    f"--output-file={dst}", "--no-hinting", "--desubroutinize"], check=True)
    return os.path.getsize(dst)

jobs = [
    (f"{noto_dir}/NotoSerifSC-Regular.otf", "noto-serif-sc-400.woff2", "charset-cjk.txt"),
    (f"{noto_dir}/NotoSerifSC-SemiBold.otf", "noto-serif-sc-600.woff2", "charset-cjk.txt"),
    (f"{gentium_dir}/GentiumPlus-Regular.ttf", "gentium-plus-400.woff2", "charset-latin.txt"),
    (f"{gentium_dir}/GentiumPlus-Italic.ttf", "gentium-plus-400i.woff2", "charset-latin.txt"),
    (f"{gentium_dir}/GentiumPlus-Bold.ttf", "gentium-plus-700.woff2", "charset-latin.txt"),
]
for src, dst, tf in jobs:
    n = subset(src, os.path.join(OUT, dst), os.path.join(ROOT, "tools", tf))
    print(dst, n // 1024, "KB")

# coverage report
cmap = TTFont(f"{noto_dir}/NotoSerifSC-Regular.otf").getBestCmap()
missing = [c for c in cjk if ord(c) not in cmap and not c.isspace()]
print("CJK chars:", len(cjk), "missing in Noto Serif SC:", "".join(missing))

css = """/* Subset web fonts. Noto Serif SC and Gentium Plus are licensed under the SIL Open Font License 1.1 (see OFL.txt). */
@font-face{font-family:"Noto Serif SC";src:url(noto-serif-sc-400.woff2) format("woff2");font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:"Noto Serif SC";src:url(noto-serif-sc-600.woff2) format("woff2");font-weight:600 700;font-style:normal;font-display:swap}
@font-face{font-family:"Gentium Plus";src:url(gentium-plus-400.woff2) format("woff2");font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:"Gentium Plus";src:url(gentium-plus-400i.woff2) format("woff2");font-weight:400;font-style:italic;font-display:swap}
@font-face{font-family:"Gentium Plus";src:url(gentium-plus-700.woff2) format("woff2");font-weight:600 700;font-style:normal;font-display:swap}
"""
open(os.path.join(OUT, "fonts.css"), "w").write(css)
