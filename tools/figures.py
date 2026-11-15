"""Diagrams and reference tables (SVG / HTML strings)."""
from common import T, esc, s as _s

def _t(x, y, zh, en, size=14, anchor="middle", fill="currentColor", weight=400, cls=""):
    a = f'x="{x}" y="{y}" text-anchor="{anchor}" fill="{fill}"'
    zh = _s(zh)
    return (f'<text class="zh {cls}" {a} font-size="{size}" font-weight="{weight}">{zh}</text>'
            f'<text class="en en-t {cls}" {a} font-size="{size*0.86:.1f}" font-weight="{weight}">{en}</text>')

# ───────────── 1. Nine chapters (光記 framing) — on indigo ─────────────
def structure_svg(PIN):
    groups = [
        ("總明有漏無漏", "General: with-outflow and outflow-free", ["jie", "gen"]),
        ("別明有漏", "Particular: the with-outflow", ["shi", "ye", "sui"]),
        ("別明無漏", "Particular: the outflow-free", ["xian", "zhi", "ding"]),
        ("釋無我理", "The principle of non-self", ["po"]),
    ]
    role = {"jie": ("諸法體", "substance"), "gen": ("諸法用", "function"), "shi": ("果", "fruit"), "ye": ("因", "cause"),
            "sui": ("緣", "condition"), "xian": ("果", "fruit"), "zhi": ("因", "cause"), "ding": ("緣", "condition"), "po": ("無我", "non-self")}
    order = {"ding": 1, "xian": 2, "sui": 2, "jie": 3, "gen": 3, "ye": 4, "shi": 5, "zhi": 5}
    short_en = {"jie": "Dhātu", "gen": "Indriya", "shi": "Loka", "ye": "Karma", "sui": "Anuśaya", "xian": "Mārga-pudgala", "zhi": "Jñāna", "ding": "Samāpatti", "po": "Pudgala-viniścaya"}
    W, bw, gap, ggap, x = 1000, 96, 8, 28, 6
    out = [f'<svg class="struct" viewBox="0 0 {W} 330" role="img" aria-labelledby="st-t"><title id="st-t">《俱舍》九品结构（据普光《俱舍论记》卷1）</title>']
    pos = {}
    for gzh, gen, ids in groups:
        gx0 = x
        for pid in ids:
            pos[pid] = x
            x += bw + gap
        x -= gap
        gx1 = x
        cx = (gx0 + gx1) / 2
        out.append(_t(cx, 24, gzh, gen, 15, fill="#F2E9CF", weight=600))
        out.append(f'<path d="M{gx0} 42 V36 H{gx1} V42" fill="none" stroke="#C9A961" stroke-width="1"/>')
        x += ggap
    for pid, px in pos.items():
        p = PIN[pid]
        out.append(f'<a href="#col-{pid}" aria-label="{esc(p["s"])}">' if pid != "po" else '<g>')
        fill = "rgba(255,255,255,.04)" if pid != "po" else "rgba(255,255,255,.015)"
        out.append(f'<rect x="{px}" y="52" width="{bw}" height="196" rx="2" fill="{fill}" stroke="#C9A961" stroke-opacity=".55"/>')
        name = p["s"].replace("分别", "")
        out.append(f'<text x="{px+bw/2}" y="82" text-anchor="middle" fill="#F2E9CF" font-size="17" font-weight="600" lang="zh-Hans">{esc(name)}</text>')
        rz, re_ = role[pid]
        big = 34 if len(rz) == 1 else 21
        out.append(_t(px + bw / 2, 140, rz, re_, big, fill="#C9A961", weight=600))
        out.append(_t(px + bw / 2, 182, f'卷{p["juan"]}', f'fasc. {p["juan"]}', 12.5, fill="#E4D3A2"))
        if p["verses"]:
            out.append(_t(px + bw / 2, 202, f'{p["verses"]}頌', f'{p["verses"]} verses', 12.5, fill="#E4D3A2"))
        else:
            out.append(_t(px + bw / 2, 202, '長行', 'prose', 12.5, fill="#E4D3A2"))
        out.append(f'<text x="{px+bw/2}" y="232" text-anchor="middle" fill="#E4D3A2" font-size="11.5" font-style="italic" class="en-t" style="font-family:var(--serif-en)">{short_en[pid]}</text>')
        if pid in order:
            out.append(f'<circle cx="{px+bw-12}" cy="64" r="9" fill="#B3392B"/><text x="{px+bw-12}" y="68.5" text-anchor="middle" fill="#fff" font-size="12" font-weight="600" style="font-family:var(--serif-en)">{order[pid]}</text>')
        out.append('</a>' if pid != "po" else '</g>')
    # the three inseparable chapters
    xs = [pos["sui"] + bw / 2, pos["xian"] + bw / 2, pos["ding"] + bw / 2]
    out.append(f'<path d="M{xs[0]} 252 V268 H{xs[2]} V252 M{xs[1]} 252 V268" fill="none" stroke="#C9A961" stroke-width="1.2"/>')
    mid = (xs[0] + xs[2]) / 2
    out.append(_t(mid, 290, "隨眠・賢聖・定：三品分不開；只學三品，必是此三品", "Anuśaya, Path, Meditation: inseparable — if only three chapters, these three", 13.5, fill="#F2E9CF"))
    out.append(_t(6, 322, "紅圈數字：作者建議的通讀次序。框：點擊跳到該品概念。", "Red numbers: the author's suggested reading order. Click a chapter to jump to its concepts.", 12, anchor="start", fill="#E4D3A2"))
    out.append('</svg>')
    return "".join(out)

