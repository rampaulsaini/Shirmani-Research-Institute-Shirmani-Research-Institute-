import json
from pathlib import Path
manifest=json.loads(Path("production/catalog.json").read_text(encoding="utf-8"))
products=manifest.get("products",[])
required=["id","name","price_inr","state","payment","delivery"]
errors=[]
for p in products:
    for key in required:
        if key not in p or p[key] in ("",None): errors.append(f"{p.get('id','UNKNOWN')}: missing {key}")
    if not isinstance(p.get("price_inr"),int) or p.get("price_inr")<=0: errors.append(f"{p.get('id','UNKNOWN')}: invalid price_inr")
    if p.get("state")!="CATALOG_LIVE": errors.append(f"{p.get('id','UNKNOWN')}: state is not CATALOG_LIVE")
status={"schema_version":"1.0","product_count":len(products),"live_catalog_products":sum(1 for p in products if p.get("state")=="CATALOG_LIVE"),"errors":errors,"gate":"PASS" if not errors and products else "FAIL"}
Path("generated").mkdir(exist_ok=True)
Path("generated/live-production-status.json").write_text(json.dumps(status,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(status,ensure_ascii=False))
if errors: raise SystemExit(1)
