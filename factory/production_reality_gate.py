#!/usr/bin/env python3
"""Reality gate: distinguish architecture/catalog from actual deliverable production."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"factory/product-catalog.json"
OUT=ROOT/"generated/production-reality-gate.json"
data=json.loads(CAT.read_text(encoding="utf-8"))
rows=[]
for lane in data.get("lanes",[]):
    for offer in lane.get("offers",[]):
        state="SERVICE_INQUIRY" if offer["id"].startswith("S") else "NOT_VERIFIED"
        if offer.get("asset_path"):
            p=ROOT/offer["asset_path"]
            state="ASSET_VERIFIED" if p.exists() and p.is_file() and p.stat().st_size>0 else "ASSET_MISSING"
        elif offer.get("asset_evidence")=="GENERATED_CERTIFICATES_EXIST":
            certs=list((ROOT/"generated/certificates").glob("certificate-*.md"))
            state="ASSET_VERIFIED" if certs else "ASSET_MISSING"
        elif offer.get("store"):
            state="EXTERNAL_PATH_UNVERIFIED"
        rows.append({"id":offer["id"],"name":offer["name"],"lane":lane["id"],"state":state,
                     "paid":offer.get("price_inr",0)>0,
                     "delivery_asset":offer.get("asset_path"),
                     "checkout_path":offer.get("store") or offer.get("destination")})
counts={}
for r in rows: counts[r["state"]]=counts.get(r["state"],0)+1
payload={"schema_version":1,"principle":"A workflow run is not a product sale; a catalog record is not delivery evidence.",
         "generated_from":"factory/product-catalog.json","offer_count":len(rows),"states":counts,"offers":rows,
         "launch_rule":"Only ASSET_VERIFIED may be labeled DELIVERY_READY. EXTERNAL_PATH_UNVERIFIED requires external delivery evidence. Paid offers without verified delivery assets remain blocked.",
         "independent_verification":"NOT_CLAIMED"}
OUT.parent.mkdir(exist_ok=True); OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"
",encoding="utf-8")
print(json.dumps({"offer_count":len(rows),"states":counts},ensure_ascii=False))
