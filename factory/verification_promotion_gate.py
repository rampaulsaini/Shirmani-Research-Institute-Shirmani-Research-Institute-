#!/usr/bin/env python3
"""Fail-closed promotion gate for independent verification.

A claim may be promoted to VERIFIED only when the durable review record
contains an independent reviewer/audit trail, explicit evidence references,
and an explicit countercase review. Missing or malformed promotion data blocks
the gate. Pending review is not a failure by itself.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "generated"
REQUIRED = ("review_id","task_id","claim_id","status","verification_status","independent","reviewer","audit_reference","evidence_references","countercase_review")

def main():
    path = OUT / "independent-verification-registry.jsonl"
    queue_path = OUT / "independent-verification-queue.jsonl"
    if not path.exists() or not queue_path.exists():
        raise SystemExit("verification registry or queue is missing")
    queue = {}
    for line in queue_path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            row = json.loads(line)
            queue[str(row["task_id"])] = row

    seen = set(); errors = []; promoted = 0; pending = 0; records = 0
    for n,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        records += 1
        try: r=json.loads(line)
        except Exception as exc:
            errors.append({"line":n,"error":"invalid_json:"+str(exc)}); continue
        local=[]
        for key in REQUIRED:
            if key not in r: local.append("missing:"+key)
        rid=r.get("review_id"); tid=str(r.get("task_id",""))
        if rid in seen: local.append("duplicate_review_id")
        seen.add(rid)
        if tid not in queue: local.append("task_id_not_in_queue")
        if r.get("verification_status") == "VERIFIED":
            promoted += 1
            if r.get("status") != "REVIEWED": local.append("verified_without_reviewed_status")
            if r.get("independent") is not True: local.append("verified_without_independent_reviewer")
            if not isinstance(r.get("reviewer"),str) or not r.get("reviewer").strip(): local.append("verified_without_reviewer")
            if not isinstance(r.get("audit_reference"),str) or not r.get("audit_reference").strip(): local.append("verified_without_audit_reference")
            if not isinstance(r.get("evidence_references"),list) or not r.get("evidence_references"): local.append("verified_without_evidence_references")
            if not isinstance(r.get("countercase_review"),dict) or not r.get("countercase_review",{}).get("completed"): local.append("verified_without_countercase_review")
        elif r.get("verification_status") == "NOT_VERIFIED":
            pending += 1
        else:
            local.append("invalid_verification_status")
        if local: errors.extend({"line":n,"error":e} for e in local)

    report={"version":1,"records":records,"pending_records":pending,"promoted_verified_records":promoted,"error_count":len(errors),"publication_gate":"BLOCK" if errors else "PASS","policy":"No VERIFIED state is accepted without independent reviewer, audit reference, explicit evidence references, and completed countercase review.","errors":errors}
    (OUT/"VERIFICATION-PROMOTION-QC.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False))
    if errors: raise SystemExit(1)

if __name__=="__main__": main()
