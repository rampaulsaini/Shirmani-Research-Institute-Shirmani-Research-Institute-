#!/usr/bin/env python3
"""SHIRMANI VIP screenshot factory."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import json, os, re
ROOT=Path(__file__).resolve().parents[1]; CAT=ROOT/"generated/1000-digital-products.json"; OUT=ROOT/"products/vip-screenshots"; MAN=ROOT/"generated/product-vip-screenshot-manifest.json"; BASE=os.environ.get("SHOWROOM_BASE","http://127.0.0.1:8765")
def slug(v): return re.sub(r"[^a-z0-9_-]+","-",str(v).lower()).strip("-") or "product"
def main():
    from playwright.sync_api import sync_playwright
    products=json.loads(CAT.read_text(encoding="utf-8")).get("products",[])
    if not products: raise SystemExit("Empty production catalog; refusing to publish an empty screenshot manifest.")
    OUT.mkdir(parents=True,exist_ok=True); batch=max(1,min(100,int(os.environ.get("VIP_SCREENSHOT_BATCH","25"))))
    selected=[p for p in products if not (OUT/(slug(p.get("id"))+".png")).exists()][:batch]; created=0
    with sync_playwright() as pw:
        browser=pw.chromium.launch(); page=browser.new_page(viewport={"width":1600,"height":1000},device_scale_factor=1)
        for p in selected:
            pid=str(p.get("id","")).strip()
            if not pid: continue
            page.goto(f"{BASE}/product-passport.html?id={pid}",wait_until="networkidle",timeout=60000); page.wait_for_timeout(1200)
            page.screenshot(path=str(OUT/(slug(pid)+".png")),full_page=True); created+=1
        browser.close()
    rows=[]
    for p in products:
        pid=str(p.get("id","")).strip(); path=OUT/(slug(pid)+".png")
        rows.append({"product_id":pid,"screenshot_asset":str(path.relative_to(ROOT)),"exists":path.exists(),"demo_route":f"product-demo.html?id={pid}","passport_route":f"product-passport.html?id={pid}","visual_asset":f"products/visuals/{slug(pid)}.svg","identity":"VIP_PUBLIC_PRODUCT_SCREENSHOT"})
    ready=sum(x["exists"] for x in rows); remaining=len(rows)-ready
    MAN.write_text(json.dumps({"schema_version":1,"generated_at":datetime.now(timezone.utc).isoformat(),"target":len(rows),"vip_screenshot_count":ready,"created_this_cycle":created,"remaining":remaining,"batch_size":batch,"screenshot_standard":{"viewport":"1600x1000","full_page":True,"source":"product-passport.html","presentation_asset":True},"truth_boundary":"VIP screenshot is a customer-facing presentation asset; it is not scientific verification.","products":rows},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"target":len(rows),"vip_screenshot_count":ready,"created_this_cycle":created,"remaining":remaining},ensure_ascii=False))
if __name__=="__main__": main()
