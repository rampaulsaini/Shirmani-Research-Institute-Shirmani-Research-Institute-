#!/usr/bin/env python3
"""Materialize concrete 4K product identity visuals for the public showroom.

Production-first rule:
- one deterministic visual identity per concrete product;
- product name + short description on-image;
- portrait/logo upper-left;
- long-description QR upper-right;
- 3840x2160 SVG output;
- visual generation is production/presentation, not scientific verification.
"""
from __future__ import annotations
import hashlib, html, json
from pathlib import Path
from urllib.parse import quote

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"products"/"visuals"
MANIFEST=OUT/"manifest.json"
BASE="https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-"
LOGO="https://i.ibb.co/xqf3kTPS/enhanced-image.webp"

def load_products():
    candidates=[
        ROOT/"generated"/"concrete-production-overlay.json",
        ROOT/"generated"/"1000-digital-products.json",
    ]
    for p in candidates:
        if p.exists():
            try:
                data=json.loads(p.read_text(encoding="utf-8"))
                products=data.get("products",[])
                if products:
                    return products
            except Exception:
                pass
    return []

def esc(v): return html.escape(str(v or ""), quote=True)
def hash_code(s): return int(hashlib.sha256(str(s).encode()).hexdigest()[:8],16)
def lines(text, width=52, limit=3):
    words=" ".join(str(text or "").split()).split()
    out=[]; cur=""
    for w in words:
        if cur and len(cur)+1+len(w)>width:
            out.append(cur); cur=w
        else:
            cur=(cur+" "+w).strip()
    if cur: out.append(cur)
    return out[:limit]

