#!/usr/bin/env python3
"""Recompute independent-verification coverage from the public 10-record registry."""
import json
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
STATUS=ROOT/"generated"/"independent-verification-status-2026-09-29.json"
REVIEWS=ROOT/"verification"/"independent-reviews.jsonl"
def rows(p):
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip() and not x.startswith("{\"_schema\"")] if p.exists() else []
def main():
    d=json.loads(STATUS.read_text(encoding="utf-8")); records=d["records"]; reviews=rows(REVIEWS)
    approved={str(x.get("claim_id")) for x in reviews if x.get("reviewer_independent") is True and x.get("decision")=="INDEPENDENT_VERIFIED" and x.get("evidence_refs")}
    verified=sum(1 for x in records if str(x.get("id")) in approved)
    d["generated_at"]=datetime.now(timezone.utc).date().isoformat()
    d["verification_summary"]["independently_verified_records"]=verified
    d["verification_summary"]["independent_verified_percent"]=round(verified/len(records)*100,4) if records else 0
    d["verification_summary"]["verification_readiness_percent"]=100 if records else 0
    d["integrity_note"]="Independent verification changes only from qualifying independent review records; workflow success, author statements, citations and evidence-supported status do not by themselves create VERIFIED."
    STATUS.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(d["verification_summary"],ensure_ascii=False))
if __name__=="__main__": main()
