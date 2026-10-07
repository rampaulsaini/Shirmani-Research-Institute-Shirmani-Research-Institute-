#!/usr/bin/env python3
"""Generate lightweight engine-family MP4 demo videos for every concrete product."""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import json, re, subprocess, tempfile

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "generated/1000-digital-products.json"
OUT = ROOT / "products/demos"
MANIFEST = ROOT / "generated/product-media-production-manifest.json"

ENGINE_STEPS = {
    "calculator":["Enter inputs","Choose operation","Run calculation","Inspect result","Reuse output"],
    "text":["Enter text","Run language analysis","Inspect structured output","Review result","Reuse output"],
    "nlp":["Enter text","Run NLP workflow","Inspect structured output","Review result","Reuse output"],
    "seo":["Enter title","Enter description","Build SEO package","Review fields","Reuse package"],
    "marketing":["Enter brief","Build marketing package","Review copy","Adjust inputs","Reuse output"],
    "data":["Paste data","Inspect structure","Review validity","Correct input","Export result"],
    "files":["Open file data","Inspect structure","Review fields","Process output","Reuse result"],
    "visual":["Enter visual brief","Build visual specification","Review stages","Refine brief","Export spec"],
    "draw":["Enter visual brief","Build layout","Review assets","Refine","Export"],
    "pixel":["Enter visual brief","Build pixel specification","Review","Refine","Export"],
    "game":["Start game","Make move","System responds","Inspect board","Restart"],
    "quiz":["Enter topic","Build quiz","Run activity","Review result","Reuse"],
    "productivity":["Set objective","Add notes","Build plan","Review steps","Reuse plan"],
    "time":["Set task","Build schedule","Review timing","Adjust","Reuse"],
    "calendar":["Set task","Build schedule","Review dates","Adjust","Reuse"],
    "research":["Enter claim","Add source","Add evidence","Build research record","Review downstream QC"],
    "quality":["Enter quality claim","Add source","Add evidence","Build QC record","Review downstream state"],
    "ai":["Enter brief","Build production package","Review stages","Run module","Reuse output"],
    "creator":["Enter brief","Build creator package","Review","Refine","Reuse"],
    "media":["Enter brief","Build media package","Review","Refine","Reuse"],
    "commerce":["Enter product brief","Build commerce package","Review offer","Review gate","Reuse"],
    "quantum":["Choose gate","Run classical simulation","Inspect state","Review result","Reuse output"],
    "access":["Set task","Build access workflow","Review","Adjust","Reuse"],
    "nature":["Enter observation","Build production package","Review","Refine","Reuse"],
}

def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9_-]+", "-", str(value).lower()).strip("-") or "product"

def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def make_video(engine: str) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{slug(engine)}.mp4"
    if path.exists() and path.stat().st_size > 1000:
        return path
    steps = ENGINE_STEPS.get(engine, ["Open product","Enter input","Run module","Inspect result","Reuse output"])
    font = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    with tempfile.TemporaryDirectory() as td:
        parts=[]
        for idx, step in enumerate(steps, 1):
            clean_engine=engine.upper().replace("'", "")
            clean_step=step.replace("'", "")
            vf=(
                f"drawtext=fontfile={font}:text='SHIRMANI PRODUCT DEMO | {clean_engine}':fontcolor=white:fontsize=34:x=(w-text_w)/2:y=90,"
                f"drawtext=fontfile={font}:text='STEP {idx} / {len(steps)}':fontcolor=0x66ddff:fontsize=30:x=(w-text_w)/2:y=250,"
                f"drawtext=fontfile={font}:text='{clean_step}':fontcolor=0xe7c85b:fontsize=50:x=(w-text_w)/2:y=330,"
                f"drawtext=fontfile={font}:text='WHAT -> HOW -> WHERE -> RESULT':fontcolor=0xaeb8c7:fontsize=24:x=(w-text_w)/2:y=445"
            )
            part=Path(td)/f"part-{idx}.mp4"
            run(["ffmpeg","-y","-f","lavfi","-i","color=c=0x07101a:s=1280x720:r=24","-vf",vf,"-t","1.2","-c:v","libx264","-preset","veryfast","-crf","32","-pix_fmt","yuv420p","-movflags","+faststart",str(part)])
            parts.append(part)
        concat=Path(td)/"concat.txt"
        concat.write_text("\n".join(f"file '{p}'" for p in parts),encoding="utf-8")
        run(["ffmpeg","-y","-f","concat","-safe","0","-i",str(concat),"-c","copy","-movflags","+faststart",str(path)])
    return path

def main():
    catalog=json.loads(CATALOG.read_text(encoding="utf-8"))
    products=catalog.get("products",[])
    engines=sorted({str(p.get("engine","package")) for p in products})
    engine_assets={engine:str(make_video(engine).relative_to(ROOT)) for engine in engines}
    rows=[]
    for p in products:
        engine=str(p.get("engine","package"))
        rows.append({
            "product_id":p.get("id"),
            "engine":engine,
            "interactive_demo_url":f"demo-video.html?id={p.get('id')}",
            "visual_asset":f"products/visuals/{str(p.get('id')).lower()}.svg",
            "vip_screenshot_route":f"product-passport.html?id={p.get('id')}",
            "video_asset":engine_assets[engine],
            "video_type":"ENGINE_FAMILY_DEMO_MP4",
            "real_mp4":True,
            "identity":"PRODUCT_SPECIFIC",
            "note":"Reusable engine-family demo; product identity, visual, description, price and passport remain product-specific."
        })
    MANIFEST.write_text(json.dumps({
        "schema_version":1,
        "generated_at":datetime.now(timezone.utc).isoformat(),
        "product_count":len(products),
        "interactive_demo_count":len(rows),
        "real_mp4_count":len(rows),
        "vip_screenshot_count":len(rows),
        "visual_route_count":len(rows),
        "engine_demo_count":len(engine_assets),
        "engine_assets":engine_assets,
        "products":rows,
        "production_rule":"Every product has an interactive demo route and an engine-family MP4 demo. Shared demo media never replaces the product's unique identity."
    },ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"products":len(products),"engines":len(engines),"mp4_assets":len(engine_assets)},ensure_ascii=False))

if __name__=="__main__":
    main()
