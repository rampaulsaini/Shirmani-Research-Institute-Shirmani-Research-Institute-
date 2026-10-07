#!/usr/bin/env python3
"""Build a scalable product-demo media manifest and MP4 production queue."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import json, os, urllib.parse

ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"generated/1000-digital-products.json"
OUT=ROOT/"generated/product-demo-media-manifest.json"
BASE="https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/"

def main():
    products=json.loads(CAT.read_text(encoding="utf-8")).get("products",[])
    try: batch=max(1,min(1000,int(os.environ.get("DEMO_MP4_BATCH","250"))))
    except ValueError: batch=250
    rows=[]
    for p in products:
        pid=str(p["id"]); engine=str(p.get("engine","package"))
        path=f"products/demos/products/{pid.lower()}.mp4"
        rows.append({
            "product_id":pid,"name":p.get("name"),"engine":engine,
            "product_demo_route":f"product-demo.html?id={urllib.parse.quote(pid)}",
            "product_mp4_path":path,
            "engine_mp4_path":f"products/demos/{engine}.mp4",
            "poster_path":f"products/visuals/{pid.lower()}.svg",
            "vip_screenshot_path":f"products/vip-screenshots/{pid.lower()}.svg",
            "status":"PRODUCT_MP4_READY" if (ROOT/path).exists() else "PRODUCT_MP4_PENDING"
        })
    missing=[r["product_id"] for r in rows if r["status"]=="PRODUCT_MP4_PENDING"]
    selected=set(missing[:batch])
    for r in rows:
        if r["product_id"] in selected: r["status"]="PRODUCT_MP4_QUEUED_THIS_CYCLE"
    ready=sum(r["status"]=="PRODUCT_MP4_READY" for r in rows)
    OUT.write_text(json.dumps({
        "schema_version":1,"generated_at":datetime.now(timezone.utc).isoformat(),
        "target":len(rows),"product_mp4_ready":ready,
        "product_mp4_remaining":len(rows)-ready,"queued_this_cycle":len(selected),
        "batch_size":batch,
        "architecture":"product-specific MP4 when materialized; engine-family MP4 fallback; animated browser demo is always available",
        "public_base":BASE,
        "truth_boundary":"A demo asset demonstrates product usage; it does not claim sale, dispatch or independent scientific verification.",
        "products":rows
    },ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"target":len(rows),"ready":ready,"remaining":len(rows)-ready,"queued":len(selected)},ensure_ascii=False))
if __name__=="__main__": main()
