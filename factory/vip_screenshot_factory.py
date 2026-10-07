#!/usr/bin/env python3
"""Generate a product-specific VIP screenshot/presentation asset for every concrete product."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import hashlib, html, json, os, urllib.parse

ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"generated/1000-digital-products.json"
OUT=ROOT/"products/vip-screenshots"
MAN=ROOT/"generated/vip-screenshot-assets.json"
STYLE="2026-10-07-vip-screenshot-v1"
BASE="https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/"
LOGO=BASE+"assets/shirmani-perspective-logo.svg"
IDENTITY="Shiromani Rampal Saini — Impartial Understanding · Beyond Comparison · Beyond Time · Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present"

def esc(v): return html.escape(str(v or ""),quote=True)

def make_svg(p):
    pid=str(p.get("id","PRODUCT")); name=str(p.get("name","SHIRMANI Digital Product"))
    family=str(p.get("family",p.get("category","Digital Product"))); engine=str(p.get("engine","digital"))
    desc=" ".join(str(p.get("short_description") or p.get("description") or "Customer-facing digital product").split())[:180]
    price=int(p.get("offer_price_inr",p.get("price_inr",0)) or 0)
    seed=hashlib.sha256(pid.encode()).hexdigest(); c1="#"+seed[:6]; c2="#"+seed[6:12]
    passport=BASE+"product-passport.html?id="+urllib.parse.quote(pid)
    demo=BASE+"product-demo.html?id="+urllib.parse.quote(pid)
    qr="https://api.qrserver.com/v1/create-qr-code/?size=500x500&margin=10&data="+urllib.parse.quote(passport,safe="")
    return f'''<!-- {STYLE} -->
<svg xmlns="http://www.w3.org/2000/svg" width="2560" height="1440" viewBox="0 0 2560 1440" role="img">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{c1}"/><stop offset=".55" stop-color="{c2}"/><stop offset="1" stop-color="#050910"/></linearGradient></defs>
<rect width="2560" height="1440" fill="url(#bg)"/><rect x="24" y="24" width="2512" height="1392" rx="70" fill="none" stroke="#e7c85b" stroke-width="7"/>
<circle cx="210" cy="205" r="150" fill="#061016" stroke="#e7c85b" stroke-width="8"/><image href="{LOGO}" x="80" y="75" width="260" height="260" preserveAspectRatio="xMidYMid slice"/>
<text x="410" y="125" fill="#e7c85b" font-family="system-ui,sans-serif" font-size="46" font-weight="950">SHIRMANI SUPREME DIGITAL PRODUCT · VIP VIEW</text>
<text x="410" y="185" fill="#fff" font-family="system-ui,sans-serif" font-size="25" font-weight="800">{esc(IDENTITY)}</text>
<text x="410" y="260" fill="#67e8f9" font-family="system-ui,sans-serif" font-size="35" font-weight="900">PRODUCT IDENTITY · {esc(pid)}</text>
<text x="410" y="345" fill="#fff" font-family="system-ui,sans-serif" font-size="72" font-weight="950">{esc(name)[:52]}</text>
<text x="410" y="410" fill="#72e6aa" font-family="system-ui,sans-serif" font-size="35" font-weight="850">{esc(family)} · {esc(engine)}</text>
<rect x="410" y="470" width="1320" height="220" rx="28" fill="#03060dcc" stroke="#3b566d" stroke-width="3"/>
<text x="450" y="525" fill="#67e8f9" font-family="system-ui,sans-serif" font-size="27" font-weight="900">SHORT DESCRIPTION</text>
<text x="450" y="575" fill="#fff" font-family="system-ui,sans-serif" font-size="30" font-weight="650">{esc(desc[:105])}</text>
<text x="450" y="620" fill="#fff" font-family="system-ui,sans-serif" font-size="30" font-weight="650">{esc(desc[105:180])}</text>
<text x="450" y="670" fill="#e7c85b" font-family="system-ui,sans-serif" font-size="39" font-weight="950">₹{price:,} · DEMO VIDEO · USAGE GUIDE · QC / GATE / DISPATCH</text>
<rect x="1890" y="95" width="540" height="610" rx="38" fill="#061016" stroke="#e7c85b" stroke-width="7"/>
<text x="1955" y="165" fill="#fff" font-family="system-ui,sans-serif" font-size="33" font-weight="950">LONG DESCRIPTION</text><text x="2040" y="205" fill="#fff" font-family="system-ui,sans-serif" font-size="33" font-weight="950">/ PRODUCT PASSPORT</text>
<rect x="1960" y="245" width="400" height="400" fill="#fff"/><image href="{qr}" x="1970" y="255" width="380" height="380" preserveAspectRatio="none"/>
<text x="1965" y="675" fill="#67e8f9" font-family="system-ui,sans-serif" font-size="25" font-weight="900">SCAN · DETAILS · USE · PURCHASE</text>
<rect x="120" y="790" width="2320" height="500" rx="42" fill="#050910cc" stroke="#284254" stroke-width="3"/>
<text x="175" y="860" fill="#e7c85b" font-family="system-ui,sans-serif" font-size="37" font-weight="950">VIP PRODUCT EXPERIENCE</text>
<text x="175" y="925" fill="#fff" font-family="system-ui,sans-serif" font-size="30" font-weight="750">1 · OPEN PRODUCT   2 · WATCH DEMO   3 · USE TOOL   4 · REVIEW RESULT   5 · READ PASSPORT   6 · BUY / USE</text>
<text x="175" y="1010" fill="#67e8f9" font-family="system-ui,sans-serif" font-size="30" font-weight="850">WHERE TO USE: {esc(family)} · {esc(engine)} · CUSTOMER-FACING DIGITAL WORK</text>
<text x="175" y="1080" fill="#72e6aa" font-family="system-ui,sans-serif" font-size="30" font-weight="850">DEMO: {esc(demo)}</text>
<text x="175" y="1150" fill="#aeb8c8" font-family="system-ui,sans-serif" font-size="28" font-weight="700">Product-specific visual identity · Product-specific passport · Product-specific demo route</text>
<text x="175" y="1215" fill="#fff" font-family="system-ui,sans-serif" font-size="25" font-weight="650">Presentation asset only: sale, dispatch and independent verification remain separate states.</text>
</svg>'''

def main():
    products=json.loads(CAT.read_text(encoding="utf-8")).get("products",[])
    OUT.mkdir(parents=True,exist_ok=True)
    try: batch=max(1,min(5000,int(os.environ.get("VIP_SCREENSHOT_BATCH","5000"))))
    except ValueError: batch=500
    rebuild=os.environ.get("VIP_REBUILD","1").lower() not in {"0","false","no"}
    missing=[p for p in products if not (OUT/(str(p["id"]).lower()+".svg")).exists()]
    selected={id(p) for p in missing[:batch]}
    rows=[]; created=updated=existing=0
    for p in products:
        pid=str(p["id"]); path=OUT/(pid.lower()+".svg")
        if path.exists() and rebuild and STYLE not in path.read_text(encoding="utf-8",errors="ignore")[:120]:
            path.write_text(make_svg(p),encoding="utf-8"); updated+=1
        elif path.exists(): existing+=1
        elif id(p) in selected: path.write_text(make_svg(p),encoding="utf-8"); created+=1
        rows.append({"product_id":pid,"name":p.get("name"),"asset_path":str(path.relative_to(ROOT)),"format":"svg","width":2560,"height":1440,"aspect_ratio":"16:9","exists":path.exists(),"state":"READY_FOR_PUBLIC_SHOWROOM" if path.exists() else "PENDING","demo_route":f"product-demo.html?id={urllib.parse.quote(pid)}","passport_route":f"product-passport.html?id={urllib.parse.quote(pid)}"})
    now=datetime.now(timezone.utc).isoformat(); ready=sum(1 for r in rows if r["exists"])
    MAN.write_text(json.dumps({"schema_version":1,"generated_at":now,"style":STYLE,"target":len(products),"vip_screenshot_assets":ready,"coverage_percent":round(100*ready/len(products),2) if products else 0,"created_this_cycle":created,"updated_this_cycle":updated,"already_existing":existing,"remaining":len(products)-ready,"principle":"Every concrete product gets a product-specific VIP presentation asset.","truth_boundary":"VIP screenshot is a customer-facing presentation asset, not independent scientific verification.","products":rows},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"target":len(products),"vip_screenshots":ready,"created_this_cycle":created,"remaining":len(products)-ready},ensure_ascii=False))
if __name__=="__main__": main()
