#!/usr/bin/env python3
"""SHIRMANI concrete product factory: production-first, customer-visible artifacts."""

from __future__ import annotations
import argparse, hashlib, html, json, os, re, subprocess
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[2]
CATALOG=ROOT/"generated/1000-digital-products.json"
CURSOR=ROOT/"generated/production-factory-cursor.json"
MANIFEST=ROOT/"generated/production-factory-manifest.json"
OVERLAY=ROOT/"generated/concrete-production-overlay.json"
MEDIA_INDEX=ROOT/"generated/public-product-media-index.json"
CONCRETE=ROOT/"products/concrete"; DEMOS=ROOT/"products/demos"; VISUALS=ROOT/"assets/generated-product-visuals"
TARGET=5000
IDENTITY="Shiromani Rampal Saini · Beyond Comparison · Beyond Time · Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present"

def load(path, default):
    try:return json.loads(path.read_text(encoding="utf-8"))
    except Exception:return default
def save(path,data):
    path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def fp(p): return hashlib.sha256(f'{p.get("id","")}|{p.get("name","")}|{p.get("engine","")}|{p.get("description","")}'.encode()).hexdigest()[:16].upper()

def visual(p):
    pid=html.escape(p["id"]); name=html.escape(p["name"]); fam=html.escape(p.get("family","Digital Product")); eng=html.escape(p.get("engine","tool")); desc=html.escape(p.get("description","Concrete customer-visible digital product.")); price=html.escape(str(p.get("offer_price_inr",p.get("price_inr",""))))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 3840 2160" width="3840" height="2160"><defs><linearGradient id="b" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#05210c"/><stop offset=".5" stop-color="#06131f"/><stop offset="1" stop-color="#061a27"/></linearGradient><linearGradient id="w"><stop stop-color="#11d6ff"/><stop offset=".5" stop-color="#00ff95"/><stop offset="1" stop-color="#19a9ff"/></linearGradient></defs><rect width="3840" height="2160" rx="70" fill="url(#b)"/><rect x="45" y="45" width="3750" height="2070" rx="60" fill="none" stroke="#e7c94e" stroke-width="12"/><circle cx="330" cy="315" r="205" fill="#081017" stroke="#e7c94e" stroke-width="9"/><image href="../shirmani-perspective-logo.svg" x="150" y="135" width="360" height="360"/><text x="95" y="620" fill="#fff" font-family="DejaVu Sans" font-size="40" font-weight="700">SHIRMANI HEART-VIEW</text><text x="95" y="685" fill="#e7c94e" font-family="DejaVu Sans" font-size="25" font-weight="700">{html.escape(IDENTITY)}</text><text x="920" y="230" fill="#e7c94e" font-family="DejaVu Sans" font-size="64" font-weight="900">SHIRMANI SUPREME DIGITAL PRODUCT</text><rect x="940" y="330" width="520" height="120" rx="60" fill="#081018" stroke="#e7c94e" stroke-width="7"/><text x="1200" y="412" text-anchor="middle" fill="#fff" font-family="DejaVu Sans" font-size="66" font-weight="900">{pid}</text><text x="940" y="700" fill="#fff" font-family="DejaVu Sans" font-size="92" font-weight="900">{name}</text><text x="940" y="825" fill="#4ee7ff" font-family="DejaVu Sans" font-size="58" font-weight="800">{fam} · {eng}</text><text x="940" y="930" fill="#fff" font-family="DejaVu Sans" font-size="45">{desc[:110]}</text><text x="940" y="990" fill="#fff" font-family="DejaVu Sans" font-size="45">{html.escape(desc[110:220])}</text><rect x="940" y="1280" width="660" height="185" rx="90" fill="#071019" stroke="#e7c94e" stroke-width="9"/><text x="1270" y="1405" text-anchor="middle" fill="#fff" font-family="DejaVu Sans" font-size="90" font-weight="900">₹{price}</text><path d="M760 1640 C1250 1400 1700 1880 2250 1580 S3300 1350 3680 1660" fill="none" stroke="url(#w)" stroke-width="36"/><rect x="3100" y="300" width="510" height="510" rx="30" fill="#fff"/><image href="https://api.qrserver.com/v1/create-qr-code/?size=480x480&amp;data=https%3A%2F%2Frampaulsaini.github.io%2FShirmani-Research-Institute-Shirmani-Research-Institute-%2Fproducts%2Fdemos%2F{pid}.html" x="3130" y="330" width="450" height="450"/><text x="3355" y="875" text-anchor="middle" fill="#fff" font-family="DejaVu Sans" font-size="34" font-weight="900">SCAN FOR LONG DESCRIPTION + DEMO</text><text x="120" y="2010" fill="#e7c94e" font-family="DejaVu Sans" font-size="64" font-weight="900">4K-READY PRODUCT IDENTITY</text><text x="120" y="2075" fill="#fff" font-family="DejaVu Sans" font-size="32">Short description · QR long details · Demo · Usage guide · Passport</text></svg>'''

def product_page(p):
    pid=p["id"]; name=html.escape(p["name"]); desc=html.escape(p.get("description","")); price=int(p.get("offer_price_inr") or p.get("price_inr") or 0)
    return f'''<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{pid} — {name}</title><style>body{{margin:0;background:#06101a;color:#eef;font:16px system-ui}}main{{max-width:1100px;margin:auto;padding:18px}}.c{{background:#0d1723;border:1px solid #345;border-radius:20px;padding:20px;margin:14px 0}}img{{width:100%;border-radius:16px}}h1,h2{{color:#e7c94e}}a{{display:inline-block;padding:11px 15px;border-radius:10px;background:#e7c94e;color:#111;text-decoration:none;font-weight:900;margin:4px}}</style><main><div class="c"><img src="../../assets/generated-product-visuals/{pid}.svg" alt="{name}"></div><div class="c"><h1>{name}</h1><p>{desc}</p><h2>₹{price}</h2><p>QC-PROD-{pid} · GATE-PRODUCTION · DISPATCH NO</p><a href="../demos/{pid}.html">▶ Demo + Usage</a><a href="../../product-passport.html?id={pid}">Passport</a><a href="../../supreme-showroom.html?id={pid}">Showroom</a></div></main>'''

def demo_page(p):
    pid=p["id"]; name=html.escape(p["name"]); desc=html.escape(p.get("description","")); fam=html.escape(p.get("family","")); eng=html.escape(p.get("engine",""))
    return f'''<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Demo — {pid}</title><style>body{{margin:0;background:#050b12;color:#fff;font:16px system-ui}}main{{max-width:1000px;margin:auto;padding:18px}}.s,.p{{background:#0d1723;border:1px solid #345;border-radius:18px;padding:18px;margin:14px 0}}.s{{overflow:hidden}}.s img{{width:100%;animation:z 4s ease-in-out infinite alternate}}@keyframes z{{to{{transform:scale(1.035)}}}}h1,h2{{color:#e7c94e}}a{{display:inline-block;padding:11px 15px;border-radius:10px;background:#e7c94e;color:#111;text-decoration:none;font-weight:900;margin:4px}}</style><main><div class="s"><img src="../../assets/generated-product-visuals/{pid}.svg" alt="{name} demo"></div><div class="p"><h1>▶ {name} — Demo + Usage Guide</h1><p>{desc}</p><h2>How to use</h2><ol><li>Open the product from the showroom.</li><li>Read the short description; scan the QR for long details.</li><li>Use the browser controls and inspect the result.</li><li>Submit customer review/rating for quality improvement.</li><li>Sale/payment/dispatch remain separate commercial states.</li></ol><p>{fam} · {eng}</p><a href="../concrete/{pid}.html">Open Product</a><a href="../../supreme-showroom.html?id={pid}">Showroom</a></div><div class="p"><h2>Demo video</h2><video controls playsinline preload="metadata" style="width:100%;border-radius:12px" src="mp4/{pid}.mp4"></video><p>Automatically generated product-introduction MP4; the interactive guide above is the usage surface.</p></div></main>'''

def video(p,out):
    from PIL import Image,ImageDraw,ImageFont
    im=Image.new("RGB",(960,540),(5,15,25)); d=ImageDraw.Draw(im)
    font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",40)
    d.rectangle((20,20,940,520),outline=(231,201,78),width=5); d.text((55,55),p["id"],fill=(231,201,78),font=font); d.text((55,135),p["name"][:40],fill="white",font=font); d.text((55,220),f'{p.get("family","")} · {p.get("engine","")}',fill=(78,231,255),font=font); d.text((55,340),"DEMO • USAGE • SHOWROOM",fill="white",font=font)
    png=out.with_suffix(".png"); im.save(png)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-loop","1","-i",str(png),"-t","3","-vf","zoompan=z='min(zoom+0.0008,1.04)':d=72:s=960x540:fps=24","-an","-c:v","libx264","-pix_fmt","yuv420p","-movflags","+faststart",str(out)],check=True); png.unlink(missing_ok=True)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--batch-size",type=int,default=int(os.getenv("BATCH_SIZE","25"))); a=ap.parse_args(); batch=max(1,min(100,a.batch_size))
    catalog=load(CATALOG,{"products":[]}); products=catalog.get("products",[])
    cur=load(CURSOR,{"next_index":1,"cycle":0}); nxt=int(cur.get("next_index",1))
    ov=load(OVERLAY,{"schema_version":"2.0","product_count":TARGET,"products":[]}); existing={p["id"]:p for p in ov.get("products",[])}
    queued=sorted([p for p in products if p.get("production_state")!="PRODUCED" and int(p.get("product_index",0))>=nxt],key=lambda x:int(x.get("product_index",0)))[:batch]
    for p in queued:
        pid=p["id"]; CONCRETE.mkdir(parents=True,exist_ok=True); (DEMOS/"mp4").mkdir(parents=True,exist_ok=True); VISUALS.mkdir(parents=True,exist_ok=True)
        (VISUALS/f"{pid}.svg").write_text(visual(p),encoding="utf-8"); (CONCRETE/f"{pid}.html").write_text(product_page(p),encoding="utf-8"); (DEMOS/f"{pid}.html").write_text(demo_page(p),encoding="utf-8"); video(p,DEMOS/"mp4"/f"{pid}.mp4")
        r=dict(p); r.update({"production_state":"PRODUCED","status":"PRODUCED_PUBLIC","artifact_url":f"products/concrete/{pid}.html","demo_url":f"products/demos/{pid}.html","demo_mp4_url":f"products/demos/mp4/{pid}.mp4","visual_url":f"assets/generated-product-visuals/{pid}.svg","qc_code":f"QC-PROD-{pid}","gate_no":"GATE-PRODUCTION","dispatch_no":"NO","commercial_status":"NOT_SOLD","verification":"FUNCTIONAL_BROWSER_BEHAVIOUR_ONLY","fingerprint":fp(p),"media_state":"VISUAL_AND_DEMO_MP4_PUBLISHED","identity_text_en":IDENTITY}); existing[pid]=r
    now=datetime.now(timezone.utc).isoformat(); produced=sorted(existing.values(),key=lambda x:int(x.get("product_index",0))); remaining=max(0,TARGET-len(produced)); cycle=int(cur.get("cycle",0))+1
    save(CURSOR,{"schema_version":"1.0","cycle":cycle,"next_index":max([int(p.get("product_index",0)) for p in queued],default=nxt)+1,"updated_at":now,"target":TARGET})
    save(OVERLAY,{"schema_version":"2.0","generated_at":now,"product_count":TARGET,"produced_count":len(produced),"remaining_count":remaining,"produced_this_cycle":len(queued),"products":produced})
    save(MANIFEST,{"schema_version":"1.0","generated_at":now,"cycle":cycle,"target":TARGET,"produced_this_cycle":len(queued),"total_concrete_products":len(produced),"remaining_to_target":remaining,"production_rate_per_cycle":len(queued),"schedule":"every 5 minutes","estimated_minimum_cycles":(remaining+batch-1)//batch if remaining else 0,"estimated_wall_clock_hours":round(((remaining+batch-1)//batch)*5/60,2) if remaining else 0,"pipeline":["INSTITUTE_RESEARCH","FACTORY_PRODUCTION","QC_GATE","PUBLIC_SHOWROOM"],"independent_verification_claim":False,"sales_claim":False,"dispatch_claim":False,"external_outreach_claim":False})
    save(MEDIA_INDEX,{"schema_version":"1.0","generated_at":now,"target":TARGET,"products_with_visual_and_demo_mp4":len(produced),"remaining_media":remaining,"products":[{"id":p["id"],"visual_url":p.get("visual_url"),"demo_url":p.get("demo_url"),"demo_mp4_url":p.get("demo_mp4_url")} for p in produced]})
    print(json.dumps({"cycle":cycle,"produced_this_cycle":len(queued),"total_concrete_products":len(produced),"remaining_to_5000":remaining},ensure_ascii=False))

if __name__=="__main__": main()
