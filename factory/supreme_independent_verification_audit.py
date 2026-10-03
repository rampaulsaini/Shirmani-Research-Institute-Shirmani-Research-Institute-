#!/usr/bin/env python3
"""Deterministic audit of independent-verification states.

Observes existing machine-readable records only. Never promotes a record to
VERIFIED and never treats workflow success, QC PASS, or confidence as proof.
"""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[1]
GENERATED=ROOT/"generated"
OUT=GENERATED/"supreme-independent-verification-audit.json"
STATES={"REGISTERED","UNVERIFIED","REVIEW","VERIFIED","BLOCKED"}
VERIFICATION_KEYS=("verification_evidence","independent_verification","verification_record","verification_report")

def digest(value:Any)->str:
    raw=json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(",",":"))
    return hashlib.sha256(raw.encode()).hexdigest()

def load_records():
    records=[]
    if not GENERATED.exists(): return records
    for path in sorted(GENERATED.rglob("*.json")):
        if path.resolve()==OUT.resolve(): continue
        try: data=json.loads(path.read_text(encoding="utf-8"))
        except (OSError,json.JSONDecodeError): continue
        for item in (data if isinstance(data,list) else [data]):
            if isinstance(item,dict) and isinstance(item.get("verification_state"),str):
                records.append((str(path.relative_to(ROOT)),item))
    return records

def has_verification_evidence(record):
    return any(record.get(k) not in (None,"",[],{}) for k in VERIFICATION_KEYS)

def main():
    records=load_records()
    counts={s:0 for s in sorted(STATES)}
    unknown=[]; missing=[]
    for path,record in records:
        state=record["verification_state"]
        if state not in STATES:
            unknown.append(f"{path}:{state}"); continue
        counts[state]+=1
        if state=="VERIFIED" and not has_verification_evidence(record):
            missing.append(path)
    report={
      "schema_version":"1.0",
      "event_id":"independent-verification-audit-"+datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
      "timestamp":datetime.now(timezone.utc).isoformat(),
      "repository":"rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-",
      "records_scanned":len(records),
      "verification_counts":counts,
      "independent_verified_count":counts["VERIFIED"],
      "verified_records_with_evidence":counts["VERIFIED"]-len(missing),
      "verified_records_missing_evidence":len(missing),
      "unknown_states":unknown,
      "missing_evidence_files":missing,
      "integrity":{
        "workflow_success_is_not_verification":True,
        "qc_pass_is_not_verification":True,
        "confidence_is_not_proof":True,
        "automatic_promotion_to_verified":False
      },
      "provenance":{"source":"generated/**/*.json","method":"deterministic verification-state audit"}
    }
    report["status"]="PASS" if not unknown and not missing else "BLOCK"
    report["fingerprint"]=digest(report)
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0 if report["status"]=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
