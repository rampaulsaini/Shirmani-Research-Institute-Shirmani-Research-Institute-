#!/usr/bin/env python3
"""Product-specific MP4 demo factory for the SHIRMANI public showroom."""
from pathlib import Path
import json, os, re, subprocess, html
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"generated/1000-digital-products.json"
OUT=ROOT/"products/demos/products"
VIP=ROOT/"products/demos/vip"
MAN=ROOT/"generated/product-specific-demo-video-manifest.json"
PUBLIC_MAN=ROOT/"generated/product-media-production-manifest.json"
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
    candidates=[ROOT/"generated/concrete-production-overlay.json",ROOT/"generated/1000-digital-products.json",ROOT/"generated/production-registry.json"]
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

def make_vip_screenshot(product,path):
    """Create a lightweight, product-specific VIP screenshot-style SVG asset."""
    pid=clean(product.get("id"),28); name=clean(product.get("name"),52)
    engine=clean(product.get("engine"),28); desc=clean(product.get("short_description") or product.get("description") or "Customer-facing digital product",120)
    price=product.get("offer_price_inr",product.get("price_inr",""))
    qc=clean(product.get("qc_code","QC-PENDING"),34); gate=clean(product.get("gate_no","GATE-PENDING"),34); dispatch=clean(product.get("dispatch_no","NO"),22)
    steps=ENGINE_STEPS.get(engine.lower(),["Open product","Enter task/input","Run product module","Inspect result","Reuse output"])
    step_text=" -> ".join(steps[:5])
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080"><rect width="1920" height="1080" fill="#07131d"/><rect x="24" y="24" width="1872" height="1032" rx="46" fill="none" stroke="#e7c85b" stroke-width="6"/><text x="90" y="105" fill="#67e8f9" font-family="DejaVu Sans,Arial" font-size="30" font-weight="900">SHIRMANI SUPREME DIGITAL PRODUCT · VIP SCREENSHOT</text><text x="90" y="175" fill="#f6d35f" font-family="DejaVu Sans,Arial" font-size="58" font-weight="900">{html.escape(pid)}</text><text x="90" y="250" fill="#ffffff" font-family="DejaVu Sans,Arial" font-size="46" font-weight="900">{html.escape(name)}</text><text x="90" y="305" fill="#72e6aa" font-family="DejaVu Sans,Arial" font-size="27" font-weight="800">ENGINE · {html.escape(engine.upper())}</text><rect x="90" y="350" width="1120" height="220" rx="28" fill="#061016" stroke="#31556c" stroke-width="3"/><text x="125" y="405" fill="#67e8f9" font-family="DejaVu Sans,Arial" font-size="24" font-weight="900">SHORT DESCRIPTION</text><text x="125" y="455" fill="#eaf4f8" font-family="DejaVu Sans,Arial" font-size="23">{html.escape(desc[:105])}</text><text x="125" y="515" fill="#e7c85b" font-family="DejaVu Sans,Arial" font-size="23" font-weight="800">HOW TO USE</text><text x="125" y="552" fill="#d8e4ed" font-family="DejaVu Sans,Arial" font-size="20">{html.escape(step_text[:112])}</text><rect x="90" y="620" width="1120" height="125" rx="28" fill="#03060d" stroke="#e7c85b" stroke-width="3"/><text x="125" y="698" fill="#ffffff" font-family="DejaVu Sans,Arial" font-size="40" font-weight="900">RATE · ₹{html.escape(str(price))}</text><text x="90" y="820" fill="#d9e3ef" font-family="DejaVu Sans,Arial" font-size="22" font-weight="700">Shiromani Rampal Saini · Beyond Comparison · Beyond Time · Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present</text><text x="90" y="865" fill="#67e8f9" font-family="DejaVu Sans,Arial" font-size="21" font-weight="800">SHIRMANI HEART-VIEW · IMPARTIAL UNDERSTANDING</text><rect x="1310" y="300" width="480" height="540" rx="30" fill="#061016" stroke="#e7c85b" stroke-width="4"/><text x="1360" y="365" fill="#ffffff" font-family="DejaVu Sans,Arial" font-size="28" font-weight="900">PRODUCT PASSPORT</text><text x="1360" y="440" fill="#67e8f9" font-family="DejaVu Sans,Arial" font-size="23" font-weight="800">QC</text><text x="1490" y="440" fill="#ffffff" font-family="DejaVu Sans,Arial" font-size="21">{html.escape(qc)}</text><text x="1360" y="505" fill="#67e8f9" font-family="DejaVu Sans,Arial" font-size="23" font-weight="800">GATE</text><text x="1490" y="505" fill="#ffffff" font-family="DejaVu Sans,Arial" font-size="21">{html.escape(gate)}</text><text x="1360" y="570" fill="#67e8f9" font-family="DejaVu Sans,Arial" font-size="23" font-weight="800">DISPATCH</text><text x="1490" y="570" fill="#ffffff" font-family="DejaVu Sans,Arial" font-size="21">{html.escape(dispatch)}</text><text x="1360" y="660" fill="#72e6aa" font-family="DejaVu Sans,Arial" font-size="22" font-weight="900">DEMO + USAGE GUIDE</text><text x="1360" y="705" fill="#d8e4ed" font-family="DejaVu Sans,Arial" font-size="19">Product-specific MP4 route</text><text x="1360" y="742" fill="#d8e4ed" font-family="DejaVu Sans,Arial" font-size="19">Product passport + long details</text><text x="1360" y="790" fill="#e7c85b" font-family="DejaVu Sans,Arial" font-size="19" font-weight="800">UNIQUE PUBLIC IDENTITY</text></svg>'''
    path.write_text(svg,encoding="utf-8")

