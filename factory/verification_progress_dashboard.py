#!/usr/bin/env python3
"""Generate a quantitative, fail-closed verification progress dashboard."""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
STATUS=ROOT/"generated/independent-verification-status-2026-09-29.json"
QUEUE=ROOT/"generated/independent-verification-queue.jsonl"
REGISTRY=ROOT/"generated/independent-verification-registry.jsonl"
OUT=ROOT/"generated/verification-progress-dashboard.json"
def jsonl(path):
    if not path.exists(): return []
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
status=json.loads(STATUS.read_text(encoding="utf-8")); records=status.get("records",[])
queue=jsonl(QUEUE); registry=jsonl(REGISTRY); counts={}
for r in records:
    counts[r.get("status","UNKNOWN")]=counts.get(r.get("status","UNKNOWN"),0)+1
total=len(records); evidence=counts.get("EVIDENCE-SUPPORTED",0); verified=sum(1 for r in records if r.get("status")=="VERIFIED"); readiness=status["verification_summary"].get("verification_readiness_percent",0)
dashboard={"generated_at":datetime.now(timezone.utc).isoformat(),"method":"count-based, fail-closed; workflow success is not independent verification","records":{"total":total,"evidence_supported":evidence,"verified":verified,"not_verified":counts.get("NOT_VERIFIED",0),"author_defined_or_proposed":counts.get("AUTHOR-DEFINED",0)+counts.get("AUTHOR-PROPOSED",0)},"percent":{"evidence_supported_of_total":round(evidence/total*100,2) if total else 0,"independently_verified_of_total":round(verified/total*100,2) if total else 0,"verification_readiness":readiness},"automation_state":{"queue_records":len(queue),"review_registry_records":len(registry),"independent_verification_required":True,"automission_may_declare_verified":False},"next_gate":"independent reviewer decision + counter-evidence review + reproducible test + audit record"}
OUT.write_text(json.dumps(dashboard,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps(dashboard,ensure_ascii=False))
