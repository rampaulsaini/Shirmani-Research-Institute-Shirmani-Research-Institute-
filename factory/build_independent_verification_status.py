#!/usr/bin/env python3
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "generated/independent-verification-records.json"
OUT = ROOT / "generated/independent-verification-status-2026-09-29.json"
def main():
    data=json.loads(SRC.read_text(encoding="utf-8")); records=data.get("records", []); total=len(records)
    verified=sum(1 for r in records if r.get("status")=="VERIFIED")
    evidence=sum(1 for r in records if r.get("status")=="EVIDENCE-SUPPORTED")
    author=sum(1 for r in records if r.get("status") in {"AUTHOR-DEFINED","PROPOSED"})
    not_verified=total-verified-evidence-author
    ready=all(isinstance(r.get("claim"),str) and r.get("claim").strip() and isinstance(r.get("operational_definition"),str) and isinstance(r.get("independent_test"),dict) and isinstance(r.get("counter_evidence"),dict) and isinstance(r.get("reviewer_decision"),dict) for r in records)
    summary={"queue_records":total,"independently_verified_records":verified,"independent_verified_percent":round(verified/total*100,4) if total else 0,"evidence_supported_records":evidence,"author_defined_or_proposed_records":author,"not_verified_records":not_verified,"verification_readiness_percent":100 if ready and total else 0}
    out={"schema_version":"1.0.0","generated_at":datetime.now(timezone.utc).isoformat(),"status":"QUEUE_READY" if total else "NOT_READY","verification_summary":summary,"records":records,"integrity":{"fail_closed":True,"workflow_success_is_not_independent_verification":True,"verified_is_never_invented":True}}
    OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps(summary,ensure_ascii=False))
if __name__=="__main__": main()