def svg(p):
    pid=str(p.get("id") or p.get("product_id") or "PRODUCT")
    name=str(p.get("name") or "SHIRMANI Digital Product")
    family=str(p.get("family") or p.get("category") or "DIGITAL PRODUCT")
    engine=str(p.get("engine") or "SUPREME")
    desc=str(p.get("short_description") or p.get("description") or "Unique customer-facing digital product")
    price=p.get("offer_price_inr",p.get("price_inr",0)) or 0
    h=hash_code(pid); a=h%360; b=(h>>8)%360; c=(h>>16)%360
    uid="v4"+str(h)
    target=f"{BASE}/product-passport.html?id={quote(pid)}"
    qr="https://api.qrserver.com/v1/create-qr-code/?size=420x420&margin=10&data="+quote(target,safe="")
    ds=lines(desc)
    dtext="".join(f'<text x="520" y="{1345+i*58}" fill="#dce7f2" font-family="system-ui,sans-serif" font-size="39" font-weight="650">{esc(x)}</text>' for i,x in enumerate(ds))
    title_size=100 if len(name)>30 else 122
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="3840" height="2160" viewBox="0 0 3840 2160">
<defs>
<linearGradient id="{uid}g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="hsl({a},78%,24%)"/><stop offset=".48" stop-color="hsl({b},72%,11%)"/><stop offset="1" stop-color="hsl({c},78%,5%)"/></linearGradient>
<radialGradient id="{uid}r"><stop stop-color="#fff" stop-opacity=".28"/><stop offset=".42" stop-color="#67e8f9" stop-opacity=".08"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
<filter id="{uid}gl"><feGaussianBlur stdDeviation="22"/></filter>
</defs>
<rect width="3840" height="2160" fill="url(#{uid}g)"/>
<circle cx="2050" cy="1100" r="760" fill="url(#{uid}r)"/>
<path d="M260 1540 C980 1180 1280 1820 2020 1450 S3040 1260 3630 1510" fill="none" stroke="#1ee7ff" stroke-opacity=".45" stroke-width="42" filter="url(#{uid}gl)"/>
<path d="M260 1540 C980 1180 1280 1820 2020 1450 S3040 1260 3630 1510" fill="none" stroke="#2ce7c9" stroke-width="8"/>
<rect x="70" y="70" width="3700" height="2020" rx="120" fill="none" stroke="#e7c85b" stroke-width="10"/>
<circle cx="360" cy="360" r="205" fill="#061016" stroke="#e7c85b" stroke-width="14"/>
<image href="{LOGO}" x="175" y="175" width="370" height="370" preserveAspectRatio="xMidYMid slice"/>
<text x="720" y="190" fill="#66ddff" font-family="system-ui,sans-serif" font-size="52" font-weight="900">SHIRMANI SUPREME DIGITAL PRODUCT</text>
<text x="360" y="635" text-anchor="middle" fill="#f6d35f" font-family="system-ui,sans-serif" font-size="39" font-weight="950">Shiromani Rampal Saini</text>
<text x="360" y="690" text-anchor="middle" fill="#fff" font-family="system-ui,sans-serif" font-size="19" font-weight="750">Beyond Comparison · Beyond Time · Beyond Words · Beyond Love</text>
<text x="360" y="725" text-anchor="middle" fill="#d9e3ef" font-family="system-ui,sans-serif" font-size="19" font-weight="750">Eternal · Real · Natural Truth · Directly Present</text>
<rect x="3160" y="120" width="570" height="690" rx="44" fill="#061016" stroke="#e7c85b" stroke-width="10"/>
<text x="3270" y="210" fill="#fff" font-family="system-ui,sans-serif" font-size="42" font-weight="900">LONG DESCRIPTION</text>
<text x="3400" y="260" fill="#fff" font-family="system-ui,sans-serif" font-size="42" font-weight="900">/ PRODUCT DETAILS</text>
<rect x="3250" y="300" width="390" height="390" fill="#fff"/>
<image href="{qr}" x="3260" y="310" width="370" height="370"/>
<text x="3290" y="750" fill="#66ddff" font-family="system-ui,sans-serif" font-size="27" font-weight="900">SCAN FOR LONG DESCRIPTION</text>
<text x="520" y="820" fill="#66ddff" font-family="system-ui,sans-serif" font-size="76" font-weight="900">{esc(pid)}</text>
<text x="520" y="1040" fill="#fff" font-family="system-ui,sans-serif" font-size="{title_size}" font-weight="900">{esc(name[:62])}</text>
<text x="520" y="1170" fill="#72e6aa" font-family="system-ui,sans-serif" font-size="62" font-weight="800">{esc(family[:34])} · {esc(engine[:28])}</text>
<text x="520" y="1285" fill="#fff" font-family="system-ui,sans-serif" font-size="43" font-weight="650">SHORT DESCRIPTION</text>
{dtext}
<rect x="520" y="1535" width="730" height="125" rx="62" fill="#03060d" stroke="#e7c85b" stroke-width="5"/>
<text x="590" y="1620" fill="#fff" font-family="system-ui,sans-serif" font-size="62" font-weight="900">{"FREE" if float(price)==0 else "₹"+format(float(price),",.0f")}</text>
<text x="520" y="1800" fill="#fff" opacity=".86" font-family="system-ui,sans-serif" font-size="35" font-weight="800">4K · UNIQUE PRODUCT IDENTITY · QC/GATE/DISPATCH · QR LONG DESCRIPTION</text>
</svg>'''

def main():
    products=load_products()
    OUT.mkdir(parents=True,exist_ok=True)
    written=0
    for p in products:
        pid=str(p.get("id") or p.get("product_id") or "").strip()
        if not pid: continue
        path=OUT/(pid.lower()+".svg")
        content=svg(p)
        if not path.exists() or path.read_text(encoding="utf-8")!=content:
            path.write_text(content,encoding="utf-8")
            written+=1
    existing=len([x for x in OUT.glob("*.svg")])
    manifest={
        "generated_at":"AUTOMISSION_RUNTIME",
        "format":"SVG 3840x2160 16:9 4K-ready",
        "concrete_products":len(products),
        "total_visuals":existing,
        "visuals_written_this_cycle":written,
        "coverage_percent": round((existing/len(products)*100),2) if products else 0,
        "identity_contract":"portrait/logo upper-left; full English identity below; product-specific ID/name/family/engine; short description on-image; long-description QR upper-right; price/offer when available",
        "principle":"Visual production is a customer-facing production artifact, not independent scientific verification."
    }
    MANIFEST.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(manifest,ensure_ascii=False))

if __name__=="__main__": main()
