#!/usr/bin/env python3
"""Generate scalable product identity masters from the concrete product passport registry."""
import json,html,pathlib,re,hashlib,urllib.parse,base64,io
import qrcode
ROOT=pathlib.Path(__file__).resolve().parents[1]
CATALOG=ROOT/"showroom-products.json"
PASSPORTS=ROOT/"generated/PRODUCT-PASSPORTS.jsonl"
OUT=ROOT/"products/visuals"; OUT.mkdir(parents=True,exist_ok=True)
BASE="https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/"
def esc(x): return html.escape(str(x or ""))
def slug(x): return re.sub(r"[^a-z0-9]+","-",str(x).lower()).strip("-")
def products():
    seen={}
    if CATALOG.exists():
        for p in json.loads(CATALOG.read_text(encoding="utf-8")).get("products",[]): seen[str(p.get("id"))]=p
    if PASSPORTS.exists():
        for line in PASSPORTS.read_text(encoding="utf-8").splitlines():
            if line.strip():
                p=json.loads(line); seen[str(p["id"])]=p
    return list(seen.values())
items=products()
for p in items:
    pid=str(p.get("id","PRODUCT")); name=str(p.get("name","Digital Product"))
    desc=str(p.get("description","Public digital product")); cat=str(p.get("category","digital"))
    price=p.get("offer_price_inr",p.get("price_inr")); qc=p.get("qc_code","QC-NOT-SET"); gate=p.get("gate_no","GATE-NOT-SET")
    artifact=p.get("asset") or p.get("artifact_url") or p.get("store_url") or ""
    public_url=urllib.parse.urljoin(BASE,artifact)
    digest=hashlib.sha256((pid+"|"+name).encode()).hexdigest(); accent="#"+digest[:6]
    qr=qrcode.QRCode(version=None,box_size=10,border=2); qr.add_data(public_url); qr.make(fit=True)
    qr_bytes=io.BytesIO(); qr.make_image().save(qr_bytes,format="PNG"); qr_b64=base64.b64encode(qr_bytes.getvalue()).decode()
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="3840" height="2160" viewBox="0 0 3840 2160" role="img">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#07111f"/><stop offset=".55" stop-color="{accent}"/><stop offset="1" stop-color="#05070d"/></linearGradient></defs>
<rect width="3840" height="2160" fill="#05070d"/><rect x="80" y="80" width="3680" height="2000" rx="70" fill="url(#g)" stroke="#e8c65b" stroke-width="8"/>
<circle cx="340" cy="330" r="150" fill="#0a0f18" stroke="#e8c65b" stroke-width="8"/><text x="340" y="365" text-anchor="middle" font-family="sans-serif" font-size="170" font-weight="900" fill="#e8c65b">꙰</text>
<text x="570" y="245" font-family="sans-serif" font-size="72" font-weight="800" fill="#62e6ff">SHIRMANI DIGITAL PRODUCT</text>
<text x="570" y="410" font-family="sans-serif" font-size="135" font-weight="950" fill="#fff">{esc(name)[:52]}</text>
<text x="570" y="535" font-family="sans-serif" font-size="58" fill="#d9e3ef">CATEGORY · {esc(cat).upper()} · ID · {esc(pid)}</text>
<rect x="570" y="700" width="2500" height="410" rx="40" fill="#05070d" fill-opacity=".58" stroke="#fff" stroke-opacity=".18"/>
<text x="660" y="815" font-family="sans-serif" font-size="62" fill="#fff">{esc(desc)[:74]}</text>
<text x="660" y="910" font-family="sans-serif" font-size="54" fill="#d9e3ef">{esc(desc)[74:148]}</text>
<text x="660" y="1020" font-family="sans-serif" font-size="52" fill="#62e6ff">PRICE ₹{esc(price)} · OFFER {esc(p.get("offer",""))}</text>
<text x="660" y="1260" font-family="sans-serif" font-size="54" fill="#fff">QC · {esc(qc)}   GATE · {esc(gate)}   DISPATCH · {esc(p.get("dispatch_no","NO"))}</text>
<text x="660" y="1430" font-family="sans-serif" font-size="82" font-weight="950" fill="#e8c65b">OPEN PRODUCT →</text>
<text x="660" y="1760" font-family="sans-serif" font-size="50" fill="#fff">Short description + identity on visual · QR route to full product description</text>
<rect x="2880" y="1300" width="540" height="540" rx="24" fill="#fff"/><image x="2900" y="1320" width="500" height="500" href="data:image/png;base64,{qr_b64}"/>
<text x="2920" y="1910" font-family="sans-serif" font-size="40" fill="#d9e3ef">Author mark · शिरोमणि रामपॉल सैनी</text>
<text x="2920" y="1975" font-family="sans-serif" font-size="34" fill="#d9e3ef">3840×2160 vector master · resolution independent</text></svg>'''
    (OUT/(slug(pid)+".svg")).write_text(svg,encoding="utf-8")
print("generated",len(items),"product identity masters")
