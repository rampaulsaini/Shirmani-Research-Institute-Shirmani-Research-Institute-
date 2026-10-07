#!/usr/bin/env python3
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import json, os
ROOT=Path(__file__).resolve().parents[1]
SOURCES=[ROOT/"generated/concrete-production-overlay.json",ROOT/"generated/public-production-catalog.json",ROOT/"generated/production-registry.json"]
OUT=ROOT/"generated/product-media-reconciliation.json"
def load_rows():
    for src in SOURCES:
        if not src.exists(): continue
        try: data=json.loads(src.read_text(encoding="utf-8"))
        except Exception: continue
        rows=data.get("products",[])
        if rows: return rows,str(src.relative_to(ROOT))
    raise SystemExit("No concrete production source found; refusing to publish an empty media queue.")
def main():
    rows,source=load_rows(); products={}
    for p in rows:
        pid=str(p.get("id","")).strip()
        if pid: products.setdefault(pid,p)
    try: batch=max(1,min(250,int(os.environ.get("MEDIA_RECONCILE_BATCH","100"))))
    except ValueError: batch=100
    def exists(route): return (ROOT/route).exists()
    media=[]
    for pid,p in products.items():
        low=pid.lower()
        q={"product_id":pid,"name":p.get("name") or f"SHIRMANI Product {pid}","artifact_url":p.get("artifact_url") or f"products/concrete/{pid}.html","visual_route":f"products/visuals/{low}.svg","vip_screenshot_route":f"products/demos/vip/{low}.svg","demo_route":f"product-demo.html?id={pid}","mp4_route":f"products/demos/products/{low}.mp4","passport_route":f"product-passport.html?id={pid}","short_description":p.get("short_description") or p.get("description") or "Concrete customer-facing digital product.","price_inr":p.get("offer_price_inr",p.get("price_inr")),"qc_code":p.get("qc_code","QC-PENDING"),"gate_no":p.get("gate_no","GATE-PENDING"),"dispatch_no":p.get("dispatch_no","NO")}
        q["visual_exists"]=exists(q["visual_route"]); q["vip_screenshot_exists"]=exists(q["vip_screenshot_route"]); q["mp4_exists"]=exists(q["mp4_route"])
        q["media_state"]="MEDIA_COMPLETE" if q["visual_exists"] and q["vip_screenshot_exists"] and q["mp4_exists"] else ("MEDIA_PARTIAL" if q["visual_exists"] or q["vip_screenshot_exists"] or q["mp4_exists"] else "READY_TO_PRODUCE")
        media.append(q)
    pending=[p for p in media if p["media_state"]!="MEDIA_COMPLETE"]
    payload={"schema_version":2,"generated_at":datetime.now(timezone.utc).isoformat(),"source":source,"concrete_product_count":len(media),"media_complete_count":sum(p["media_state"]=="MEDIA_COMPLETE" for p in media),"visual_count":sum(p["visual_exists"] for p in media),"vip_screenshot_count":sum(p["vip_screenshot_exists"] for p in media),"real_mp4_count":sum(p["mp4_exists"] for p in media),"media_pending_count":len(pending),"next_batch":[p["product_id"] for p in pending[:batch]],"truth_boundary":"Customer-facing media demonstrates and presents a concrete product; it is not independent scientific verification.","products":media}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:payload[k] for k in ["source","concrete_product_count","media_complete_count","visual_count","vip_screenshot_count","real_mp4_count","media_pending_count"]},ensure_ascii=False))
if __name__=="__main__": main()
