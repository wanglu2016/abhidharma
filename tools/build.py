"""Build every page of the site from src/. Run: python3 tools/build.py"""
import json, re
from common import T, esc, s, page, write, pdf, BOOK_JT, BOOK_HD, SITE_ZH, SITE_EN
import data as D
import figures as F
import jiuti as JT
import concepts as CM

PIN, PIN_IDS = D.PIN, D.PIN_IDS
TIER = D.TIER

def mark(c):
    t = TIER[c["tier"]]
    m = f'<span class="mk" title="{t[0]}">{t[2]}</span>' if t[2] else ""
    memo = '<span class="memo" title="入门必背 (entrance test)">背</span>' if c["memo"] else ""
    return m, memo

def chip(c, href=None, extra=""):
    m, memo = mark(c)
    tag = "a" if href else "button"
    attr = f'href="{href}"' if href else 'type="button" aria-pressed="false"'
    mile = f'<span class="mile">{T(c["mile"][0], c["mile"][1])}</span>' if c.get("mile") else ""
    return (f'<{tag} class="chip" {attr} data-id="{c["id"]}" data-tier="{c["tier"]}"{extra}><span class="ct">{m}<span lang="zh-Hans">{esc(c["s"])}</span>{memo}{mile}</span>'
            f'<span class="en" lang="en">{esc(c["en"])}</span></{tag}>')

def pin_short(pid):
    return PIN[pid]["s"].replace("分别", "")

def verse_link(v):
    return f'<a href="verses.html#{v["id"]}">{pin_short(v["pin"])} {v["label"]}</a>'

def related_chips(ids):
    return "".join(chip(D.CBYID[i], href=f"concepts.html#{i}") for i in ids if i in D.CBYID)

# ══════════════════════ HOME ══════════════════════
def build_home():
    hero_verse = ["淨慧隨行名對法", "及能得此諸慧論", "攝彼勝義依彼故", "此立對法俱舍名"]
    vv = "".join(f"<span>{l}</span>" for l in hero_verse)
    hero = f"""
<section class="hero" aria-labelledby="hero-h">
 <div class="hero-in">
  <div>
   <h1 id="hero-h">{T("说一切有部阿毗达磨学习", "Studying Sarvāstivāda Abhidharma")}</h1>
   <p>{T("以《阿毗达磨俱舍论》为中心，按王路的四部著作安排学习：先看全局地图，再读纲要、背颂文，最后进入《俱舍九题》的高阶问题。",
         "Centred on the Abhidharmakośa and organised around Wang Lu's four books: see the whole map first, then read the outline and learn the verses, and finally take on the advanced problems of the Nine Questions.")}</p>
   <p class="by">{T("王路 著　网站内容据作者著作整理", "Writings by Wang Lu, arranged for study")}</p>
   <div class="cta">
     <a class="btn" href="map.html">{T("看全局地图", "Open the map")}</a>
     <a class="btn ghost" href="outline.html">{T("从纲要读起", "Start with the outline")}</a>
     <a class="btn ghost" href="translations.html">{T("读英译本的人从这里开始", "Reading Pruden or Sangpo? Start here")}</a>
   </div>
   <p class="gloss">{T("右为《俱舍论》开卷第二颂：清净的慧及其随行名为“对法”（阿毗达磨），能得此慧的论也名对法；此论摄彼胜义、依彼而成，故名“对法俱舍”。",
        "At right, the second verse of the Kośa: pure understanding with what accompanies it is called Abhidharma, and so are the treatises that lead to it; this work gathers their essence and rests on them, hence the name Abhidharma-kośa, 'treasury of Abhidharma'.")}</p>
  </div>
  <p class="vverse" lang="zh-Hant">{vv}<cite>俱舍論頌・分別界品</cite></p>
 </div>
</section>"""

    steps = [
        ("读纲要，记住“是什么”", "Read the outline: remember the 'what'", "outline.html",
         "《俱舍万字》用约一万字列出《俱舍》纲目。作者说基础阶段“不适合多问为什么，而适合多记住是什么”；前面看不懂的先跳过。",
         "The Ten Thousand Characters lays out the Kośa's framework in about ten thousand characters. At this stage, the author says, remember what things are rather than asking why; skip what you don't yet understand."),
        ("背《俱舍论颂》", "Memorise the Verses", "verses.html",
         "作者心目中熟练的标准：八十分钟内背完全部颂，随机抽取任意一颂都能正确讲解。颂文页提供随机抽颂和遮盖自测。",
         "The author's benchmark: recite all the verses within eighty minutes and correctly explain any verse drawn at random. The verse page offers random draws and masking for self-testing."),
        ("按建议次序通读《俱舍》，对照地图", "Read the Kośa in the suggested order, with the map", "map.html",
         "建议次序：定品；贤圣品、随眠品；界品、根品；业品；世间品、智品。地图标出每个概念属于哪一品、作者认为它是要点、难点还是基本操作。",
         "Suggested order: Meditation; Path and Anuśaya; Elements and Faculties; Action; World and Knowledge. The map shows which chapter each concept belongs to and whether the author treats it as a key point, a difficulty or a basic operation."),
        ("做入门测验", "Take the entrance test", "jiuti.html#entry",
         "默写九十八随眠、七十五法、三十七道品、二十二根；能解释二十二根的异熟、三性、何所断等。半小时内闭卷全对，即具备读《九题》的基础。",
         "Write out the 98 anuśayas, 75 dharmas, 37 factors of awakening and 22 faculties; explain the faculties by retribution, nature and mode of abandonment. All correct, closed-book, in half an hour means you are ready for the Nine Questions."),
        ("读《俱舍九题》", "Work through the Nine Questions", "jiuti.html",
         "前四题“登堂”，五、六题“入室”，第七题“专家”，八、九题是向阿毗达磨深处的探寻。全日制、每日五小时，从零起步约八个月。",
         "Questions 1–4: entering the hall; 5–6: the inner room; 7: expert; 8–9: the far reaches. Full-time, five hours a day, about eight months from zero."),
    ]
    path = "".join(f'<li><div><h3><a href="{h}">{T(zh, en)}</a></h3><p>{T(dz, de)}</p></div></li>' for zh, en, h, dz, de in steps)

    books = [
        ("outline.html", "俱舍万字", "Ten Thousand Characters on the Kośa", "基础", "Basic",
         "《俱舍》纲目，约一万字，用简体写成，面向初学。本站全文收录并配英译。", "The Kośa's framework in ~10,000 characters, for beginners. Full text with English on this site."),
        ("translations.html", "俱舍英译百瑕", "One Hundred Flaws in the English Kośa", "比《九题》简单", "Easier than the Nine Questions",
         "逐条指出 Pruden 与 Lodrö Sangpo 两部英译本的一百处错误。附录有十余条英文稿。", "One hundred errors in the Pruden and Lodrö Sangpo translations, entry by entry; an appendix gives a dozen in English."),
        ("emendations.html", "阿毗达磨理校百例", "One Hundred Doctrinal Emendations", "难于《百瑕》，易于《九题》", "Harder than the Flaws, easier than the Nine Questions",
         "依阿毗达磨义理校正《大正藏》毘昙部的误字，示范如何“理校”。", "Corrects scribal errors in the Taishō Abhidharma section by doctrinal reasoning, showing how such emendation works."),
        ("jiuti.html", "俱舍九题", "The Nine Questions of the Kośa", "高阶", "Advanced",
         "高阶阿毗达磨串讲。九个问题贯穿全论，2024 年在台湾出版。", "An advanced course: nine problems that run through the whole treatise. Published in Taiwan, 2024."),
    ]
    bk = "".join(f'<div class="book"><h3><a href="{h}">{T("《"+zh+"》", en)}</a></h3><p class="lvl">{T(lz, le)}</p><p>{T(dz, de)}</p></div>' for h, zh, en, lz, le, dz, de in books)

    method = [
        ("要学好阿毗达磨，必须反反复复看《婆沙》、《俱舍》、《正理》原文，有些段落可能要读过五十遍以上。不过要记住，不是让你通读……所有读过五十遍以上的段落，基本上都是因为碰到具体问题去检索，然后反复读。",
         "To learn Abhidharma well you must read the Vibhāṣā, the Kośa and the Nyāyānusāra again and again; some passages fifty times or more. But not by reading straight through: those passages get read fifty times because a concrete problem sends you searching for them.", "《俱舍九题》序"),
        ("我强烈建议结合问题学习《俱舍》。", "I strongly recommend studying the Kośa through problems.", "《俱舍九题》要点"),
        ("可以尝试一个概念一个概念地学。但千万不要企图“掌握了一个概念之后再学下一个”——不把所有概念学完，有些概念是无论如何也掌握不了的。",
         "You can try to learn concept by concept, but never try to master one before moving to the next: some concepts cannot be grasped until all have been learned.", "《俱舍九题》要点"),
        ("阿毗达磨的核心就是两个字：离染。", "The core of Abhidharma is one word: detachment.", "《俱舍九题》要点"),
    ]
    mq = "".join(f'<blockquote class="quote"><span class="zh" lang="zh-Hans">{z}</span><span class="en" lang="en">{e}</span><cite>{c}</cite></blockquote>' for z, e, c in method)

    body = f"""{hero}
<div class="wrap">
 <section class="block" style="margin-top:2.6rem" aria-labelledby="path-h">
  <div class="cols" style="grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);align-items:start">
   <div>
    <h2 id="path-h">{T("学习路线", "A route through the material")}</h2>
    <p class="muted read">{T("下面的次序整理自作者在《俱舍九题》序与要点中的建议。", "This sequence follows the author's advice in the preface and key points of the Nine Questions.")}</p>
    <ol class="path">{path}</ol>
   </div>
   <div>
    <h2>{T("作者谈方法", "The author on method")}</h2>
    <div style="margin-top:1rem">{mq}</div>
    <p class="note">{T("检索工具：CBETA（毘昙部原文）、SAT（快道林常《俱舍论法义》），见", "Search tools: CBETA for the Abhidharma texts, SAT for Kaidō's Hōgi; see")} <a href="resources.html#tools">{T("资源", "Resources")}</a>。</p>
   </div>
  </div>
 </section>
 <section class="block" aria-labelledby="books-h">
  <h2 id="books-h">{T("四部著作", "Four books")}</h2>
  <p class="muted read">{T("难度按作者自己的说明排列。", "Ordered by difficulty, as the author describes them.")}</p>
  <div class="books">{bk}</div>
 </section>
 <section class="block" aria-labelledby="en-h">
  <h2 id="en-h">{T("给中文不熟练的读者", "If Chinese is not your first language")}</h2>
  <div class="read">
   <p>{T("作者认为玄奘的译语最为精确：“只懂汉语完全可以”学好《俱舍》，而只依靠英译本则会被大量误译带偏。本站为英文读者准备了：",
         "The author holds that Xuanzang's Chinese is the most precise vehicle for the Kośa, and that relying on the English translations alone leads readers astray at many points. For English readers this site provides:")}</p>
   <ul>
    <li>{T("《俱舍万字》全文逐段英译，以及近百个概念的中、梵、英对照释义；", "an English rendering of the whole outline, and some ninety concepts with Chinese, Sanskrit and English;")}</li>
    <li>{T("《英译百瑕》一百条的英文提要，标出颂号和两部英译本的页码，可以边读英译边查；", "English summaries of all one hundred Translation Flaws, keyed to verse numbers and to page numbers in Pruden and Lodrö Sangpo, for use while reading;")}</li>
    <li>{T("界面可切换为中英对照：中文术语始终保留，便于在 CBETA 检索原文。", "a parallel Chinese–English view; Chinese terms are always kept so you can search the originals on CBETA.")}</li>
   </ul>
  </div>
 </section>
</div>"""
    write("index.html", page("index.html", "首页", "Home", body,
          "以王路《俱舍九题》《俱舍万字》《俱舍英译百瑕》《阿毗达磨理校百例》为骨架的说一切有部阿毗达磨学习网站：全局地图、纲要、颂文、概念与英译指误。",
          "A study site for Sarvāstivāda Abhidharma built on Wang Lu's books: map, outline, verses, concepts and the flaws of the English Kośa."))

