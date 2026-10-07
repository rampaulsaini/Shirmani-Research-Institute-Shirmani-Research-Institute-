#!/usr/bin/env python3
"""Create missing product-specific QR assets for the public showroom."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import json, os
import qrcode
from qrcode.image.svg import SvgPathImage

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"products/visuals/qr"
MAN=ROOT/"generated/product-qr-assets.json"
SOURCES=[ROOT/"generated/1000-digital-products.json",ROOT/"showroom-products.json",ROOT/"generated/product-catalog-public.json"]
BASE="https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/showroom-product.html?id="

def make_qr(payload:str)->str:
    qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=5,border=2)
    qr.add_data(payload); qr.make(fit=True)
    img=qr.make_image(image_factory=SvgPathImage)
    import io
    b=io.BytesIO(); img.save(b)
    return b.getvalue().decode("utf-8")

def main():
    products=[]; source=None
    for CAT in SOURCES:
        if not CAT.exists() or CAT.stat().st_size == 0: continue
        try: raw=json.loads(CAT.read_text(encoding="utf-8"))
        except Exception: continue
        items=raw.get("products") if isinstance(raw,dict) else None
        if not items and isinstance(raw,dict): items=raw.get("offers")
        if isinstance(items,list) and items:
            seen=set()
            for i,p in enumerate(items):
                if not isinstance(p,dict): continue
                pid=str(p.get("id") or f"CAT-{i+1:05d}")
                if pid in seen: continue
                seen.add(pid); products.append({"id":pid,"name":str(p.get("name") or "SHIRMANI Digital Product")})
            source=str(CAT.relative_to(ROOT)); break
    if not products: raise SystemExit("No real product catalogue source available")
    OUT.mkdir(parents=True,exist_ok=True)
    try: batch=max(1,min(1000,int(os.environ.get("QR_BATCH","250"))))
    except ValueError: batch=250
    missing=[p for p in products if not (OUT/(str(p["id"]).lower()+".svg")).exists()]
    selected={id(p) for p in missing[:batch]}
    created=0; rows=[]
    for p in products:
        pid=str(p["id"]); path=OUT/(pid.lower()+".svg")
        url=BASE+pid+".html"
        if not path.exists() and id(p) in selected:
            path.write_text(make_qr(url),encoding="utf-8"); created+=1
        rows.append({"product_id":pid,"qr_asset_path":str(path.relative_to(ROOT)),
                     "long_description_url":url,"exists":path.exists(),
                     "state":"READY" if path.exists() else "PENDING"})
    ready=sum(1 for x in rows if x["exists"])
    MAN.write_text(json.dumps({
        "version":1,"generated_at":datetime.now(timezone.utc).isoformat(),
        "target":len(products),"qr_assets":ready,"created_this_cycle":created,
        "remaining":len(products)-ready,"batch_size":batch,
        "state":"READY" if ready==len(products) else "IN_PROGRESS",
        "source":source,"purpose":"Per-product QR for long description / product details",
        "products":rows
    },ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"target":len(products),"qr_assets":ready,"created_this_cycle":created,"remaining":len(products)-ready}))
if __name__=="__main__": main()
