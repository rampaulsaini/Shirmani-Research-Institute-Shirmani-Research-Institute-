"""Fail-closed Evidence -> VERIFIED promotion evaluator."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

REQUIRED=("id","claim","operational_definition","evidence","independent_test","reproducibility","counter_evidence","audit","reviewer_decision")

def check_record(r):
    errors=[f"MISSING:{k}" for k in REQUIRED if k not in r]
    if errors: return False, errors
    e,t,p,c,a,d=r["evidence"],r["independent_test"],r["reproducibility"],r["counter_evidence"],r["audit"],r["reviewer_decision"]
    if not e.get("sources") or len(e.get("evidence_hash",""))<16: errors.append("EVIDENCE_INCOMPLETE")
    if not t.get("protocol") or not t.get("result") or len(t.get("test_hash",""))<16: errors.append("INDEPENDENT_TEST_INCOMPLETE")
    if not p.get("environment") or not p.get("reproduction_steps") or p.get("result_match") is not True: errors.append("REPRODUCIBILITY_FAILED")
    if c.get("reviewed") is not True: errors.append("COUNTER_EVIDENCE_NOT_REVIEWED")
    if a.get("passed") is not True or not a.get("audit_id") or not a.get("timestamp"): errors.append("AUDIT_NOT_PASSED")
    if d.get("decision")=="VERIFIED" and not (d.get("reviewer_identity") and d.get("reviewer_role") and d.get("timestamp")): errors.append("REVIEWER_PROVENANCE_MISSING")
    return not errors, errors

def evaluate(path="generated/independent-verification-records.json"):
    p=Path(path)
    data=json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"records":[]}
    report=[]; eligible=0
    for r in data.get("records",[]):
        ok,errors=check_record(r)
        decision=r.get("reviewer_decision",{}).get("decision")
        is_verified=ok and decision=="VERIFIED"
        eligible += int(is_verified)
        report.append({"id":r.get("id"),"eligible_for_verified":is_verified,"requested_decision":decision,"errors":errors})
    total=len(report)
    return {"generated_at":datetime.now(timezone.utc).isoformat(),"queue_records":total,"verified_records":eligible,"verified_percent":(eligible/total*100 if total else 0),"records":report,"fail_closed":True,"automation_cannot_create_independent_review":True}

if __name__=="__main__":
    out=evaluate()
    Path("generated").mkdir(exist_ok=True)
    Path("generated/independent-verification-promotion-report.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,ensure_ascii=False))
