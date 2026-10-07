#!/usr/bin/env python3
"""Create stable, unique 4K-ready visual identity assets for every concrete product."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import hashlib, html, json, os

ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"generated/1000-digital-products.json"
OUT=ROOT/"products/visuals"
MAN=ROOT/"generated/product-visual-assets.json"
STYLE_VERSION="2026-10-07-production-visual-v8-persistent-logo-qr"
LOGO_URL=SHOWROOM_BASE+"assets/shirmani-perspective-logo.svg"
IDENTITY="Shiromani Rampal Saini — Beyond Comparison · Beyond Time · Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present"
SHOWROOM_BASE="https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/"

def esc(v): return html.escape(str(v), quote=True)

def visual(p):
    pid=str(p.get("id","PRODUCT")); name=str(p.get("name","SHIRMANI Digital Product"))
    family=str(p.get("family",p.get("category","Digital Product"))); engine=str(p.get("engine","digital"))
    h=hashlib.sha256(pid.encode()).hexdigest(); c1="#"+h[0:6]; c2="#"+h[6:12]
    desc=" ".join(str(p.get("short_description") or p.get("description") or "Unique customer-facing digital product").split())[:145]
    price=int(p.get("offer_price_inr",p.get("price_inr",0)) or 0)
    import urllib.parse
    long_url=SHOWROOM_BASE+"product-passport.html?id="+urllib.parse.quote(pid)
    qr="https://api.qrserver.com/v1/create-qr-code/?size=430x430&margin=10&data="+urllib.parse.quote(long_url,safe="")
    title_size=132 if len(name)<=30 else 108
    return f'''<!-- {STYLE_VERSION} -->
<svg xmlns="http://www.w3.org/2000/svg" width="3840" height="2160" viewBox="0 0 3840 2160" role="img" aria-labelledby="title desc">
<title id="title">{esc(name)} — {esc(pid)}</title><desc id="desc">Unique 4K product identity visual with logo, English identity line, short description and QR long-description access.</desc>
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{c1}"/><stop offset=".55" stop-color="{c2}"/><stop offset="1" stop-color="#050910"/></linearGradient><linearGradient id="wave" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#00d2ff"/><stop offset=".5" stop-color="#00ff99"/><stop offset="1" stop-color="#00d2ff"/></linearGradient><filter id="shadow"><feDropShadow dx="0" dy="24" stdDeviation="28" flood-opacity=".55"/></filter></defs>
<rect width="3840" height="2160" fill="url(#bg)"/><rect x="28" y="28" width="3784" height="2104" rx="120" fill="none" stroke="#e7c85b" stroke-width="10"/>
<circle cx="300" cy="310" r="205" fill="#061016" stroke="#e7c85b" stroke-width="12"/><image href="{LOGO_URL}" x="105" y="115" width="390" height="390" preserveAspectRatio="xMidYMid slice"/>
<text x="570" y="160" fill="#e7c85b" font-family="system-ui,sans-serif" font-size="72" font-weight="950">✦ SHIRMANI SUPREME DIGITAL PRODUCT</text>
<text x="570" y="245" fill="#ffffff" font-family="system-ui,sans-serif" font-size="34" font-weight="800">Shiromani Rampal Saini — Beyond Comparison · Beyond Time · Beyond Words · Beyond Love</text><text x="570" y="295" fill="#ffffff" font-family="system-ui,sans-serif" font-size="34" font-weight="800">Eternal · Real · Natural Truth · Directly Present</text>
<rect x="2920" y="105" width="720" height="790" rx="48" fill="#061016" stroke="#e7c85b" stroke-width="9" filter="url(#shadow)"/><text x="3060" y="205" fill="#ffffff" font-family="system-ui,sans-serif" font-size="48" font-weight="950">LONG DESCRIPTION</text><text x="3230" y="265" fill="#ffffff" font-family="system-ui,sans-serif" font-size="48" font-weight="950">/ PRODUCT DETAILS</text><rect x="3050" y="330" width="470" height="470" fill="#fff"/><image href="{qr}" x="3060" y="340" width="450" height="450" preserveAspectRatio="none"/><text x="3070" y="850" fill="#52d8ff" font-family="system-ui,sans-serif" font-size="31" font-weight="900">SCAN FOR LONG DESCRIPTION</text>
<path d="M160 1740 C900 1320 1350 1970 1980 1540 S3020 1290 3710 1690" fill="none" stroke="url(#wave)" stroke-width="24" opacity=".82"/>
<text x="520" y="760" fill="#64d9ff" font-family="system-ui,sans-serif" font-size="72" font-weight="950" letter-spacing="10">PRODUCT IDENTITY</text><text x="520" y="940" fill="#ffffff" font-family="system-ui,sans-serif" font-size="{title_size}" font-weight="950">{esc(name)}</text><text x="520" y="1050" fill="#6ee7a8" font-family="system-ui,sans-serif" font-size="58" font-weight="850">{esc(family)} · {esc(engine)}</text>
<rect x="520" y="1125" width="660" height="112" rx="56" fill="#050910" stroke="#e5c35b" stroke-width="6"/><text x="585" y="1203" fill="#e5c35b" font-family="system-ui,sans-serif" font-size="64" font-weight="950">{esc(pid)}</text>
<text x="520" y="1305" fill="#62e6ff" font-family="system-ui,sans-serif" font-size="46" font-weight="850">SHORT DESCRIPTION · {esc(desc)}</text><rect x="520" y="1390" width="680" height="135" rx="68" fill="#03060d" stroke="#e7c85b" stroke-width="5"/><text x="590" y="1480" fill="#ffffff" font-family="system-ui,sans-serif" font-size="68" font-weight="950">₹{price:,}</text>
<text x="520" y="1595" fill="#6ee7a8" font-family="system-ui,sans-serif" font-size="38" font-weight="850">UNIQUE PRODUCT · 3840×2160 · 16:9 · 4K-READY</text><text x="520" y="1660" fill="#ffffff" opacity=".78" font-family="system-ui,sans-serif" font-size="34" font-weight="800">SHORT DESCRIPTION ON IMAGE · DEMO VIDEO · QR FOR LONG DESCRIPTION</text><text x="520" y="2020" fill="#aeb8c8" font-family="system-ui,sans-serif" font-size="30">Production-first public showroom · Product identity remains bound to {esc(pid)}</text></svg>'''
def main():
    if not CAT.exists(): raise SystemExit("generated/1000-digital-products.json missing")
    products=json.loads(CAT.read_text(encoding="utf-8")).get("products",[])
    OUT.mkdir(parents=True,exist_ok=True); rows=[]; created=updated=existing=0
    try: batch=max(1,min(5000,int(os.environ.get("VISUAL_BATCH","5000"))))
    except ValueError: batch=250
    rebuild=os.environ.get("VISUAL_REBUILD","1").lower() not in {"0","false","no"}
    missing=[p for p in products if not (OUT/(str(p["id"]).lower()+".svg")).exists()]
    selected=set(id(x) for x in missing[:batch])
    for p in products:
        pid=str(p["id"]); path=OUT/(pid.lower()+".svg")
        needs_rebuild=rebuild and path.exists() and STYLE_VERSION not in path.read_text(encoding="utf-8",errors="ignore")[:120]
        if needs_rebuild:
            path.write_text(visual(p),encoding="utf-8"); updated+=1
        elif path.exists(): existing+=1
        elif id(p) in selected: path.write_text(visual(p),encoding="utf-8"); created+=1
        rows.append({"product_id":pid,"name":p.get("name"),"family":p.get("family"),"engine":p.get("engine"),"asset_path":str(path.relative_to(ROOT)),"format":"svg","width":3840,"height":2160,"aspect_ratio":"16:9","exists":path.exists(),"state":"READY_FOR_PUBLIC_SHOWROOM" if path.exists() else "PENDING_VISUAL_ASSET"})
    now=datetime.now(timezone.utc).isoformat()
    MAN.write_text(json.dumps({"version":1,"generated_at":now,"target":len(products),"visual_assets":sum(1 for x in rows if x["exists"]),"created_this_cycle":created,"updated_this_cycle":updated,"already_existing":existing,"style_version":STYLE_VERSION,"batch_size":batch,"remaining_visual_assets":sum(1 for x in rows if not x["exists"]),"state":"READY_FOR_PUBLIC_SHOWROOM","note":"4K-ready vector visual identity assets; raster/AI-photographic variants can be added later without changing product IDs. Public-ready count requires the asset file to exist.","products":rows},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"target":len(products),"visual_assets":len(rows),"created_this_cycle":created},ensure_ascii=False))
if __name__=="__main__": main()
