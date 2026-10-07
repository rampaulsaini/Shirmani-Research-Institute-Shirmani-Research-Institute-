#!/usr/bin/env python3
"""Product-specific demo video factory for the SHIRMANI showroom."""
from pathlib import Path
import json, os, re, subprocess
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"generated/1000-digital-products.json"
OUT=ROOT/"products/demos/products"
MAN=ROOT/"generated/product-specific-demo-video-manifest.json"
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def clean(value, limit):
    return re.sub(r"[^A-Za-z0-9 ._&-]+", " ", str(value or "")).strip()[:limit] or "SHIRMANI PRODUCT"

def make_video(product, path):
    pid=clean(product.get("id"),24)
    name=clean(product.get("name"),42)
    engine=clean(product.get("engine"),24)
    vf=",".join([
        f"drawtext=fontfile={FONT}:text='{pid}':fontcolor=white:fontsize=30:x=(w-text_w)/2:y=60",
        f"drawtext=fontfile={FONT}:text='{name}':fontcolor=0xe7c85b:fontsize=23:x=(w-text_w)/2:y=115",
        f"drawtext=fontfile={FONT}:text='ENGINE: {engine}':fontcolor=0x66ddff:fontsize=20:x=(w-text_w)/2:y=165",
        f"drawtext=fontfile={FONT}:text='OPEN  ->  USE  ->  REVIEW  ->  QR DETAILS':fontcolor=white:fontsize=19:x=(w-text_w)/2:y=220",
        f"drawtext=fontfile={FONT}:text='HOW TO USE  |  WHERE TO USE  |  RESULT':fontcolor=0xaeb8c7:fontsize=17:x=(w-text_w)/2:y=275",
    ])
    subprocess.run(["ffmpeg","-y","-f","lavfi","-i","color=c=0x071018:s=640x360:r=12",
                    "-vf",vf,"-t","2.4","-c:v","libx264","-preset","ultrafast","-crf","35",
                    "-pix_fmt","yuv420p","-movflags","+faststart",str(path)],
                   check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

def main():
    products=json.loads(CAT.read_text(encoding="utf-8")).get("products",[])
    batch=max(1,min(50,int(os.environ.get("PRODUCT_DEMO_BATCH","10"))))
    OUT.mkdir(parents=True,exist_ok=True)
    missing=[p for p in products if not (OUT/(str(p.get("id","")).lower()+".mp4")).exists()]
    for product in missing[:batch]:
        make_video(product, OUT/(str(product["id"]).lower()+".mp4"))
    rows=[]
    for product in products:
        pid=str(product.get("id",""))
        rel=f"products/demos/products/{pid.lower()}.mp4"
        rows.append({"product_id":pid,"name":product.get("name"),"engine":product.get("engine"),
                     "video_url":rel,"real_mp4":(ROOT/rel).exists(),
                     "demo_route":f"product-demo.html?id={pid}","animated_fallback":True})
    real=sum(1 for row in rows if row["real_mp4"])
    MAN.write_text(json.dumps({
        "schema_version":1,"generated_at":datetime.now(timezone.utc).isoformat(),
        "catalog_count":len(products),"real_mp4_count":real,
        "remaining_real_mp4":len(products)-real,
        "created_this_cycle":min(batch,len(missing)),
        "mode":"PRODUCT_SPECIFIC_LIGHTWEIGHT_MP4",
        "truth_boundary":"Demo media demonstrates product usage flow; it is not scientific verification.",
        "products":rows
    },ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"catalog_count":len(products),"real_mp4_count":real,"remaining":len(products)-real}))
if __name__=="__main__":
    main()
