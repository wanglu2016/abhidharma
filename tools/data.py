"""Load and cross-link all source data."""
import re
from common import load_json, s, pdf
import concepts as CM
import wanzi_en as WE
import baixia_en as BE
import jiuti as JT

PIN_IDS = [p[0] for p in CM.PINS]
PIN = {p[0]: {"id": p[0], "t": p[1], "s": p[2], "en": p[3], "juan": p[4], "verses": p[5]} for p in CM.PINS}
for k, (zh, en) in CM.PIN_NOTES.items():
    PIN[k]["note_zh"], PIN[k]["note_en"] = zh, en
for k, (a, b) in CM.STRUCTURE.items():
    PIN[k]["group"], PIN[k]["role"] = a, b

# ---------- verses (CBETA T1560) ----------
SONG = load_json("song.json")
VERSES = []        # flat list of dicts
VERSE_BY_PIN = {}
for pi, chap in enumerate(SONG):
    pid = PIN_IDS[pi]
    lines = chap["lines"]
    vs = []
    for k in range(0, len(lines), 2):
        pair = lines[k:k + 2]
        halves = []
        for ln in pair:
            if "|" in ln:
                a, b = ln.split("|", 1)
            else:
                m = re.match(r"^(.+?[，、；：])(.+)$", ln)
                a, b = (m.group(1), m.group(2)) if m else (ln, "")
            halves.append((a.strip(), b.strip()))
        vs.append(halves)
    prefix, suffix = [], []
    if pid == "jie":
        prefix, vs = vs[:3], vs[3:]
    if pid == "ding":
        vs, suffix = vs[:-4], vs[-4:]
    rows = []
    for i, h in enumerate(prefix):
        rows.append({"id": f"v-{pid}-p{i+1}", "pin": pid, "label": f"序{i+1}", "label_en": f"Pr.{i+1}", "h": h, "kind": "pre"})
    for i, h in enumerate(vs):
        rows.append({"id": f"v-{pid}-{i+1}", "pin": pid, "label": str(i + 1), "label_en": str(i + 1), "h": h, "kind": "main"})
    for i, h in enumerate(suffix):
        rows.append({"id": f"v-{pid}-e{i+1}", "pin": pid, "label": f"结{i+1}", "label_en": f"Ep.{i+1}", "h": h, "kind": "post"})
    for r in rows:
        r["text"] = "".join(a + b for a, b in r["h"])
    VERSE_BY_PIN[pid] = {"head": chap["head"], "note": chap["note"], "rows": rows,
                         "count": sum(1 for r in rows if r["kind"] == "main")}
    VERSES.extend(rows)

def find_verse(q):
    for v in VERSES:
        if q in v["text"]:
            return v
    return None

# ---------- 萬字 ----------
WZ = load_json("wanzi.json")
WZ_SEC = {}
for ch in WZ["chapters"]:
    for sec in ch["sections"]:
        en = WE.EN[sec["id"]]
        sec["pairs"] = list(zip(sec["paras"], en))
        sec["chapter"] = ch["no"]
        WZ_SEC[sec["id"]] = sec
WZ_PREFACE = list(zip(WZ["preface"], WE.PREFACE))
WZ_NOTES = list(zip(WZ["notes"], WE.NOTES))

# ---------- 九題 ----------
JTQ = {q["no"]: q for q in JT.Q}

# ---------- 百瑕 ----------
BX_RAW = load_json("baixia.json")
PIN_FROM_HEAD = {"分別界品第一": "jie", "分別根品第二": "gen", "分別世間品第三": "shi", "分別業品第四": "ye",
                 "分別隨眠品第五": "sui", "分別賢聖品第六": "xian", "分別智品第七": "zhi", "分別定品第八": "ding"}

def _gist(e):
    if e["no"] in BE.ZH_OVERRIDE:
        return BE.ZH_OVERRIDE[e["no"]]
    raw = e["raw"]
    paras = [p.replace("\n", "") for p in re.split(r"\n\s*\n", raw) if p.strip()]
    cand = [p for p in paras if len(re.findall(r"[一-鿿]", p)) > 10 and not p.startswith("《") and "CBETA" not in p]
    t = cand[0] if cand else ""
    # cut after the first full stop beyond 20 chars, cap ~130
    out = ""
    for seg in re.split(r"(?<=[。；])", t):
        out += seg
        if len(out) >= 24:
            break
    if len(out) > 140:
        out = out[:138] + "……"
    return out.strip()

