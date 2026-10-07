#!/usr/bin/env python3
import json, os, subprocess
from pathlib import Path
from datetime import datetime, timezone
from PIL import Image, ImageDraw, ImageFont
import qrcode

ROOT=Path(__file__).resolve().parents[1]; BATCH=int(os.environ.get("MEDIA_BATCH_SIZE","10"))
VID=ROOT/"products/demos"; VIP=ROOT/"products/vip-screenshots"; VID.mkdir(parents=True,exist_ok=True); VIP.mkdir(parents=True,exist_ok=True)
REG=ROOT/"generated/concrete-production-overlay.json"; PAS=ROOT/"generated/PRODUCT-PASSPORTS.jsonl"; MM=ROOT/"generated/product-media-production-manifest.json"; VM=ROOT/"generated/product-vip-screenshot-manifest.json"
def font(n,b=False):
 p="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if b else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
 return ImageFont.truetype(p,n)
def products():
 d=json.loads(REG.read_text()); ps={}
 if PAS.exists():
  for line in PAS.read_text().splitlines():
   if line.strip(): x=json.loads(line); ps[x.get("id")]=x
 out=[]
 for p in d.get("products",[]):
  if str(p.get("production_state","")).upper()=="PRODUCED":
   x=dict(ps.get(p.get("id"),{})); x.update(p); out.append(x)
 return out
def make_vip(p):
 pid=str(p["id"]); name=str(p.get("name",pid)); desc=str(p.get("description") or p.get("short_description") or "SHIRMANI digital product.")
 im=Image.new("RGB",(1920,1080),(7,13,21)); d=ImageDraw.Draw(im); d.rounded_rectangle((35,35,1885,1045),35,outline=(240,207,90),width=5,fill=(11,20,31))
 d.text((80,70),"꙰ SHIRMANI RESEARCH INSTITUTE",font=font(42,True),fill=(240,207,90))
 d.text((80,130),"Shiromani Rampal Saini · Impartial Understanding · Beyond Comparison · Beyond Time · Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present",font=font(24),fill=(102,221,255))
 d.text((80,220),name[:58],font=font(54,True),fill=(245,247,251)); d.text((80,305),pid+" · "+str(p.get("category") or p.get("family") or "digital product"),font=font(30,True),fill=(121,226,162))
 d.text((80,390),desc[:145],font=font(31),fill=(230,235,242)); d.text((80,650),"HOW TO USE",font=font(30,True),fill=(240,207,90)); d.text((80,710),"Open → follow guide → inspect result → review/improve",font=font(28),fill=(190,202,216))
 qr=qrcode.make("https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/product-passport.html?id="+pid).convert("RGB").resize((360,360)); im.paste(qr,(1490,620)); d.text((1480,995),"QR · Product Passport",font=font(24,True),fill=(102,221,255))
 im.save(VIP/(pid.lower()+".png"),"PNG",optimize=True)
def make_video(p):
 pid=str(p["id"]); name=str(p.get("name",pid)); desc=str(p.get("description") or p.get("short_description") or "SHIRMANI digital product."); w=ROOT/".media-work"/pid.lower(); w.mkdir(parents=True,exist_ok=True)
 steps=[("01 · WHAT",name),("02 · HOW","Open the product and follow the on-page instructions."),("03 · WHERE","Use the Product Passport for the applicable route."),("04 · RESULT","Inspect the concrete customer-facing output."),("05 · NEXT","Read the passport, use/order and submit feedback.")]
 for i,(h,body) in enumerate(steps):
  im=Image.new("RGB",(1280,720),(5,10,16)); d=ImageDraw.Draw(im); d.rectangle((30,30,1250,690),outline=(240,207,90),width=4)
  d.text((70,65),"꙰ SHIRMANI PRODUCT DEMO",font=font(34,True),fill=(240,207,90)); d.text((70,125),pid,font=font(26,True),fill=(102,221,255)); d.text((70,205),h,font=font(58,True),fill=(245,247,251)); d.text((70,300),body[:70],font=font(34),fill=(121,226,162)); d.text((70,380),desc[:105],font=font(26),fill=(190,202,216)); d.text((70,600),"Interactive guide + Product Passport + customer feedback loop",font=font(24),fill=(174,186,202)); im.save(w/f"{i:02d}.png")
 subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate","1/2","-i",str(w/"%02d.png"),"-c:v","libx264","-pix_fmt","yuv420p","-movflags","+faststart",str(VID/(pid.lower()+".mp4"))],check=True)
def main():
 ps=products()
 try: m=json.loads(MM.read_text())
 except: m={}
 rows={x["product_id"]:x for x in m.get("products",[])}; made=0
 for p in [x for x in ps if x["id"] not in rows][:BATCH]:
  make_video(p); make_vip(p); pid=str(p["id"]); rows[pid]={"product_id":pid,"video_asset":f"products/demos/{pid.lower()}.mp4","vip_screenshot":f"products/vip-screenshots/{pid.lower()}.png","interactive_demo":f"demo-video.html?id={pid}","passport":f"product-passport.html?id={pid}","status":"PRODUCED_MEDIA"}; made+=1
 total=len(ps); mp4=sum(bool(x.get("video_asset")) for x in rows.values()); vip=sum(bool(x.get("vip_screenshot")) for x in rows.values()); now=datetime.now(timezone.utc).isoformat()
 MM.write_text(json.dumps({"schema_version":2,"generated_at":now,"catalog_count":total,"interactive_demo_count":total,"real_mp4_count":mp4,"remaining_real_mp4":max(0,total-mp4),"vip_screenshot_count":vip,"remaining_vip_screenshots":max(0,total-vip),"created_this_cycle":made,"batch_size":BATCH,"mode":"PRODUCT_SPECIFIC_MP4_FACTORY","truth_boundary":"Demo media demonstrates product usage flow; it is not scientific verification.","products":sorted(rows.values(),key=lambda x:x["product_id"])},ensure_ascii=False,indent=2)+"\n")
 VM.write_text(json.dumps({"schema_version":1,"generated_at":now,"vip_screenshot_count":vip,"remaining_vip_screenshots":max(0,total-vip),"products":sorted([{"product_id":k,"screenshot":v["vip_screenshot"]} for k,v in rows.items()],key=lambda x:x["product_id"])},ensure_ascii=False,indent=2)+"\n")
 print(f"MEDIA_FACTORY products={total} created={made} mp4={mp4} vip={vip}")
if __name__=="__main__": main()
