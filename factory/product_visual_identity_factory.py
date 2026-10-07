#!/usr/bin/env python3
"""Create stable, unique 4K-ready visual identity assets for every concrete product."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import hashlib, html, json, os

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"products/visuals"
MAN=ROOT/"generated/product-visual-assets.json"
SOURCES=[ROOT/"generated/1000-digital-products.json",ROOT/"showroom-products.json",ROOT/"generated/product-catalog-public.json"]

def esc(v): return html.escape(str(v), quote=True)

def visual(p):
    pid=str(p.get("id","PRODUCT")); name=str(p.get("name","SHIRMANI Digital Product"))
    family=str(p.get("family",p.get("category","Digital Product"))); engine=str(p.get("engine","digital"))
    h=hashlib.sha256(pid.encode()).hexdigest(); c1="#"+h[0:6]; c2="#"+h[6:12]; accent="#"+h[12:18]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="3840" height="2160" viewBox="0 0 3840 2160" role="img" aria-labelledby="title desc">
<title id="title">{esc(name)} — SHIRMANI product visual</title><desc id="desc">Unique 4K-ready product identity for {esc(pid)}, {esc(family)}, {esc(engine)}.</desc>
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{c1}"/><stop offset=".52" stop-color="{c2}"/><stop offset="1" stop-color="#050910"/></linearGradient><linearGradient id="glass" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#ffffff" stop-opacity=".20"/><stop offset="1" stop-color="#ffffff" stop-opacity=".035"/></linearGradient><filter id="glow"><feGaussianBlur stdDeviation="38"/></filter><filter id="shadow"><feDropShadow dx="0" dy="28" stdDeviation="30" flood-opacity=".45"/></filter></defs>
<rect width="3840" height="2160" fill="url(#bg)"/><circle cx="3150" cy="420" r="500" fill="{accent}" opacity=".12" filter="url(#glow)"/><circle cx="650" cy="1770" r="650" fill="#64d9ff" opacity=".07" filter="url(#glow)"/>
<g filter="url(#shadow)"><path d="M430 1760 L760 410 L3090 330 L3460 1680 Z" fill="url(#glass)" stroke="#e5c35b" stroke-opacity=".50" stroke-width="12"/><path d="M760 410 L1110 690 L3460 590 L3090 330 Z" fill="#ffffff" opacity=".075"/><path d="M1110 690 L1110 1600 L3460 1680 L3460 590 Z" fill="#000000" opacity=".18"/></g>
<circle cx="2990" cy="1290" r="350" fill="none" stroke="#64d9ff" stroke-opacity=".38" stroke-width="9"/><circle cx="2990" cy="1290" r="245" fill="none" stroke="#e5c35b" stroke-opacity=".30" stroke-width="6"/><circle cx="2990" cy="1290" r="120" fill="{accent}" opacity=".18"/>
<text x="520" y="790" fill="#64d9ff" font-family="system-ui,sans-serif" font-size="82" font-weight="900" letter-spacing="12">SHIRMANI DIGITAL PRODUCT</text>
<text x="520" y="1110" fill="#f7f9fc" font-family="system-ui,sans-serif" font-size="138" font-weight="900">{esc(name)}</text>
<text x="520" y="1270" fill="#6ee7a8" font-family="system-ui,sans-serif" font-size="64" font-weight="800">{esc(family)} · {esc(engine)}</text>
<rect x="520" y="1380" width="650" height="112" rx="56" fill="#050910" opacity=".78"/><text x="585" y="1458" fill="#e5c35b" font-family="system-ui,sans-serif" font-size="68" font-weight="900">{esc(pid)}</text>
<text x="520" y="1505" fill="#62e6ff" font-family="system-ui,sans-serif" font-size="48" font-weight="800">PRICE ₹{int(p.get("offer_price_inr",p.get("price_inr",0)) or 0):,} · {esc(str(p.get("offer","PUBLIC LAUNCH PRICE"))[:54])}</text><text x="520" y="1590" fill="#ffffff" opacity=".82" font-family="system-ui,sans-serif" font-size="42" font-weight="800">SHORT DESCRIPTION</text><text x="520" y="1655" fill="#ffffff" opacity=".72" font-family="system-ui,sans-serif" font-size="34">{esc(str(p.get("description","")).replace(chr(10)," ")[:120])}</text><text x="520" y="1730" fill="#ffffff" opacity=".55" font-family="system-ui,sans-serif" font-size="34">UNIQUE PRODUCT IDENTITY · 3840×2160 · 16:9 · 4K-READY · QR → LONG DESCRIPTION</text></svg>'''

def main():
    products=[]; source=None
    for CAT in SOURCES:
        if not CAT.exists() or CAT.stat().st_size == 0: continue
        try: raw=json.loads(CAT.read_text(encoding="utf-8"))
        except Exception: continue
        items=raw.get("products") if isinstance(raw,dict) else None
        if not items and isinstance(raw,dict): items=raw.get("offers")
        if isinstance(items,list) and items:
            seen=set()
            for i,p in enumerate(items):
                if not isinstance(p,dict): continue
                pid=str(p.get("id") or f"CAT-{i+1:05d}")
                if pid in seen: continue
                seen.add(pid)
                p=dict(p); p["id"]=pid; p.setdefault("family",p.get("category",p.get("lane","Digital Product"))); p.setdefault("engine",p.get("delivery","digital")); p.setdefault("description","Customer-facing digital product."); products.append(p)
            source=str(CAT.relative_to(ROOT)); break
    if not products: raise SystemExit("No real product catalogue source available")
    OUT.mkdir(parents=True,exist_ok=True); rows=[]; created=existing=0
    try: batch=max(1,min(5000,int(os.environ.get("VISUAL_BATCH","5000"))))
    except ValueError: batch=250
    missing=[p for p in products if not (OUT/(str(p["id"]).lower()+".svg")).exists()]
    selected=set(id(x) for x in missing[:batch])
    for p in products:
        pid=str(p["id"]); path=OUT/(pid.lower()+".svg")
        if path.exists(): existing+=1
        elif id(p) in selected: path.write_text(visual(p),encoding="utf-8"); created+=1
        rows.append({"product_id":pid,"name":p.get("name"),"family":p.get("family"),"engine":p.get("engine"),"asset_path":str(path.relative_to(ROOT)),"format":"svg","width":3840,"height":2160,"aspect_ratio":"16:9","exists":path.exists(),"state":"READY_FOR_PUBLIC_SHOWROOM" if path.exists() else "PENDING_VISUAL_ASSET"})
    now=datetime.now(timezone.utc).isoformat()
    MAN.write_text(json.dumps({"version":1,"generated_at":now,"target":len(products),"visual_assets":sum(1 for x in rows if x["exists"]),"created_this_cycle":created,"already_existing":existing,"batch_size":batch,"remaining_visual_assets":sum(1 for x in rows if not x["exists"]),"state":"READY_FOR_PUBLIC_SHOWROOM","source":source,"note":"4K-ready vector visual identity assets; real catalogue identities only. Raster/AI-photographic variants can be added later without changing product IDs. Public-ready count requires the asset file to exist.","products":rows},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"target":len(products),"visual_assets":len(rows),"created_this_cycle":created},ensure_ascii=False))
if __name__=="__main__": main()