def _refs(e):
    out = []
    for who, r in e["refs"]:
        who = "LS" if who in ("Lodrö Sangpo", "LS") else "Pruden"
        r = re.sub(r"\s+", " ", r).replace("，", ", ").replace("頌與長行", "verse & comm.").replace("長行", "comm.").replace("頌文", "verse").replace("頌", "verse").strip()
        out.append((who, r))
    # de-dup, keep first two distinct
    seen, res = set(), []
    for w, r in out:
        if (w, r) in seen:
            continue
        seen.add((w, r)); res.append((w, r))
    return res[:3]

BX = []
for e in BX_RAW:
    refs = _refs(e)
    verse = ""
    for w, r in refs:
        m = re.match(r"(\d-\d+[a-f\-]*)", r)
        if m:
            verse = m.group(1); break
    BX.append({"no": e["no"], "page": e["page"], "pin": PIN_FROM_HEAD.get(e["pin"], ""),
               "refs": refs, "verse": verse, "who": sorted(set(w for w, _ in refs)),
               "zh": _gist(e), "en": BE.EN[e["no"]], "concept": BE.CONCEPT.get(e["no"])})

# ---------- 理校百例 ----------
LJ_RAW = load_json("lijiao.json")
LJ = []
for e in LJ_RAW:
    sec = e["sec"] or ""
    m = re.match(r"^《([^》]+)》（(T\d{4})）", sec)
    text, tno = (m.group(1), m.group(2)) if m else (("百例之餘", "") if sec == "百例之餘" else (sec, ""))
    juan = e["juan"] if e["juan"] else ""
    loc = e["loc"]
    if tno and loc and (" " + tno[1:] + " ") not in (" " + loc + " "):
        loc = ""
    q = re.sub(r"\[[^\]]*\]", "", e["quote"])
    q = re.split(r"」|\(CBETA", q)[0]
    q = q[:36] + ("……" if len(q) > 36 else "")
    LJ.append({"no": e["no"], "page": e["page"], "text": text, "tno": tno, "juan": juan, "loc": loc, "quote": q})

# ---------- concepts ----------
def _wz_text(c):
    zh, en, secs = [], [], []
    for sid, a, b in c.get("wzq", []):
        sec = WZ_SEC[sid]
        for i in range(a, b + 1):
            zh.append(sec["paras"][i]); en.append(WE.EN[sid][i])
        if sid not in secs:
            secs.append(sid)
    return zh, en, secs

CONCEPTS = []
CBYID = {}
for c in CM.C:
    zh, en, secs = _wz_text(c)
    src = "wz" if zh else "ed"
    if c.get("zh_def"):
        zh.append(s(c["zh_def"])); en.append(c["en_def"])
    if c.get("zh_extra"):
        zh.append(s(c["zh_extra"])); en.append(c["en_extra"])
    vrefs = []
    for q in c.get("verse", []):
        v = find_verse(q)
        if v and v["id"] not in [x["id"] for x in vrefs]:
            vrefs.append({"id": v["id"], "pin": v["pin"], "label": v["label"], "text": v["text"]})
    rec = {
        "id": c["id"], "pin": c["pin"], "t": c["t"], "s": s(c["t"]), "skt": c["skt"], "en": c["en"],
        "tier": c["tier"], "memo": bool(c.get("memo")), "mile": c.get("mile"),
        "zh": zh, "enl": en, "src": src, "wz": secs,
        "note_zh": s(c["note_zh"]) if c.get("note_zh") else "", "note_en": c.get("note_en", ""),
        "verses": vrefs, "jt": c.get("jt", []), "bx": c.get("bx", []), "rel": c.get("rel", []),
    }
    CONCEPTS.append(rec); CBYID[rec["id"]] = rec

# Back-links: 九題 questions and 百瑕 entries that name a concept
for q in JT.Q:
    for cid in q["concepts"]:
        if q["no"] not in CBYID[cid]["jt"]:
            CBYID[cid]["jt"].append(q["no"])
for b in BX:
    if b["concept"] and b["no"] not in CBYID[b["concept"]]["bx"]:
        CBYID[b["concept"]]["bx"].append(b["no"])
for c in CONCEPTS:
    c["jt"].sort(); c["bx"].sort()

# concepts mentioned per 萬字 section
WZ_CONCEPTS = {}
for c in CONCEPTS:
    for sid in c["wz"]:
        WZ_CONCEPTS.setdefault(sid, []).append(c["id"])

TIER = {
    "key": ("要点", "Key point", "◎"),
    "hard": ("难点", "Difficult point", "●"),
    "method": ("基本操作", "Basic operation", "○"),
    "term": ("术语", "Listed term", ""),
}
