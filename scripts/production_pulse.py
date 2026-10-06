#!/usr/bin/env python3
import json,datetime,collections,pathlib
root=pathlib.Path(__file__).resolve().parents[1]
catalog=json.loads((root/"generated/1000-digital-products.json").read_text(encoding="utf-8"))
products=catalog.get("products",[])
by_engine=collections.Counter(p.get("engine","unknown") for p in products)
by_family=collections.Counter(p.get("family","unknown") for p in products)
stage=collections.Counter(p.get("production_stage","unknown") for p in products)
showroom=sum(p.get("sale_status")=="SHOWROOM_READY" for p in products)
pulse={
 "generated_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),
 "mode":"PRODUCTION_FIRST_AUTOMISSION",
 "pipeline":["INSTITUTE_DISCOVERY","FACTORY_PRODUCTION","QC_GATE","SHOWROOM_PUBLIC","SALE/DISPATCH"],
 "principle":"Verification is downstream of produced results; production work continues independently.",
 "catalog_count":len(products),
 "engine_count":len(by_engine),
 "family_count":len(by_family),
 "produced_module_count":stage.get("PRODUCED_MODULE",0),
 "showroom_ready_count":showroom,
 "dispatch_default":"NO",
 "engines":dict(sorted(by_engine.items())),
 "families":dict(sorted(by_family.items())),
 "next_work":{
   "strategy":"multi-work rotation",
   "batch_size":25,
   "cycle":"5-minute scheduled pulse",
   "priority":["new product module","existing module enrichment","QC packaging","showroom enrichment","offer/metadata refresh"]
 }
}
out=root/"generated/production-pulse.json"
out.write_text(json.dumps(pulse,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"products":len(products),"engines":len(by_engine),"families":len(by_family),"showroom_ready":showroom}))