# ══════════════════════ MAP ══════════════════════
def build_map():
    cols = []
    for pid in PIN_IDS:
        if pid == "po":
            continue
        p = PIN[pid]
        cs = [c for c in D.CONCEPTS if c["pin"] == pid]
        role = {"jie": ("总明：诸法体", "general: substance"), "gen": ("总明：诸法用", "general: function"),
                "shi": ("有漏之果", "fruit, with-outflow"), "ye": ("有漏之因", "cause, with-outflow"), "sui": ("有漏之缘", "condition, with-outflow"),
                "xian": ("无漏之果", "fruit, outflow-free"), "zhi": ("无漏之因", "cause, outflow-free"), "ding": ("无漏之缘", "condition, outflow-free")}[pid]
        cols.append(f'''<div class="acol" id="col-{pid}"><h3 data-pin="{pid}">{T(p["s"].replace("分别",""), p["en"].split(":")[0])}<span class="juan">{T("卷"+p["juan"], "fasc. "+p["juan"])}</span></h3><span class="role">{T(role[0], role[1])}</span>{"".join(chip(c) for c in cs)}</div>''')
    tiers_legend = "".join(f'<li><span class="mk">{t[2] or "　"}</span>{T(t[0], t[1])}</li>' for k, t in TIER.items())
    filt = "".join(f'<label><input type="checkbox" data-tier-filter="{k}" checked> <span class="mk">{t[2]}</span>{T(t[0], t[1])}</label>' for k, t in TIER.items())
    notes = "".join(f'''<div class="pin-note" id="note-{pid}"><h3>{T(PIN[pid]["s"], PIN[pid]["en"])}</h3><p class="zh" lang="zh-Hant">{esc(PIN[pid]["note_zh"])}</p><p class="en">{esc(PIN[pid]["note_en"])}</p></div>''' for pid in PIN_IDS if pid != "po")
    atlas_data = {
        "pins": {pid: {"s": PIN[pid]["s"], "en": PIN[pid]["en"], "short": pin_short(pid)} for pid in PIN_IDS},
        "tiers": {k: [v[0], v[1], v[2]] for k, v in TIER.items()},
        "concepts": D.CONCEPTS,
    }
    empty = f'<p class="empty">{T("点选左侧任一概念，这里显示它的定义、颂文、在作者著作中的去处，以及相关概念（左侧以红边标出）。", "Select any concept to see its definition, verses, where the author discusses it, and related concepts (outlined in red).")}</p>'
    body = f"""
<div class="map-band">
 <div class="wrap">
  <h1 style="color:var(--gold-3)">{T("全局地图", "The map")}</h1>
  <p class="muted lede" style="color:var(--gold-2)">{T("普光《俱舍论记》卷一把九品分为三层：界、根二品总明有漏无漏；世间、业、随眠三品别明有漏的果、因、缘；贤圣、智、定三品别明无漏的果、因、缘；破执我品单释无我。",
      "Puguang (Jushelun ji, fasc. 1) reads the nine chapters in three layers: Elements and Faculties treat the with-outflow and outflow-free in general; World, Action and Anuśaya treat the fruit, cause and condition of the with-outflow; Path, Knowledge and Meditation the fruit, cause and condition of the outflow-free; the last chapter refutes the self.")}</p>
  {F.structure_svg(PIN)}
 </div>
</div>
<div class="wrap">
 <section class="block" aria-labelledby="atlas-h">
  <h2 id="atlas-h">{T("概念地图", "Concept atlas")}</h2>
  <p class="muted read">{T("概念依作者〈《俱舍》术语要点一览〉排列。标记只来自作者自己的判断：", "Concepts follow the author's list of key Kośa terms. Marks reflect only the author's own judgements:")}</p>
  <ul class="legend">{tiers_legend}<li><span class="memo" style="margin:0 .3em 0 0">背</span>{T("入门测验必背", "In the entrance test")}</li><li><span class="mile" style="margin:0 .3em 0 0">{T("登堂", "Hall")}</span>{T("作者所说的学习关口", "A milestone the author names")}</li></ul>
  <div class="atlas-tools" style="margin-top:1rem">
   <input type="search" id="f-search" placeholder="搜索 / Search" aria-label="搜索概念 Search concepts">
   {filt}
   <label><input type="checkbox" id="f-memo"> {T("只看必背", "Entrance test only")}</label>
  </div>
  <div class="atlas" id="atlas">
   <div class="atlas-cols">{"".join(cols)}</div>
   <aside class="panel idle" id="panel" aria-live="polite" data-empty="{esc(empty)}">{empty}</aside>
  </div>
 </section>
 <section class="block" aria-labelledby="pins-h">
  <h2 id="pins-h">{T("作者对各品的判断", "The author on each chapter")}</h2>
  <p class="muted read">{T("原文见《俱舍九题》〈《俱舍》术语要点一览〉。", "From the Nine Questions, 'Key Kośa terms at a glance'.")}</p>
  <div class="cols">{notes}</div>
 </section>
</div>
<script>window.ATLAS={json.dumps(atlas_data, ensure_ascii=False)};</script>"""
    write("map.html", page("map.html", "全局地图", "Map", body,
          "《俱舍》九品结构与概念地图：每个概念所属的品，以及作者判定的要点、难点、基本操作。",
          "The structure of the Kośa's nine chapters and a map of its concepts, with the author's own importance marks.",
          scripts=["assets/js/map.js"]))