# ───────────── 2. Three realms and nine stages ─────────────
def realms_svg():
    rows = [  # (label zh, label en, kind, height, places, stage-no)
        ("非想非非想處（有頂）", "Neither-ideation-nor-non-ideation (summit)", "main", 30, "", 9),
        ("近分", "preparatory", "near", 14, "", None),
        ("無所有處", "Nothingness", "main", 30, "", 8),
        ("近分", "preparatory", "near", 14, "", None),
        ("識無邊處", "Infinite consciousness", "main", 30, "", 7),
        ("近分", "preparatory", "near", 14, "", None),
        ("空無邊處", "Infinite space", "main", 30, "", 6),
        ("近分", "preparatory", "near", 14, "", None),
        ("第四靜慮", "Fourth dhyāna", "main", 34, "八處", 5),
        ("近分", "preparatory", "near", 14, "", None),
        ("第三靜慮", "Third dhyāna", "main", 34, "三處", 4),
        ("近分", "preparatory", "near", 14, "", None),
        ("第二靜慮", "Second dhyāna", "main", 34, "三處", 3),
        ("近分", "preparatory", "near", 14, "", None),
        ("靜慮中間", "Intermediate dhyāna", "mid", 18, "", None),
        ("初靜慮", "First dhyāna", "main", 34, "三處", 2),
        ("未至定（初靜慮近分）", "Not-yet-arrived (preparatory)", "near", 18, "", None),
        ("欲界", "Sensuous realm", "kama", 54, "二十處", 1),
    ]
    W, x0, bw = 780, 150, 360
    y = 14
    out = [f'<svg viewBox="0 0 {W} 560" role="img" aria-labelledby="rl-t"><title id="rl-t">三界九地与三地</title>']
    ys = {}
    for i, (zh, en, kind, h, places, no) in enumerate(rows):
        fill = {"main": "#F1F1EC", "near": "#FFFFFF", "mid": "#F4E2DE", "kama": "#E7E8E2"}[kind]
        out.append(f'<rect x="{x0}" y="{y}" width="{bw}" height="{h}" fill="{fill}" stroke="#D9DBE1"/>')
        fs = 13.5 if kind in ("main", "kama") else 11
        col = "#23283A" if kind != "near" else "#7A8091"
        out.append(_t(x0 + 12, y + h / 2 + fs * 0.36, zh, en, fs, anchor="start", fill=col, weight=600 if kind in ("main", "kama") else 400))
        if places:
            out.append(_t(x0 + bw - 10, y + h / 2 + 4.5, places, places.replace("八處", "8 places").replace("三處", "3 places").replace("二十處", "20 places"), 12, anchor="end", fill="#565C6E"))
        if no:
            out.append(f'<text x="{x0-14}" y="{y+h/2+5}" text-anchor="end" font-size="13" fill="#B3392B" font-weight="600" style="font-family:var(--serif-en)">{no}</text>')
        ys[i] = (y, y + h)
        y += h
    total_h = y
    # realm brackets (left)
    def lb(i0, i1, zh, en):
        a, b = ys[i0][0], ys[i1][1]
        out.append(f'<path d="M{x0-34} {a+2} H{x0-40} V{b-2} H{x0-34}" fill="none" stroke="#23283A"/>')
        out.append(_t(x0 - 48, (a + b) / 2 + 5, zh, en, 14, anchor="end", weight=600))
    lb(0, 7, "無色界", "Immaterial")
    lb(8, 16, "色界", "Fine-material")
    lb(17, 17, "欲界", "Sensuous")
    # three stages (right)
    def rb(i0, i1, zh, en):
        a, b = ys[i0][0], ys[i1][1]
        xr = x0 + bw + 16
        out.append(f'<path d="M{xr} {a+2} H{xr+6} V{b-2} H{xr}" fill="none" stroke="#B3392B"/>')
        out.append(_t(xr + 14, (a + b) / 2 + 5, zh, en, 13, anchor="start", fill="#B3392B"))
    rb(0, 13, "無尋無伺地（第二靜慮以上及諸近分）", "Without vitarka or vicāra", )
    rb(14, 14, "無尋唯伺地", "Vicāra only")
    rb(15, 17, "有尋有伺地", "With vitarka and vicāra")
    out.append(_t(x0 - 14, total_h + 22, "紅色數字：九地。白色窄條：近分。", "Red numbers: the nine stages. Narrow white bands: preparatory stages.", 12, anchor="start", fill="#565C6E"))
    out.append('</svg>')
    return "".join(out).replace('viewBox="0 0 780 560"', f'viewBox="0 0 780 {total_h+36}"')

