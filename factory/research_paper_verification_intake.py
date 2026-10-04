#!/usr/bin/env python3
"""Create verification-ready Research Paper tasks without promotion."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
claims=json.loads((ROOT/"generated/research-paper-claims.json").read_text(encoding="utf-8"))["claims"]
out=ROOT/"generated/research-paper-verification-intake.jsonl"
rows=[{"task_id":"SRP-VT-"+c["id"].split("-",1)[1],"claim_id":c["id"],"source_repository":"rampaulsaini/Shirmani-Research-Paper","task_type":"INDEPENDENT_VERIFICATION_REQUIRED","verification_status":"UNVERIFIED","independent":False,"promotion_allowed":False,"evidence_requirements":c["evidence_required"],"status":"QUEUED"} for c in claims]
out.write_text("".join(json.dumps(r,ensure_ascii=False,sort_keys=True)+"\n" for r in rows),encoding="utf-8")
print(f"Research Paper verification intake: {len(rows)} queued")
