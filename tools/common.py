"""Shared helpers for the static site generator."""
import html, json, os, re, sys
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
sys.path.insert(0, SRC)

from opencc import OpenCC
_t2s = OpenCC("t2s")

def s(t):
    """Traditional -> simplified (for terms written in Xuanzang's characters)."""
    return _t2s.convert(t).replace("阿毘达磨", "阿毗达磨")

def esc(x):
    return html.escape(str(x), quote=True)

def T(zh, en, tag="span", cls="", zlang="zh-Hans"):
    """Bilingual inline/blocks. Visibility is controlled by html[data-lang]."""
    c = (" " + cls) if cls else ""
    return (f'<{tag} class="zh{c}" lang="{zlang}">{zh}</{tag}>'
            f'<{tag} class="en{c}" lang="en">{en}</{tag}>')

BOOK_JT = "books/" + quote("俱舍九題電子書.pdf")
BOOK_HD = "books/" + quote("《俱舍萬字》《俱舍英譯百瑕》《阿毘達磨理校百例》250401.pdf")

def pdf(book, page):
    return f"{BOOK_JT if book == 'jt' else BOOK_HD}#page={page}"

NAV = [
    ("index.html", "首页", "Home"),
    ("map.html", "地图", "Map"),
    ("outline.html", "纲要", "Outline"),
    ("verses.html", "颂文", "Verses"),
    ("concepts.html", "概念", "Concepts"),
    ("jiuti.html", "九题", "Nine Questions"),
    ("translations.html", "英译百瑕", "Translation Flaws"),
    ("emendations.html", "理校百例", "Emendations"),
    ("genpin-1.html", "练习", "Practice"),
    ("resources.html", "资源", "Resources"),
]

LANG_BOOT = """<script>(function(){var l;try{l=localStorage.getItem('abhi-lang')}catch(e){}if(l!=='zh'&&l!=='en'&&l!=='both'){l=((navigator.language||'').toLowerCase().indexOf('zh')===0)?'zh':'en'}document.documentElement.setAttribute('data-lang',l)})();</script>"""

SITE_ZH = "说一切有部阿毗达磨"
SITE_EN = "Sarvāstivāda Abhidharma"
BASE_URL = "https://wanglu2016.github.io/abhidharma/"

def page(fname, title_zh, title_en, body, desc_zh, desc_en="", scripts=(), body_cls="", head_extra=""):
    nav = []
    for href, zh, en in NAV:
        cur = ' aria-current="page"' if href == fname else ""
        nav.append(f'<a href="{href}"{cur}>{T(zh, en)}</a>')
    scr = "".join(f'<script src="{x}"></script>' for x in scripts)
    full_title = f"{title_zh} | {SITE_ZH}" if fname != "index.html" else f"{SITE_ZH}学习 | {SITE_EN}"
    return f"""<!DOCTYPE html>
<html lang="zh-CN" data-lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc_zh)} {esc(desc_en)}">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(desc_zh)}">
<meta property="og:image" content="{BASE_URL}assets/og.png">
<meta property="og:type" content="website">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
{LANG_BOOT}
<link rel="stylesheet" href="assets/fonts/fonts.css">
<link rel="stylesheet" href="assets/css/site.css">
{head_extra}
</head>
<body class="{body_cls}">
<a class="skip" href="#main">{T("跳到正文", "Skip to content")}</a>
<header class="site">
  <div class="bar">
    <a class="brand" href="index.html"><span class="seal" aria-hidden="true">論</span><span class="brand-t">{T(SITE_ZH + "学习", "Studying " + SITE_EN)}</span></a>
    <div class="lang" role="group" aria-label="Language / 语言">
      <button type="button" data-set-lang="zh" lang="zh-Hans">中</button><button type="button" data-set-lang="en" lang="en">EN</button><button type="button" data-set-lang="both" lang="zh-Hans">中英</button>
    </div>
  </div>
  <nav class="main-nav" aria-label="主导航 Main">{''.join(nav)}</nav>
</header>
<main id="main">
{body}
</main>
<footer class="site">
  <div class="foot">
    <p>{T("内容取自王路的阿毗达磨著作；颂文据 CBETA《阿毘達磨俱舍論本頌》（T1560），供非商业使用。英文为辅助译文，以玄奘译语为准。",
          "Content is drawn from Wang Lu's Abhidharma writings; verses from CBETA, T1560, for non-commercial use. English renderings are reading aids: Xuanzang's Chinese terms are authoritative.")}</p>
    <ul class="foot-links"><li><a href="https://github.com/wanglu2016/abhidharma">GitHub</a></li><li><a href="resources.html#books">{T("下载著作 PDF", "Download the PDFs")}</a></li><li>{T("勘误请寄", "Corrections to")} <a href="mailto:cuechin@163.com">cuechin@163.com</a></li></ul>
  </div>
</footer>
<script src="assets/js/site.js"></script>
{scr}
</body>
</html>
"""

def write(fname, content):
    path = os.path.join(ROOT, fname)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def load_json(name):
    with open(os.path.join(SRC, name), encoding="utf-8") as f:
        return json.load(f)
