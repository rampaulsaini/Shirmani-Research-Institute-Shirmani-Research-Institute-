#!/usr/bin/env python3
"""Build a truthful, product-first production manifest.

Only real repository assets or explicitly configured external delivery paths
become publishable candidates. Verification remains downstream.
"""
from pathlib import Path
import json
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
CATALOG=ROOT/"factory"/"product-catalog.json"
OUT=ROOT/"generated"/"public-product-production-manifest.json"

def asset_state(o):
    p=o.get("asset_path")
    if p and (ROOT/p).exists():
        return "ASSET_READY"
    evidence=o.get("asset_evidence","")
    if evidence=="VERIFIED_IN_REPOSITORY":
        return "ASSET_READY" if p and (ROOT/p).exists() else "EVIDENCE_PATH_MISSING"
    if o.get("destination") or o.get("store"):
        return "EXTERNAL_DELIVERY_PATH"
    if o.get("delivery") in {"service","creative-service"}:
        return "SERVICE_PRODUCT"
    return "ASSET_MISSING"

def main():
    catalog=json.loads(CATALOG.read_text(encoding="utf-8"))
    rows=[]
    for lane in catalog.get("lanes",[]):
        for offer in lane.get("offers",[]):
            state=asset_state(offer)
            rows.append({
                "id":offer["id"],"lane":lane["id"],"name":offer["name"],
                "price_inr":offer.get("price_inr"),"delivery":offer.get("delivery"),
                "asset_path":offer.get("asset_path"),"store":offer.get("store"),
                "destination":offer.get("destination"),
                "production_state":state,
                "publish_candidate":state in {"ASSET_READY","EXTERNAL_DELIVERY_PATH"},
                "verification_stage":"DOWNSTREAM"
            })
    counts={}
    for r in rows: counts[r["production_state"]]=counts.get(r["production_state"],0)+1
    payload={
        "version":1,"generated_at":datetime.now(timezone.utc).isoformat(),
        "principle":"PRODUCTION_FIRST_WITH_REALITY_GATE",
        "total_product_records":len(rows),
        "publishable_candidates":sum(1 for r in rows if r["publish_candidate"]),
        "counts":counts,"verification_is_downstream":True,"products":rows
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"total_product_records":len(rows),"publishable_candidates":payload["publishable_candidates"],"counts":counts},ensure_ascii=False))

if __name__=="__main__": main()
