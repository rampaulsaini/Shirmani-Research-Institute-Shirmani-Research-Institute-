#!/usr/bin/env python3
"""Build a truthful, machine-readable digital-product reality map.

Separates:
- executable family engines
- runnable product identities
- registered commercial offers
- independent verification / sales evidence

It never treats a workflow run as a sale or independent verification.
"""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
GEN=ROOT/"generated"
OUT=ROOT/"digital-product-reality-map.html"

def load(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default

def main():
    modes=load(GEN/"1000-digital-products.json", {})
    commercial=load(GEN/"product-catalog-public.json", {})
    verification=load(GEN/"VERIFICATION-REGISTRY.json", {})
    engines=len(modes.get("family_definitions", []))
    identities=int(modes.get("product_count", len(modes.get("products", []))))
    offers=len(commercial.get("offers", []))
    verified=int(verification.get("verified", 0))
    html=f"""<!doctype html><html lang="hi"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>SHIRMANI Digital Product Reality Map</title>
<style>
body{{margin:0;background:#071018;color:#eef5f8;font:16px system-ui;line-height:1.55}}
main{{max-width:1250px;margin:auto;padding:22px 14px 70px}}h1,h2{{color:#ffd84a}}
.hero,.card,.truth{{background:#101923;border:1px solid #354858;border-radius:18px;padding:18px;margin:12px 0}}
.hero{{border:2px solid #ffd84a}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}}
.num{{font-size:2rem;font-weight:900}}.ok{{color:#6ee7b7}}.warn{{color:#f6c453}}.bad{{color:#fb7185}}
table{{width:100%;border-collapse:collapse}}td,th{{padding:9px;border-bottom:1px solid #293747;text-align:left}}
a{{color:#67e8f9}}
</style></head><body><main>
<section class="hero"><h1>꙰ SHIRMANI — Digital Product Reality Map</h1>
<p><b>चार अलग स्तर:</b> engine → runnable identity → commercial offer → verified/sold outcome.</p>
<p>Generated from current repository records. Workflow activity is never counted as a sale or independent verification.</p></section>
<section class="grid">
<div class="card"><small>Executable family engines</small><div class="num">{engines:,}</div><div class="ok">engine layer</div></div>
<div class="card"><small>Runnable product identities</small><div class="num">{identities:,}</div><div class="ok">factory identity/assets layer</div></div>
<div class="card"><small>Registered commercial offers</small><div class="num">{offers:,}</div><div class="warn">catalog-ready</div></div>
<div class="card"><small>Independent VERIFIED</small><div class="num">{verified:,}</div><div class="bad">downstream review</div></div>
<div class="card"><small>Sales claimed</small><div class="num">0</div><div class="warn">transaction evidence required</div></div>
<div class="card"><small>Customer deliveries claimed</small><div class="num">0</div><div class="warn">delivery evidence required</div></div>
</section>
<section class="truth"><h2>25 / 1,016 = 2.46% — सही अर्थ</h2>
<p>यदि 25 executable engines को 1,016 runnable identities से divide करें तो 2.46% आता है। यह “केवल 2.46% product production” नहीं है। 1,016 identities पहले से generated हैं; 25 underlying family engines हैं।</p>
<table>
<tr><th>स्तर</th><th>वर्तमान अर्थ</th></tr>
<tr><td>Engine layer</td><td class="ok">{engines} executable families</td></tr>
<tr><td>Runnable identity layer</td><td class="ok">{identities} browser-runnable product modes/assets</td></tr>
<tr><td>Commercial layer</td><td class="warn">{offers} registered offers</td></tr>
<tr><td>Independent verification</td><td class="bad">{verified} verified records</td></tr>
<tr><td>Sales / delivery evidence</td><td class="bad">0 claimed unless transaction/delivery evidence exists</td></tr>
</table></section>
<section class="card"><h2>अब वास्तविक शेष काम</h2>
<ul>
<li>Selected product modes को meaningful feature/use-case/output से differentiate करना।</li>
<li>हर commercial product के लिए package, demo, license, delivery asset और support path पूरा करना।</li>
<li>External checkout/payment को वास्तविक transaction evidence से जोड़ना।</li>
<li>Payment → fulfilment → delivery proof → settlement → audit pipeline पूरा करना।</li>
<li>Research claims के लिए independent review को production से अलग रखना।</li>
</ul></section>
<section class="card"><h2>मुख्य pipeline</h2>
<p><b>{engines} Engines → {identities} Runnable Modes → Product Selection → Packaging → Checkout → Delivery → Evidence → Revenue</b></p>
<p><a href="products.html">Real Product Catalog</a> · <a href="products/production-launch-center.html">Product Launch Center</a> · <a href="production-dashboard.html">Production Dashboard</a></p>
</section>
</main></body></html>"""
    OUT.write_text(html,encoding="utf-8")
    print(json.dumps({"engines":engines,"runnable_identities":identities,"commercial_offers":offers,"independent_verified":verified},ensure_ascii=False))

if __name__=="__main__":
    main()
