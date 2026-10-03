#!/usr/bin/env python3
"""Fail-closed independent-verification status gate."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/"generated"/"claim-evidence.jsonl"
OUT=ROOT/"generated"/"independent-verification-status.json"
ALLOWED={"REGISTERED","UNVERIFIED","REVIEW","VERIFIED","BLOCKED"}
def canonical_hash(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(",",":")).encode()).hexdigest()
def main():
    counts={s:0 for s in sorted(ALLOWED)}; malformed=0; total=0
    if INPUT.exists():
        for raw in INPUT.read_text(encoding="utf-8").splitlines():
            if not raw.strip(): continue
            total+=1
            try:
                row=json.loads(raw); state=row.get("verification_state","UNVERIFIED")
                if state not in ALLOWED: malformed+=1
                else: counts[state]+=1
            except json.JSONDecodeError: malformed+=1
    report={"schema_version":"1.0","status":"VERIFIED_RECORDS_PRESENT" if counts["VERIFIED"] else "NO_INDEPENDENTLY_VERIFIED_RECORDS",
      "total_records":total,"verification_counts":counts,"verified_records":counts["VERIFIED"],"malformed_records":malformed,
      "independent_verification_required":True,
      "promotion_rule":"Only explicit VERIFIED records count; workflow success, QC PASS, provenance, or generated artifacts do not promote a record.",
      "source":"generated/claim-evidence.jsonl"}
    report["fingerprint"]=canonical_hash(report)
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2)); return 1 if malformed else 0
if __name__=="__main__": raise SystemExit(main())
