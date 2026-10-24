#!/usr/bin/env python3
from pathlib import Path
import json, html
ROOT=Path(__file__).resolve().parents[1]
catalog=json.loads((ROOT/"factory/product-catalog.json").read_text(encoding="utf-8"))
out=ROOT/"generated"; out.mkdir(exist_ok=True)
offers=[o|{"lane":lane["id"],"priority":lane["priority"]} for lane in catalog["lanes"] for o in lane["offers"]]
public={"schema_version":1,"mode":"REAL_PRODUCT_CATALOG","principle":"A product record is not a completed sale; checkout/delivery must remain explicit.","offer_count":len(offers),"offers":offers}
(out/"product-catalog-public.json").write_text(json.dumps(public,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
cards=[]
for o in offers:
    price_value=float(o.get("price_inr",0) or 0)
    paid=price_value > 0
    evidence=o.get("asset_evidence","NOT_VERIFIED")
    verified_repo=evidence=="VERIFIED_IN_REPOSITORY"
    verified_external=evidence=="VERIFIED_EXTERNAL_STORE_MANIFEST"
    is_tool=o.get("delivery")=="browser-tool" and bool(o.get("asset_path")) and verified_repo
    is_free_resource=price_value==0 and bool(o.get("store") or o.get("asset_path")) and verified_repo

    if is_tool:
        status="TOOL AVAILABLE / OPEN IN BROWSER"
        cta=o["asset_path"]
        label="Open tool"
    elif is_free_resource:
        status="FREE RESOURCE / REPOSITORY ASSET"
        cta=o.get("store") or o.get("asset_path")
        label="Open free resource"
    elif paid and verified_external:
        status="LISTED IN EXTERNAL STORE / CONFIRM CURRENT AVAILABILITY"
        cta=o.get("store") or "https://wa.me/918082935186"
        label="Open external store"
    elif paid:
        status="INQUIRY ONLY / PRODUCT ASSET NOT VERIFIED"
        cta="https://wa.me/918082935186"
        label="Ask about availability"
    elif o.get("destination"):
        status="SERVICE PAGE / CONFIRM SCOPE AND PRICE"
        cta=o["destination"]
        label="View service page"
    else:
        status="SERVICE INQUIRY / QUOTE REQUIRED"
        cta="https://wa.me/918082935186"
        label="Ask for a quote"

    price=(f"₹{o['price_inr']:,}" + (" · "+o["price_note"] if o.get("price_note") else "")) if "price_inr" in o else "Service"
    cards.append(f'<article class="card"><div class="tag">{html.escape(o["lane"])}</div><h2>{html.escape(o["name"])}</h2><div class="price">{price}</div><p>Delivery: <b>{html.escape(o.get("delivery",""))}</b></p><p class="status">{status}</p><a class="btn" href="{html.escape(cta)}" target="_blank" rel="noopener">{label}</a></article>')
page=f'''<!doctype html><html lang="hi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SHIRMANI — Real Product Catalog</title><meta name="description" content="SHIRMANI real product and service catalog generated from the repository product registry."><style>
body{{margin:0;background:#080b11;color:#eef2f7;font-family:system-ui,sans-serif;line-height:1.55}}main{{max-width:1200px;margin:auto;padding:24px 16px 70px}}h1,h2{{color:#d4af37}}.hero,.card,.rule{{background:#111827;border:1px solid #334155;border-radius:16px;padding:18px}}.hero{{margin-bottom:18px}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}}.tag{{display:inline-block;border:1px solid #475569;border-radius:999px;padding:4px 8px;color:#67e8f9;font-size:.76rem}}.price{{font-size:1.25rem;font-weight:800;color:#f5d76e;margin:8px 0}}.status{{color:#6ee7b7;font-weight:700;font-size:.88rem}}.btn{{display:inline-block;background:#d4af37;color:#111;padding:10px 14px;border-radius:10px;text-decoration:none;font-weight:800;margin-top:10px}}.muted{{color:#aeb8c8}}a{{color:#67e8f9}}footer{{margin-top:24px;color:#aeb8c8}}</style></head><body><main>
<section class="hero"><h1>꙰ SHIRMANI Real Product Catalog</h1><p><strong>{len(offers)} registered offers</strong> are now represented as explicit product/service records. This is the bridge from “showroom architecture” to concrete offerings.</p><p class="muted">Paid checkout remains external until a payment provider is explicitly connected. A catalog entry is not a claim that a sale has already occurred.</p><p><a href="index.html">Main Hub</a> · <a href="public-production-results-hub.html">Production Results</a> · <a href="generated/product-catalog-public.json">Machine-readable catalog</a></p></section>
<div class="grid">{''.join(cards)}</div>
<section class="rule" style="margin-top:20px"><h2>Production rule</h2><p>Product record → product page → order/inquiry → delivery → delivery evidence → settlement → audit. Automission may prepare and publish the product layer; paid/external actions require authorized human/provider gates.</p></section>
<footer>Generated from <code>factory/product-catalog.json</code>. Source-bound catalog; no fabricated sales or income.</footer>
</main></body></html>'''
(ROOT/"products.html").write_text(page,encoding="utf-8")
