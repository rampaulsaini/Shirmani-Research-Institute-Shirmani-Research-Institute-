#!/usr/bin/env python3
"""Product-specific MP4 demo factory for the SHIRMANI public showroom."""
from pathlib import Path
import json, os, re, subprocess
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"generated/1000-digital-products.json"
OUT=ROOT/"products/demos/products"
MAN=ROOT/"generated/product-specific-demo-video-manifest.json"
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

ENGINE_STEPS={
 "calculator":["Open calculator","Enter inputs","Run calculation","Inspect result","Reuse result"],
 "text":["Open text tool","Enter text","Run language task","Review output","Reuse output"],
 "nlp":["Open NLP tool","Enter text","Run NLP task","Review structured output","Reuse output"],
 "seo":["Open SEO tool","Enter title","Build SEO package","Review fields","Reuse package"],
 "research":["Open research tool","Enter research task","Add evidence","Review result","Export/use result"],
 "quality":["Open quality tool","Enter quality task","Run quality pass","Review result","Improve output"],
 "ai":["Open AI tool","Enter brief","Run production task","Review output","Reuse output"],
 "marketing":["Open marketing tool","Enter brief","Build package","Review copy","Reuse package"],
 "data":["Open data tool","Load data","Process data","Review result","Export/reuse"],
 "visual":["Open visual tool","Enter visual brief","Build visual","Review result","Export"],
 "draw":["Open drawing tool","Create layout","Refine visual","Review result","Export"],
 "game":["Open game","Start","Interact","Review state","Restart/reuse"],
 "quiz":["Open quiz","Choose topic","Run quiz","Review result","Retry/reuse"],
 "productivity":["Open productivity tool","Set objective","Build plan","Review steps","Reuse"],
 "commerce":["Open commerce tool","Enter product brief","Build offer","Review package","Reuse"],
 "quantum":["Open simulation","Choose parameters","Run classical simulation","Inspect state","Reuse result"],
}

def clean(value,limit):
    return re.sub(r"[^A-Za-z0-9 ._&:/-]+"," ",str(value or "")).strip()[:limit] or "SHIRMANI PRODUCT"
def draw(value,limit=72):
    return clean(value,limit).replace("\\","\\\\").replace(":","\\:").replace("'","\\'").replace(",","\\,")

