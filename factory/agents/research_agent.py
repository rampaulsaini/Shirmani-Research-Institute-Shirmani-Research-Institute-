import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
src=ROOT/"generated"/"canonical-corpus.jsonl"; out=ROOT/"generated"/"research-queue.jsonl"
rows=[]
if src.exists():
    for i,line in enumerate(src.read_text(encoding="utf-8").splitlines(),1):
        r=json.loads(line)
        rows.append({"research_id":f"R{i:06d}","question":r["text"],"source":r["source"],"canonical_id":r["canonical_id"],"status":"draft"})
out.write_text("\n".join(json.dumps(r,ensure_ascii=False) for r in rows)+"\n",encoding="utf-8")
print("research-agent:",len(rows))
