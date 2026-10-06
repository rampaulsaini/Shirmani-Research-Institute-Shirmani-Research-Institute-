#!/usr/bin/env python3
"""Production release gate for product traceability.

Creates a batch manifest from the canonical product catalog. It never marks a
missing asset as delivery-ready and never claims that a dispatch occurred.
"""
from __future__ import annotations
import hashlib, json, os
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"factory/product-catalog.json"
OUT=ROOT/"generated/production-release-manifest-100200.json"
BATCH=os.environ.get("PRODUCTION_BATCH_NO","100200")

def qc(pid,name):
    return "QC-"+hashlib.sha256(f"{pid}|{name}|SHIRMANI".encode()).hexdigest()[:12].upper()

def state(offer):
    evidence=offer.get("asset_evidence","")
    if offer.get("asset_path"):
        p=ROOT/offer["asset_path"]
        return "DELIVERY_READY" if p.is_file() and p.stat().st_size>0 else "ASSET_REQUIRED"
    if evidence=="GENERATED_CERTIFICATES_EXIST":
        certs=list((ROOT/"generated/certificates").glob("certificate-*.md"))
        return "DELIVERY_READY" if certs else "ASSET_REQUIRED"
    if offer.get("delivery")=="creative-service" or offer["id"].startswith("S"):
        return "SERVICE_INQUIRY"
    return "ASSET_REQUIRED"

def main():
    data=json.loads(CAT.read_text(encoding="utf-8"))
    products=[]; seq=0
    for lane in data.get("lanes",[]):
        for offer in lane.get("offers",[]):
            seq+=1
            pid=offer["id"]; name=offer["name"]
            q=qc(pid,name); gate=f"GATE-{seq:03d}"
            dispatch=f"SHR-{datetime.now(timezone.utc):%Y%m%d}-{pid}-D0001"
            st=state(offer)
            b=f"{BATCH}.{seq:03d}"
            payload=f"SHIRMANI|BATCH={b}|PRODUCT={pid}|QC={q}|GATE={gate}|DISPATCH={dispatch}|STATUS={st}"
            products.append({"product_id":pid,"name":name,"price_inr":offer.get("price_inr"),
              "delivery":offer.get("delivery"),"asset_evidence":offer.get("asset_evidence"),
              "batch_no":b,"qc_verification_code":q,"gate_no":gate,"dispatch_no":dispatch,
              "dispatch_status":"NOT_DISPATCHED","production_state":st,"qr_payload":payload})
    out={"schema_version":1,"generated_at":datetime.now(timezone.utc).isoformat(),
      "batch_no":BATCH,"sequence_rule":f"{BATCH}.001 starts the batch; .NNN increments per production unit.",
      "purpose":"Production trace record; QC/gate/dispatch fields do not imply dispatch or sale.",
      "products":products,
      "integrity":{"production_first":True,"verification_downstream":True,
                   "fabricated_sale_claim":False,"fabricated_dispatch_claim":False}}
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"batch":BATCH,"products":len(products),
      "delivery_ready":sum(x["production_state"]=="DELIVERY_READY" for x in products),
      "asset_required":sum(x["production_state"]=="ASSET_REQUIRED" for x in products),
      "service_inquiry":sum(x["production_state"]=="SERVICE_INQUIRY" for x in products)},ensure_ascii=False))
if __name__=="__main__":
    main()
