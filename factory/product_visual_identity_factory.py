#!/usr/bin/env python3
"""Create stable, unique 4K-ready product visual identity assets for the public showroom."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import hashlib, html, json, os

ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"generated/1000-digital-products.json"
OUT=ROOT/"products/visuals"
MAN=ROOT/"generated/product-visual-assets.json"
BASE="https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/products/concrete/"

def esc(v): return html.escape(str(v), quote=True)
def money(v):
    try: n=int(float(v or 0))
    except (TypeError,ValueError): n=0
    return "FREE" if n==0 else "₹"+f"{n:,}"

def visual(p):
    pid=str(p.get("id","PRODUCT")); name=str(p.get("name","SHIRMANI Supreme Digital Product"))
    family=str(p.get("family",p.get("category","Digital Product"))); engine=str(p.get("engine","digital"))
    desc=" ".join(str(p.get("short_description") or p.get("description") or "Unique customer-facing digital product").split())[:118]
    price=money(p.get("offer_price_inr",p.get("price_inr",0))); base_price=money(p.get("price_inr",0))
    offer=" ".join(str(p.get("offer","PUBLIC LAUNCH OFFER")).split())[:70]
    qc=str(p.get("qc_code","QC-PENDING")); gate=str(p.get("gate_no","GATE-PRODUCTION")); dispatch=str(p.get("dispatch_no","NO"))
    h=hashlib.sha256(pid.encode()).hexdigest(); c1="#"+h[0:6]; c2="#"+h[6:12]; accent="#"+h[12:18]
    qr_rel="qr/"+pid.lower()+".svg"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="3840" height="2160" viewBox="0 0 3840 2160" role="img" aria-labelledby="title desc">
<title id="title">{esc(name)} — SHIRMANI Supreme Digital Product</title>
<desc id="desc">{esc(desc)} Product ID {esc(pid)}. Long description QR included.</desc>
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{c1}"/><stop offset=".50" stop-color="{c2}"/><stop offset="1" stop-color="#050910"/></linearGradient><linearGradient id="glass" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#ffffff" stop-opacity=".20"/><stop offset="1" stop-color="#ffffff" stop-opacity=".035"/></linearGradient><filter id="glow"><feGaussianBlur stdDeviation="38"/></filter><filter id="shadow"><feDropShadow dx="0" dy="28" stdDeviation="30" flood-opacity=".45"/></filter></defs>
<rect width="3840" height="2160" fill="url(#bg)"/><circle cx="3210" cy="380" r="520" fill="{accent}" opacity=".12" filter="url(#glow)"/><circle cx="560" cy="1810" r="650" fill="#64d9ff" opacity=".07" filter="url(#glow)"/>
<g filter="url(#shadow)"><path d="M350 1790 L690 350 L3160 300 L3500 1700 Z" fill="url(#glass)" stroke="#e5c35b" stroke-opacity=".60" stroke-width="12"/><path d="M690 350 L1080 650 L3500 570 L3160 300 Z" fill="#ffffff" opacity=".075"/><path d="M1080 650 L1080 1610 L3500 1700 L3500 570 Z" fill="#000000" opacity=".18"/></g>
<path d="M230 1550 C800 1160 1130 1850 1700 1390 S2800 1110 3620 1510" fill="none" stroke="#64d9ff" stroke-opacity=".35" stroke-width="24"/><path d="M270 1600 C820 1230 1190 1910 1740 1450 S2840 1190 3580 1560" fill="none" stroke="#6ee7a8" stroke-opacity=".20" stroke-width="12"/>
<text x="520" y="560" fill="#64d9ff" font-family="system-ui,sans-serif" font-size="82" font-weight="900" letter-spacing="10">꙰ SHIRMANI SUPREME DIGITAL PRODUCT</text>
<text x="520" y="900" fill="#f7f9fc" font-family="system-ui,sans-serif" font-size="{138 if len(name)<34 else 108}" font-weight="900">{esc(name)}</text>
<text x="520" y="1050" fill="#6ee7a8" font-family="system-ui,sans-serif" font-size="66" font-weight="900">{esc(pid)}</text>
<text x="520" y="1160" fill="#e5c35b" font-family="system-ui,sans-serif" font-size="58" font-weight="800">{esc(family)} · {esc(engine)}</text>
<text x="520" y="1270" fill="#f7f9fc" font-family="system-ui,sans-serif" font-size="44" font-weight="650" opacity=".94">{esc(desc)}</text>
<rect x="520" y="1340" width="850" height="154" rx="77" fill="#050910" opacity=".84" stroke="#e5c35b" stroke-opacity=".55" stroke-width="5"/><text x="600" y="1442" fill="#ffffff" font-family="system-ui,sans-serif" font-size="62" font-weight="900">{esc(price)}</text>
<text x="520" y="1548" fill="#6ee7a8" font-family="system-ui,sans-serif" font-size="36" font-weight="800">{esc(offer)}</text>
<text x="520" y="1640" fill="#ffffff" opacity=".62" font-family="system-ui,sans-serif" font-size="30">Base {esc(base_price)} · QC {esc(qc)} · {esc(gate)} · DISPATCH {esc(dispatch)}</text>
<text x="520" y="1725" fill="#ffffff" opacity=".76" font-family="system-ui,sans-serif" font-size="31" font-weight="800">SHORT DESCRIPTION ON VISUAL · LONG DESCRIPTION VIA QR · 3840×2160 · 16:9</text>
<rect x="3020" y="820" width="390" height="570" rx="30" fill="#ffffff" opacity=".97"/><image href="{esc(qr_rel)}" x="3042" y="842" width="346" height="346" preserveAspectRatio="xMidYMid meet"/>
<text x="3215" y="1250" text-anchor="middle" fill="#101010" font-family="system-ui,sans-serif" font-size="34" font-weight="900">SCAN FOR LONG</text><text x="3215" y="1300" text-anchor="middle" fill="#101010" font-family="system-ui,sans-serif" font-size="34" font-weight="900">DESCRIPTION</text><text x="3215" y="1360" text-anchor="middle" fill="#0b5e78" font-family="system-ui,sans-serif" font-size="24" font-weight="800">{esc(pid)}</text>
</svg>'''

def main():
    if not CAT.exists(): raise SystemExit("generated/1000-digital-products.json missing")
    products=json.loads(CAT.read_text(encoding="utf-8")).get("products",[])
    OUT.mkdir(parents=True,exist_ok=True)
    try: batch=max(1,min(5000,int(os.environ.get("VISUAL_BATCH","250"))))
    except ValueError: batch=250
    missing=[p for p in products if not (OUT/(str(p["id"]).lower()+".svg")).exists()]
    selected_ids={str(p["id"]) for p in missing[:batch]}
    created=existing=0; rows=[]
    for p in products:
        pid=str(p["id"]); path=OUT/(pid.lower()+".svg")
        if path.exists(): existing+=1
        elif pid in selected_ids: path.write_text(visual(p),encoding="utf-8"); created+=1
        rows.append({"product_id":pid,"name":p.get("name"),"family":p.get("family"),"engine":p.get("engine"),"asset_path":str(path.relative_to(ROOT)),"format":"svg","width":3840,"height":2160,"aspect_ratio":"16:9","exists":path.exists(),"qr_path":"products/visuals/qr/"+pid.lower()+".svg","long_description_url":BASE+pid+".html","short_description_on_visual":True,"state":"READY_FOR_PUBLIC_SHOWROOM" if path.exists() else "PENDING_VISUAL_ASSET"})
    ready=sum(1 for x in rows if x["exists"]); now=datetime.now(timezone.utc).isoformat()
    MAN.write_text(json.dumps({"version":2,"generated_at":now,"target":len(products),"visual_assets":ready,"created_this_cycle":created,"already_existing":existing,"batch_size":batch,"remaining_visual_assets":len(products)-ready,"state":"READY_FOR_PUBLIC_SHOWROOM" if ready==len(products) else "IN_PROGRESS","design_contract":"4K 16:9 unique product identity; short description, price/offer and QC metadata on visual; product-specific QR for long description.","products":rows},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"target":len(products),"visual_assets":ready,"created_this_cycle":created,"remaining":len(products)-ready},ensure_ascii=False))
if __name__=="__main__":
    main()