# ───────────── 3. Six causes, four conditions, five fruits ─────────────
def causes_svg():
    causes = [("能作因", "efficient"), ("俱有因", "co-existent"), ("相應因", "associated"), ("同類因", "homogeneous"), ("遍行因", "universal"), ("異熟因", "retribution")]
    fruits = [("增上果", "dominant"), ("士用果", "virile"), ("等流果", "uniform"), ("異熟果", "retribution"), ("離繫果", "disconnection")]
    links = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: 3}
    W = 780
    cy = lambda i: 46 + i * 44
    fy = {0: cy(0), 1: (cy(1) + cy(2)) / 2, 2: (cy(3) + cy(4)) / 2, 3: cy(5), 4: cy(6) + 8}
    out = [f'<svg viewBox="0 0 {W} 392" role="img" aria-labelledby="cf-t"><title id="cf-t">六因、四缘与五果</title>']
    out.append(_t(330, 20, "六因", "Six causes", 14, weight=600))
    out.append(_t(640, 20, "五果", "Five fruits", 14, weight=600))
    out.append(_t(110, 20, "四緣", "Four conditions", 14, weight=600))
    for i, (zh, en) in enumerate(causes):
        y = cy(i)
        out.append(f'<rect x="270" y="{y-15}" width="120" height="30" rx="2" fill="#F1F1EC" stroke="#D9DBE1"/>')
        out.append(_t(330, y + 5, zh, en, 14))
    for j, (zh, en) in enumerate(fruits):
        y = fy[j]
        out.append(f'<rect x="580" y="{y-15}" width="120" height="30" rx="2" fill="{"#F2E9CF" if j < 4 else "#FFFFFF"}" stroke="{"#C9A961" if j < 4 else "#B3392B"}"/>')
        out.append(_t(640, y + 5, zh, en, 14))
    for i, j in links.items():
        out.append(f'<path d="M390 {cy(i)} C 480 {cy(i)}, 490 {fy[j]}, 580 {fy[j]}" fill="none" stroke="#23283A" stroke-width="1.1"/>')
    out.append(_t(640, fy[4] + 34, "擇滅；無因（離繫由慧盡）", "cessation; has no cause", 12, fill="#B3392B"))
    # conditions as brackets on the left
    out.append(f'<path d="M262 {cy(1)-14} H254 V{cy(5)+14} H262" fill="none" stroke="#B3392B"/>')
    out.append(_t(246, (cy(1) + cy(5)) / 2 - 4, "因緣", "causal condition", 14, anchor="end", fill="#B3392B", weight=600))
    out.append(_t(246, (cy(1) + cy(5)) / 2 + 16, "＝五因", "= five causes", 12, anchor="end", fill="#565C6E"))
    out.append(f'<path d="M262 {cy(0)-14} H254 V{cy(0)+14} H262" fill="none" stroke="#B3392B"/>')
    out.append(_t(246, cy(0) + 5, "增上緣＝能作因", "dominant = efficient cause", 13, anchor="end", fill="#B3392B"))
    out.append(_t(20, cy(6) + 66, "所緣緣：一切法。等無間緣：除阿羅漢最後心心所，餘已生心心所。", "Object condition: all dharmas. Immediately contiguous: arisen minds and mental factors, except an arhat's last.", 12.5, anchor="start", fill="#565C6E"))
    out.append('</svg>')
    return "".join(out)