# ══════════════════════ OUTLINE (萬字) ══════════════════════
FIG_AFTER = {
    "1.3": ("五位七十五法", "The seventy-five dharmas in five groups", F.dharmas_html),
    "2.1": ("三界九地与三地（据《万字》2.1、6.4）", "Three realms, nine stages, three vitarka-stages", F.realms_svg),
    "2.2": ("九十八随眠：三界 × 五部", "The 98 anuśayas: three realms × five classes", F.anusaya_table),
    "2.3": ("二十二根诸门分别（据《万字》2.3；三界系据根品颂“欲色无色系，如次除后三……”）", "The 22 faculties analysed (realm column from the verse of the faculties chapter)", F.roots_table),
    "3.3": ("六因、四缘、五果的对应", "How the six causes, four conditions and five fruits correspond", F.causes_svg),
    "5.4": ("四向四果的位置（据《万字》5.3–5.4）", "Where the four candidates and four fruits stand", lambda: F.path_chain() + F.track_html()),
    "6.5": ("缘起十二支：三际与惑、业、事", "The twelve links: three periods; defilement, action, things", F.links_svg),
}
def build_outline():
    toc = []
    secs = []
    toc.append(f'<li><a href="#preface">{T("说明", "Notes")}</a></li>')
    for ch in D.WZ["chapters"]:
        items = []
        for sec in ch["sections"]:
            sid = sec["id"]; anchor = "s" + sid.replace(".", "-")
            items.append(f'<li><a href="#{anchor}">{sid} {esc(sec["title"])}</a></li>')
        toc.append(f'<li><span class="ch">{T("第"+str(ch["no"])+"章", "Chapter "+str(ch["no"]))}</span><ol>{"".join(items)}</ol></li>')
    pre = "".join(f'<div class="par"><p class="zh">{esc(z)}</p><p class="en" lang="en">{esc(e)}</p></div>' for z, e in D.WZ_PREFACE)
    notes = "".join(f'<div class="par"><p class="zh">{esc(z)}</p><p class="en" lang="en">{esc(e)}</p></div>' for z, e in D.WZ_NOTES)
    for ch in D.WZ["chapters"]:
        secs.append(f'<h2 class="chapter-h">{T("第"+str(ch["no"])+"章", "Chapter "+str(ch["no"]))}</h2>')
        for sec in ch["sections"]:
            sid = sec["id"]; anchor = "s" + sid.replace(".", "-")
            pars = "".join(f'<div class="par"><p class="zh">{esc(z)}</p><p class="en" lang="en">{esc(e)}</p></div>' for z, e in sec["pairs"])
            fig = ""
            if sid in FIG_AFTER:
                fz, fe, fn = FIG_AFTER[sid]
                fig = f'<figure class="fig"><figcaption>{T(fz, fe)}</figcaption>{fn()}</figure>'
            rel = D.WZ_CONCEPTS.get(sid, [])
            relh = f'<p class="related">{T("地图上的概念：", "On the map: ")}{"".join(chip(D.CBYID[i], href="map.html#c="+i) for i in rel)}</p>' if rel else ""
            secs.append(f'<section class="sec" id="{anchor}"><h3><span class="no">{sid}</span><span lang="zh-Hans">{esc(sec["title"])}</span></h3>{pars}{fig}{relh}</section>')
    body = f"""
<div class="wrap">
 <header class="page-head">
  <h1>{T("纲要：《俱舍万字》", "Outline: Ten Thousand Characters on the Kośa")}</h1>
  <p class="lede">{T("王路为零基础读者写的《俱舍》纲目，全文收录于刚晓法师主编《灵山海会》第 49 期。中文为作者原文；英文是本站的辅助译文。图表为本站据原文所制。",
       "Wang Lu's outline of the Kośa for readers starting from zero (also printed in Lingshan Haihui no. 49). The Chinese is the author's text; the English is this site's reading aid; the figures are drawn from the text.")}</p>
 </header>
 <div class="doc">
  <nav class="toc" aria-label="目录 Contents"><ol>{"".join(toc)}</ol></nav>
  <article>
   <section class="sec" id="preface">
    {pre}
    <h3><span lang="zh-Hans">说明</span><span class="en" lang="en" style="font-weight:400;color:var(--ink-2)">Notes</span></h3>
    {notes}
   </section>
   {"".join(secs)}
   <p class="note"><a href="{pdf('hd', 10)}">{T("在 PDF 中阅读《俱舍万字》原排版（第 10–37 页）", "Read the original layout in the PDF (pp. 10–37)")}</a></p>
  </article>
 </div>
</div>"""
    write("outline.html", page("outline.html", "纲要", "Outline", body,
          "王路《俱舍万字》全文网页版，逐段英译，并配七十五法、九十八随眠、二十二根、三界九地、因缘果、四向四果、十二缘起图表。",
          "Wang Lu's outline of the Kośa with a paragraph-by-paragraph English rendering and reference figures."))

