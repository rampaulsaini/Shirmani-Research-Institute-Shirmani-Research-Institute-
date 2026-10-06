#!/usr/bin/env python3
"""SHIRMANI production reconciliation: catalog -> concrete asset -> priced showroom registry."""
from __future__ import annotations
import json, hashlib
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; GEN=ROOT/"generated"; CATALOG=GEN/"1000-digital-products.json"
def digest(v): return hashlib.sha256(v.encode()).hexdigest()[:16].upper()
def main():
    data=json.loads(CATALOG.read_text(encoding="utf-8")); products=data.get("products",[]); rows=[]
    for i,p in enumerate(products,1):
        pid=p["id"]; asset=ROOT/p.get("asset",f"products/production/{pid.lower()}.html"); produced=asset.is_file()
        price=int(p.get("price_inr") or 0); offer=int(p.get("offer_price_inr") or 0); qc=p.get("qc_code") or "QC-PENDING"; gate=p.get("gate_no") or f"GATE-{i:04d}"
        rows.append({"id":pid,"name":p.get("name"),"family":p.get("family"),"category":p.get("category"),"engine":p.get("engine"),"unit_no":f"PROD-{i:06d}","qc_code":qc,"gate_no":gate,"dispatch_no":"NO","price_inr":price,"offer_price_inr":offer,"offer":p.get("offer","LAUNCH OFFER"),"description":p.get("description",""),"guarantee":p.get("guarantee","7-day digital quality correction window"),"packing":p.get("packing","SUPREME DIGITAL PRIME PACK"),"production_state":"PRODUCED" if produced else "QUEUED","asset_exists":produced,"production_url":p.get("asset",f"products/production/{pid.lower()}.html"),"showroom_url":f"supreme-showroom.html?id={pid}","passport_url":f"supreme-marking-hub.html?id={pid}","qr_payload":f"{pid}|QC:{qc}|GATE:{gate}|DISPATCH:NO|PRICE:{offer}","production_fingerprint":digest(pid+"|"+str(p.get("asset"))+"|"+str(price)+"|"+str(offer))})
    now=datetime.now(timezone.utc).isoformat(); produced=sum(r["asset_exists"] for r in rows)
    payload={"schema_version":3,"generated_at":now,"architecture":["INSTITUTE","FACTORY","QC","SHOWROOM_SALE"],"production_first":True,"verification_is_downstream":True,"catalog_count":len(rows),"produced_count":produced,"remaining_count":len(rows)-produced,"price_ready_count":sum(r["offer_price_inr"]>0 for r in rows),"dispatch_released":0,"products":rows,"integrity":{"asset_existence_checked":True,"price_source":"generated/1000-digital-products.json","verification_claim":False}}
    (GEN/"production-registry.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    fees={"generated_at":now,"showroom_entry_fee":{"currency":"INR","pricing_mode":"time_based","tiers":[{"minutes":15,"price_inr":499},{"minutes":30,"price_inr":899},{"minutes":60,"price_inr":1499},{"minutes":120,"price_inr":2499},{"minutes":180,"price_inr":3499},{"minutes":300,"price_inr":4999}],"note":"Entry fee is separate from product price; payment integration is not claimed live."},"production_rule":"Product price and showroom entry fee are separate commercial layers."}
    (GEN/"showroom-entry-fees.json").write_text(json.dumps(fees,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"catalog":len(rows),"produced":produced,"remaining":len(rows)-produced,"priced":payload["price_ready_count"]},ensure_ascii=False))
if __name__=="__main__": main()
