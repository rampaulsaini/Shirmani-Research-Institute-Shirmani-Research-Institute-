#!/usr/bin/env python3
"""Deterministic product QC gate: structure, asset, QR passport and dispatch state."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; GEN=ROOT/"generated"
catalog=json.loads((GEN/"1000-digital-products.json").read_text(encoding="utf-8"))
products=catalog.get("products",[]); errors=[]; passed=0
required=["id","name","category","engine","asset","price_inr","offer_price_inr","qc_code","gate_no","dispatch_no","qr_payload","description","guarantee","packing"]
for p in products:
 missing=[k for k in required if k not in p or p[k] in ("",None)]
 asset=ROOT/p.get("asset",""); qr=str(p.get("qr_payload",""))
 tokens=[f"QC:{p.get('qc_code')}",f"GATE:{p.get('gate_no')}","DISPATCH:NO",f"PRICE:{p.get('offer_price_inr')}"]
 if missing: errors.append({"id":p.get("id"),"error":"missing_fields","fields":missing})
 if not asset.is_file(): errors.append({"id":p.get("id"),"error":"missing_asset","asset":p.get("asset")})
 for token in tokens:
  if token not in qr: errors.append({"id":p.get("id"),"error":"qr_missing","token":token})
 if not missing and asset.is_file() and all(t in qr for t in tokens): passed+=1
ids={e["id"] for e in errors}
payload={"generated_at":datetime.now(timezone.utc).isoformat(),"gate":"PRODUCT-QC-GATE","product_count":len(products),
 "qc_passed":passed,"qc_failed":len(ids),"pass_percent":round(passed/len(products)*100,2) if products else 0,
 "categories":len({p.get("category") for p in products}),"dispatch_default":"NO",
 "release_state":"QC_PASS_READY_FOR_DISPATCH" if not errors else "QC_REVIEW_REQUIRED",
 "checks":["catalog fields","browser asset","QR QC code","Gate No.","Dispatch No.","offer price","description","guarantee","packing"],
 "errors":errors[:500],"integrity":{"deterministic_qc":True,"independent_scientific_verification":False,"sale_claim":False}}
(GEN/"product-qc-gate.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,ensure_ascii=False))
if errors: raise SystemExit(1)
