#!/usr/bin/env python3
"""Product-specific MP4 demo factory.

Creates small, reproducible customer-facing MP4 demos from each product's
existing 4K identity visual. The video is intentionally a presentation/demo
asset, not a scientific verification claim.

Environment:
  PRODUCT_DEMO_BATCH: max products to materialize per cycle (default 25)
"""
from __future__ import annotations
import json, os, subprocess, tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
GEN=ROOT/"generated"
CAT=GEN/"1000-digital-products.json"
VIS=ROOT/"products/visuals"
OUT=ROOT/"products/demos/products"
MAN=GEN/"product-specific-demo-video-manifest.json"
BATCH=max(1,int(os.environ.get("PRODUCT_DEMO_BATCH","25")))
FPS=24
DURATION=6

def now(): return datetime.now(timezone.utc).isoformat()

def run(cmd):
    subprocess.run(cmd,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

def main():
    catalog=json.loads(CAT.read_text(encoding="utf-8")).get("products",[])
    previous={}
    if MAN.exists():
        try:
            previous=json.loads(MAN.read_text(encoding="utf-8"))
        except Exception:
            previous={}
    rows={str(x.get("product_id")):x for x in previous.get("products",[]) if isinstance(x,dict)}
    OUT.mkdir(parents=True,exist_ok=True)
    changed=0

    todo=[]
    for p in catalog:
        pid=str(p["id"])
        target=OUT/f"{pid.lower()}.mp4"
        if not target.exists() or target.stat().st_size < 1000:
            todo.append(p)

    for p in todo[:BATCH]:
        pid=str(p["id"])
        name=str(p.get("name","SHIRMANI Digital Product"))
        visual=VIS/f"{pid.lower()}.svg"
        target=OUT/f"{pid.lower()}.mp4"
        if not visual.exists():
            continue
        with tempfile.TemporaryDirectory(prefix="shirmani-demo-") as td:
            png=Path(td)/"frame.png"
            # Convert the already-produced product identity visual to a frame.
            run(["rsvg-convert","-w","1280","-h","720",str(visual),"-o",str(png)])
            # A short Ken-Burns-style presentation with product-specific text.
            # No claim of product functionality is added beyond the source catalog.
            run([
                "ffmpeg","-y","-loop","1","-i",str(png),
                "-vf",f"scale=1280:720,zoompan=z='min(zoom+0.0007,1.04)':d={DURATION*FPS}:s=1280x720:fps={FPS}",
                "-t",str(DURATION),"-an",
                "-c:v","libx264","-preset","veryfast","-crf","30",
                "-pix_fmt","yuv420p","-movflags","+faststart",str(target)
            ])
        rows[pid]={
            "product_id":pid,
            "name":name,
            "video_path":str(target.relative_to(ROOT)),
            "duration_seconds":DURATION,
            "resolution":"1280x720",
            "source_visual":str(visual.relative_to(ROOT)),
            "production_state":"PRODUCED",
            "usage":"Product-specific visual demo/presentation",
            "qc_state":"READY_FOR_QC",
            "dispatch":"NO",
            "generated_at":now()
        }
        changed+=1

    ordered=[rows[str(p["id"])] for p in catalog if str(p["id"]) in rows]
    manifest={
        "schema_version":1,
        "generated_at":now(),
        "factory":"SHIRMANI Product-Specific MP4 Demo Factory",
        "catalog_target":len(catalog),
        "videos_produced":len(ordered),
        "remaining":max(0,len(catalog)-len(ordered)),
        "produced_this_cycle":changed,
        "batch_size":BATCH,
        "format":"MP4/H.264",
        "resolution":"1280x720",
        "duration_seconds":DURATION,
        "customer_route":"product-demo.html?id=PRODUCT_ID",
        "truth_boundary":"Demo video is a customer-facing production asset; QC, dispatch and independent verification remain separate states.",
        "products":ordered
    }
    MAN.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:manifest[k] for k in ["catalog_target","videos_produced","remaining","produced_this_cycle"]}))

if __name__=="__main__":
    main()
