#!/usr/bin/env python3
import argparse,hashlib,json
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; SRC=ROOT/"generated/1000-digital-products.json"; OUT=ROOT/"generated"; BATCH=100200
def code(seed,prefix): return prefix+"-"+hashlib.sha256(seed.encode()).hexdigest()[:12].upper()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--batch-size",type=int,default=250); a=ap.parse_args()
 src=json.loads(SRC.read_text(encoding="utf-8")); products=src.get("products",[]); stamp=datetime.now(timezone.utc).isoformat(); rows=[]
 for n,p in enumerate(products,1):
  pid=p["id"]; price=int(p.get("price_inr",0) or 0); offer=int(p.get("offer_price_inr",round(price*.8)) or 0); offer=offer if offer>0 else price
  r=dict(p); r.update({"production_batch":BATCH,"unit_no":f"{BATCH}.{n:03d}","qc_code":code(pid+str(BATCH),"QC"),"gate_no":f"GATE-{((n-1)//max(1,a.batch_size))+1:04d}","dispatch_no":"NO","production_state":"PRODUCED","qc_state":"READY","sale_state":"OFFERED","offer_price_inr":offer,"offer":"Launch offer","guarantee":"Digital delivery / asset availability as stated on product page","packing":"Prime digital package","passport_url":f"product-passport.html?id={pid}","showroom_url":f"supreme-marking-hub.html?id={pid}","production_url":f"products/1000-digital-product-factory.html?id={pid}","generated_at":stamp}); rows.append(r)
 registry={"schema_version":2,"generated_at":stamp,"architecture":["INSTITUTE","FACTORY","QC","SHOWROOM_SALE"],"production_first":True,"verification_is_downstream":True,"batch":BATCH,"product_count":len(rows),"engine_count":src.get("engine_count",0),"family_count":len(set(r.get("family") for r in rows)),"products":rows}
 (OUT/"production-registry.json").write_text(json.dumps(registry,ensure_ascii=False,indent=2),encoding="utf-8")
 q=[{"product_id":r["id"],"unit_no":r["unit_no"],"family":r.get("family"),"engine":r.get("engine"),"work":"PRODUCE","state":"READY","qc_code":r["qc_code"],"gate_no":r["gate_no"],"dispatch_no":"NO","production_url":r["production_url"]} for r in rows]
 (OUT/"production-work-queue.jsonl").write_text("\n".join(json.dumps(x,ensure_ascii=False) for x in q)+"\n",encoding="utf-8")
 status={"generated_at":stamp,"architecture":["INSTITUTE","FACTORY","QC","SHOWROOM_SALE"],"product_count":len(rows),"produced":len(rows),"qc_ready":len(rows),"offered":len(rows),"dispatch_no":len(rows),"dispatch_yes":0,"verification_scope":"DOWNSTREAM_PRODUCT_RESULT","next_work":"expand product families and production engines without replacing canonical source"}
 (OUT/"production-status.json").write_text(json.dumps(status,ensure_ascii=False,indent=2),encoding="utf-8")
 print(json.dumps(status,ensure_ascii=False))
if __name__=="__main__": main()
