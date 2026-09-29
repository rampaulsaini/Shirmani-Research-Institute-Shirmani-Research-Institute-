#!/usr/bin/env python3
"""Independent verification coverage gate; never upgrades claims automatically."""
import json
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/"generated"/"claim-evidence.jsonl"
REVIEWS=ROOT/"verification"/"independent-reviews.jsonl"
STATUS=ROOT/"generated"/"independent-verification-status.json"
REQ={"claim_id","reviewer_id","reviewer_independent","evidence_refs","counter_evidence_refs","method","reproduction_result","decision","reviewed_at"}
def rows(p):
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []
def main():
    claims=rows(INPUT); reviews=rows(REVIEWS); valid={}; errors=[]
    for r in reviews:
        if "_schema" in r: continue
        missing=sorted(REQ-set(r)); cid=str(r.get("claim_id",""))
        if missing: errors.append({"claim_id":cid,"error":"missing_fields","fields":missing}); continue
        if r.get("reviewer_independent") is not True: errors.append({"claim_id":cid,"error":"reviewer_not_independent"}); continue
        if not isinstance(r.get("evidence_refs"),list) or not r["evidence_refs"]: errors.append({"claim_id":cid,"error":"missing_independent_evidence"}); continue
        if not isinstance(r.get("counter_evidence_refs"),list): errors.append({"claim_id":cid,"error":"missing_counter_evidence_field"}); continue
        if r.get("reproduction_result") not in {"PASS","NOT_APPLICABLE_WITH_REASON"}: errors.append({"claim_id":cid,"error":"reproduction_gate_failed"}); continue
        if r.get("decision")=="INDEPENDENT_VERIFIED": valid[cid]=r
    total=len(claims); verified=sum(1 for c in claims if str(c.get("id","")) in valid)
    out={"generated_at":datetime.now(timezone.utc).isoformat(),"total_claim_evidence_records":total,"independent_verified_records":verified,"independent_verification_percent":round(verified/total*100,4) if total else 0.0,"workflow_success_is_not_verification":True,"review_records":len(reviews),"invalid_review_records":len(errors),"remaining_unverified_records":total-verified}
    STATUS.parent.mkdir(parents=True,exist_ok=True); STATUS.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,ensure_ascii=False))
if __name__=="__main__": main()
