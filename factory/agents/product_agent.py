import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
src=ROOT/"generated"/"research-queue.jsonl"; out=ROOT/"generated"/"product-queue.jsonl"
rows=[]
if src.exists():
    for i,line in enumerate(src.read_text(encoding="utf-8").splitlines(),1):
        r=json.loads(line)
        rows.append({"product_id":f"P{i:06d}","research_id":r["research_id"],"formats":["mahagranth","verse","paper","audio-script"],"source":r["source"],"draft_only":True})
out.write_text("\n".join(json.dumps(r,ensure_ascii=False) for r in rows)+"\n",encoding="utf-8")
print("product-agent:",len(rows))
