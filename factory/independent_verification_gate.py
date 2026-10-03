#!/usr/bin/env python3
"""Deterministic readiness gate for independent verification."""
import hashlib,json
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/"generated"/"claim-evidence.jsonl"
OUT=ROOT/"generated"/"independent-verification-readiness.json"
def sha(text): return hashlib.sha256(text.encode("utf-8")).hexdigest()
def main():
    records=eligible=verified=blocked=0; errors=[]
    if not INPUT.exists(): errors.append("claim-evidence.jsonl is missing")
    else:
        for n,line in enumerate(INPUT.read_text(encoding="utf-8").splitlines(),1):
            if not line.strip(): continue
            records+=1
            try: r=json.loads(line)
            except Exception as e: errors.append(f"line {n}: invalid JSON: {e}"); blocked+=1; continue
            v=r.get("verification") or {}; evidence=r.get("evidence") or []
            source=r.get("source") or []; trace=r.get("source_traceability") or {}
            minimum=bool(r.get("id")) and bool(r.get("claim")) and bool(source) and bool(evidence) and trace.get("status")=="PASS" and trace.get("resolved") is True and v.get("status") in {"NOT_VERIFIED","CHECK"} and v.get("independent") is False
            if minimum: eligible+=1
            else: blocked+=1
            if v.get("status")=="PASS" and v.get("independent") is True:
                verified+=1; errors.append(f"line {n}: unearned independent verification detected")
    state="READY_FOR_INDEPENDENT_REVIEW" if eligible and not errors else ("NO_RECORDS" if records==0 and not errors else "BLOCKED")
    report={"event_id":"independent-verification-readiness-"+datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),"timestamp":datetime.now(timezone.utc).isoformat(),"repository":"rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-","input":"generated/claim-evidence.jsonl","records":records,"eligible_for_independent_review":eligible,"independently_verified":verified,"blocked_or_incomplete":blocked,"verification_state":"VERIFIED" if verified else ("UNVERIFIED" if records else "UNAVAILABLE"),"status":state,"errors":errors,"input_sha256":sha(INPUT.read_text(encoding="utf-8")) if INPUT.exists() else None,"rule":"Independent verification must be performed separately; automation cannot self-certify VERIFIED."}
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps(report,ensure_ascii=False,indent=2))
    if errors: raise SystemExit(1)
if __name__=="__main__": main()
