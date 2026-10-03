#!/usr/bin/env python3
"""Build a fail-closed progress report for independent verification."""
from __future__ import annotations
import argparse, gzip, json
from collections import Counter
from pathlib import Path

def load_jsonl_gz(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, 1):
            if line.strip():
                yield line_no, json.loads(line)

def pct(n, d):
    return round((100.0*n/d), 2) if d else 0.0

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--queue", required=True)
    p.add_argument("--registry", required=True)
    p.add_argument("--output", required=True)
    args=p.parse_args()
    queue=list(load_jsonl_gz(Path(args.queue)))
    registry=list(load_jsonl_gz(Path(args.registry)))
    q_ids={str(r.get("task_id")) for _,r in queue if r.get("task_id") is not None}
    r_ids={str(r.get("task_id")) for _,r in registry if r.get("task_id") is not None}
    verification=Counter(str(r.get("verification_status","UNKNOWN")).upper() for _,r in registry)
    status=Counter(str(r.get("status","UNKNOWN")).upper() for _,r in registry)
    independent=sum(1 for _,r in registry if str(r.get("verification_status","")).upper() in {"VERIFIED","INDEPENDENT_VERIFIED"})
    matched=len(q_ids & r_ids)
    report={
      "version":1,"scope":"independent-verification","queue_total":len(queue),
      "registry_total":len(registry),"queue_registry_task_id_match":matched,
      "queue_registry_match_pct":pct(matched,len(queue)),
      "verification_status_counts":dict(sorted(verification.items())),
      "registry_status_counts":dict(sorted(status.items())),
      "independent_verified_records":independent,
      "verification_completion_pct":pct(independent,len(queue)),
      "remaining_to_100_percent":max(len(queue)-independent,0),
      "promotion_policy":"FAIL_CLOSED","workflow_success_is_not_verification":True,
      "human_review_inferred":False
    }
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False))

if __name__=="__main__":
    main()
