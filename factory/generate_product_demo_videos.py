#!/usr/bin/env python3
"""Generate lightweight customer-facing demo videos for every SHIRMANI product engine."""
from pathlib import Path
import json, subprocess
ROOT=Path(__file__).resolve().parents[1]; CAT=ROOT/"generated/1000-digital-products.json"; OUT=ROOT/"products/demos"; OUT.mkdir(parents=True,exist_ok=True)
products=json.loads(CAT.read_text(encoding="utf-8")).get("products",[])
engines=sorted({str(p.get("engine","package")) for p in products})
steps={"calculator":["Enter values","Choose operation","Run calculation","Reuse result"],"text":["Enter text","Analyze language","Review output","Reuse result"],"seo":["Enter title","Add description","Build SEO package","Publish metadata"],"data":["Paste JSON or CSV","Inspect data","Review validity","Reuse output"],"visual":["Enter visual brief","Build specification","Review stages","Export plan"],"game":["Start game","Interact","Inspect output","Replay"],"planner":["Enter task","Build plan","Review steps","Reuse plan"],"research":["Enter question","Add source","Record evidence","Record limitations"],"package":["Enter production brief","Build package","Review QC stages","Reuse package"],"quantum":["Choose gate","Run classical simulation","Inspect output","Use as research/demo"]}
for engine in engines:
    path=OUT/(engine+".mp4")
    if path.exists(): continue
    lines=[f"SHIRMANI {engine.upper()} PRODUCT DEMO","HOW TO USE / WHERE TO USE"]+steps.get(engine,steps["package"])
    filters=[]
    for i,line in enumerate(lines[:7]):
        safe=line.replace(":","\\:").replace("'","\\'")
        filters.append(f"drawtext=text='{safe}':fontcolor=white:fontsize={48 if i==0 else 32}:x=(w-text_w)/2:y={70+i*70}:enable='between(t,{i*1.2},{(i+1)*1.2})'")
    vf=",".join(filters)
    subprocess.run(["ffmpeg","-y","-f","lavfi","-i","color=c=0x071018:s=1280x720:r=30","-vf",vf,"-t","8","-pix_fmt","yuv420p","-movflags","+faststart",str(path)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
print("DEMO_ENGINES",len(engines))
