"""Fail-closed Evidence -> VERIFIED promotion evaluator with integrity checks."""
from __future__ import annotations
import json
import re
from datetime import datetime, timezone
from pathlib import Path

REQUIRED=("id","claim","operational_definition","evidence","independent_test",
          "reproducibility","counter_evidence","audit","reviewer_decision")
DECISIONS={"PENDING","VERIFIED","NOT_VERIFIED","CONTRADICTED","INCONCLUSIVE"}
HEX64=re.compile(r"^[0-9a-f]{64}$")

def check_record(r):
    errors=[f"MISSING:{k}" for k in REQUIRED if k not in r]
    if errors:
        return False, errors
    e,t,p,c,a,d=r["evidence"],r["independent_test"],r["reproducibility"],r["counter_evidence"],r["audit"],r["reviewer_decision"]
    if not isinstance(e.get("sources"),list) or not e.get("sources"):
        errors.append("EVIDENCE_INCOMPLETE")
    if not HEX64.fullmatch(str(e.get("evidence_hash",""))):
        errors.append("EVIDENCE_HASH_NOT_SHA256")
    if not t.get("protocol") or not t.get("result"):
        errors.append("INDEPENDENT_TEST_INCOMPLETE")
    if not HEX64.fullmatch(str(t.get("test_hash",""))):
        errors.append("TEST_HASH_NOT_SHA256")
    if not p.get("environment") or not p.get("reproduction_steps") or p.get("result_match") is not True:
        errors.append("REPRODUCIBILITY_FAILED")
    if c.get("reviewed") is not True:
        errors.append("COUNTER_EVIDENCE_NOT_REVIEWED")
    if a.get("passed") is not True or not a.get("audit_id") or not a.get("timestamp"):
        errors.append("AUDIT_NOT_PASSED")
    decision=d.get("decision")
    if decision not in DECISIONS:
        errors.append("INVALID_REVIEWER_DECISION")
    if decision=="VERIFIED" and not (d.get("reviewer_identity") and d.get("reviewer_role") and d.get("timestamp")):
        errors.append("REVIEWER_PROVENANCE_MISSING")
    return not errors, errors

def evaluate(path="generated/independent-verification-records.json"):
    p=Path(path)
    data=json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"records":[]}
    records=data.get("records",[])
    summary=data.get("verification_summary",{})
    report=[]
    eligible=0
    for r in records:
        ok,errors=check_record(r)
        decision=r.get("reviewer_decision",{}).get("decision")
        is_verified=ok and decision=="VERIFIED"
        eligible += int(is_verified)
        report.append({"id":r.get("id"),"eligible_for_verified":is_verified,
                       "requested_decision":decision,"errors":errors})

    evidence_supported=sum(1 for r in records if r.get("status")=="EVIDENCE-SUPPORTED")
    declared_verified=sum(1 for r in records if r.get("reviewer_decision",{}).get("decision")=="VERIFIED")

    if summary.get("queue_records") != len(records):
        raise SystemExit("QUEUE_SUMMARY_MISMATCH")
    if summary.get("evidence_supported_records", evidence_supported) != evidence_supported:
        raise SystemExit("EVIDENCE_SUMMARY_MISMATCH")
    if declared_verified != eligible:
        raise SystemExit("UNEARNED_VERIFIED_DECISION")
    if int(summary.get("independently_verified_records", 0)) != eligible:
        raise SystemExit("VERIFIED_SUMMARY_MISMATCH")
    expected_pct=round((eligible/len(records))*100, 6) if records else 0
    if float(summary.get("independent_verified_percent", 0)) != expected_pct:
        raise SystemExit("VERIFIED_PERCENT_MISMATCH")

    return {
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "queue_records":len(records),
        "evidence_supported_records":evidence_supported,
        "verified_records":eligible,
        "verified_percent":expected_pct,
        "records":report,
        "fail_closed":True,
        "automation_cannot_create_independent_review":True
    }

if __name__=="__main__":
    out=evaluate()
    Path("generated").mkdir(exist_ok=True)
    Path("generated/independent-verification-promotion-report.json").write_text(
        json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,ensure_ascii=False))
