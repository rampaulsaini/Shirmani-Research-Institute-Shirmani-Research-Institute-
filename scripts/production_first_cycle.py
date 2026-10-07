#!/usr/bin/env python3
import json
from datetime import datetime,timezone
from pathlib import Path

root=Path(__file__).resolve().parents[1]
cat=json.loads((root/"generated/1000-digital-products.json").read_text(encoding="utf-8"))
products=cat.get("products",[])

priority={"AI Prompt Tools":1,"ML/NLP Tools":1,"Research":1,"Education":2,"Creator Tools":2,"Commerce":2,"Security & Quality":2,"Nature & Earth":2,"Quantum-Inspired":3}
goal={"AI Prompt Tools":"reusable prompt packs, examples and export","ML/NLP Tools":"real text/data transformations and repeatable examples","Research":"structured research workspaces and reproducible outputs","Education":"exercises, scoring, explanations and export","Creator Tools":"creation, preview, export and templates","Commerce":"catalogue, offers, order-intent and product copy","Security & Quality":"deterministic checks and remediation reports","Nature & Earth":"calculators, trackers and educational tools","Quantum-Inspired":"classical simulations with explicit boundaries"}

concrete_root=root/"products/concrete"
production_root=root/"products/production"

def public_route(p):
    pid=str(p.get("id",""))
    concrete=concrete_root/(pid+".html")
    production=production_root/(pid.lower()+".html")
    if concrete.is_file():
        return "products/concrete/"+pid+".html"
    if production.is_file():
        return "products/production/"+pid.lower()+".html"
    return p.get("artifact_url") or "products/1000-digital-product-factory.html?id="+pid

rows=[]
for p in products:
    f=p.get("family","")
    rows.append({
        "product_id":p.get("id"),
        "name":p.get("name"),
        "family":f,
        "engine":p.get("engine"),
        "priority":priority.get(f,4),
        "action":"DEPTH_UPGRADE",
        "goal":goal.get(f,"product-specific examples, richer inputs/outputs, export and customer guidance"),
        "public_route":public_route(p)
    })

rows.sort(key=lambda x:(x["priority"],x["family"],x["product_id"] or ""))

produced=sum(
    1 for p in products
    if p.get("status")=="PRODUCED_PUBLIC"
    or p.get("production_state")=="PRODUCED"
    or (concrete_root/(str(p.get("id"))+".html")).is_file()
    or (production_root/(str(p.get("id")).lower()+".html")).is_file()
)
priced=sum(1 for p in products if p.get("pricing_status")=="PUBLISHED_LAUNCH_PRICE")

payload={
    "schema_version":"1.1",
    "generated_at":datetime.now(timezone.utc).isoformat(),
    "mode":"PRODUCTION_FIRST",
    "pipeline":["INSTITUTE_RESEARCH","FACTORY_PRODUCTION","QC_GATE","PUBLIC_SHOWROOM_SALE"],
    "production":{
        "catalog_products":len(products),
        "produced_public":produced,
        "pricing_published":priced,
        "sold_evidence":sum(1 for p in products if p.get("commercial_status")=="SOLD"),
        "next_scale_target":5000,
        "remaining_to_scale_target":max(0,5000-produced)
    },
    "customer_loop":["DISCOVER","BUILD","QC/GATE","SHOW","USE","REVIEW/RATE","IMPROVE","BUILD_AGAIN"],
    "verification_boundary":"Independent verification is downstream and is not a substitute for production.",
    "next_work_units":rows[:100],
    "summary":{
        "families":len(cat.get("families",[])),
        "priority_units":sum(1 for x in rows[:100] if x["priority"]==1),
        "concrete_assets_detected":produced
    }
}
(root/"generated/production-operations-status.json").write_text(
    json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"
)
print("production operations state refreshed:",len(products),"catalog products,",produced,"produced public")