# ══════════════════════ VERSES ══════════════════════
def build_verses():
    opts = "".join(f'<option value="{pid}">{PIN[pid]["s"]}</option>' for pid in PIN_IDS if pid != "po")
    secs = []
    for pid in PIN_IDS:
        if pid == "po":
            continue
        vb = D.VERSE_BY_PIN[pid]
        vs = []
        for v in vb["rows"]:
            l1 = f'<span class="l"><span class="h h1">{esc(v["h"][0][0])}</span><span class="h h2">{esc(v["h"][0][1])}</span></span>'
            l2 = f'<span class="l"><span class="h">{esc(v["h"][1][0])}</span><span class="h">{esc(v["h"][1][1])}</span></span>' if len(v["h"]) > 1 else ""
            where = f'{PIN[pid]["s"]} {v["label"]}'
            vs.append(f'<div class="verse {v["kind"]}" id="{v["id"]}" data-text="{esc(v["text"])}" data-where="{esc(where)}"><span class="n"><a href="#{v["id"]}">{v["label"]}</a></span><span lang="zh-Hant">{l1}{l2}</span></div>')
        note = PIN[pid].get("verses")
        extra = ""
        if pid == "jie": extra = T("（另有开卷归敬三颂）", " (plus three opening verses)")
        if pid == "ding": extra = T("（另有卷末结颂四首）", " (plus four closing verses)")
        if pid == "shi": extra = T("（CBETA 品题注“九十九颂”，按四句一颂计为一百）", " (the heading says 99; counting four lines per verse gives 100)")
        secs.append(f'<section class="pin-sec" data-pin="{pid}" id="p-{pid}"><h2>{T(PIN[pid]["s"], PIN[pid]["en"])}</h2><p class="sub">{T(str(vb["count"])+"颂", str(vb["count"])+" verses")}{extra}</p><div class="vlist">{"".join(vs)}</div></section>')
    body = f"""
<div class="wrap">
 <header class="page-head">
  <h1>{T("颂文：《俱舍论颂》", "Verses of the Abhidharmakośa")}</h1>
  <p class="lede">{T("玄奘译《阿毘达磨俱舍论本颂》（T1560）全文。作者对熟练的要求是：八十分钟内背完，随机抽取任意一颂都可以正确讲解。下面可以按品筛选、随机抽颂，或遮盖后点击逐颂自测。",
       "The complete verses in Xuanzang's translation (T1560). The author's benchmark: recite them all within eighty minutes, and explain any verse drawn at random. Filter by chapter, draw at random, or mask the text and click a verse to check yourself.")}</p>
  <p class="note">{T("颂序号按 CBETA 本四句一颂顺序编排，仅供本站检索，与梵本及英译本的偈颂编号不完全一致。", "Numbering counts four lines per verse in the CBETA text, for reference on this site only; it does not match the Sanskrit kārikā numbering used by the English translations.")}</p>
 </header>
 <div class="vtools" role="group" aria-label="背诵工具 Recitation tools">
  <label>{T("品", "Chapter")} <select id="v-pin"><option value="">全部八品 / All eight</option>{opts}</select></label>
  <span class="seg" role="group" aria-label="遮盖 Mask"><button type="button" data-mask="none" aria-pressed="true">{T("不遮", "Show all")}</button><button type="button" data-mask="tail">{T("只露首句", "First line only")}</button><button type="button" data-mask="all">{T("全遮", "Hide all")}</button></span>
  <button type="button" class="btn" id="v-draw">{T("随机抽一颂", "Draw a verse")}</button>
  <input type="search" id="v-search" placeholder="查颂 / Find" aria-label="查找颂文 Find in verses">
  <span class="count"><span id="v-count"></span> {T("颂", "verses")}</span>
 </div>
 <div class="draw" id="draw" hidden>
  <div class="note where"></div>
  <p class="v" lang="zh-Hant"></p>
  <button type="button" class="btn ghost reveal">{T("揭示全颂", "Reveal")}</button> <a class="go" href="#">{T("在列表中定位", "Locate in list")}</a>
 </div>
 {"".join(secs)}
 <p class="note">{T("文本来源：CBETA 电子佛典，T29, no. 1560。依 CBETA 授权，供非商业使用。", "Source: CBETA, T29 no. 1560, for non-commercial use under CBETA's terms.")}</p>
</div>"""
    write("verses.html", page("verses.html", "颂文", "Verses", body,
          "《俱舍论颂》全文（CBETA T1560），按品浏览、随机抽颂与遮盖自测。",
          "The complete verses of the Kośa with chapter filter, random draw and self-test masking.",
          scripts=["assets/js/verses.js"]))

