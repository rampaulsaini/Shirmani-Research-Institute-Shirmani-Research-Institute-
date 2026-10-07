#!/usr/bin/env python3
"""Build a scalable sharded public catalogue index.

This is a delivery/production architecture tool, not a verification engine.
"""
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"generated/1000-digital-products.json"
OUT=ROOT/"generated/catalog-shards"
INDEX=ROOT/"generated/catalog-shard-index.json"

def main():
    data=json.loads(CAT.read_text(encoding="utf-8"))
    products=data.get("products",[])
    try: size=max(100,min(5000,int(os.environ.get("CATALOG_SHARD_SIZE","1000"))))
    except ValueError: size=1000
    OUT.mkdir(parents=True,exist_ok=True)
    shards=[]
    for start in range(0,len(products),size):
        part=products[start:start+size]
        no=start//size+1
        name=f"shard-{no:04d}.json"
        (OUT/name).write_text(json.dumps({"schema_version":1,"shard":no,"start_index":start,"end_index":start+len(part)-1,"count":len(part),"products":part},ensure_ascii=False,separators=(",",":"))+"\n",encoding="utf-8")
        shards.append({"shard":no,"path":f"generated/catalog-shards/{name}","count":len(part),"first_id":part[0].get("id") if part else None,"last_id":part[-1].get("id") if part else None})
    target=150000
    INDEX.write_text(json.dumps({"schema_version":1,"generated_at":datetime.now(timezone.utc).isoformat(),"current_catalog":len(products),"current_target":5000,"long_term_target":target,"shard_size":size,"current_shards":len(shards),"shards":shards,"estimated_shards_at_150k":(target+size-1)//size,"architecture":"INDEX -> SHARD -> PRODUCT -> PASSPORT -> DEMO/VISUAL -> QC -> SHOWROOM","production_truth":"Shard presence is catalogue packaging; it is not evidence that every identity has a concrete production asset."},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"products":len(products),"shards":len(shards),"target_150k":target},ensure_ascii=False))
if __name__=="__main__": main()