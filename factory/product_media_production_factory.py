#!/usr/bin/env python3
"""SHIRMANI product-specific demo media factory."""
from __future__ import annotations
import json, os, re, subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OVERLAY=ROOT/"generated/concrete-production-overlay.json"
MANIFEST=ROOT/"generated/product-media-production-manifest.json"
VIDEO_DIR=ROOT/"generated/product-media/mp4"
SHOT_DIR=ROOT/"products/vip-screenshots"
BATCH_SIZE=int(os.environ.get("PRODUCT_MEDIA_BATCH","20"))
FPS=24; DURATION=4; W,H=1280,720
IDENTITY=("Shiromani Rampal Saini · Impartial Understanding · Beyond Comparison · "
          "Beyond Time · Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present")

def now(): return datetime.now(timezone.utc).isoformat()
def safe(s): return re.sub(r"[^A-Za-z0-9._-]+","-",str(s)).strip("-")[:90]
def load(p,d):
    try:return json.loads(p.read_text(encoding="utf-8"))
    except Exception:return d
def run(cmd): return subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

def make_video(p,out):
    name=safe(p.get("name") or p["id"]).replace(":","\\:")
    ident=IDENTITY.replace(":","\\:")
    steps="OPEN / USE  |  READ SHORT DESCRIPTION  |  TRY THE TOOL  |  VIEW PASSPORT".replace(":","\\:")
    vf=(f"drawtext=text='{name}':fontcolor=white:fontsize=42:x=(w-text_w)/2:y=170,"
        f"drawtext=text='{ident}':fontcolor=gold:fontsize=22:x=(w-text_w)/2:y=245,"
        f"drawtext=text='{steps}':fontcolor=white:fontsize=22:x=(w-text_w)/2:y=330,"
        f"drawtext=text='Product ID: {p['id']}':fontcolor=cyan:fontsize=20:x=(w-text_w)/2:y=405,"
        "drawtext=text='DEMO • NOT A SALE / PAYMENT / VERIFICATION':fontcolor=white:fontsize=18:x=(w-text_w)/2:y=525")
    r=run(["ffmpeg","-y","-f","lavfi","-i",f"color=c=0x081019:s={W}x{H}:r={FPS}:d={DURATION}",
           "-vf",vf,"-c:v","libx264","-pix_fmt","yuv420p","-movflags","+faststart","-an",str(out)])
    return r.returncode==0

def make_vip(p,out):
    name=str(p.get("name") or p["id"]).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    short=str(p.get("description") or "Concrete public digital product.")[:180].replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    ident=IDENTITY.replace("&","&amp;")
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080"><defs><linearGradient id="g" x1="0" x2="1"><stop stop-color="#07101a"/><stop offset="1" stop-color="#16283b"/></linearGradient></defs><rect width="1920" height="1080" fill="url(#g)"/><rect x="38" y="38" width="1844" height="1004" rx="34" fill="none" stroke="#d4af37" stroke-width="5"/><text x="90" y="110" fill="#f2cf58" font-size="34" font-family="Arial">꙰ SHIRMANI HEART-VIEW</text><text x="90" y="154" fill="#dce7f2" font-size="21" font-family="Arial">{ident}</text><text x="960" y="350" text-anchor="middle" fill="#f2cf58" font-size="58" font-family="Arial" font-weight="700">{name}</text><text x="960" y="430" text-anchor="middle" fill="#dce7f2" font-size="28" font-family="Arial">{short}</text><text x="960" y="515" text-anchor="middle" fill="#67e8f9" font-size="25" font-family="Arial">PRODUCT ID: {p["id"]}</text><text x="960" y="610" text-anchor="middle" fill="#79e2a2" font-size="28" font-family="Arial">SHORT DESCRIPTION • DEMO • PASSPORT • QC GATE</text><text x="960" y="925" text-anchor="middle" fill="#aeb9c8" font-size="20" font-family="Arial">VIP PRODUCT SCREENSHOT • 16:9 • 1920×1080</text></svg>'''
    tmp=out.with_suffix(".svg"); tmp.write_text(svg,encoding="utf-8")
    r=run(["convert",str(tmp),str(out)])
    try:tmp.unlink()
    except OSError:pass
    return r.returncode==0

def main():
    VIDEO_DIR.mkdir(parents=True,exist_ok=True); SHOT_DIR.mkdir(parents=True,exist_ok=True)
    data=load(OVERLAY,{})
    products=[p for p in data.get("products",[]) if p.get("production_state")=="PRODUCED"]
    manifest=load(MANIFEST,{"schema_version":1,"principle":"Product-specific media is production output; verification remains downstream.","products":{}})
    existing=manifest.setdefault("products",{})
    candidates=[p for p in products if not (existing.get(p["id"],{}).get("mp4",{}).get("status")=="PRODUCED" and existing.get(p["id"],{}).get("vip_screenshot",{}).get("status")=="PRODUCED")][:BATCH_SIZE]
    results=[]; ffmpeg_ok=run(["ffmpeg","-version"]).returncode==0
    for p in candidates:
        pid=p["id"].lower(); vp=VIDEO_DIR/f"{pid}.mp4"; sp=SHOT_DIR/f"{pid}.png"
        video_ok=ffmpeg_ok and make_video(p,vp); shot_ok=make_vip(p,sp)
        existing[p["id"]]={"product_id":p["id"],"name":p.get("name"),"updated_at":now(),
          "demo_route":f"demo-video.html?id={p['id']}","passport_route":f"product-passport.html?id={p['id']}",
          "visual_route":f"products/visuals/{pid}.svg",
          "mp4":{"status":"PRODUCED" if video_ok else "PENDING_RUNNER","path":str(vp.relative_to(ROOT)) if video_ok else None,"duration_seconds":DURATION if video_ok else None,"resolution":"1280x720" if video_ok else None},
          "vip_screenshot":{"status":"PRODUCED" if shot_ok else "PENDING","path":str(sp.relative_to(ROOT)) if shot_ok else None,"resolution":"1920x1080" if shot_ok else None},
          "integrity":{"source_product_id":p["id"],"production_is_not_verification":True}}
        results.append({"id":p["id"],"mp4":video_ok,"vip":shot_ok})
    manifest.update({"generated_at":now(),"batch_size":BATCH_SIZE,"source_concrete_product_count":len(products),
      "real_mp4_count":sum(1 for v in existing.values() if v.get("mp4",{}).get("status")=="PRODUCED"),
      "vip_screenshot_count":sum(1 for v in existing.values() if v.get("vip_screenshot",{}).get("status")=="PRODUCED"),
      "demo_route_count":len(products),"remaining_media":max(0,len(products)-sum(1 for v in existing.values() if v.get("mp4",{}).get("status")=="PRODUCED")),"last_batch":results,
      "integrity":{"source_bound":True,"independent_verification_claim":False,"commercial_sale_claim":False}})
    MANIFEST.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"source_products":len(products),"batch":len(results),"real_mp4":manifest["real_mp4_count"],"vip":manifest["vip_screenshot_count"]},ensure_ascii=False))
if __name__=="__main__": main()
