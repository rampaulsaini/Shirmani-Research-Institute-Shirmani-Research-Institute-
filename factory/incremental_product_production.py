#!/usr/bin/env python3
"""Incrementally materialize the next concrete SHIRMANI product batch."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import json, os
ROOT=Path(__file__).resolve().parents[1]
GEN=ROOT/"generated"; CAT=GEN/"canonical-5000-product-catalog.json"
OUT=ROOT/"products/production"; VIS=ROOT/"products/visuals"
LIVE=GEN/"live-production-state.json"; OVERLAY=GEN/"concrete-production-overlay.json"
LEDGER=GEN/"incremental-production-ledger.jsonl"
def load(p,d):
    try:return json.loads(p.read_text(encoding="utf-8"))
    except Exception:return d
def main():
    from factory.canonical_product_catalog import write_catalog
    write_catalog(CAT)
    target=max(5000,int(os.getenv("PRODUCT_TARGET","5000")))
    batch=max(1,min(1000,int(os.getenv("PRODUCTION_BATCH","500"))))
    catalog=load(CAT,{})
    products=catalog.get("products",[])
    if not products: raise SystemExit("No product catalogue")
    OUT.mkdir(parents=True,exist_ok=True); VIS.mkdir(parents=True,exist_ok=True)
    from factory.materialize_all_product_assets import make as make_product
    from factory.product_visual_identity_factory_v2 import make as make_visual
    before=sum((OUT/(str(p["id"]).lower()+".html")).is_file() for p in products)
    selected=[p for p in products if not (OUT/(str(p["id"]).lower()+".html")).is_file()][:batch]
    for p in selected:
        pid=str(p["id"])
        (OUT/(pid.lower()+".html")).write_text(make_product(p),encoding="utf-8")
        (VIS/(pid.lower()+".svg")).write_text(make_visual(p),encoding="utf-8")
    produced=sum((OUT/(str(p["id"]).lower()+".html")).is_file() for p in products)
    visuals=sum((VIS/(str(p["id"]).lower()+".svg")).is_file() for p in products)
    now=datetime.now(timezone.utc).isoformat()
    rows=[]
    for p in products:
        pid=str(p["id"])
        if (OUT/(pid.lower()+".html")).is_file():
            rows.append({"id":pid,"production_state":"PRODUCED","sale_state":"READY_FOR_ORDER",
                         "artifact_url":f"products/production/{pid.lower()}.html",
                         "qc_code":p.get("qc_code","QC-PENDING"),"gate_no":p.get("gate_no","GATE-PRODUCTION"),
                         "dispatch_no":"NO","production_batch":os.getenv("GITHUB_RUN_ID","LOCAL")})
    OVERLAY.write_text(json.dumps({"schema_version":2,"generated_at":now,
        "architecture":["INSTITUTE","FACTORY","QC_GATE","PUBLIC_SHOWROOM"],"production_first":True,
        "verification_is_downstream":True,"product_count":len(products),"produced_count":produced,
        "remaining_count":max(0,len(products)-produced),"batch_size":batch,"products":rows},
        ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    remaining=max(0,target-produced)
    LIVE.write_text(json.dumps({"schema_version":3,"generated_at":now,"production_first":True,
        "catalog_identities":len(products),"concrete_repository_assets":produced,
        "current_catalog_pending":max(0,len(products)-produced),"five_thousand_scale_target":target,
        "remaining_to_scale_target":remaining,
        "concrete_materialization_percent_of_catalog":round(100*produced/len(products),2),
        "concrete_materialization_percent_of_scale_target":round(100*produced/target,2),
        "module_products_generated":produced,"visual_assets_observed":visuals,
        "visual_coverage_of_produced":round(100*visuals/produced,2) if produced else 0,
        "last_batch_requested":batch,"last_batch_produced":len(selected),
        "dispatch_released":0,"sales_claimed":0,"payment_claimed":0,
        "independent_verification_claimed":0,
        "state":"PRODUCTION_COMPLETE_CURRENT_CATALOG" if produced>=len(products) else "PRODUCTION_IN_PROGRESS",
        "truth_boundary":"Production is observable from repository assets; QC, dispatch, payment, sales and independent verification are separate downstream states."
        },ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    with LEDGER.open("a",encoding="utf-8") as f:
        f.write(json.dumps({"generated_at":now,"run_id":os.getenv("GITHUB_RUN_ID"),
            "batch_size":batch,"produced_before":before,"produced_this_cycle":len(selected),
            "produced_after":produced,"remaining_to_5000":remaining,"visual_assets":visuals},
            ensure_ascii=False)+"\n")
    print(json.dumps({"produced_before":before,"produced_this_cycle":len(selected),
        "produced_after":produced,"remaining_to_5000":remaining,"visual_assets":visuals}))
if __name__=="__main__": main()
