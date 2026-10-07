#!/usr/bin/env python3
"""Materialize a unique 16:9, 1600x900 SVG visual for every catalog product.
These are repository-bound product identity masters, not claims of photographic realism.
"""
import json, html, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CATALOG=ROOT/"generated/1000-digital-products.json"
OUT=ROOT/"products/visuals"
OUT.mkdir(parents=True, exist_ok=True)

def h32(s):
    h=0
    for ch in s:
        h=((h<<5)-h+ord(ch)) & 0xffffffff
    return h

def svg(p):
    pid=str(p["id"]); h=h32(pid)
    hue=h%360; hue2=(h*7)%360; hue3=(h*13)%360
    uid=re.sub(r"[^A-Za-z0-9_-]","",pid)
    name=html.escape(str(p.get("name",pid)))
    family=html.escape(str(p.get("family","Digital Product")))
    engine=html.escape(str(p.get("engine","engine")))
    price=p.get("offer_price_inr")
    price_text=("₹"+format(float(price),",.0f")) if price is not None else "PRICE PENDING"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900">
<defs>
 <linearGradient id="bg-{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="hsl({hue} 65% 16%)"/><stop offset=".52" stop-color="hsl({hue2} 70% 24%)"/><stop offset="1" stop-color="hsl({hue3} 75% 10%)"/></linearGradient>
 <linearGradient id="card-{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".48" stop-color="#dfe8f4"/><stop offset="1" stop-color="#8798ad"/></linearGradient>
 <filter id="shadow-{uid}"><feGaussianBlur stdDeviation="24"/></filter>
 <pattern id="grid-{uid}" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#fff" stroke-opacity=".055"/></pattern>
</defs>
<rect width="1600" height="900" fill="url(#bg-{uid})"/><rect width="1600" height="900" fill="url(#grid-{uid})"/>
<ellipse cx="800" cy="790" rx="520" ry="55" fill="#000" opacity=".5" filter="url(#shadow-{uid})"/>
<g transform="translate(190 150) rotate(-3 610 270)">
 <rect x="25" y="35" width="1220" height="540" rx="44" fill="#000" opacity=".42" filter="url(#shadow-{uid})"/>
 <rect width="1220" height="540" rx="44" fill="url(#card-{uid})" stroke="#fff" stroke-opacity=".65" stroke-width="3"/>
 <rect x="34" y="34" width="1152" height="472" rx="30" fill="#07101a"/>
 <text x="82" y="108" fill="#fff" font-family="system-ui,sans-serif" font-size="25" font-weight="900" letter-spacing="3">꙰ SHIRMANI SUPREME DIGITAL PRODUCT</text>
 <text x="82" y="205" fill="#fff" font-family="system-ui,sans-serif" font-size="54" font-weight="900">{name}</text>
 <text x="82" y="254" fill="#8eeaff" font-family="system-ui,sans-serif" font-size="25" font-weight="700">{family} · {engine}</text>
 <rect x="82" y="302" width="330" height="62" rx="31" fill="#fff" fill-opacity=".09" stroke="#8eeaff" stroke-opacity=".4"/>
 <text x="115" y="342" fill="#fff" font-family="monospace" font-size="24" font-weight="900">{pid}</text>
 <rect x="82" y="402" width="430" height="60" rx="30" fill="hsl({hue} 90% 58%)" fill-opacity=".18" stroke="hsl({hue} 90% 70%)" stroke-opacity=".5"/>
 <text x="115" y="441" fill="#fff" font-family="system-ui,sans-serif" font-size="25" font-weight="900">{price_text}</text>
 <g transform="translate(930 325)"><rect width="190" height="130" rx="18" fill="#fff"/>
  <rect x="16" y="16" width="42" height="42" fill="#111"/><rect x="132" y="16" width="42" height="42" fill="#111"/><rect x="16" y="72" width="42" height="42" fill="#111"/>
  <path d="M78 16h18v18H78zM102 40h18v18h-18zM78 72h18v18H78zM102 96h18v18h-18zM132 72h18v18h-18z" fill="#111"/>
 </g>
 <text x="82" y="494" fill="#aeb9c8" font-family="system-ui,sans-serif" font-size="17" letter-spacing="2">UNIQUE IDENTITY · PRODUCT PASSPORT · QC / GATE / DISPATCH</text>
</g>
<text x="800" y="850" text-anchor="middle" fill="#fff" opacity=".82" font-family="system-ui,sans-serif" font-size="21" font-weight="800" letter-spacing="4">PREMIUM SHOWROOM VISUAL · 1600×900 · 16:9 · 4K-READY VECTOR MASTER</text>
</svg>'''

catalog=json.loads(CATALOG.read_text(encoding="utf-8"))
products=catalog.get("products",[])
for p in products:
    (OUT/f"{p['id']}.svg").write_text(svg(p),encoding="utf-8")

manifest={
 "generated_at":catalog.get("generated_at"),
 "visual_asset_count":len(products),
 "canvas":"1600x900",
 "aspect_ratio":"16:9",
 "format":"SVG",
 "purpose":"unique product identity visual for public showroom",
 "truth_boundary":"These are generated product identity masters; they are not photographic evidence, customer-use evidence, sale evidence, or scientific verification.",
 "assets":[{"id":p["id"],"visual":f"products/visuals/{p['id']}.svg"} for p in products]
}
(ROOT/"generated/product-visual-asset-manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"Materialized {len(products)} product visual masters in {OUT}")
