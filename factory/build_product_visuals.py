#!/usr/bin/env python3
"""Build deterministic, 4K-ready SVG product identity cards for the public showroom.
SVG is vector and resolution-independent. The author mark is a text/icon mark,
not a photographic likeness, until an authorized source portrait is supplied.
"""
import json,html,pathlib,re,hashlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
data=json.loads((ROOT/"showroom-products.json").read_text(encoding="utf-8"))
out=ROOT/"products/visuals"; out.mkdir(parents=True,exist_ok=True)
def esc(x): return html.escape(str(x or ""))
def slug(x): return re.sub(r"[^a-z0-9]+","-",str(x).lower()).strip("-")
for p in data.get("products",[]):
    pid=str(p.get("id","PRODUCT")); name=str(p.get("name","Digital Product"))
    desc=str(p.get("description","Public digital product")); cat=str(p.get("category","digital"))
    digest=hashlib.sha256((pid+"|"+name).encode()).hexdigest(); accent="#"+digest[:6]
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="3840" height="2160" viewBox="0 0 3840 2160" role="img">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#07111f"/><stop offset=".55" stop-color="{accent}"/><stop offset="1" stop-color="#05070d"/></linearGradient></defs>
<rect width="3840" height="2160" fill="#05070d"/><rect x="80" y="80" width="3680" height="2000" rx="70" fill="url(#g)" stroke="#e8c65b" stroke-width="8"/>
<circle cx="340" cy="330" r="150" fill="#0a0f18" stroke="#e8c65b" stroke-width="8"/><text x="340" y="365" text-anchor="middle" font-family="sans-serif" font-size="170" font-weight="900" fill="#e8c65b">꙰</text>
<text x="570" y="245" font-family="sans-serif" font-size="72" font-weight="800" fill="#62e6ff">SHIRMANI DIGITAL PRODUCT</text>
<text x="570" y="410" font-family="sans-serif" font-size="150" font-weight="950" fill="#fff">{esc(name)[:48]}</text>
<text x="570" y="540" font-family="sans-serif" font-size="62" fill="#d9e3ef">CATEGORY · {esc(cat).upper()}</text>
<rect x="570" y="700" width="2700" height="420" rx="40" fill="#05070d" fill-opacity=".55" stroke="#fff" stroke-opacity=".18"/>
<text x="660" y="830" font-family="sans-serif" font-size="68" fill="#fff">{esc(desc)[:78]}</text>
<text x="660" y="930" font-family="sans-serif" font-size="58" fill="#d9e3ef">{esc(desc)[78:156]}</text>
<text x="660" y="1040" font-family="sans-serif" font-size="54" fill="#62e6ff">PRODUCT ID · {esc(pid)}</text>
<text x="660" y="1450" font-family="sans-serif" font-size="92" font-weight="950" fill="#e8c65b">OPEN PRODUCT →</text>
<text x="660" y="1770" font-family="sans-serif" font-size="55" fill="#fff">Short description on visual · Full description + QR route on product page</text>
<text x="2920" y="1770" text-anchor="middle" font-family="sans-serif" font-size="42" fill="#d9e3ef">Author mark</text>
<text x="2920" y="1840" text-anchor="middle" font-family="sans-serif" font-size="44" font-weight="700" fill="#fff">शिरोमणि रामपॉल सैनी</text>
<text x="2920" y="1960" text-anchor="middle" font-family="sans-serif" font-size="38" fill="#d9e3ef">3840×2160 vector master · scalable beyond 4K</text></svg>'''
    (out/(slug(pid)+".svg")).write_text(svg,encoding="utf-8")
print("generated",len(data.get("products",[])),"visual identities")
