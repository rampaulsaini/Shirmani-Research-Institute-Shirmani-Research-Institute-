#!/usr/bin/env python3
"""Create missing product-specific QR assets for the public showroom."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import json, os
import qrcode
from qrcode.image.svg import SvgPathImage

ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"generated/canonical-5000-product-catalog.json"
OUT=ROOT/"products/visuals/qr"
MAN=ROOT/"generated/product-qr-assets.json"
BASE="https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/product-passport.html?id="

def make_qr(payload:str)->str:
    qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=5,border=2)
    qr.add_data(payload); qr.make(fit=True)
    img=qr.make_image(image_factory=SvgPathImage)
    import io
    b=io.BytesIO(); img.save(b)
    return b.getvalue().decode("utf-8")

def main():
    from factory.canonical_product_catalog import write_catalog
    write_catalog(CAT)
    products=json.loads(CAT.read_text(encoding="utf-8")).get("products",[])
    OUT.mkdir(parents=True,exist_ok=True)
    try: batch=max(1,min(5000,int(os.environ.get("QR_BATCH","250"))))
    except ValueError: batch=250
    missing=[p for p in products if not (OUT/(str(p["id"]).lower()+".svg")).exists()]
    selected={id(p) for p in missing[:batch]}
    created=0; rows=[]
    for p in products:
        pid=str(p["id"]); path=OUT/(pid.lower()+".svg")
        url=BASE+pid
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
        "purpose":"Per-product QR for long description / product details",
        "products":rows
    },ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"target":len(products),"qr_assets":ready,"created_this_cycle":created,"remaining":len(products)-ready}))
if __name__=="__main__": main()
