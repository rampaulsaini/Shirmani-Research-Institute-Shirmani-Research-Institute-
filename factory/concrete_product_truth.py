#!/usr/bin/env python3
"""Concrete product truth audit: only distinct non-empty repository assets count."""
import json
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
GEN=ROOT/"generated"; CAT=GEN/"1000-digital-products.json"; ASSET_DIR=ROOT/"products/concrete"
OUT=GEN/"concrete-product-truth.json"; STATUS=GEN/"concrete-product-production-status.json"; OVERLAY=GEN/"concrete-production-overlay.json"
def main():
    catalog=json.loads(CAT.read_text(encoding="utf-8")); products=catalog.get("products",[])
    overlay=json.loads(OVERLAY.read_text(encoding="utf-8")) if OVERLAY.exists() else {"products":[]}
    claimed={x.get("id") for x in overlay.get("products",[]) if x.get("id")}
    rows=[]; concrete=0
    for p in products:
        pid=p["id"]; asset=ASSET_DIR/f"{pid}.html"; exists=asset.is_file() and asset.stat().st_size>=100
        if exists: concrete+=1
        rows.append({"id":pid,"name":p.get("name"),"family":p.get("family"),"engine":p.get("engine"),
                     "asset":f"products/concrete/{pid}.html","asset_exists":exists,
                     "asset_bytes":asset.stat().st_size if asset.is_file() else 0,
                     "overlay_claimed":pid in claimed,"state":"CONCRETE_PRODUCED" if exists else "NOT_YET_CONCRETE"})
    target=len(products); ts=datetime.now(timezone.utc).isoformat()
    payload={"schema_version":1,"generated_at":ts,"truth_model":"DISTINCT_REPOSITORY_ASSET_REQUIRED",
             "catalog_count":target,"concrete_produced":concrete,"remaining":target-concrete,
             "concrete_production_percent":round(100*concrete/target,2) if target else 0,
             "overlay_claimed":len(claimed),"overlay_only_gap":max(0,len(claimed)-concrete),
             "asset_directory":"products/concrete/","rule":"Only an existing non-empty product-specific repository asset counts as concrete production.",
             "sales_claimed":0,"payment_claimed":0,"independent_verification_claimed":0,"products":rows}
    GEN.mkdir(exist_ok=True); OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    STATUS.write_text(json.dumps({"generated_at":ts,"target":target,"concrete_produced":concrete,
      "concrete_production_percent":payload["concrete_production_percent"],"remaining":target-concrete,
      "overlay_claimed":len(claimed),"overlay_only_gap":payload["overlay_only_gap"],
      "status":"COMPLETE" if concrete==target else "IN_PROGRESS",
      "next_layer":"QC → packaging → commercial listing → delivery evidence → independent review"},
      ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:payload[k] for k in ("catalog_count","concrete_produced","remaining","concrete_production_percent","overlay_claimed","overlay_only_gap")},ensure_ascii=False))
if __name__=="__main__": main()
