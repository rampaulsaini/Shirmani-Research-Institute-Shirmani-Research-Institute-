import json, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
src=ROOT/"generated"/"agent-source-index.jsonl"; out=ROOT/"generated"/"canonical-corpus.jsonl"
seen=set(); rows=[]
if src.exists():
    for line in src.read_text(encoding="utf-8").splitlines():
        r=json.loads(line); h=r.get("canonical_hash") or hashlib.sha256(r["text"].encode()).hexdigest()
        if h in seen: continue
        seen.add(h); r["canonical_id"]="C"+h[:16]; rows.append(r)
out.write_text("\n".join(json.dumps(r,ensure_ascii=False) for r in rows)+"\n",encoding="utf-8")
print("dedup-indexer:",len(rows))
