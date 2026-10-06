#!/usr/bin/env python3
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
d=json.load((ROOT/"showroom-products.json").open(encoding="utf-8"))
products=d.get("products",[])
required={"id","category","name","price_inr","status","store_url"}
ids=set()
if not isinstance(products,list):
    raise SystemExit("products must be a list")
for p in products:
    missing=required-set(p)
    if missing:
        raise SystemExit(f"{p.get('id','UNKNOWN')}: missing {sorted(missing)}")
    pid=p["id"]
    if pid in ids:
        raise SystemExit(f"duplicate product id: {pid}")
    ids.add(pid)
    if not isinstance(p["price_inr"],(int,float)) or p["price_inr"]<0:
        raise SystemExit(f"bad price: {pid}")
    url=str(p["store_url"]).strip()
    if not url:
        raise SystemExit(f"empty store url: {pid}")
    parsed=urlparse(url)
    if parsed.scheme in ("http","https"):
        pass
    elif parsed.scheme:
        raise SystemExit(f"unsupported store url scheme: {pid}")
    else:
        # Repository-relative customer routes are valid public showroom destinations.
        target=(ROOT/url.lstrip("/")).resolve()
        if not target.is_file():
            raise SystemExit(f"missing relative store target: {pid} -> {url}")

print(f"SHOWROOM PRODUCTION OK — {len(products)} catalogue records")