# ══════════════════════ CONCEPTS ══════════════════════
def build_concepts():
    groups = []
    for pid in PIN_IDS:
        if pid == "po":
            continue
        cards = []
        for c in [x for x in D.CONCEPTS if x["pin"] == pid]:
            m, memo = mark(c)
            mile = f'<span class="mile">{T(c["mile"][0], c["mile"][1])}</span>' if c["mile"] else ""
            tier = TIER[c["tier"]]
            body = "".join(f'<p class="zh">{esc(z)}</p><p class="en" lang="en">{esc(e)}</p>' for z, e in zip(c["zh"], c["enl"]))
            if c["note_zh"]:
                body += f'<div class="callout">{T(esc(c["note_zh"]), esc(c["note_en"]))}</div>'
            links = []
            if c["verses"]:
                links.append(f'<div><b>{T("颂", "Verses")}</b>{"　".join(verse_link(v) for v in c["verses"])}</div>')
            if c["wz"]:
                links.append(f'<div><b>{T("纲要", "Outline")}</b>{" ".join(f"<a href=\"outline.html#s{x.replace(chr(46), chr(45))}\">{x}</a>" for x in c["wz"])}</div>')
            if c["jt"]:
                links.append(f'<div><b>{T("九题", "Nine Q.")}</b>{" ".join(f"<a href=\"jiuti.html#q{n}\">{T(f'第{n}题', f'Q{n}')}</a>" for n in c["jt"])}</div>')
            if c["bx"]:
                links.append(f'<div><b>{T("英译百瑕", "Flaws")}</b>{" ".join(f"<a href=\"translations.html#f{n}\">#{n}</a>" for n in c["bx"])}</div>')
            if c["rel"]:
                links.append(f'<div><b>{T("相关", "Related")}</b>{"、".join(f"<a href=\"#{r}\">{esc(D.CBYID[r][chr(115)])}</a>" for r in c["rel"])}</div>')
            src = T("释义取自《俱舍万字》" + "、".join(c["wz"]), "Definition from the Outline " + ", ".join(c["wz"])) if c["src"] == "wz" else T("编者据《俱舍》撰写简释", "Short definition by the site editor, from the Kośa")
            text = " ".join([c["s"], c["t"], c["skt"], c["en"]] + c["zh"] + c["enl"])
            trad = f'<span class="trad" lang="zh-Hant">{esc(c["t"])}</span>' if c["t"] != c["s"] else ""
            cards.append(f'''<article class="ccard" id="{c["id"]}" data-filter-item data-text="{esc(text)}" data-tier="{c["tier"]}"{' data-memo="1"' if c["memo"] else ''}>
<div class="head"><h3>{m}<span lang="zh-Hans">{esc(c["s"])}</span>{memo}</h3>{trad}<i class="skt">{esc(c["skt"])}</i><span class="ename">{esc(c["en"])}</span>
<span class="note">{T(tier[0], tier[1])}{mile}</span><br><a class="note" href="map.html#c={c["id"]}">{T("在地图上看", "Show on map")}</a></div>
<div class="body">{body}<div class="links">{"".join(links)}</div><p class="src">{src}</p></div></article>''')
        groups.append(f'<section class="cgroup" data-filter-group id="g-{pid}"><h2>{T(PIN[pid]["s"], PIN[pid]["en"])}<small>{T("卷"+PIN[pid]["juan"], "fasc. "+PIN[pid]["juan"])}</small></h2>{"".join(cards)}</section>')
    tier_opts = "".join(f'<option value="{k}">{t[0]} {t[1]}</option>' for k, t in TIER.items())
    body = f"""
<div class="wrap" data-filter-scope>
 <header class="page-head">
  <h1>{T("概念", "Concepts")}</h1>
  <p class="lede">{T("按品排列的全部概念：简体、繁体（玄奘原字，便于检索 CBETA）、梵语、英文，附定义、颂文与去处。释义凡见于《俱舍万字》者照录原文。",
       "All concepts by chapter: simplified and traditional Chinese (Xuanzang's characters, for searching CBETA), Sanskrit and English, with definitions, verses and cross-references. Where the Outline covers a term its text is quoted verbatim.")}</p>
 </header>
 <div class="cfilter">
  <input type="search" data-filter-input placeholder="搜索：随增、anuśaya、faculty……" aria-label="搜索 Search">
  <label>{T("类别", "Mark")} <select data-filter-select="tier"><option value="">全部 / All</option>{tier_opts}</select></label>
  <label>{T("必背", "Entrance test")} <select data-filter-select="memo"><option value="">全部 / All</option><option value="1">只看必背 / Only these</option></select></label>
  <span class="count"><span data-filter-count></span> {T("个概念", "concepts")}</span>
 </div>
 {"".join(groups)}
</div>"""
    write("concepts.html", page("concepts.html", "概念", "Concepts", body,
          "说一切有部阿毗达磨概念表：中、繁、梵、英对照，附《俱舍万字》释义、颂文与《九题》《英译百瑕》去处。",
          "A bilingual glossary of Sarvāstivāda Abhidharma concepts with verses and cross-references."))

# ══════════════════════ NINE QUESTIONS ══════════════════════
def build_jiuti():
    parts = []
    for part in JT.PARTS:
        qs = []
        for n in part["qs"]:
            q = D.JTQ[n]
            secs = "".join(f'<li><a href="{pdf("jt", pg)}" target="_blank" rel="noopener">{esc(t)}</a><span class="pg">p. {pg}</span></li>' for t, pg in q["secs"])
            cs = related_chips(q["concepts"])
            vl = ""
            for vq in q["verse"]:
                v = D.find_verse(vq)
                if v:
                    vl += f'<p class="note">{T("相关颂", "Verse")}：{verse_link(v)}　<span lang="zh-Hant">{esc(v["text"])}</span></p>'
            qs.append(f'''<article class="q" id="q{n}"><div class="qn">{n}<small>{T("《俱舍》的"+s(q["nick"]), q["nick_en"])}</small></div>
<div><h3 lang="zh-Hant">{esc(q["q"])}</h3><p class="qen">{esc(q["q_en"])}</p><p class="en" lang="en">{esc(q["desc_en"])}</p>
<ul class="secs">{secs}</ul>{vl}<div>{cs}</div>
<p class="note"><a href="{pdf("jt", q["page"])}" target="_blank" rel="noopener">{T(f"在 PDF 中从第 {q['page']} 页读起", f"Read from p. {q['page']} in the PDF")}</a></p></div></article>''')
        parts.append(f'''<section class="part"><header><span class="stage">{T(part["stage"][0], part["stage"][1])}</span><p style="margin:0">{T(esc(s(part["zh"])), esc(part["en"]))}</p></header>{"".join(qs)}</section>''')
    test = "".join(f'<li>{T(esc(s(z)), esc(e))}</li>' for z, e in JT.ENTRY_TEST)
    se = JT.SPLIT_EXAMPLE
    body = f"""
<div class="wrap">
 <header class="page-head">
  <h1>{T("《俱舍九题：高阶阿毗达磨串讲》导读", "Guide to The Nine Questions of the Kośa")}</h1>
  <p class="lede">{T("“本书是串讲。虽然只有九题，内容却覆盖了阿毗达磨的方方面面。”九题分三部分，前八题有系统，可以用题目串起来；第九题是较为繁难的细节。点击小节标题直接打开 PDF 对应页。",
       "'Though there are only nine questions, they cover every aspect of Abhidharma.' The first eight form a system; the ninth gathers hard details. Click a section title to open the PDF at that page.")}</p>
  <p><a class="btn" href="{pdf('jt', 1)}" target="_blank" rel="noopener">{T("打开《俱舍九题》PDF", "Open the PDF")}</a></p>
 </header>
 <div class="cols" style="margin-bottom:2.5rem">
  <section id="entry">
   <h2>{T("入门测验", "Entrance test")}</h2>
   <p class="muted">{T("作者在序中给出的两道题：", "Two questions from the preface:")}</p>
   <ol>{test}</ol>
   <p class="note">{T(esc(s(JT.ENTRY_NOTE[0])), esc(JT.ENTRY_NOTE[1]))}</p>
   <p class="note"><a href="concepts.html">{T("在概念页筛选“必背”", "Filter the concepts page by 'entrance test'")}</a>　<a href="genpin-1.html">{T("做二十二根练习", "Try the 22-faculties quiz")}</a></p>
  </section>
  <section>
   <h2>{T("怎样拆分问题", "How to split a question")}</h2>
   <p><b lang="zh-Hant">{esc(se["q"])}</b><br><span class="en" lang="en">{esc(se["q_en"])}</span></p>
   <blockquote class="quote"><span class="zh" lang="zh-Hant">{esc(se["zh"])}</span><span class="en" lang="en">{esc(se["en"])}</span><cite>{T("《俱舍九题》第 17 页", "Nine Questions, p. 17")}</cite></blockquote>
  </section>
 </div>
 {"".join(parts)}
</div>"""
    write("jiuti.html", page("jiuti.html", "九题导读", "Nine Questions", body,
          "《俱舍九题：高阶阿毗达磨串讲》导读：九个问题、学习阶段、各节页码与相关概念。",
          "A guide to Wang Lu's advanced course: the nine questions, stages, sections with page links, related concepts."))

