#!/usr/bin/env python3
"""Create an independently reviewable queue from reasoning metadata.

This queue never marks an artifact verified automatically.
"""
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"generated"; REASONING=OUT/"reasoning-manifest.jsonl"; REVIEW=OUT/"independent-review-queue.jsonl"
def sha(text): return hashlib.sha256(text.encode("utf-8")).hexdigest()
def main():
    rows=[]
    if REASONING.exists():
        for line in REASONING.read_text(encoding="utf-8").splitlines():
            if not line.strip(): continue
            r=json.loads(line)
            rows.append({"review_id":"review-"+sha(str(r["kind"])+"|"+str(r["artifact_id"]))[:16],
                "artifact_id":r["artifact_id"],"kind":r["kind"],"content_sha256":r["content_sha256"],
                "source_ids":r["source_ids"],"claim_class":r["claim_class"],
                "evidence_status":"requires_independent_verification","review_status":"queued",
                "reviewer":None,"evidence_notes":[],"counterevidence":[],"reproducibility_notes":None,
                "decision":None,"reviewed_at":None,"human_review_required":True})
    REVIEW.write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows),encoding="utf-8")
    print(json.dumps({"review_queue_records":len(rows),"publication_decision":"human_review_required"},ensure_ascii=False))
if __name__=="__main__": main()
