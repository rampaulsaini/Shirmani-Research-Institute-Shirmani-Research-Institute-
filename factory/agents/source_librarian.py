import json, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
inp=ROOT/"generated"/"source-units.jsonl"; out=ROOT/"generated"/"agent-source-index.jsonl"
seen=set(); rows=[]
if inp.exists():
    for line in inp.read_text(encoding="utf-8").splitlines():
        r=json.loads(line); key=hashlib.sha256(r["text"].strip().encode()).hexdigest()
        if key not in seen:
            seen.add(key); r["canonical_hash"]=key; rows.append(r)
out.write_text("\n".join(json.dumps(r,ensure_ascii=False) for r in rows)+"\n",encoding="utf-8")
print("source-librarian:",len(rows))