# ══════════════════════ TRANSLATION FLAWS ══════════════════════
def build_translations():
    rows = []
    for b in D.BX:
        refs = "<br>".join(f'<span class="who">{w}</span> {esc(r)}' for w, r in b["refs"])
        c = D.CBYID.get(b["concept"]) if b["concept"] else None
        ch = f'<a href="concepts.html#{c["id"]}">{esc(c["s"])}</a>' if c else ""
        text = " ".join([b["en"], b["zh"], " ".join(r for _, r in b["refs"]), c["s"] if c else "", c["en"] if c else ""])
        rows.append(f'''<tr id="f{b["no"]}" data-filter-item data-text="{esc(text)}" data-pin="{b["pin"]}" data-who="{" ".join(b["who"])}">
<td class="no">{b["no"]}</td><td class="pin">{T(pin_short(b["pin"]), PIN[b["pin"]]["en"].split(":")[0])}</td><td class="ref">{refs}</td>
<td><span class="en" lang="en">{esc(b["en"])}</span><span class="zh zh-gist" lang="zh-Hant">{esc(b["zh"])}</span></td>
<td>{ch}</td><td><a class="pg" href="{pdf("hd", b["page"])}" target="_blank" rel="noopener">p. {b["page"]}</a></td></tr>''')
    pin_opts = "".join(f'<option value="{pid}">{PIN[pid]["s"]} {PIN[pid]["en"].split(":")[0]}</option>' for pid in PIN_IDS if pid != "po")
    body = f"""
<div class="wrap" data-filter-scope>
 <header class="page-head">
  <h1>{T("《俱舍英译百瑕》：英译本一百处错误", "One Hundred Flaws in the English Translations of the Kośa")}</h1>
  <div class="read">
   <p class="lede"><span class="en" lang="en">Wang Lu read the two English translations of the Abhidharmakośabhāṣya against Xuanzang's Chinese and recorded one hundred errors, mostly in chapters 5–8 (the anuśaya, path, knowledge and meditation chapters). Each entry quotes the English, gives Xuanzang's text (and Paramārtha's or the Sanskrit where useful), and explains the doctrinal point. Errors may originate in La Vallée Poussin's French or in the Sanskrit; the book judges only on doctrinal grounds.</span><span class="zh">王路以玄奘译本对读《俱舍》两部英译本，记下一百处错误，主要在后四品（随眠、贤圣、智、定）。每条列出英译与玄奘译文（必要时兼列真谛本或梵本），并从阿毗达磨义理上说明。错误有的来自 LVP 法译或梵本，书中只就义理指误。</span></p>
  </div>
  <dl class="tools" style="margin-top:1.2rem">
   <dt>Pruden</dt><dd lang="en">Leo M. Pruden, trans., <i>Abhidharmakośabhāṣyam of Vasubandhu</i>. Berkeley: Asian Humanities Press, 1988–1990 (from La Vallée Poussin's French).</dd>
   <dt>LS</dt><dd lang="en">Gelong Lodrö Sangpo, trans., <i>Abhidharmakośa-Bhāṣya of Vasubandhu: The Treasury of the Abhidharma and its (Auto)Commentary</i>. Delhi: Motilal Banarsidass, 2012.</dd>
   <dt>{T("英文附录", "In English")}</dt><dd>{T("书末附录 Part I–III（PDF 第 229–260 页）是与丁一合写、发于 H-Buddhism 的英文条目，附梵文、法文平行文本。", "Appendix Parts I–III (PDF pp. 229–260) give about a dozen entries in English, written with Ding Yi and first posted on H-Buddhism, with Sanskrit and French parallels.")} <a href="{pdf('hd', 229)}" target="_blank" rel="noopener">{T("打开附录", "Open the appendix")}</a></dd>
  </dl>
  <p class="note">{T("下表的英文提要由本站编写，中文要旨节录自作者原文；完整论证请点页码打开 PDF。“颂号”沿用英译本的偈颂编号。", "English summaries are this site's condensations; the Chinese is excerpted from the author's text. Click the page number for the full argument. Verse numbers follow the English translations.")}</p>
 </header>
 <div class="ftools">
  <input type="search" data-filter-input placeholder="Search: 2-13c, ājñā, 練根…" aria-label="Search">
  <label>{T("品", "Chapter")} <select data-filter-select="pin"><option value="">全部 / All</option>{pin_opts}</select></label>
  <label>{T("译本", "Translation")} <select data-filter-select="who"><option value="">全部 / Both</option><option value="Pruden">Pruden</option><option value="LS">Lodrö Sangpo</option></select></label>
  <span class="count"><span data-filter-count></span> {T("条", "entries")}</span>
 </div>
 <div class="scroll-x">
 <table class="flaws">
  <thead><tr><th>#</th><th>{T("品", "Ch.")}</th><th>{T("出处", "Where")}</th><th>{T("提要", "Summary")}</th><th>{T("概念", "Concept")}</th><th>PDF</th></tr></thead>
  <tbody>{"".join(rows)}</tbody>
 </table>
 </div>
</div>"""
    write("translations.html", page("translations.html", "英译百瑕", "Translation Flaws", body,
          "《俱舍英译百瑕》一百条索引：颂号、Pruden 与 Lodrö Sangpo 页码、英文提要与中文要旨。",
          "Index of Wang Lu's one hundred flaws in the Pruden and Lodrö Sangpo translations of the Abhidharmakośa, with English summaries."))

# ══════════════════════ EMENDATIONS ══════════════════════
def build_emendations():
    from collections import OrderedDict
    groups = OrderedDict()
    for e in D.LJ:
        key = (e["text"], e["tno"])
        groups.setdefault(key, []).append(e)
    out = []
    for (text, tno), es in groups.items():
        rows = []
        for e in es:
            loc = []
            if e["juan"]: loc.append(f'卷{e["juan"]}')
            if e["loc"]:
                vol, no, pg_ = e["loc"].split(" ")
                loc.append(f"{vol}n{no}, p. {pg_}")
            rows.append(f'<div class="lj" data-filter-item data-text="{esc(text+" "+e["quote"]+" "+" ".join(loc))}"><span class="no">{e["no"]}</span><span class="loc">{esc(" ".join(loc))}</span><span class="snip" lang="zh-Hant">{esc(e["quote"])}</span><a class="pgc" href="{pdf("hd", e["page"])}" target="_blank" rel="noopener">p. {e["page"]}</a></div>')
        label = "百例之余（补例）" if text == "百例之餘" else "《" + text + "》"
        out.append(f'<section class="lj-text" data-filter-group><h3><span lang="zh-Hant">{esc(label)}</span><small>{tno}</small></h3>{"".join(rows)}</section>')
    body = f"""
<div class="wrap" data-filter-scope>
 <header class="page-head">
  <h1>{T("《阿毗达磨理校百例》索引", "One Hundred Doctrinal Emendations: index")}</h1>
  <div class="read">
   <p class="lede">{T("依据阿毗达磨义理，对《大正藏》毘昙部汉译论典（《集异门》T1536 至《显宗》T1563，《发智》居首）进行“理校”：判断异文中何者为是，或指出诸本皆误之处。讨论对象是截至 2024 年 6 月 30 日 CBETA 尚未修订的错误。作者说：“当你懂得一例，就能看懂三例；当你懂得一百例，就几乎可以看懂所有可以运用阿毗达磨来理校的地方。”",
        "Emendation by doctrinal reasoning (理校) of the Chinese Abhidharma treatises in the Taishō (T1536–T1563, with the Jñānaprasthāna first): deciding between variant readings, or showing that all witnesses are wrong. It covers errors not yet corrected in CBETA as of 30 June 2024. 'Understand one example and you can follow three; understand a hundred and you can follow almost every place where Abhidharma can be used to emend a text.'")}</p>
   <p class="note">{T("难度：比《英译百瑕》难一些，比《俱舍九题》简单一些。下表列出每例所在论典、卷次、CBETA 位置和所讨论文本的开头；点页码打开 PDF。", "Difficulty: a little harder than the Translation Flaws, a little easier than the Nine Questions. Each line gives the text, fascicle, CBETA locus and the opening of the passage discussed; click the page number to open the PDF.")}</p>
  </div>
 </header>
 <div class="ftools"><input type="search" data-filter-input placeholder="查找：發智、隨眠、T1542……" aria-label="Search"><span class="count"><span data-filter-count></span> {T("例", "entries")}</span></div>
 {"".join(out)}
</div>"""
    write("emendations.html", page("emendations.html", "理校百例", "Emendations", body,
          "《阿毗达磨理校百例》索引：按论典列出每例的卷次、CBETA 位置与页码。",
          "Index of Wang Lu's one hundred doctrinal emendations of the Taishō Abhidharma texts."))