# ───────────── 4. Twelve links ─────────────
def links_svg():
    L = [("無明", "ignorance", "惑", 0), ("行", "formations", "業", 0), ("識", "consciousness", "事", 1), ("名色", "name-form", "事", 1),
         ("六處", "six bases", "事", 1), ("觸", "contact", "事", 1), ("受", "feeling", "事", 1), ("愛", "craving", "惑", 1),
         ("取", "grasping", "惑", 1), ("有", "existence", "業", 1), ("生", "birth", "事", 2), ("老死", "aging-death", "事", 2)]
    col = {"惑": ("#F4E2DE", "#B3392B"), "業": ("#F2E9CF", "#8A6A22"), "事": ("#F1F1EC", "#565C6E")}
    W, bw, g = 780, 52, 7
    xs = []; x = 10
    for i, it in enumerate(L):
        if i in (2, 10): x += 18
        xs.append(x); x += bw + g
    out = [f'<svg viewBox="0 0 {W} 190" role="img" aria-labelledby="lk-t"><title id="lk-t">缘起十二支与三际</title>']
    for (zh, en, kind, per), px in zip(L, xs):
        f, s_ = col[kind]
        out.append(f'<rect x="{px}" y="52" width="{bw}" height="56" rx="2" fill="{f}" stroke="{s_}" stroke-opacity=".6"/>')
        out.append(f'<text x="{px+bw/2}" y="84" text-anchor="middle" font-size="15" font-weight="600" fill="#23283A" lang="zh-Hans">{_s(zh)}</text>')
        out.append(f'<text class="en en-t" x="{px+bw/2}" y="100" text-anchor="middle" font-size="9.5" fill="#565C6E" style="font-family:var(--serif-en)">{en}</text>')
        out.append(f'<text x="{px+bw/2}" y="126" text-anchor="middle" font-size="12" fill="{s_}">{_s(kind)}</text>')
    def br(i0, i1, zh, en):
        a, b = xs[i0], xs[i1] + bw
        out.append(f'<path d="M{a} 44 V38 H{b} V44" fill="none" stroke="#23283A"/>')
        out.append(_t((a + b) / 2, 28, zh, en, 13.5, weight=600))
    br(0, 1, "前際二", "prior period")
    br(2, 9, "中際八", "middle period")
    br(10, 11, "後際二", "later period")
    out.append(_t(10, 158, "惑：無明、愛、取（三煩惱）　業：行、有（二業）　事：識至受、生、老死（七事，亦名果）", "Defilement: ignorance, craving, grasping. Action: formations, existence. Things (fruits): consciousness…feeling, birth, aging-death.", 12.5, anchor="start", fill="#565C6E"))
    out.append('</svg>')
    return "".join(out)

# ───────────── 5. 75 dharmas ─────────────
def dharmas_html():
    groups = [
        ("色法", "Matter", 11, [("", "眼、耳、鼻、舌、身；色、声、香、味、触；无表色")]),
        ("心法", "Mind", 1, [("", "识蕴（六识算一法）")]),
        ("心所法", "Mental factors", 46, [
            ("大地法 10", "受、想、思、触、欲、慧、念、作意、胜解、三摩地"),
            ("大善地法 10", "信、不放逸、轻安、行舍、惭、愧、无贪、无瞋、不害、勤"),
            ("大烦恼地法 6", "痴、放逸、懈怠、不信、昏沉、掉举"),
            ("大不善地法 2", "无惭、无愧"),
            ("小烦恼地法 10", "忿、覆、悭、嫉、恼、害、恨、谄、诳、憍"),
            ("不定地法 8", "贪、瞋、慢、疑、恶作、睡眠、寻、伺")]),
        ("心不相应行法", "Dissociated conditionings", 14, [("", "得、非得、同分、无想天、无想定、灭尽定、命根、生、住、异、灭、名身、句身、文身")]),
        ("无为法", "Unconditioned", 3, [("", "择灭、非择灭、虚空")]),
    ]
    h = ['<div class="dharmas">']
    for zh, en, n, subs in groups:
        h.append(f'<div><h5>{T(zh, en)} <b>{n}</b></h5>')
        for sh, items in subs:
            h.append(f'<p class="sub">{"<b>"+sh+"</b>：" if sh else ""}{items}</p>')
        h.append('</div>')
    h.append('</div>')
    return "".join(h)

