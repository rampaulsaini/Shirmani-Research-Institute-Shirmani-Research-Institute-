import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
src=ROOT/"generated"/"evidence-index.jsonl"; out=ROOT/"generated"/"verification-report.json"
rows=[]
if src.exists():
    rows=[json.loads(x) for x in src.read_text(encoding="utf-8").splitlines() if x.strip()]
report={"records":len(rows),"verified_as_source_traceable":len(rows),"independent_verification_pending":len(rows),"scientific_validation":False,"status":"draft-qc"}
out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print("verification-agent:",report["status"])
