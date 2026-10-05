#!/usr/bin/env python3
"""SHIRMANI production truth gate.

Counts only observable repository artifacts and explicit product routes.
It never converts workflow runs into sales, delivery, accreditation,
currency deployment, or independent verification.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
GEN=ROOT/"generated"
CATALOG=GEN/"product-catalog-public.json"
RESULTS=GEN/"production-results.jsonl"
VERIFICATION=GEN/"VERIFICATION-REGISTRY.json"
OUT=GEN/"PRODUCTION-TRUTH.json"

def count_lines(p):
    if not p.exists(): return 0
    return sum(1 for x in p.read_text(encoding="utf-8",errors="ignore").splitlines() if x.strip())

def main():
    catalog=json.loads(CATALOG.read_text(encoding="utf-8")) if CATALOG.exists() else {"offers":[]}
    verification=json.loads(VERIFICATION.read_text(encoding="utf-8")) if VERIFICATION.exists() else {}
    offers=catalog.get("offers",[])
    result_count=count_lines(RESULTS)
    digital=sum(1 for x in offers if x.get("delivery") in {"digital-audio","digital-asset","creator-assets"})
    services=sum(1 for x in offers if x.get("delivery") in {"service","creative-service"})
    payload={
      "generated_at":datetime.now(timezone.utc).isoformat(),
      "truth_model":"OBSERVABLE_PRODUCTION_ONLY",
      "offers_registered":len(offers),
      "digital_offers":digital,
      "service_offers":services,
      "persistent_production_records":result_count,
      "independent_verified_records":int(verification.get("verified",0)),
      "sales_claimed":0,
      "delivered_customer_orders_claimed":0,
      "institutional_accreditation_claimed":False,
      "court_authority_claimed":False,
      "currency_contract_deployed_claimed":False,
      "gates":{
        "catalog":"READY" if offers else "MISSING",
        "production_records":"ACTIVE" if result_count else "NOT_PERSISTED",
        "commercial_transaction":"EVIDENCE_REQUIRED",
        "delivery":"EVIDENCE_REQUIRED",
        "independent_verification":"DOWNSTREAM"
      },
      "rule":"A workflow run, catalog entry, generated card or public page is not a sale, delivery, accreditation, court authority, currency deployment or independent verification."
    }
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,ensure_ascii=False))

if __name__=="__main__":
    main()