# ══════════════════════ PRACTICE (keeps the original URL genpin-1.html) ══════════════════════
QUIZ = [
 ("以下哪些根，依次容是色蘊、受蘊、行蘊、識蘊？", ["身根、憂根、命根、意根", "男根、樂根、已知根、意根", "舌根、喜根、信根、具知根", "眼根、苦根、未知當知根、具知根", "耳根、捨根、慧根、已知根"], "abcde"),
 ("以下哪些地，依次有苦根、樂根、憂根、喜根、捨根？", ["欲界、初靜慮、欲界、第二靜慮、第四靜慮", "欲界、第二靜慮、欲界、初靜慮、空無邊處", "初靜慮、初靜慮、欲界、初靜慮、非想非非想處", "欲界、第三靜慮、欲界、第二靜慮、識無邊處", "欲界、欲界、欲界、初靜慮、無所有處"], "ade"),
 ("以下哪些根，依次容是身受、心受？", ["第二靜慮捨根、欲界樂根", "初靜慮喜根、初靜慮樂根", "第三靜慮樂根、初靜慮樂根", "初靜慮未知當知根、欲界捨根", "初靜慮捨根、初靜慮具知根"], "e"),
 ("以下哪些根，依次容有漏、容無漏、必有漏、必無漏？", ["樂根、信根、憂根、未知當知根", "捨根、命根、眼根、已知根", "勤根、定根、命根、具知根", "身根、慧根、信根、已知根", "慧根、樂根、苦根、未知當知根"], "ace"),
 ("以下哪些根，依次容是異熟、容非異熟、必是異熟、必非異熟？", ["眼根、捨根、命根、憂根", "身根、意根、憂根、信根", "意根、樂根、命根、定根", "苦根、憂根、命根、念根", "樂根、苦根、捨根、憂根"], "acd"),
 ("以下哪些根，依次容是異熟、容有異熟、容非異熟、容無異熟？", ["命根、苦根、憂根、捨根", "樂根、信根、未知當知根、具知根", "女根、未知當知根、具知根、已知根", "意根、憂根、命根、捨根", "眼根、苦根、信根、女根"], "abe"),
 ("以下哪些根，依次容是善、容是不善、容是無記、容是三種？", ["捨根、信根、命根、苦根", "苦根、眼根、身根、樂根", "喜根、意根、憂根、捨根", "男根、憂根、舌根、樂根", "苦根、喜根、眼根、樂根"], "e"),
 ("以下哪些根，依次容是欲界繫、必是欲界繫、容非色界繫、必非無色界繫？", ["命根、憂根、眼根、樂根", "已知根、苦根、樂根、身根", "定根、女根、未知當知根、喜根", "身根、喜根、具知根、憂根", "憂根、憂根、苦根、命根"], "ac"),
 ("以下哪些根，依次容是見所斷、容是修所斷、定非見所斷、定非修所斷？", ["樂根、信根、命根、已知根", "喜根、眼根、身根、未知當知根", "捨根、命根、信根、具知根", "意根、已知根、女根、具知根", "苦根、意根、定根、已知根"], "abc"),
 ("以下哪些根，依次容是欲界受生初得異熟、色界受生初得異熟、欲界受生後得異熟、色界受生後得異熟？", ["女根、身根、憂根、喜根", "身根、鼻根、苦根、樂根", "命根、眼根、已知根、捨根", "眼根、耳根、喜根、信根", "意根、命根、捨根、喜根"], "b"),
]
def build_practice():
    qs = []
    for i, (q, opts, ans) in enumerate(QUIZ, 1):
        labels = "".join(f'<label><input type="checkbox" name="q{i}" value="{"abcde"[j]}"><span class="opt">{"ABCDE"[j]}</span><span lang="zh-Hant">{esc(o)}</span></label>' for j, o in enumerate(opts))
        qs.append(f'<div class="qz" id="qz{i}"><fieldset><legend><span lang="zh-Hant">{i}、{esc(q)}</span></legend>{labels}</fieldset><div class="res" aria-live="polite"></div></div>')
    key = {str(i): a for i, (_, _, a) in enumerate(QUIZ, 1)}
    glossary = "".join(f'<tr><td>{zh}</td><td lang="en">{en}</td></tr>' for zh, en in F.ROOTS)
    body = f"""
<div class="wrap">
 <header class="page-head">
  <h1 lang="zh-Hant">分別根品測試一</h1>
  <p class="lede">{T("作者设计的二十二根测验。不定项选择，每题 10 分，共 100 分；少选、多选、错选皆不得分。开卷，答题时间 5 小时。",
       "The author's quiz on the twenty-two faculties. Each question may have several correct options; 10 points each, 100 in total; a question scores only if exactly the right options are chosen. Open-book; five hours.")}</p>
  <p class="note" lang="zh-Hant">註：「容」字的理解：若甲定是乙，則甲容是乙；若甲必非乙，則甲容非乙。</p>
  <p class="note en" lang="en">Note on 容 ('can be'): if A is always B, then A can be B; if A is never B, then A can be non-B.</p>
 </header>
 <details class="ref"><summary>{T("参考表：二十二根诸门分别（开卷）", "Reference table: the 22 faculties (open-book)")}</summary>{F.roots_table()}<p class="note">{T("据《俱舍万字》2.3 与根品颂。更多见", "From Outline 2.3 and the faculties chapter. See also")} <a href="outline.html#s2-3">{T("纲要 2.3", "Outline 2.3")}</a>。</p></details>
 <details class="ref en"><summary lang="en">English names of the 22 faculties</summary><table class="grid">{glossary}</table></details>
 <form id="quiz" class="quiz" data-key='{json.dumps(key)}'>
  {"".join(qs)}
  <div class="score"><button type="submit" class="btn">{T("提交答案", "Submit")}</button><button type="button" class="btn ghost" id="show-key" hidden>{T("显示正确答案", "Show the answers")}</button><button type="button" class="btn ghost" id="reset">{T("重做", "Start over")}</button><span>{T("最终得分", "Score")}：<output id="score">—</output></span></div>
 </form>
</div>"""
    write("genpin-1.html", page("genpin-1.html", "练习：分别根品测试一", "Practice", body,
          "分别根品测试一：二十二根十道不定项选择题，自动评分并可查看答案。",
          "Quiz on the twenty-two faculties with automatic scoring.", scripts=["assets/js/quiz.js"]))
    # index.html used to be the same quiz; keep a copy-free redirect page is unnecessary since index is now home.

