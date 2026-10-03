#!/usr/bin/env python3
"""Build a fail-closed progress report for independent verification.

This report distinguishes the instantiated review layer from the
authoritative 100,200-record verification target. Neither scale may be
conflated, and workflow activity never creates a VERIFIED decision.
"""
from __future__ import annotations
import argparse, gzip, json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUTHORITATIVE_QUEUE = ROOT / "generated/VERIFICATION-QUEUE.json"
AUTHORITATIVE_REGISTRY = ROOT / "generated/VERIFICATION-REGISTRY.json"

def load_jsonl(path: Path):
    """Load either plain JSONL or gzip-compressed JSONL."""
    if not path.exists():
        return
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as fh:
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

    queue=list(load_jsonl(Path(args.queue)))
    registry=list(load_jsonl(Path(args.registry)))
    q_ids={str(r.get("task_id")) for _,r in queue if r.get("task_id") is not None}
    r_ids={str(r.get("task_id")) for _,r in registry if r.get("task_id") is not None}
    verification=Counter(str(r.get("verification_status","UNKNOWN")).upper() for _,r in registry)
    status=Counter(str(r.get("status","UNKNOWN")).upper() for _,r in registry)
    independent=sum(
        1 for _,r in registry
        if str(r.get("verification_status","")).upper() in {"VERIFIED","INDEPENDENT_VERIFIED"}
    )
    matched=len(q_ids & r_ids)

    authoritative = {}
    if AUTHORITATIVE_QUEUE.exists():
        authoritative = json.loads(AUTHORITATIVE_QUEUE.read_text(encoding="utf-8"))
    authoritative_registry = {}
    if AUTHORITATIVE_REGISTRY.exists():
        authoritative_registry = json.loads(AUTHORITATIVE_REGISTRY.read_text(encoding="utf-8"))

    target=int(authoritative.get("records", 0))
    authoritative_verified=int(authoritative_registry.get("verified", 0))
    authoritative_queued=int(authoritative_registry.get("queued", target))

    report={
      "version":2,
      "scope":"independent-verification",
      "instantiated_review_layer":{
          "queue_total":len(queue),
          "registry_total":len(registry),
          "queue_registry_task_id_match":matched,
          "queue_registry_match_pct":pct(matched,len(queue)),
          "verification_status_counts":dict(sorted(verification.items())),
          "registry_status_counts":dict(sorted(status.items())),
          "independent_verified_records":independent,
          "verification_completion_pct":pct(independent,len(queue)),
          "remaining_to_instantiated_100_percent":max(len(queue)-independent,0)
      },
      "authoritative_target":{
          "records":target,
          "queued":authoritative_queued,
          "verified":authoritative_verified,
          "verified_completion_pct":pct(authoritative_verified,target),
          "remaining_to_target":max(target-authoritative_verified,0),
          "remaining_pct":pct(max(target-authoritative_verified,0),target)
      },
      "policy":{
          "promotion_policy":"FAIL_CLOSED",
          "workflow_success_is_not_verification":True,
          "human_review_inferred":False,
          "scales_must_not_be_conflated":True
      }
    }
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False))

if __name__=="__main__":
    main()
