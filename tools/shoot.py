"""Screenshot pages and report console errors / font status.
Usage: python3 tools/shoot.py BASE_URL OUTDIR [page ...] [--lang zh|en|both] [--mobile] [--full]"""
import sys, os, json
from playwright.sync_api import sync_playwright

args = [a for a in sys.argv[1:] if not a.startswith("--")]
flags = [a for a in sys.argv[1:] if a.startswith("--")]
base, out = args[0], args[1]
pages = args[2:] or ["index.html"]
lang = next((f.split("=")[1] for f in flags if f.startswith("--lang=")), "zh")
mobile = "--mobile" in flags
full = "--full" in flags
os.makedirs(out, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
    vp = {"width": 390, "height": 844} if mobile else {"width": 1440, "height": 900}
    ctx = b.new_context(viewport=vp, device_scale_factor=1)
    ctx.add_init_script(f"try{{localStorage.setItem('abhi-lang','{lang}')}}catch(e){{}}")
    for pg_name in pages:
        pg = ctx.new_page()
        errs = []
        pg.on("console", lambda m: errs.append(m.text) if m.type in ("error", "warning") else None)
        pg.on("pageerror", lambda e: errs.append("PAGEERROR " + str(e)))
        url = base.rstrip("/") + "/" + pg_name.split("#")[0] + (("#" + pg_name.split("#")[1]) if "#" in pg_name else "")
        pg.goto(url, wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        st = pg.evaluate("Array.from(document.fonts).map(f=>f.family+' '+f.weight+' '+f.style+' '+f.status).filter(s=>s.indexOf('loaded')>=0)")
        name = pg_name.replace("/", "_").replace("#", "_") + ("-m" if mobile else "") + f"-{lang}.png"
        pg.screenshot(path=os.path.join(out, name), full_page=full)
        print(pg_name, "errors:", errs, "fonts loaded:", st)
        pg.close()
    b.close()
