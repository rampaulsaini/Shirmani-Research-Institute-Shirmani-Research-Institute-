#!/usr/bin/env python3
import json, os, html
from datetime import datetime, timezone

src="production/generated/catalog.json"
out="production/showroom/index.html"
os.makedirs(os.path.dirname(out),exist_ok=True)
data=json.load(open(src,encoding="utf-8"))
products=data.get("products",[])

cards=[]
for p in products:
    cards.append(f"""
    <article class="card" data-category="{html.escape(p['category'])}">
      <div class="badge">{html.escape(p['category'])}</div>
      <h2>{html.escape(p['name'])}</h2>
      <p>{html.escape(p['description'])}</p>
      <div class="meta"><b>₹{p['price_inr']:,}</b> · {html.escape(p['offer'])}</div>
      <div class="qc">QC: {html.escape(p.get('qc_gate','QC-PENDING'))} · Dispatch: {html.escape(p.get('dispatch','NO'))}</div>
      <p class="small">Guarantee: {html.escape(p.get('guarantee','Digital delivery'))}</p>
      <a class="buy" href="{html.escape(p.get('purchase_url','#'))}" target="_blank" rel="noopener">View / Purchase</a>
    </article>""")

page=f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SHIRMANI Supreme Marking Hub — Public Showroom</title>
<style>
body{{margin:0;font-family:system-ui,sans-serif;background:#07111f;color:#eef4ff}}
header{{padding:42px 6%;background:linear-gradient(135deg,#101f38,#182d4d)}}
h1{{font-size:clamp(30px,5vw,58px);margin:0 0 12px}}
p{{line-height:1.6}} .controls{{padding:20px 6%;position:sticky;top:0;background:#07111fee;backdrop-filter:blur(10px)}}
select{{padding:12px;border-radius:10px}} .grid{{padding:30px 6%;display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:20px}}
.card{{background:#102039;border:1px solid #29405f;border-radius:18px;padding:22px;box-shadow:0 10px 30px #0004}}
.badge,.qc{{font-size:12px;letter-spacing:.05em;text-transform:uppercase;opacity:.8}}
.meta{{font-size:20px;margin:18px 0}} .small{{font-size:13px;opacity:.75}}
.buy{{display:inline-block;margin-top:12px;padding:11px 16px;border-radius:10px;background:#fff;color:#07111f;text-decoration:none;font-weight:700}}
</style></head>
<body>
<header><h1>꙰ SHIRMANI Supreme Marking Hub</h1>
<p>Production-first public showroom: discover → factory production → QC gate → public presentation → purchase.</p>
<p><b>{len(products)}</b> materialized products in the current showroom window. Production expands automatically every 5 minutes.</p></header>
<div class="controls"><label>Category: <select id="cat"><option>All</option></select></label></div>
<main class="grid" id="grid">{''.join(cards)}</main>
<script>
const cards=[...document.querySelectorAll('.card')], select=document.querySelector('#cat');
const cats=[...new Set(cards.map(x=>x.dataset.category))].sort();
cats.forEach(c=>{{const o=document.createElement('option');o.textContent=c;select.appendChild(o)}});
select.onchange=()=>cards.forEach(c=>c.style.display=(select.value==='All'||c.dataset.category===select.value)?'block':'none');
</script></body></html>"""
open(out,"w",encoding="utf-8").write(page)
