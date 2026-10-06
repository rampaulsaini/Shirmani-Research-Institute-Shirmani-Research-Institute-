#!/usr/bin/env python3
"""Synchronize concrete product assets into the public production/showroom layer."""
from __future__ import annotations
import json, hashlib
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; GEN=ROOT/"generated"; CAT=GEN/"1000-digital-products.json"; PROD=ROOT/"products"/"production"
def qc(pid): return "QC-PROD-"+hashlib.sha256((pid+"|SHIRMANI").encode()).hexdigest()[:12].upper()
def main():
    data=json.loads(CAT.read_text(encoding="utf-8")); products=data.get("products",[]); rows=[]; missing=[]
    for p in products:
        pid=p["id"]; asset=ROOT/(p.get("asset") or f"products/production/{pid.lower()}.html")
        if not asset.is_file(): missing.append(pid); continue
        rows.append({"id":pid,"production_state":"PRODUCED","sale_state":"READY_FOR_ORDER","artifact_url":str(asset.relative_to(ROOT)),"production_batch":"PUBLIC-PRODUCTION-SYNC","produced_at":datetime.now(timezone.utc).isoformat(),"qc_code":p.get("qc_code") or qc(pid),"gate_no":p.get("gate_no") or f"GATE-{int(pid.split('-')[-1]):04d}","dispatch_no":"NO","price_inr":p.get("price_inr"),"offer_price_inr":p.get("offer_price_inr"),"offer":p.get("offer"),"guarantee":p.get("guarantee"),"packing":p.get("packing")})
    stamp=datetime.now(timezone.utc).isoformat()
    overlay={"schema_version":2,"generated_at":stamp,"architecture":["INSTITUTE","FACTORY","QC","SHOWROOM_SALE"],"production_first":True,"verification_is_downstream":True,"product_count":len(products),"produced_count":len(rows),"remaining_count":len(products)-len(rows),"missing_asset_count":len(missing),"products":rows}
    (GEN/"concrete-production-overlay.json").write_text(json.dumps(overlay,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    registry={"schema_version":4,"generated_at":stamp,"architecture":["INSTITUTE","FACTORY","QC","SHOWROOM_SALE"],"production_first":True,"verification_is_downstream":True,"catalog_count":len(products),"produced_count":len(rows),"remaining_count":len(products)-len(rows),"engine_count":data.get("engine_count",0),"family_count":len(data.get("family_definitions",[])),"products":rows}
    (GEN/"production-registry.json").write_text(json.dumps(registry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    status={"generated_at":stamp,"catalog_count":len(products),"produced":len(rows),"remaining":len(products)-len(rows),"qc_ready":len(rows),"offered":len(rows),"dispatch_no":len(rows),"dispatch_yes":0,"production_first":True,"verification_scope":"DOWNSTREAM_PRODUCT_RESULT","missing_assets":missing[:1000]}
    (GEN/"production-status.json").write_text(json.dumps(status,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"catalog":len(products),"produced":len(rows),"remaining":len(products)-len(rows),"missing_assets":len(missing)}))
if __name__=="__main__": main()
