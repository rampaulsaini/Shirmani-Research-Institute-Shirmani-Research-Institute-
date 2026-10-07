from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]; SRC=ROOT/"generated/1000-digital-products.json"; OUT=ROOT/"catalog/shards"; MAN=ROOT/"catalog/manifest.json"
SIZE=500; CAPACITY=150000
def main():
 data=json.loads(SRC.read_text(encoding="utf-8")); rows=[p for p in data.get("products",[]) if str(p.get("id","")).strip()]
 OUT.mkdir(parents=True,exist_ok=True)
 for f in OUT.glob("shard-*.json"): f.unlink()
 shards=[]
 for n in range(0,len(rows),SIZE):
  chunk=rows[n:n+SIZE]; i=n//SIZE; raw=json.dumps({"schema_version":1,"shard":i,"capacity":SIZE,"products":chunk},ensure_ascii=False,separators=(",",":"))+"\n"; f=OUT/f"shard-{i:04d}.json"; f.write_text(raw,encoding="utf-8"); shards.append({"shard":i,"path":f"catalog/shards/{f.name}","count":len(chunk),"sha256":hashlib.sha256(raw.encode()).hexdigest()})
 MAN.parent.mkdir(exist_ok=True); MAN.write_text(json.dumps({"schema_version":1,"generated_at":datetime.now(timezone.utc).isoformat(),"capacity":CAPACITY,"shard_size":SIZE,"catalog_count":len(rows),"shard_count":len(shards),"remaining_capacity":max(0,CAPACITY-len(rows)),"scale_status":"READY_FOR_150K_CATALOG_SHARDS","source":"generated/1000-digital-products.json","shards":shards},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print("catalog_count",len(rows),"capacity",CAPACITY,"remaining",max(0,CAPACITY-len(rows)))
if __name__=="__main__": main()
