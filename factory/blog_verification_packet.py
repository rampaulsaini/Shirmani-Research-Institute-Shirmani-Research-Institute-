#!/usr/bin/env python3
"""Create a deterministic human-review packet from the blog-derived claim inventory."""
import argparse, hashlib, json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--batch-size",type=int,default=25)
    ap.add_argument("--offset",type=int,default=0)
    args=ap.parse_args()
    if not 1 <= args.batch_size <= 100:
        raise SystemExit("batch-size must be 1..100")
    if args.offset < 0:
        raise SystemExit("offset must be >= 0")
    src=Path("generated/BLOG-CLAIM-INVENTORY.json")
    if not src.exists():
        raise SystemExit("BLOG_CLAIM_INVENTORY_MISSING")
    d=json.loads(src.read_text(encoding="utf-8"))
    claims=d.get("claims",[])
    if d.get("claim_count") != len(claims):
        raise SystemExit("BLOG_CLAIM_INVENTORY_INVALID")
    batch=claims[args.offset:args.offset+args.batch_size]
    if not batch:
        raise SystemExit("NO_REVIEW_CLAIMS_AT_OFFSET")
    task_hash=hashlib.sha256(json.dumps(batch,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
    out=Path(f"generated/blog-verification-packet-{args.offset+1:06d}-{args.offset+len(batch):06d}.json")
    payload={
      "status":"READY_FOR_HUMAN_REVIEW",
      "verification_status":"NOT_PERFORMED",
      "inventory_source_sha256":d["source_sha256"],
      "inventory_source_url":d["source_url"],
      "inventory_claim_count":len(claims),
      "offset":args.offset,
      "batch_size":len(batch),
      "task_hash":task_hash,
      "claims":[
        {
          "claim_id":c["claim_id"],
          "claim_text":c["claim_text"],
          "claim_type":c["claim_type"],
          "claim_tags":c.get("claim_tags",[]),
          "source_url":c["source_url"],
          "source_sha256":c["source_sha256"],
          "source_unit":c["source_unit"],
          "review_template":{
            "exact_claim_reviewed":False,
            "definitions_checked":False,
            "evidence_references":[],
            "counter_evidence_references":[],
            "reproduction_or_test":[],
            "uncertainty":"",
            "independent_reviewer":"",
            "review_timestamp":"",
            "conclusion":""
          }
        } for c in batch
      ]
    }
    out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":payload["status"],"verification_status":payload["verification_status"],"packet":str(out),"claims":len(batch),"task_hash":task_hash},ensure_ascii=False))

if __name__=="__main__":
    main()
