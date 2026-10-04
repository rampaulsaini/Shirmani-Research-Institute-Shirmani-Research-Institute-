#!/usr/bin/env python3
"""Deterministic independent-verification registry gate. Never upgrades claims to VERIFIED."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/"generated"/"claim-evidence.jsonl"
OUTPUT=ROOT/"generated"/"independent-verification-status.json"

def main():
    if not INPUT.exists():
        report={"schema_version":"1.0","status":"BLOCK","reason":"claim-evidence.jsonl is missing","records":0,"verified":0,"unverified":0,"verification_completion_percent":0.0}
        OUTPUT.parent.mkdir(parents=True,exist_ok=True)
        OUTPUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        return 1
    records=[]; errors=[]
    for line_no,line in enumerate(INPUT.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        try: records.append(json.loads(line))
        except json.JSONDecodeError as exc: errors.append({"line":line_no,"error":f"invalid_json:{exc}"})
    verified=unverified=review=blocked=0
    for r in records:
        v=r.get("verification") or {}; status=v.get("status"); independent=v.get("independent") is True
        if status=="PASS" and independent and v.get("verifier") and v.get("provenance"): verified+=1
        elif status in {"FAIL","BLOCKED"}: blocked+=1
        elif status=="REVIEW": review+=1
        else: unverified+=1
        if independent and not (status=="PASS" and v.get("verifier") and v.get("provenance")):
            errors.append({"id":r.get("id"),"error":"unearned_independent_verification"})
    total=len(records); completion=round(verified/total*100,2) if total else 0.0
    report={"schema_version":"1.0","status":"PASS" if total and not errors else "BLOCK","records":total,"verified":verified,"unverified":unverified,"review":review,"blocked":blocked,"verification_completion_percent":completion,"remaining_percent":round(100-completion,2) if total else 100.0,"errors":errors,"promotion_rule":"PASS + independent=true + verifier + provenance","integrity_boundary":"Workflow success, QC success, evidence support, and author declaration do not by themselves constitute independent verification."}
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    OUTPUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0 if report["status"]=="PASS" else 1
if __name__=="__main__":
    raise SystemExit(main())