# ══════════════════════ RESOURCES ══════════════════════
ABBR = [("阿毘達磨發智論", "T1544", "發智", "Jñānaprasthāna"), ("阿毘達磨大毘婆沙論", "T1545", "婆沙", "Mahāvibhāṣā"),
        ("阿毘曇毘婆沙論", "T1546", "涼譯《婆沙》", "Vibhāṣā (Liang tr.)"), ("阿毘達磨俱舍論", "T1558", "俱舍", "Abhidharmakośabhāṣya (Xuanzang)"),
        ("阿毘達磨俱舍釋論", "T1559", "真諦譯《俱舍》", "Abhidharmakośabhāṣya (Paramārtha)"), ("阿毘達磨順正理論", "T1562", "正理", "Nyāyānusāra"),
        ("阿毘達磨藏顯宗論", "T1563", "顯宗", "Abhidharmasamayapradīpikā"), ("俱舍論記", "T1821", "光記", "Puguang's commentary"),
        ("俱舍論疏", "T1822", "寶疏", "Fabao's commentary"), ("俱舍論頌疏", "T1823", "頌疏", "Yuanhui's verse commentary"),
        ("阿毘達磨集異門足論", "T1536", "集異門", "Saṃgītiparyāya"), ("阿毘達磨識身足論", "T1539", "識身", "Vijñānakāya"),
        ("阿毘達磨品類足論", "T1542", "品類", "Prakaraṇapāda"), ("阿毘達磨俱舍論法義", "T2251", "法義", "Kaidō Rinjō, Kusharon hōgi")]
def build_resources():
    rows = "".join(f'<tr><td lang="zh-Hant">《{a}》</td><td>{b}</td><td lang="zh-Hant">《{c}》</td><td lang="en"><i>{d}</i></td></tr>' if not c.startswith(("涼", "真")) else f'<tr><td lang="zh-Hant">《{a}》</td><td>{b}</td><td lang="zh-Hant">{c}</td><td lang="en"><i>{d}</i></td></tr>' for a, b, c, d in ABBR)
    body = f"""
<div class="wrap">
 <header class="page-head"><h1>{T("资源", "Resources")}</h1></header>
 <section class="block" id="books">
  <h2>{T("著作下载", "The books (PDF)")}</h2>
  <dl class="tools">
   <dt><a href="{BOOK_JT}">{T("《俱舍九题》", "Nine Questions")}</a></dt><dd>{T("《俱舍九题：高阶阿毗达磨串讲》电子书，220 页。2024 年 6 月台湾华夏出版。", "The Nine Questions of the Kośa: An Advanced Course in Abhidharma. E-book, 220 pp. Taiwan, June 2024.")}</dd>
   <dt><a href="{BOOK_HD}">{T("合订稿", "Combined volume")}</a></dt><dd>{T("《俱舍万字》《俱舍英译百瑕》《阿毗达磨理校百例》合订稿（2025-04-01），466 页。", "Ten Thousand Characters, One Hundred Flaws, One Hundred Emendations (2025-04-01), 466 pp.")}</dd>
  </dl>
  <p class="note">{T("作者 2025 年说明：", "The author, 2025: ")}<span class="zh">“我打算把三稿合成一个 PDF 放在网上，便于读者自行取阅。”</span><span class="en" lang="en">'I plan to combine the three manuscripts into one PDF online, for readers to take freely.'</span></p>
 </section>
 <section class="block" id="abbr">
  <h2>{T("典籍简称", "Abbreviations")}</h2>
  <p class="muted read">{T("《俱舍九题》所用简称。引文皆可在 CBETA 直接检索，故书中往往不标册卷页栏行。“原文”指玄奘所译。", "Abbreviations used in the Nine Questions. All quotations can be found by searching CBETA, so locations are often omitted. 'The original' means Xuanzang's translation.")}</p>
  <div class="scroll-x"><table class="abbr"><thead><tr><th>{T("全名", "Title")}</th><th>{T("编号", "No.")}</th><th>{T("简称", "Short")}</th><th>{T("通行梵名或说明", "Usual name")}</th></tr></thead><tbody>{rows}</tbody></table></div>
 </section>
 <section class="block" id="tools">
  <h2>{T("在线工具", "Online tools")}</h2>
  <dl class="tools">
   <dt><a href="https://cbetaonline.dila.edu.tw/">CBETA Online</a></dt><dd>{T("中华电子佛典。毘昙部原文检索，作者引文均出于此。", "The Chinese Buddhist canon online; search the Abhidharma texts here.")}</dd>
   <dt><a href="https://21dzk.l.u-tokyo.ac.jp/SAT/">SAT</a></dt><dd>{T("大正藏数据库，可检索快道林常《俱舍论法义》等。", "The Taishō database; needed for Kaidō's Hōgi.")}</dd>
   <dt><a href="http://www.buddhism-dict.net/ddb/">DDB</a></dt><dd>{T("Digital Dictionary of Buddhism。作者曾就阿毗达磨词条向主编穆勒教授反馈，多数获采纳。", "Digital Dictionary of Buddhism; the author's corrections to Abhidharma entries were mostly adopted by its editor, Charles Muller.")}</dd>
   <dt><a href="https://gretil.sub.uni-goettingen.de/">GRETIL</a></dt><dd>{T("梵文电子文本库。《英译百瑕》摘录了其中部分梵本，作者提醒录文间有错误。", "Sanskrit e-texts; the Flaws quotes some of them, with the author's caution that the transcriptions contain errors.")}</dd>
  </dl>
 </section>
 <section class="block" id="site">
  <h2>{T("关于本站", "About this site")}</h2>
  <div class="read">
   <p>{T("中文内容取自作者著作；英文译文、提要和图表由本站整理，供阅读参考，如有出入以作者原文和玄奘译语为准。全站可离线使用：", "Chinese content comes from the author's books; the English renderings, summaries and figures were prepared for this site as reading aids, and the author's text and Xuanzang's terms prevail. The whole site works offline:")} <a href="download/abhidharma-site.zip">{T("下载离线版", "download the offline version")}</a>。</p>
  </div>
 </section>
</div>"""
    write("resources.html", page("resources.html", "资源", "Resources", body,
          "著作 PDF 下载、典籍简称表与在线检索工具。", "PDF downloads, abbreviations and online tools."))

if __name__ == "__main__":
    build_home(); build_map(); build_outline(); build_verses(); build_concepts()
    build_jiuti(); build_translations(); build_emendations(); build_practice(); build_resources()
    print("built")
