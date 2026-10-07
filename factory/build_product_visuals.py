#!/usr/bin/env python3
"""Generate scalable product identity masters from the concrete product passport registry."""
import json,html,pathlib,re,hashlib,urllib.parse,base64,io
import qrcode
ROOT=pathlib.Path(__file__).resolve().parents[1]
CATALOG=ROOT/"showroom-products.json"
PASSPORTS=ROOT/"generated/PRODUCT-PASSPORTS.jsonl"
OUT=ROOT/"products/visuals"; OUT.mkdir(parents=True,exist_ok=True)
BASE="https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/"
LOGO="https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/assets/shirmani-perspective-logo.svg"
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
<circle cx="340" cy="330" r="150" fill="#0a0f18" stroke="#e8c65b" stroke-width="8"/><image href="{LOGO}" x="205" y="195" width="270" height="270" preserveAspectRatio="xMidYMid slice"/>
<text x="340" y="535" text-anchor="middle" font-family="sans-serif" font-size="34" font-weight="900" fill="#e8c65b">Shiromani Rampal Saini</text>
<text x="340" y="575" text-anchor="middle" font-family="sans-serif" font-size="17" font-weight="700" fill="#fff">NISHPAKSH UNDERSTANDING · SHIRMANI HEART-VIEW</text>
<text x="340" y="606" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#d9e3ef">Beyond Comparison · Beyond Time · Beyond Words · Beyond Love</text>
<text x="340" y="632" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="700" fill="#d9e3ef">Eternal · Real · Natural Truth · Directly Present</text>
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
<rect x="2920" y="120" width="620" height="650" rx="28" fill="#061016" stroke="#e8c65b" stroke-width="8"/><text x="3020" y="205" font-family="sans-serif" font-size="42" font-weight="900" fill="#fff">LONG DESCRIPTION</text><text x="3100" y="255" font-family="sans-serif" font-size="42" font-weight="900" fill="#fff">/ PRODUCT DETAILS</text><rect x="3025" y="295" width="410" height="410" fill="#fff"/><image x="3035" y="305" width="390" height="390" href="data:image/png;base64,{qr_b64}"/>
<text x="2920" y="1900" font-family="sans-serif" font-size="34" fill="#d9e3ef">Shiromani Rampal Saini · Product Identity</text>
<text x="2920" y="1960" font-family="sans-serif" font-size="30" fill="#d9e3ef">3840×2160 vector master · resolution independent</text></svg>'''
    (OUT/(slug(pid)+".svg")).write_text(svg,encoding="utf-8")
print("generated",len(items),"product identity masters")
