#!/usr/bin/env python3
import json
from urllib.parse import urlparse
d=json.load(open("showroom-products.json",encoding="utf-8")); products=d.get("products",[])
required={"id","category","name","price_inr","status","store_url"}; ids=set()
if not isinstance(products,list): raise SystemExit("products must be a list")
for p in products:
    missing=required-set(p)
    if missing: raise SystemExit(f"{p.get('id','UNKNOWN')}: missing {sorted(missing)}")
    if p["id"] in ids: raise SystemExit(f"duplicate product id: {p['id']}")
    ids.add(p["id"])
    if not isinstance(p["price_inr"],(int,float)) or p["price_inr"]<0: raise SystemExit(f"bad price: {p['id']}")
    if urlparse(p["store_url"]).scheme not in ("http","https"): raise SystemExit(f"bad store url: {p['id']}")
print(f"SHOWROOM PRODUCTION OK — {len(products)} catalogue records")