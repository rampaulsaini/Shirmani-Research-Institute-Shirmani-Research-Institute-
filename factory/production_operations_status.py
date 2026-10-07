#!/usr/bin/env python3
"""Publish production-first operational telemetry for the public showroom."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
GEN=ROOT/"generated"
CAT=GEN/"1000-digital-products.json"
OVERLAY=GEN/"concrete-production-overlay.json"
BATCH=GEN/"continuous-production-batch-status.json"
OUT=GEN/"production-operations-status.json"

def load(path, default):
    try: return json.loads(path.read_text(encoding="utf-8"))
    except Exception: return default

def main():
    catalog=load(CAT,{"products":[]})
    overlay=load(OVERLAY,{"products":[]})
    batch=load(BATCH,{})
    products=catalog.get("products",[])
    produced={x.get("id"):x for x in overlay.get("products",[]) if x.get("production_state")=="PRODUCED"}
    families=sorted({str(x.get("family") or "Unclassified") for x in products})
    lanes=sorted({(str(x.get("family") or "Unclassified"),str(x.get("engine") or "digital")) for x in products})
    pricing=sum(1 for x in products if float(x.get("offer_price_inr",x.get("price_inr",0)) or 0)>0)
    pending=[x for x in products if x.get("id") not in produced]
    target=5000
    produced_count=len(produced)
    next_units=[]
    for p in pending[:24]:
        next_units.append({
            "priority":1,"product_id":p.get("id"),"name":p.get("name"),
            "family":p.get("family"),"engine":p.get("engine"),
            "goal":"Materialize concrete product module and publish it to the public showroom.",
            "public_route":"products/1000-digital-product-factory.html?id="+str(p.get("id",""))
        })
    state={
      "schema_version":1,"generated_at":datetime.now(timezone.utc).isoformat(),
      "production":{
        "catalog_products":len(products),"produced_public":produced_count,
        "pricing_published":pricing,"sold_evidence":0,
        "next_scale_target":target,"production_lanes":len(lanes),
        "families":len(families),"module_products_generated":produced_count
      },
      "summary":{
        "priority_units":len(pending),"families":len(families),
        "production_lanes":len(lanes),"remaining_to_scale_target":max(0,target-produced_count)
      },
      "production_outputs":{
        "concrete_results_this_cycle":int(batch.get("produced_this_cycle",0)),
        "production_modules":produced_count
      },
      "scheduled_work_units":len(pending),
      "next_work_units":next_units,
      "principle":"Production first: research → factory → QC/gate → public showroom/sale. Reviews improve products; verification remains downstream.",
      "commercial_truth":"No sale or settlement is claimed without transaction evidence."
    }
    OUT.write_text(json.dumps(state,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"catalog":len(products),"produced":produced_count,"remaining":len(pending),"families":len(families),"lanes":len(lanes)},ensure_ascii=False))

if __name__=="__main__": main()