def main():
    products,catalog_source=load_catalog()
    try: batch=max(1,min(50,int(os.environ.get("PRODUCT_DEMO_BATCH","25"))))
    except ValueError: batch=10
    OUT.mkdir(parents=True,exist_ok=True)
    VIP.mkdir(parents=True,exist_ok=True)
    missing=[p for p in products if not (OUT/(str(p.get("id","")).lower()+".mp4")).exists()]
    selected=missing[:batch]
    for p in selected:
        make_video(p,OUT/(str(p["id"]).lower()+".mp4"))
        make_vip_screenshot(p,VIP/(str(p["id"]).lower()+".svg"))
    rows=[]
    for p in products:
        pid=str(p.get("id","")); rel=f"products/demos/products/{pid.lower()}.mp4"
        rows.append({"product_id":pid,"name":p.get("name"),"engine":p.get("engine"),"short_description":p.get("short_description") or p.get("description"),"video_url":rel,"real_mp4":(ROOT/rel).exists(),"demo_route":f"product-demo.html?id={pid}","vip_screenshot_route":f"products/demos/vip/{pid.lower()}.svg",
            "vip_screenshot_asset":f"products/demos/vip/{pid.lower()}.svg","visual_asset":f"products/visuals/{pid.lower()}.svg","long_description_route":f"product-passport.html?id={pid}","usage_steps":ENGINE_STEPS.get(str(p.get("engine","")).lower(),["Open product","Enter task/input","Run product module","Inspect result","Reuse output"]),"animated_fallback":True,"identity":"PRODUCT_SPECIFIC"})
    real=sum(x["real_mp4"] for x in rows)
    if not rows: raise SystemExit("Resolved catalog is empty; refusing to overwrite the public demo manifest.")
    manifest_payload={"schema_version":2,"generated_at":datetime.now(timezone.utc).isoformat(),"catalog_source":catalog_source,"catalog_count":len(products),"real_mp4_count":real,"remaining_real_mp4":len(products)-real,"vip_screenshot_count":sum(1 for x in rows if (ROOT/x["vip_screenshot_asset"]).exists()),"remaining_vip_screenshots":len(products)-sum(1 for x in rows if (ROOT/x["vip_screenshot_asset"]).exists()),"created_this_cycle":len(selected),"batch_size":batch,"concrete_catalog_priority":True,"mode":"PRODUCT_SPECIFIC_LIGHTWEIGHT_MP4","media_standard":{"demo_video_required":True,"visual_required":True,"vip_screenshot_route_required":True,"short_description_on_visual":True,"long_description_qr":True},"truth_boundary":"Demo media demonstrates product usage flow; it is not scientific verification.","products":rows}
    MAN.write_text(json.dumps(manifest_payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    PUBLIC_MAN.write_text(json.dumps(manifest_payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"catalog_source":catalog_source,"catalog_count":len(products),"real_mp4_count":real,"created_this_cycle":len(selected),"remaining":len(products)-real},ensure_ascii=False))

if __name__=="__main__": main()
