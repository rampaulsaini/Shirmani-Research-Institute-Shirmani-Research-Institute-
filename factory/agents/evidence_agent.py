import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
src=ROOT/"generated"/"canonical-corpus.jsonl"; out=ROOT/"generated"/"evidence-index.jsonl"
rows=[]
if src.exists():
    for line in src.read_text(encoding="utf-8").splitlines():
        r=json.loads(line)
        rows.append({"canonical_id":r["canonical_id"],"source":r["source"],"hash":r.get("canonical_hash"),"evidence_status":"source-present","verification_required":True})
out.write_text("\n".join(json.dumps(r,ensure_ascii=False) for r in rows)+"\n",encoding="utf-8")
print("evidence-agent:",len(rows))
