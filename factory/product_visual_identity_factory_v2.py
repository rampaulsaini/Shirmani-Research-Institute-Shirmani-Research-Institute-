#!/usr/bin/env python3
"""SHIRMANI v2 product visual identity factory: logo + English identity + short description + QR."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import hashlib, html, json, os
from urllib.parse import quote

ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"generated/1000-digital-products.json"
OUT=ROOT/"products/visuals"
MAN=ROOT/"generated/product-visual-assets-v2.json"
VERSION="2026-10-07-production-visual-v11-centered-logo-local-qr-short-description"
SHOWROOM_BASE="https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/"
LOGO=SHOWROOM_BASE+"assets/shirmani-perspective-logo.svg"
IDENTITY="Shiromani Rampal Saini — Beyond Comparison · Beyond Time · Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present"

def esc(v): return html.escape(str(v), quote=True)

def make(p):
    pid=str(p["id"]); name=str(p.get("name","SHIRMANI Digital Product"))
    family=str(p.get("family",p.get("category","Digital Product"))); engine=str(p.get("engine","digital"))
    desc=" ".join(str(p.get("description","Unique customer-facing digital product")).split())[:135]
    price=int(p.get("offer_price_inr",p.get("price_inr",0)) or 0)
    offer=str(p.get("offer","PUBLIC LAUNCH PRICE"))[:48]
    h=hashlib.sha256(pid.encode()).hexdigest(); c1="#"+h[:6]; c2="#"+h[6:12]
    qc=str(p.get("qc_code","QC-PENDING")); gate=str(p.get("gate_no","GATE-PENDING")); dispatch=str(p.get("dispatch_no","NO"))
    qr_target=SHOWROOM_BASE+"product-passport.html?id="+quote(pid)
    qr_asset=f"qr/{pid.lower()}.svg"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="3840" height="2160" viewBox="0 0 3840 2160">
<defs><linearGradient id="b" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{c1}"/><stop offset=".55" stop-color="{c2}"/><stop offset="1" stop-color="#050910"/></linearGradient></defs>
<rect width="3840" height="2160" fill="url(#b)"/><title>{esc(name)} — {esc(pid)}</title><desc>{esc(IDENTITY)} · Short description on image · QR for long product description · 3840×2160 4K-ready product identity.</desc><rect x="70" y="70" width="3700" height="2020" rx="120" fill="none" stroke="#e7c85b" stroke-width="10"/>
<circle cx="1920" cy="285" r="205" fill="#061016" stroke="#e7c85b" stroke-width="14"/><image href="{LOGO}" x="1735" y="100" width="370" height="370" preserveAspectRatio="xMidYMid slice"/>
<text x="1920" y="540" text-anchor="middle" fill="#f6d35f" font-family="system-ui,sans-serif" font-size="40" font-weight="950">Shiromani Rampal Saini</text>
<text x="1920" y="592" text-anchor="middle" fill="#fff" font-family="system-ui,sans-serif" font-size="22" font-weight="750">SHIRMANI HEART-VIEW · IMPARTIAL UNDERSTANDING</text>
<text x="1920" y="630" text-anchor="middle" fill="#d9e3ef" font-family="system-ui,sans-serif" font-size="18" font-weight="700">Shiromani Rampal Saini — Beyond Comparison · Beyond Time · Beyond Words · Beyond Love</text>
<text x="1920" y="664" text-anchor="middle" fill="#d9e3ef" font-family="system-ui,sans-serif" font-size="18" font-weight="700">Eternal · Real · Natural Truth · Directly Present</text>
<text x="610" y="190" fill="#66ddff" font-family="system-ui,sans-serif" font-size="52" font-weight="900">SHIRMANI SUPREME DIGITAL PRODUCT</text>
<rect x="3160" y="120" width="570" height="690" rx="44" fill="#061016" stroke="#e7c85b" stroke-width="10"/>
<text x="3270" y="210" fill="#fff" font-family="system-ui,sans-serif" font-size="42" font-weight="900">LONG DESCRIPTION</text>
<text x="3400" y="260" fill="#fff" font-family="system-ui,sans-serif" font-size="42" font-weight="900">/ PRODUCT DETAILS</text>
<rect x="3250" y="300" width="390" height="390" fill="#fff"/><image href="{qr_asset}" x="3260" y="310" width="370" height="370"/>
<text x="3290" y="750" fill="#66ddff" font-family="system-ui,sans-serif" font-size="27" font-weight="900">SCAN FOR LONG DESCRIPTION</text>
<text x="520" y="820" fill="#66ddff" font-family="system-ui,sans-serif" font-size="76" font-weight="900">{esc(pid)}</text>
<text x="520" y="1040" fill="#fff" font-family="system-ui,sans-serif" font-size="125" font-weight="900">{esc(name)}</text>
<text x="520" y="1170" fill="#72e6aa" font-family="system-ui,sans-serif" font-size="62" font-weight="800">{esc(family)} · {esc(engine)}</text>
<text x="520" y="1300" fill="#fff" font-family="system-ui,sans-serif" font-size="43" font-weight="650">SHORT DESCRIPTION · {esc(desc)}</text>
<rect x="520" y="1390" width="730" height="125" rx="62" fill="#03060d" stroke="#e7c85b" stroke-width="5"/><text x="590" y="1475" fill="#fff" font-family="system-ui,sans-serif" font-size="62" font-weight="900">₹{price:,}</text><text x="1340" y="1475" fill="#66ddff" font-family="system-ui,sans-serif" font-size="44" font-weight="800">{esc(offer)}</text>
<text x="520" y="1710" fill="#fff" opacity=".82" font-family="system-ui,sans-serif" font-size="35" font-weight="800">UNIQUE PRODUCT IDENTITY · 3840×2160 · 16:9 · 4K-READY · SHORT DESCRIPTION + QR LONG DESCRIPTION</text>
<text x="520" y="1780" fill="#e7c85b" opacity=".92" font-family="system-ui,sans-serif" font-size="32" font-weight="700">QC · {esc(qc)} · GATE · {esc(gate)} · DISPATCH · {esc(dispatch)}</text>
</svg>'''

def main():
    products=json.loads(CAT.read_text(encoding="utf-8")).get("products",[])
    OUT.mkdir(parents=True,exist_ok=True)
    previous={}
    if MAN.exists():
        try: previous=json.loads(MAN.read_text(encoding="utf-8"))
        except Exception: pass
    previous_rows={str(r.get("product_id")):r for r in previous.get("products",[]) if isinstance(r,dict)}
    batch=max(1,min(5000,int(os.environ.get("VISUAL_BATCH","1000"))))
    # Refresh is version-aware per product. A partial batch must not falsely mark
    # the whole catalogue as upgraded; later cycles continue until every product is current.
    todo=[p for p in products if (
        not (OUT/(str(p["id"]).lower()+".svg")).exists()
        or previous_rows.get(str(p["id"]),{}).get("visual_version")!=VERSION
    )]
    chosen={id(p) for p in todo[:batch]}
    rows=[]; changed=0
    for p in products:
        pid=str(p["id"])
        path=OUT/(pid.lower()+".svg")
        if id(p) in chosen:
            path.write_text(make(p),encoding="utf-8"); changed+=1
            product_version=VERSION
        else:
            product_version=previous_rows.get(pid,{}).get("visual_version","LEGACY")
        rows.append({"product_id":pid,"asset_path":str(path.relative_to(ROOT)),"exists":path.exists(),
                     "visual_version":product_version,"qr_asset_path":f"products/visuals/qr/{pid.lower()}.svg",
                     "short_description_on_visual":True,"qr_upper_right":True,
                     "logo_photo":True,"english_identity_line":IDENTITY})
    ready=sum(1 for x in rows if x["exists"])
    current=sum(1 for x in rows if x["exists"] and x["visual_version"]==VERSION)
    remaining=len(products)-current
    MAN.write_text(json.dumps({"version":2,"visual_version":VERSION if current==len(products) else "IN_PROGRESS",
        "target_visual_version":VERSION,"generated_at":datetime.now(timezone.utc).isoformat(),
        "target":len(products),"visual_assets":ready,"current_version_assets":current,
        "changed_this_cycle":changed,"remaining":remaining,
        "logo":LOGO,"english_identity_line":IDENTITY,"short_description_on_visual":True,
        "qr_upper_right":True,"qr_asset_local":True,"qr_purpose":"long description / product details","visual_contract":{"logo_photo":True,"logo_position":"upper-center","english_identity":"Shiromani Rampal Saini — Beyond Comparison · Beyond Time · Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present","short_description":"on-image","qr_position":"upper-right","qr_target":"product passport / long description","canvas":"3840x2160 16:9 4K-ready"},"products":rows},
        ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"target":len(products),"visual_assets":ready,"current_version_assets":current,
                      "changed_this_cycle":changed,"remaining":remaining}))
if __name__=="__main__": main()
