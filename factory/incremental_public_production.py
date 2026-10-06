#!/usr/bin/env python3
"""Incremental public production: materialize a bounded batch of real product assets each cycle."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; GEN=ROOT/"generated"; PROD=ROOT/"products"/"production"; BATCH_SIZE=100
def load(path, default):
    try: return json.loads(path.read_text(encoding="utf-8"))
    except Exception: return default
def main():
    catalog=load(GEN/"1000-digital-products.json",{"products":[]}); products=catalog.get("products",[])
    overlay=load(GEN/"concrete-production-overlay.json",{"products":[]})
    existing={p.get("id"):p for p in overlay.get("products",[]) if p.get("production_state")=="PRODUCED"}
    pending=[p for p in products if p.get("id") not in existing]; batch=pending[:BATCH_SIZE]; PROD.mkdir(parents=True,exist_ok=True)
    for p in batch:
        pid=p["id"]; target=ROOT/(p.get("asset") or f"products/production/{pid.lower()}.html")
        if not target.is_file():
            from concrete_product_modules import page
            target.write_text(page(p),encoding="utf-8")
        existing[pid]={"id":pid,"production_state":"PRODUCED","sale_state":"READY_FOR_ORDER","artifact_url":str(target.relative_to(ROOT)),"production_batch":datetime.now(timezone.utc).strftime("%Y-%m-%d-batch"),"produced_at":datetime.now(timezone.utc).isoformat(),"qc_code":p.get("qc_code","QC-PENDING"),"gate_no":p.get("gate_no","GATE-PENDING"),"dispatch_no":"NO","price_inr":p.get("price_inr",0),"offer_price_inr":p.get("offer_price_inr",0),"offer":p.get("offer",""),"guarantee":p.get("guarantee",""),"packing":p.get("packing","")}
    rows=[existing[p["id"]] for p in products if p.get("id") in existing]; stamp=datetime.now(timezone.utc).isoformat()
    overlay={"schema_version":3,"generated_at":stamp,"architecture":["INSTITUTE","FACTORY","QC","SHOWROOM_SALE"],"production_first":True,"verification_is_downstream":True,"batch_size":BATCH_SIZE,"catalog_count":len(products),"produced_count":len(rows),"remaining_count":len(products)-len(rows),"cycle_produced_count":len(batch),"products":rows}
    (GEN/"concrete-production-overlay.json").write_text(json.dumps(overlay,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    registry={"schema_version":5,"generated_at":stamp,"architecture":["INSTITUTE","FACTORY","QC","SHOWROOM_SALE"],"production_first":True,"verification_is_downstream":True,"catalog_count":len(products),"produced_count":len(rows),"remaining_count":len(products)-len(rows),"engine_count":len({p.get("engine") for p in products}),"family_count":len({p.get("family") for p in products}),"products":rows}
    (GEN/"production-registry.json").write_text(json.dumps(registry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    status={"generated_at":stamp,"catalog_count":len(products),"produced":len(rows),"remaining":len(products)-len(rows),"cycle_produced":len(batch),"batch_size":BATCH_SIZE,"qc_ready":len(rows),"offered":len(rows),"dispatch_no":len(rows),"dispatch_yes":0,"production_first":True,"verification_scope":"DOWNSTREAM_PRODUCT_RESULT"}
    (GEN/"production-status.json").write_text(json.dumps(status,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"catalog":len(products),"produced":len(rows),"cycle_produced":len(batch),"remaining":len(products)-len(rows)}))
if __name__=="__main__": main()
