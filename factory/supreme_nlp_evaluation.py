"""Dependency-free Supreme NLP structural evaluation gate."""
import json
import sys
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "factory" / "fixtures" / "supreme_nlp_records.jsonl"
REQUIRED = ("record_id","measured_signal","model_inference","interpretation","confidence","evidence","uncertainty","provenance","verification_state")
ALLOWED_STATES = {"UNVERIFIED","REVIEW","VERIFIED","BLOCKED"}
FORBIDDEN_UNQUALIFIED = ("proved feeling","proved consciousness","proved intention","directly proves emotion")

def load_records(path):
    for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if raw.strip():
            yield n, json.loads(raw)

def evaluate(records):
    checks, confidences = [], []
    for line, r in records:
        errors = [f"missing:{','.join(k for k in REQUIRED if k not in r)}"] if any(k not in r for k in REQUIRED) else []
        c = r.get("confidence")
        if not isinstance(c, (int,float)) or not 0 <= c <= 1: errors.append("confidence_out_of_range")
        else: confidences.append(float(c))
        if r.get("verification_state") not in ALLOWED_STATES: errors.append("invalid_verification_state")
        if not isinstance(r.get("provenance"), dict) or not r["provenance"].get("source_id"): errors.append("missing_provenance")
        if not isinstance(r.get("evidence"), dict) or not r["evidence"].get("status"): errors.append("missing_evidence_status")
        if not str(r.get("uncertainty","")).strip(): errors.append("missing_uncertainty")
        joined = " ".join(str(r.get(k,"")).lower() for k in ("model_inference","interpretation"))
        if any(term in joined for term in FORBIDDEN_UNQUALIFIED): errors.append("unqualified_subjective_claim")
        checks.append({"line":line,"record_id":r.get("record_id"),"errors":errors})
    total = len(checks); passed = sum(not x["errors"] for x in checks)
    return {"records":total,"passed":passed,"failed":total-passed,
            "structural_pass_rate":round(passed/total,6) if total else 0.0,
            "mean_confidence":round(mean(confidences),6) if confidences else None,
            "status":"PASS" if total and passed == total else "FAIL",
            "failures":[x for x in checks if x["errors"]]}

if __name__ == "__main__":
    result = evaluate(load_records(FIXTURE))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result["status"] == "PASS" else 1)
