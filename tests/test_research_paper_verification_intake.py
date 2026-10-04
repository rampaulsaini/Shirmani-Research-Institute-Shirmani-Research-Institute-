#!/usr/bin/env python3
import json, subprocess, sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(root/"factory/research_paper_verification_intake.py")],check=True)
claims=json.loads((root/"generated/research-paper-claims.json").read_text())["claims"]
rows=[json.loads(x) for x in (root/"generated/research-paper-verification-intake.jsonl").read_text().splitlines() if x.strip()]
assert len(rows)==len(claims)
assert {r["claim_id"] for r in rows}=={c["id"] for c in claims}
assert all(r["verification_status"]=="UNVERIFIED" and r["promotion_allowed"] is False and r["status"]=="QUEUED" for r in rows)
print("Research Paper verification intake: PASS (fail-closed)")