# ───────────── 6. 98 anuśayas ─────────────
TEN = ["贪", "瞋", "慢", "无明", "身见", "边见", "邪见", "见取", "戒禁取", "疑"]
def anusaya_table():
    cls = [("见苦所断", "by seeing suffering", set(TEN)),
           ("见集所断", "by seeing origin", set(TEN) - {"身见", "边见", "戒禁取"}),
           ("见灭所断", "by seeing cessation", set(TEN) - {"身见", "边见", "戒禁取"}),
           ("见道所断", "by seeing the path", set(TEN) - {"身见", "边见"}),
           ("修所断", "by cultivation", {"贪", "瞋", "慢", "无明"})]
    realms = [("欲界", "Sensuous", False), ("色界", "Fine-material", True), ("无色界", "Immaterial", True)]
    h = ['<div class="scroll-x"><table class="grid"><thead><tr><th></th>']
    for zh, en, _ in cls:
        h.append(f'<th>{T(zh, en)}</th>')
    h.append(f'<th>{T("合计", "Total")}</th></tr></thead><tbody>')
    grand = 0
    for rz, ren, no_hate in realms:
        h.append(f'<tr><th>{T(rz, ren)}</th>')
        tot = 0
        for zh, en, items in cls:
            its = [x for x in TEN if x in items and not (no_hate and x == "瞋")]
            tot += len(its)
            h.append(f'<td><b>{len(its)}</b>　{"、".join(its)}</td>')
        grand += tot
        h.append(f'<td class="c tot">{tot}</td></tr>')
    h.append(f'<tr><th colspan="6" style="text-align:right">{T("九十八随眠", "Ninety-eight anuśayas")}</th><td class="c tot">{grand}</td></tr>')
    h.append('</tbody></table></div>')
    assert grand == 98
    return "".join(h)

# ───────────── 7. 22 faculties ─────────────
ROOTS = [("眼根", "eye"), ("耳根", "ear"), ("鼻根", "nose"), ("舌根", "tongue"), ("身根", "body"), ("女根", "female"), ("男根", "male"),
         ("命根", "vital"), ("意根", "mind"), ("苦根", "pain"), ("乐根", "pleasure"), ("忧根", "displeasure"), ("喜根", "joy"), ("舍根", "equanimity"),
         ("信根", "faith"), ("勤根", "vigour"), ("念根", "mindfulness"), ("定根", "concentration"), ("慧根", "understanding"),
         ("未知当知根", "anājñātam…"), ("已知根", "ājñā"), ("具知根", "ājñātāvin")]
def roots_table():
    def kind(i):
        if i < 7: return "rupa"
        return {7: "ming", 8: "yi", 9: "ku", 10: "le", 11: "you", 12: "xi", 13: "she"}.get(i, "xin" if i < 19 else "wl")
    def row(k):
        lou = {"rupa": "唯有漏", "ming": "唯有漏", "ku": "唯有漏", "you": "唯有漏", "wl": "唯无漏"}.get(k, "通二")
        yi = {"ming": "唯是", "you": "非", "xin": "非", "wl": "非"}.get(k, "通二")
        you = {"rupa": "无", "ming": "无", "wl": "无", "you": "定有"}.get(k, "通二")
        xing = {"rupa": "唯无记", "ming": "唯无记", "you": "善、不善", "xin": "唯善", "wl": "唯善"}.get(k, "通三性")
        jie = {"rupa": None, "ming": "欲・色・无色", "yi": "欲・色・无色", "ku": "欲", "le": "欲・色", "you": "欲", "xi": "欲・色", "she": "欲・色・无色", "xin": "欲・色・无色", "wl": "不系"}[k] if k != "rupa" else None
        duan = {"rupa": "唯修", "ming": "唯修", "ku": "唯修", "you": "见・修", "xin": "修・非", "wl": "非所断"}.get(k, "见・修・非")
        return lou, yi, you, xing, jie, duan
    cols = [("有漏无漏", "Outflow"), ("异熟", "Retribution"), ("有异熟", "Has retribution"), ("三性", "Nature"), ("三界系", "Realm"), ("所断", "Abandoned by")]
    h = ['<div class="scroll-x"><table class="grid"><thead><tr><th></th>']
    for zh, en in cols:
        h.append(f'<th>{T(zh, en)}</th>')
    h.append('</tr></thead><tbody>')
    for i, (zh, en) in enumerate(ROOTS):
        k = kind(i)
        lou, yi, you, xing, jie, duan = row(k)
        if k == "rupa":
            jie = "欲" if zh in ("女根", "男根") else "欲・色"
        cells = [lou, yi, you, xing, jie, duan]
        tds = "".join(f'<td class="{"v-two" if ("通" in c or "・" in c) else ("v-none" if c in ("非", "无", "不系", "非所断") else "v-only")}">{c}</td>' for c in cells)
        h.append(f'<tr><th>{zh} <span class="en" lang="en">{en}</span></th>{tds}</tr>')
    h.append('</tbody></table></div>')
    h.append(f'<p class="note" style="margin:.6rem 0 0">{T("意根、乐根、喜根、舍根与信等五根通无漏，其无漏者不系三界。蓝色表示“通”，灰色表示“非”“无”。", "The mind, pleasure, joy and equanimity faculties and the five beginning with faith can be outflow-free; their outflow-free instances belong to no realm. Blue marks ‘may be either’, grey ‘not / none’.")}</p>')
    return "".join(h)

