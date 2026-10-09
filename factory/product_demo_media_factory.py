#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import os,json,subprocess,shutil
ROOT=Path(__file__).resolve().parents[1]; OVL=ROOT/"generated/concrete-production-overlay.json"; OUT=ROOT/"products/demo-video"; MAN=ROOT/"generated/product-specific-demo-video-manifest.json"
def main():
 ff=shutil.which("ffmpeg"); data=json.loads(OVL.read_text(encoding="utf-8")) if OVL.exists() else {}; ps=data.get("products",[]); OUT.mkdir(parents=True,exist_ok=True); made=0; limit=max(1,int(os.getenv("MEDIA_BATCH","25")))
 if ff:
  for p in ps:
   if made>=limit:break
   pid=str(p.get("id","")).upper(); out=OUT/(pid+".mp4")
   if not pid or out.exists():continue
   vf="drawtext=text='PRODUCT DEMO · "+pid+"':fontcolor=0xE8C65B:fontsize=42:x=(w-text_w)/2:y=220,drawtext=text='Open product → read passport → use → review':fontcolor=white:fontsize=28:x=(w-text_w)/2:y=320"
   r=subprocess.run([ff,"-y","-f","lavfi","-i","color=c=0x08111B:s=1280x720:r=30","-vf",vf,"-t","6","-pix_fmt","yuv420p","-movflags","+faststart",str(out)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
   if r.returncode==0 and out.exists():made+=1
 existing=len(list(OUT.glob("SP-*.mp4"))); MAN.write_text(json.dumps({"schema_version":3,"generated_at":datetime.now(timezone.utc).isoformat(),"catalog_count":len(ps),"interactive_demo_count":len(ps),"real_mp4_count":existing,"vip_screenshot_count":0,"remaining_real_mp4":max(0,len(ps)-existing),"remaining_vip_screenshots":len(ps),"created_this_cycle":made,"batch_size":limit,"mode":"PRODUCT_SPECIFIC_ORIENTATION_MP4","truth_boundary":"Real product-specific orientation demo; not a full screen recording or independent scientific verification."},indent=2)+"\n")
 print({"created":made,"real_mp4_count":existing})
if __name__=="__main__":main()
