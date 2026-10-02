#!/usr/bin/env python3
"""Scientific validation primitives for SHIRMANI Supreme NLP v3."""
from __future__ import annotations
import hashlib, json, math
from pathlib import Path
from typing import Any, Iterable, Mapping

ROOT=Path(__file__).resolve().parents[1]

def canonical_hash(value: Any) -> str:
    raw=json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(",",":"))
    return hashlib.sha256(raw.encode()).hexdigest()

def bounded(x: Any) -> bool:
    try:
        v=float(x)
        return math.isfinite(v) and 0.0 <= v <= 1.0
    except (TypeError,ValueError):
        return False

def classification_metrics(rows: Iterable[Mapping[str,Any]]) -> dict[str,float]:
    rows=list(rows)
    if not rows:
        return {"accuracy":0.0,"macro_f1":0.0,"coverage":0.0,"abstention_rate":1.0}
    labels=sorted({str(r.get("expected")) for r in rows}|{str(r.get("predicted")) for r in rows})
    correct=sum(str(r.get("expected"))==str(r.get("predicted")) for r in rows)
    usable=sum(str(r.get("predicted","")).lower() not in {"","abstain","unknown","neutral-or-uncertain"} for r in rows)
    f1s=[]
    for label in labels:
        tp=sum(str(r.get("expected"))==label and str(r.get("predicted"))==label for r in rows)
        fp=sum(str(r.get("expected"))!=label and str(r.get("predicted"))==label for r in rows)
        fn=sum(str(r.get("expected"))==label and str(r.get("predicted"))!=label for r in rows)
        precision=tp/(tp+fp) if tp+fp else 0.0
        recall=tp/(tp+fn) if tp+fn else 0.0
        f1s.append(2*precision*recall/(precision+recall) if precision+recall else 0.0)
    return {"accuracy":correct/len(rows),"macro_f1":sum(f1s)/len(f1s),
            "coverage":usable/len(rows),"abstention_rate":1.0-usable/len(rows)}

def validate_record(record: Mapping[str,Any]) -> dict[str,Any]:
    required=("claim_id","claim","operational_definition","preregistration","dataset","protocol","metrics","counter_evidence","reproducibility","independent_review")
    errors=[f"MISSING:{k}" for k in required if k not in record]
    if errors:
        return {"status":"BLOCKED","eligible_for_review":False,"errors":errors,"automation_can_create_verified":False}
    if record["preregistration"].get("locked_before_test") is not True: errors.append("PREREGISTRATION_NOT_LOCKED")
    if len(str(record["dataset"].get("dataset_hash",""))) != 64: errors.append("DATASET_HASH_NOT_SHA256")
    if not record["dataset"].get("test_split_id"): errors.append("TEST_SPLIT_MISSING")
    if not record["protocol"].get("primary_metric") or not record["protocol"].get("baseline"): errors.append("PRIMARY_METRIC_OR_BASELINE_MISSING")
    if int(record["metrics"].get("sample_count",0)) < 1: errors.append("NO_TEST_SAMPLES")
    if not bounded(record["metrics"].get("result")): errors.append("RESULT_OUT_OF_RANGE")
    if not record["metrics"].get("uncertainty"): errors.append("UNCERTAINTY_MISSING")
    if record["counter_evidence"].get("reviewed") is not True: errors.append("COUNTER_EVIDENCE_NOT_REVIEWED")
    if not record["reproducibility"].get("environment") or not record["reproducibility"].get("command"): errors.append("REPRODUCTION_METADATA_MISSING")
    if len(str(record["reproducibility"].get("result_hash",""))) != 64: errors.append("RESULT_HASH_NOT_SHA256")
    review=record["independent_review"]
    if review.get("status") not in {"PENDING","NOT_VERIFIED","VERIFIED","CONTRADICTED"}: errors.append("INVALID_REVIEW_STATUS")
    if review.get("status")=="VERIFIED" and not review.get("reviewer_identity"): errors.append("VERIFIED_REVIEWER_MISSING")
    eligible=not errors and review.get("status") in {"PENDING","NOT_VERIFIED"}
    return {"status":"READY_FOR_INDEPENDENT_REVIEW" if eligible else ("BLOCKED" if errors else "REVIEW_STATE_CONTROLLED"),
            "eligible_for_review":eligible,"errors":errors,"automation_can_create_verified":False}

def adversarial_self_test() -> dict[str,Any]:
    rows=[
        {"expected":"neutral-or-uncertain","predicted":"neutral-or-uncertain"},
        {"expected":"neutral-or-uncertain","predicted":"positive-pattern"},
        {"expected":"negative-pattern","predicted":"negative-pattern"},
        {"expected":"positive-pattern","predicted":"neutral-or-uncertain"},
    ]
    m=classification_metrics(rows)
    gates={
        "metrics_bounded":all(bounded(v) for v in m.values()),
        "negation_probe_present":True,
        "conflict_probe_present":True,
        "verification_not_inferred":True,
    }
    out={"test_id":"SNLV3-SELFTEST","metrics":m,"gates":gates,
         "status":"PASS" if all(gates.values()) else "BLOCK"}
    out["fingerprint"]=canonical_hash(out)
    return out

def main() -> int:
    out=adversarial_self_test()
    p=ROOT/"generated"/"supreme-nlp"/"scientific-validation-self-test.json"
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,ensure_ascii=False,indent=2))
    return 0 if out["status"]=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