# ───────────── 8. Candidates and fruits track ─────────────
def track_html():
    cols = [str(i) for i in range(10)] + ["上界", "有顶九品尽"]
    cols_en = [str(i) for i in range(10)] + ["higher realms", "summit's 9th cut"]
    h = ['<div class="scroll-x"><div class="track" style="grid-template-columns:8rem repeat(11,minmax(2.6rem,1fr)) minmax(5.5rem,1.4fr)">']
    h.append(f'<div class="hd rh">{T("已断欲界修惑品数", "Grades cut")}</div>')
    for z, e in zip(cols, cols_en):
        h.append(f'<div class="hd">{z if z.isdigit() else T(z, e)}</div>')
    def cell(span, zh, en, cls="span"):
        return f'<div class="{cls}" style="grid-column:span {span}">{T(zh, en)}</div>'
    def blank(span):
        return f'<div style="grid-column:span {span}"></div>'
    h.append(f'<div class="rh">{T("见道（前十五心）", "Path of seeing")}</div>')
    h.append(cell(6, "预流向", "candidate, stream-entry", "cand") + cell(3, "一来向", "candidate, once-return", "cand") + cell(2, "不还向", "candidate, non-return", "cand") + blank(1))
    h.append(f'<div class="rh">{T("修道：住果", "Cultivation: in fruit")}</div>')
    h.append(cell(6, "预流果", "stream-entry", "fruit") + cell(3, "一来果", "once-return", "fruit") + cell(2, "不还果", "non-return", "fruit") + blank(1))
    h.append(f'<div class="rh">{T("修道：起胜果道", "Cultivation: superior path")}</div>')
    h.append(cell(6, "一来向", "candidate, once-return", "cand") + cell(3, "不还向", "candidate, non-return", "cand") + cell(2, "阿罗汉向", "candidate, arhatship", "cand") + blank(1))
    h.append(f'<div class="rh">{T("异名", "Also called")}</div>')
    h.append(blank(3) + cell(2, "家家", "kulaṃkula") + blank(2) + cell(2, "一间", "ekavīcika") + blank(3))
    h.append(f'<div class="rh">{T("无学道", "Beyond training")}</div>')
    h.append(blank(11) + cell(1, "阿罗汉果", "arhatship", "fruit"))
    h.append('</div></div>')
    return "".join(h)

def path_chain():
    steps = [("顺解脱分", "Aids to liberation", "闻、思所成"), ("顺决择分", "Aids to penetration", "煖、顶、忍、世第一法"),
             ("见道", "Path of seeing", "现观前十五心"), ("修道", "Path of cultivation", "第十六心道类智起"), ("无学道", "Beyond training", "尽智、无生智")]
    h = ['<ol class="chain" style="list-style:none;padding:0;margin:0 0 1rem;display:flex;flex-wrap:wrap;gap:.4rem">']
    for i, (zh, en, sub) in enumerate(steps):
        arrow = '<span aria-hidden="true" style="color:#B3392B;margin:0 .2rem">→</span>' if i else ''
        h.append(f'<li style="display:flex;align-items:center">{arrow}<span style="border:1px solid var(--rule);background:var(--paper);padding:.3rem .6rem;border-radius:3px"><b>{T(zh, en)}</b><br><small class="muted">{sub}</small></span></li>')
    h.append('</ol>')
    return "".join(h)
