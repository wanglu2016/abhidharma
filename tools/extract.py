"""Regenerate src/*.json from the author's PDFs and the CBETA XML.
Usage: python3 tools/extract.py PATH/TO/T29n1560.xml
Needs: pip install pymupdf lxml
Outputs: src/wanzi.json, src/baixia.json, src/lijiao.json, src/song.json
"""
import json, os, re, sys
import pymupdf
from lxml import etree

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
HD = os.path.join(ROOT, "books", "《俱舍萬字》《俱舍英譯百瑕》《阿毘達磨理校百例》250401.pdf")

def pages(path):
    d = pymupdf.open(path)
    return {i + 1: p.get_text() for i, p in enumerate(d)}

def dump(name, obj):
    with open(os.path.join(SRC, name), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)

P = pages(HD)

# ---- 《俱舍萬字》 pp. 10–37: paragraphs end with a trailing space in the PDF text layer ----
raw = "".join(P[n] for n in range(10, 38))
s = raw[raw.find("《俱舍万字》 \n我已经"):raw.find("《俱舍英譯百瑕》 \n序")]
paras, buf = [], ""
for l in s.split("\n"):
    if not l.strip():
        if buf: paras.append(buf.strip()); buf = ""
        continue
    buf += l.rstrip() if l.endswith(" ") else l
    if l.endswith(" "):
        paras.append(buf.strip()); buf = ""
if buf: paras.append(buf.strip())
merged, i = [], 0
while i < len(paras):
    if re.fullmatch(r"\d+\.", paras[i]) and i + 1 < len(paras):
        merged.append(paras[i] + " " + paras[i + 1]); i += 2
    else:
        merged.append(paras[i]); i += 1
doc = {"preface": [], "notes": [], "chapters": []}
mode, ch, sec = "pre", None, None
for p in merged[1:]:
    if p == "说明": mode = "notes"; continue
    m = re.match(r"^第(\d) 章$", p)
    if m:
        ch = {"no": int(m.group(1)), "sections": []}; doc["chapters"].append(ch); mode = "body"; continue
    m = re.match(r"^\d+\. (\d\.\d) (.+)$", p)
    if m:
        sec = {"id": m.group(1), "title": m.group(2), "paras": []}; ch["sections"].append(sec); continue
    {"pre": doc["preface"], "notes": doc["notes"]}.get(mode, sec["paras"] if sec else []).append(p)
dump("wanzi.json", doc)

# ---- 《俱舍英譯百瑕》 pp. 44–229 ----
PINS = ["分別界品第一", "分別根品第二", "分別世間品第三", "分別業品第四", "分別隨眠品第五", "分別賢聖品第六", "分別智品第七", "分別定品第八"]
entries, cur, pin = [], None, None
for n in range(44, 230):
    for line in P[n].split("\n"):
        t = line.strip()
        if t in PINS: pin = t; continue
        if t == "附錄": break
        m = re.match(r"^(\d{1,3})\.\s*$", t)
        if m and (cur is None or int(m.group(1)) == cur["no"] + 1):
            cur = {"no": int(m.group(1)), "page": n, "pin": pin, "lines": []}; entries.append(cur); continue
        if cur: cur["lines"].append(t)
out = []
for e in entries:
    txt = "\n".join(e["lines"])
    refs = re.findall(r"(Pruden|Lodrö Sangpo|LS)\s*[（(]([^)）]*)[)）]", txt)
    out.append({"no": e["no"], "page": e["page"], "pin": e["pin"], "refs": refs, "raw": txt})
dump("baixia.json", out)

# ---- 《阿毘達磨理校百例》 pp. 265–466 ----
entries, cur, sec = [], None, None
secre = re.compile(r"^《[^》]+》（T\d{4}）(略)?$")
for n in range(265, 467):
    for line in P[n].split("\n"):
        t = line.strip()
        if secre.match(t) or t == "百例之餘": sec = t; continue
        m = re.match(r"^(\d{1,3})\.\s*$", t)
        if m and ((cur is None and int(m.group(1)) == 1) or (cur and int(m.group(1)) == cur["no"] + 1)):
            cur = {"no": int(m.group(1)), "page": n, "sec": sec, "lines": []}; entries.append(cur); continue
        if cur: cur["lines"].append(t)
out = []
for e in entries:
    txt = "".join(e["lines"])
    m = re.search(r"《([^》]+)》卷(\d+)", txt)
    loc = re.search(r"\(CBETA [^,]+, (T\d+), no\. ?(\d+), pp?\. ?([0-9a-c\-]+)\)", txt)
    q = re.search(r"：「(.{0,60})", txt)
    out.append({"no": e["no"], "page": e["page"], "sec": e["sec"], "juan": m.group(2) if m else "", "title": m.group(1) if m else "",
                "loc": " ".join(loc.groups()) if loc else "", "quote": q.group(1) if q else ""})
dump("lijiao.json", out)

# ---- CBETA T1560 verses ----
NS = {"t": "http://www.tei-c.org/ns/1.0", "cb": "http://www.cbeta.org/ns/1.0"}
tree = etree.parse(sys.argv[1])
body = tree.find(".//t:body", NS)
def text_of(el):
    buf = []
    def walk(e):
        tag = etree.QName(e).localname if isinstance(e.tag, str) else None
        if tag in ("note", "rdg", "anchor", "lb", "pb", "milestone"):
            pass
        elif tag == "caesura":
            buf.append("|")
        else:
            if e.text: buf.append(e.text)
            for c in e: walk(c)
        if e is not el and e.tail: buf.append(e.tail)
    if el.text: buf.append(el.text)
    for c in el: walk(c)
    return "".join(buf)
res = []
for div in body.iter("{http://www.cbeta.org/ns/1.0}div"):
    head = div.find("t:head", NS)
    note = head.find("t:note", NS) if head is not None else None
    res.append({"head": text_of(head) if head is not None else "", "note": note.text if note is not None else "",
                "lines": [text_of(l).strip() for l in div.iter("{http://www.tei-c.org/ns/1.0}l")]})
dump("song.json", res)
print("extracted")
