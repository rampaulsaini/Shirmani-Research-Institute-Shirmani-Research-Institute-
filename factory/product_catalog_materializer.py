#!/usr/bin/env python3
from pathlib import Path
import json, html
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
catalog=json.loads((ROOT/"factory/product-catalog.json").read_text(encoding="utf-8"))
out=ROOT/"generated"; out.mkdir(exist_ok=True)
offers=[o|{"lane":lane["id"],"priority":lane["priority"]} for lane in catalog["lanes"] for o in lane["offers"]]

def reality_state(o):
    evidence=str(o.get("asset_evidence","")).upper()
    asset_path=o.get("asset_path")
    if asset_path and (ROOT/asset_path).exists():
        return "ASSET_READY"
    if evidence in {"VERIFIED_IN_REPOSITORY","GENERATED_CERTIFICATES_EXIST"}:
        return "EVIDENCE_DECLARED_ASSET_UNLOCATED"
    if o.get("delivery") in {"creative-service","service"}:
        return "SERVICE_INQUIRY"
    if evidence == "NOT_IN_REPOSITORY":
        return "OFFER_ONLY_ASSET_MISSING"
    return "NOT_READY"

for o in offers:
    o["reality_state"]=reality_state(o)
    o["production_claim"]="CONCRETE_DELIVERABLE" if o["reality_state"]=="ASSET_READY" else "PUBLIC_OFFER_ONLY"

counts={}
for o in offers:
    counts[o["reality_state"]]=counts.get(o["reality_state"],0)+1
ready=[o["id"] for o in offers if o["production_claim"]=="CONCRETE_DELIVERABLE"]

public={
    "schema_version":2,
    "mode":"REAL_PRODUCT_CATALOG_WITH_REALITY_GATE",
    "principle":"Catalog is not production. A product is concrete only when its deliverable asset or evidenced external delivery path is available.",
    "offer_count":len(offers),
    "concrete_deliverable_count":len(ready),
    "offer_only_or_missing_count":len(offers)-len(ready),
    "reality_counts":counts,
    "offers":offers,
}
(out/"product-catalog-public.json").write_text(json.dumps(public,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
(out/"product-reality-status.json").write_text(json.dumps({
    "generated_at":datetime.now(timezone.utc).isoformat(),
    "offer_count":len(offers),
    "concrete_deliverable_count":len(ready),
    "concrete_deliverable_ids":ready,
    "reality_counts":counts,
    "rule":"No offer is labeled production-ready merely because it has a price or an order link."
},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

cards=[]
for o in offers:
    paid="price_inr" in o
    state=o["reality_state"]
    if state=="ASSET_READY":
        status="PRODUCTION READY · ASSET EVIDENCED"
    elif state=="SERVICE_INQUIRY":
        status="SERVICE OFFER · INQUIRY REQUIRED"
    else:
        status="OFFER ONLY · DELIVERY ASSET MISSING"
    cta=o.get("store") or o.get("destination") or "https://wa.me/918082935186"
    label="Open delivery/order path" if state=="ASSET_READY" else ("Service inquiry" if state=="SERVICE_INQUIRY" else "Order path / add asset")
    price=(f"₹{o['price_inr']:,}" + (" · "+o["price_note"] if o.get("price_note") else "")) if paid else "Service"
    cards.append(f'<article class="card"><div class="tag">{html.escape(o["lane"])}</div><h2>{html.escape(o["name"])}</h2><div class="price">{price}</div><p>Reality state: <b>{html.escape(state)}</b></p><p class="status">{html.escape(status)}</p><a class="btn" href="{html.escape(cta)}" target="_blank" rel="noopener">{html.escape(label)}</a></article>')

page=f'''<!doctype html><html lang="hi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>SHIRMANI — Real Product Catalog</title><meta name="description" content="SHIRMANI product catalog with an explicit production reality gate."><style>
body{{margin:0;background:#080b11;color:#eef2f7;font-family:system-ui,sans-serif;line-height:1.55}}main{{max-width:1200px;margin:auto;padding:24px 16px 70px}}h1,h2{{color:#d4af37}}.hero,.card,.rule{{background:#111827;border:1px solid #334155;border-radius:16px;padding:18px}}.hero{{margin-bottom:18px}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}}.tag{{display:inline-block;border:1px solid #475569;border-radius:999px;padding:4px 8px;color:#67e8f9;font-size:.76rem}}.price{{font-size:1.25rem;font-weight:800;color:#f5d76e;margin:8px 0}}.status{{color:#6ee7b7;font-weight:700;font-size:.88rem}}.btn{{display:inline-block;background:#d4af37;color:#111;padding:10px 14px;border-radius:10px;text-decoration:none;font-weight:800;margin-top:10px}}.muted{{color:#aeb8c8}}a{{color:#67e8f9}}footer{{margin-top:24px;color:#aeb8c8}}.gate{{border-left:4px solid #67e8f9;padding:12px;background:#0d1522}}</style></head><body><main>
<section class="hero"><h1>꙰ SHIRMANI Real Product Catalog</h1><p><strong>{len(offers)} registered offers</strong> are separated by a production reality gate. <strong>{len(ready)}</strong> currently have repository-evidenced deliverable assets; the remaining entries are offers/services awaiting asset or external-delivery evidence.</p><div class="gate"><b>Reality rule:</b> price + order link ≠ production. Production-ready requires a concrete deliverable asset or evidenced delivery path.</div><p><a href="index.html">Main Hub</a> · <a href="public-production-results-hub.html">Production Results</a> · <a href="production/reality-first-status.html">Reality Dashboard</a> · <a href="generated/product-catalog-public.json">Machine-readable catalog</a></p></section>
<div class="grid">{''.join(cards)}</div>
<section class="rule" style="margin-top:20px"><h2>Production rule</h2><p>Product record → deliverable asset → product page → order/inquiry → delivery → delivery evidence → settlement → audit. Automission may prepare and publish the product layer; paid/external actions require authorized human/provider gates.</p></section>
<footer>Generated from <code>factory/product-catalog.json</code>. No fabricated sales or income.</footer>
</main></body></html>'''
(ROOT/"products.html").write_text(page,encoding="utf-8")
