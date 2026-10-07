#!/usr/bin/env python3
"""Build a 150,000-capacity sharded catalogue from real product records only."""
from datetime import datetime,timezone
from pathlib import Path
import json,math,os
ROOT=Path(__file__).resolve().parents[1]; CAT=ROOT/"generated/1000-digital-products.json"; OUT=ROOT/"generated/catalog-shards"; MAN=ROOT/"generated/sharded-catalog-manifest.json"
CAP=int(os.getenv("CATALOG_CAPACITY","150000")); SIZE=int(os.getenv("CATALOG_SHARD_SIZE","1000"))
def main():
 d=json.loads(CAT.read_text(encoding="utf-8")); ps=d.get("products",[])
 if not ps: raise SystemExit("Empty catalogue; refusing to publish a fake catalogue.")
 if CAP<len(ps): raise SystemExit("Capacity below actual product count.")
 OUT.mkdir(parents=True,exist_ok=True)
 for p in OUT.glob("shard-*.json"): p.unlink()
 populated=math.ceil(len(ps)/SIZE); planned=math.ceil(CAP/SIZE)
 rows=[]
 for i in range(populated):
  part=ps[i*SIZE:(i+1)*SIZE]; path=OUT/f"shard-{i:04d}.json"
  path.write_text(json.dumps({"schema_version":1,"shard_id":f"{i:04d}","capacity":SIZE,"record_count":len(part),"records":part},ensure_ascii=False,separators=(",",":"))+"\n",encoding="utf-8")
  rows.append({"shard_id":f"{i:04d}","path":str(path.relative_to(ROOT)),"record_count":len(part),"capacity":SIZE,"state":"POPULATED"})
 payload={"schema_version":1,"generated_at":datetime.now(timezone.utc).isoformat(),"architecture":"SHARDED_PRODUCT_CATALOG","capacity":CAP,"shard_size":SIZE,"planned_shards":planned,"populated_shards":populated,"actual_product_records":len(ps),"empty_capacity_slots":CAP-len(ps),"source":"generated/1000-digital-products.json","truth_boundary":"Capacity is an architecture target; empty slots are not products.","shards":rows}
 MAN.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(json.dumps({"capacity":CAP,"actual_product_records":len(ps),"planned_shards":planned,"populated_shards":populated,"remaining_capacity":CAP-len(ps)}))
if __name__=="__main__": main()
