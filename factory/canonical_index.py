#!/usr/bin/env python3
"""Create a compact, deterministic index over the canonical knowledge layer."""
import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]; GEN=ROOT/"generated"
SRC=GEN/"canonical-knowledge.jsonl"; OUT=GEN/"canonical-index.json"; BATCH=GEN/"canonical-batches"
def main():
    rows=[]
    for line in SRC.read_text(encoding="utf-8").splitlines():
        if line.strip():
            r=json.loads(line)
            if r.get("active"): rows.append(r)
    rows.sort(key=lambda r:r["id"])
    BATCH.mkdir(parents=True,exist_ok=True)
    size=250
    batches=[]
    for i in range(0,len(rows),size):
        chunk=rows[i:i+size]; bid=f"batch-{i//size+1:04d}"
        path=BATCH/f"{bid}.jsonl"
        path.write_text("".join(json.dumps(x,ensure_ascii=False)+"\n" for x in chunk),encoding="utf-8")
        batches.append({"id":bid,"records":len(chunk),"sha256":hashlib.sha256(path.read_bytes()).hexdigest(),"path":str(path.relative_to(ROOT))})
    out={"version":1,"generated_at":datetime.now(timezone.utc).isoformat(),"active_records":len(rows),
         "batch_size":size,"batch_count":len(batches),"batches":batches,
         "source":"generated/canonical-knowledge.jsonl","generated_output_is_not_source":True}
    OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,ensure_ascii=False))
if __name__=="__main__": main()
