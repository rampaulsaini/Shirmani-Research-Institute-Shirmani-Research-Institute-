#!/usr/bin/env python3
from datetime import datetime, timezone
from pathlib import Path
import json, os
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"generated/concrete-production-overlay.json"
OUT=ROOT/"generated/catalog-shards/index.json"
SHARDS=ROOT/"generated/catalog-shards/shards"
def main():
    target=150000
    size=int(os.environ.get("CATALOG_SHARD_SIZE","1000"))
    size=max(100,min(5000,size))
    data=json.loads(SOURCE.read_text(encoding="utf-8"))
    rows=[p for p in data.get("products",[]) if p.get("id")]
    SHARDS.mkdir(parents=True,exist_ok=True)
    records=[]
    for start in range(0,len(rows),size):
        chunk=rows[start:start+size]
        number=start//size
        path=SHARDS/f"shard-{number:05d}.json"
        payload={"schema_version":1,"shard":number,"count":len(chunk),"state":"CONCRETE_PRODUCED","products":chunk}
        path.write_text(json.dumps(payload,ensure_ascii=False,separators=(",",":"))+"\n",encoding="utf-8")
        records.append({"shard":number,"path":str(path.relative_to(ROOT)),"count":len(chunk),"state":"CONCRETE_PRODUCED"})
    OUT.parent.mkdir(parents=True,exist_ok=True)
    result={"schema_version":1,"generated_at":datetime.now(timezone.utc).isoformat(),"long_term_target":target,"concrete_product_count":len(rows),"remaining_to_long_term_target":max(0,target-len(rows)),"shard_size":size,"concrete_shard_count":len(records),"rule":"Future capacity is not inventory; only concrete records are materialized.","shards":records}
    OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result))
if __name__=="__main__": main()
