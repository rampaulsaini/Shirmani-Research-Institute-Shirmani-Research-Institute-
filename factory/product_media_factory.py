#!/usr/bin/env python3
import json,os,subprocess,tempfile,hashlib
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"generated/1000-digital-products.json"
IMG=ROOT/"products/vip-screenshots"; VID=ROOT/"products/demos"; MAN=ROOT/"generated/product-specific-demo-video-manifest.json"
BATCH=max(1,min(50,int(os.getenv("MEDIA_BATCH","10")))); W,H=1280,720
def run(*a): subprocess.run(a,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
def esc(s): return str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")
def frame(p,n):
 pid=str(p["id"]); name=str(p.get("name","SHIRMANI Digital Product")); fam=str(p.get("family",p.get("category","Digital Product")))
 desc=" ".join(str(p.get("short_description") or p.get("description") or "Concrete digital product").split())[:145]
 steps=[("01 · WHAT","Identify the product, purpose and unique Product ID."),("02 · HOW","Open the product and follow the interactive usage guide."),("03 · WHERE","Use it in the supported browser/platform workflow."),("04 · RESULT","Review the concrete output, price/offer and release metadata."),("05 · NEXT","Open the Passport, use/order the product and leave feedback.")]
 title,body=steps[n]; h=hashlib.sha256((pid+str(n)).encode()).hexdigest()
 return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720"><defs><linearGradient id="g"><stop stop-color="#{h[:6]}"/><stop offset="1" stop-color="#{h[6:12]}"/></linearGradient></defs><rect width="1280" height="720" fill="url(#g)"/><rect x="24" y="24" width="1232" height="672" rx="32" fill="#050910" opacity=".88" stroke="#e7c85b" stroke-width="5"/><text x="65" y="82" fill="#e7c85b" font-family="DejaVu Sans" font-size="29" font-weight="bold">꙰ SHIRMANI SUPREME PRODUCT DEMO</text><text x="65" y="124" fill="#fff" font-family="DejaVu Sans" font-size="19">Shiromani Rampal Saini · Impartial Understanding · Beyond Comparison · Beyond Time</text><text x="65" y="168" fill="#66ddff" font-family="DejaVu Sans" font-size="23" font-weight="bold">{esc(pid)} · {esc(fam)}</text><text x="65" y="235" fill="#fff" font-family="DejaVu Sans" font-size="43" font-weight="bold">{esc(name[:48])}</text><text x="65" y="305" fill="#e7c85b" font-family="DejaVu Sans" font-size="33" font-weight="bold">{esc(title)}</text><text x="65" y="355" fill="#fff" font-family="DejaVu Sans" font-size="25">{esc(body)}</text><rect x="65" y="405" width="1120" height="105" rx="20" fill="#07131d" stroke="#66ddff" stroke-width="3"/><text x="90" y="447" fill="#66ddff" font-family="DejaVu Sans" font-size="20" font-weight="bold">SHORT DESCRIPTION</text><text x="90" y="482" fill="#fff" font-family="DejaVu Sans" font-size="19">{esc(desc)}</text><text x="65" y="580" fill="#6ee7a8" font-family="DejaVu Sans" font-size="20" font-weight="bold">INTERACTIVE DEMO · PRODUCT PASSPORT · QC/GATE · SHOWROOM ORDER ROUTE</text><text x="65" y="625" fill="#aeb8c8" font-family="DejaVu Sans" font-size="17">Presentation media only · not independent scientific verification</text></svg>'''
def main():
 products=json.loads(CAT.read_text(encoding="utf-8"))["products"]; IMG.mkdir(parents=True,exist_ok=True); VID.mkdir(parents=True,exist_ok=True)
 old=json.loads(MAN.read_text()) if MAN.exists() and MAN.read_text().strip() else {}; rows={x["product_id"]:x for x in old.get("products",[])}; todo=[]
 for p in products:
  k=str(p["id"]).lower()
  if not (VID/(k+".mp4")).exists() or not (IMG/(k+".png")).exists(): todo.append(p)
  if len(todo)>=BATCH: break
 with tempfile.TemporaryDirectory() as td:
  td=Path(td)
  for p in todo:
   k=str(p["id"]).lower(); fs=[]
   for n in range(5):
    s=td/f"{k}-{n}.svg"; q=td/f"{k}-{n}.png"; s.write_text(frame(p,n),encoding="utf-8"); run("convert",str(s),"-resize",f"{W}x{H}",str(q)); fs.append(q)
   (IMG/(k+".png")).write_bytes(fs[-1].read_bytes()); c=td/f"{k}.txt"; c.write_text("\n".join([f"file '{x}'\nduration 1.2" for x in fs])+f"\nfile '{fs[-1]}'\n")
   run("ffmpeg","-y","-f","concat","-safe","0","-i",str(c),"-r","24","-c:v","libx264","-pix_fmt","yuv420p","-movflags","+faststart",str(VID/(k+".mp4")))
   pid=str(p["id"]); rows[pid]={"product_id":pid,"name":p.get("name"),"video_asset":f"products/demos/{k}.mp4","vip_screenshot":f"products/vip-screenshots/{k}.png","video_format":"mp4","video_resolution":"1280x720","duration_seconds":6,"demo_type":"PRODUCT_SPECIFIC_PRESENTATION_AND_USAGE_FLOW","interactive_demo":"demo-video.html?id="+pid,"passport":"product-passport.html?id="+pid,"state":"READY_FOR_PUBLIC_SHOWROOM","truth_boundary":"Demo media demonstrates customer-facing usage flow; it is not independent scientific verification"}
 mp4=sum((VID/(str(p["id"]).lower()+".mp4")).exists() for p in products); png=sum((IMG/(str(p["id"]).lower()+".png")).exists() for p in products)
 ordered=[rows[str(p["id"])] for p in products if str(p["id"]) in rows]
 MAN.write_text(json.dumps({"schema_version":2,"generated_at":datetime.now(timezone.utc).isoformat(),"catalog_count":len(products),"interactive_demo_count":len(products),"real_mp4_count":mp4,"vip_screenshot_count":png,"remaining_real_mp4":len(products)-mp4,"remaining_vip_screenshots":len(products)-png,"created_this_cycle":len(todo),"batch_size":BATCH,"mode":"PRODUCT_SPECIFIC_LIGHTWEIGHT_MP4","truth_boundary":"Demo media demonstrates product usage flow; it is not independent scientific verification.","products":ordered},ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__": main()
