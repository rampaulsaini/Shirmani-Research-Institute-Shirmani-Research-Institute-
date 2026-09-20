#!/usr/bin/env python3
"""Fail-closed structural QC for independent verification review records."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"

def main():
    queue = OUT / "independent-verification-queue.jsonl"
    registry = OUT / "independent-verification-registry.jsonl"
    if not queue.exists() or not registry.exists():
        raise SystemExit("verification queue or registry is missing")
    queue_ids = {str(json.loads(x)["task_id"]) for x in queue.read_text(encoding="utf-8").splitlines() if x.strip()}
    seen = set(); errors=[]; count=0
    required=("review_id","task_id","claim_id","status","verification_status","independent",
              "reviewer","reviewed_at","evidence_references","countercase_review",
              "reproduction_or_test","audit","created_at","generator")
    for n,line in enumerate(registry.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        count += 1
        try: r=json.loads(line)
        except Exception as e:
            errors.append({"line":n,"error":"invalid_json:"+str(e)}); continue
        for k in required:
            if k not in r: errors.append({"line":n,"error":"missing:"+k})
        rid=r.get("review_id")
        if rid in seen: errors.append({"line":n,"error":"duplicate_review_id"})
        seen.add(rid)
        if r.get("task_id") not in queue_ids: errors.append({"line":n,"error":"task_not_in_queue"})
        if r.get("status") != "QUEUED": errors.append({"line":n,"error":"invalid_initial_status"})
        if r.get("verification_status") != "NOT_VERIFIED": errors.append({"line":n,"error":"unearned_initial_verification"})
        if r.get("independent") is not False: errors.append({"line":n,"error":"initial_independent_must_be_false"})
        if r.get("reviewer") is not None or r.get("reviewed_at") is not None: errors.append({"line":n,"error":"fabricated_reviewer_metadata"})
        if not isinstance(r.get("evidence_references"),list): errors.append({"line":n,"error":"evidence_references_not_list"})
        cc=r.get("countercase_review") or {}
        if cc.get("status") != "NOT_REVIEWED": errors.append({"line":n,"error":"countercase_not_fail_closed"})
        rt=r.get("reproduction_or_test") or {}
        if rt.get("status") != "NOT_RUN": errors.append({"line":n,"error":"reproduction_not_fail_closed"})
        audit=r.get("audit") or {}
        if not audit.get("recorded_at") or not audit.get("record_hash"): errors.append({"line":n,"error":"audit_metadata_missing"})
    if count != len(queue_ids): errors.append({"error":"registry_queue_count_mismatch","queue":len(queue_ids),"registry":count})
    report={"version":1,"records":count,"unique_reviews":len(seen),"queue_records":len(queue_ids),
            "error_count":len(errors),"publication_gate":"PASS" if not errors else "BLOCK","errors":errors}
    (OUT/"VERIFICATION-REGISTRY-QC.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False))
    if errors: raise SystemExit(1)

if __name__=="__main__": main()