def make_video(product,path):
    pid=clean(product.get("id"),28); name=clean(product.get("name"),48)
    engine=clean(product.get("engine"),28).lower()
    desc=clean(product.get("short_description") or product.get("description") or "Customer-facing digital product",72)
    steps=ENGINE_STEPS.get(engine,["Open product","Enter task/input","Run product module","Inspect result","Reuse output"])
    parts=[]
    for i,step in enumerate(steps,1):
        vf=",".join([
          f"drawtext=fontfile={FONT}:text='{draw(pid)}':fontcolor=white:fontsize=30:x=(w-text_w)/2:y=45",
          f"drawtext=fontfile={FONT}:text='{draw(name,48)}':fontcolor=0xe7c85b:fontsize=23:x=(w-text_w)/2:y=92",
          f"drawtext=fontfile={FONT}:text='ENGINE: {draw(engine.upper(),28)}':fontcolor=0x66ddff:fontsize=20:x=(w-text_w)/2:y=140",
          f"drawtext=fontfile={FONT}:text='{draw(desc)}':fontcolor=white:fontsize=16:x=(w-text_w)/2:y=185",
          f"drawtext=fontfile={FONT}:text='STEP {i} / {len(steps)}':fontcolor=0x66ddff:fontsize=28:x=(w-text_w)/2:y=245",
          f"drawtext=fontfile={FONT}:text='{draw(step,64)}':fontcolor=0xe7c85b:fontsize=38:x=(w-text_w)/2:y=315",
          f"drawtext=fontfile={FONT}:text='HOW TO USE  |  WHERE TO USE  |  RESULT':fontcolor=0xaeb8c7:fontsize=18:x=(w-text_w)/2:y=400",
          f"drawtext=fontfile={FONT}:text='SHIRMANI · PRODUCT-SPECIFIC DEMO':fontcolor=0x72e6aa:fontsize=18:x=(w-text_w)/2:y=650"
        ])
        part=path.with_name(path.stem+f".part{i}.mp4")
        subprocess.run(["ffmpeg","-y","-f","lavfi","-i","color=c=0x071018:s=1280x720:r=12","-vf",vf,"-t","1.25","-c:v","libx264","-preset","ultrafast","-crf","34","-pix_fmt","yuv420p","-movflags","+faststart",str(part)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        parts.append(part)
    concat=path.with_suffix(".concat.txt")
    concat.write_text("\n".join(f"file '{p.name}'" for p in parts),encoding="utf-8")
    subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i",str(concat),"-c","copy","-movflags","+faststart",str(path)],cwd=path.parent,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    for p in parts:p.unlink(missing_ok=True)
    concat.unlink(missing_ok=True)

def load_catalog():
    """Resolve the strongest available production catalog instead of silently producing zero demos."""
    candidates=[ROOT/"generated/1000-digital-products.json",ROOT/"generated/production-registry.json",ROOT/"generated/concrete-production-overlay.json"]
    for source in candidates:
        if not source.exists(): continue
        try: data=json.loads(source.read_text(encoding="utf-8"))
        except Exception: continue
        rows=data.get("products",[])
        if rows:
            normalized=[]
            for p in rows:
                pid=str(p.get("id","")).strip()
                if not pid: continue
                normalized.append({**p,"id":pid,"name":p.get("name") or f"SHIRMANI Concrete Product {pid}","engine":p.get("engine") or "package","short_description":p.get("short_description") or p.get("description") or "Customer-facing SHIRMANI digital product."})
            if normalized: return normalized,str(source.relative_to(ROOT))
    raise SystemExit("No non-empty production catalog is available; refusing to publish a zero-product demo manifest.")

def main():
    products,catalog_source=load_catalog()
    try: batch=max(1,min(50,int(os.environ.get("PRODUCT_DEMO_BATCH","10"))))
    except ValueError: batch=10
    OUT.mkdir(parents=True,exist_ok=True)
    missing=[p for p in products if not (OUT/(str(p.get("id","")).lower()+".mp4")).exists()]
    selected=missing[:batch]
    for p in selected: make_video(p,OUT/(str(p["id"]).lower()+".mp4"))
    rows=[]
    for p in products:
        pid=str(p.get("id","")); rel=f"products/demos/products/{pid.lower()}.mp4"
        rows.append({"product_id":pid,"name":p.get("name"),"engine":p.get("engine"),"short_description":p.get("short_description") or p.get("description"),"video_url":rel,"real_mp4":(ROOT/rel).exists(),"demo_route":f"product-demo.html?id={pid}","vip_screenshot_route":f"product-passport.html?id={pid}","visual_asset":f"products/visuals/{pid.lower()}.svg","long_description_route":f"product-passport.html?id={pid}","usage_steps":ENGINE_STEPS.get(str(p.get("engine","")).lower(),["Open product","Enter task/input","Run product module","Inspect result","Reuse output"]),"animated_fallback":True,"identity":"PRODUCT_SPECIFIC"})
    real=sum(x["real_mp4"] for x in rows)
    if not rows: raise SystemExit("Resolved catalog is empty; refusing to overwrite the public demo manifest.")
    MAN.write_text(json.dumps({"schema_version":2,"generated_at":datetime.now(timezone.utc).isoformat(),"catalog_source":catalog_source,"catalog_count":len(products),"real_mp4_count":real,"remaining_real_mp4":len(products)-real,"created_this_cycle":len(selected),"batch_size":batch,"mode":"PRODUCT_SPECIFIC_LIGHTWEIGHT_MP4","media_standard":{"demo_video_required":True,"visual_required":True,"vip_screenshot_route_required":True,"short_description_on_visual":True,"long_description_qr":True},"truth_boundary":"Demo media demonstrates product usage flow; it is not scientific verification.","products":rows},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"catalog_source":catalog_source,"catalog_count":len(products),"real_mp4_count":real,"created_this_cycle":len(selected),"remaining":len(products)-real},ensure_ascii=False))

if __name__=="__main__": main()
