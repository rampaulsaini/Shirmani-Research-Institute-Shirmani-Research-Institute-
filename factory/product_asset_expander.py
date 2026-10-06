#!/usr/bin/env python3
from __future__ import annotations
import html, json
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
GEN=ROOT/"generated"; CATALOG=GEN/"1000-digital-products.json"; OUT=ROOT/"products"/"production"; INDEX=GEN/"product-production-assets.json"
def esc(v): return html.escape(str(v),quote=True)
def page(p):
    pid=p["id"]; engine=p.get("engine","creator"); qc=p.get("qc_code","QC-PENDING"); gate=p.get("gate_no","GATE-PENDING"); module=p.get("module","")
    meta=json.dumps({"id":pid,"engine":engine,"qc":qc,"gate":gate},ensure_ascii=False)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(p["name"])} — SHIRMANI Production</title>
<style>body{{margin:0;background:#080b12;color:#eef2f7;font:16px system-ui,sans-serif;line-height:1.5}}main{{max-width:980px;margin:auto;padding:22px}}section{{background:#111722;border:1px solid #334155;border-radius:16px;padding:18px;margin:12px 0}}h1,h2{{color:#e7c45f}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:10px}}.card{{background:#0b1019;padding:12px;border-radius:10px}}.v{{font-weight:800;color:#67e8f9}}button{{padding:10px 14px;border:0;border-radius:9px;cursor:pointer}}textarea{{width:100%;box-sizing:border-box;padding:10px;background:#070a0f;color:#fff;border:1px solid #334155;border-radius:8px;margin:5px 0}}pre{{white-space:pre-wrap;background:#070a0f;padding:12px;border-radius:8px;overflow:auto}}a{{color:#67e8f9}}</style></head>
<body><main><section><h1>꙰ {esc(p["name"])}</h1><p><b>Product-specific production asset</b> — concrete public product surface.</p><div class="grid"><div class="card">Product ID<div class="v">{esc(pid)}</div></div><div class="card">Family<div class="v">{esc(p.get("family"))}</div></div><div class="card">Engine<div class="v">{esc(engine)}</div></div><div class="card">State<div class="v">PRODUCTION-CANDIDATE</div></div></div></section>
<section><h2>Production input</h2><p>{esc(p.get("objective","Create a reusable production output."))}</p><textarea id="input" rows="7" placeholder="Enter the material, brief, text, data or task for this product."></textarea><button onclick="produce()">Produce result</button><div id="result"></div></section>
<section><h2>QC / Gate / Dispatch Passport</h2><div class="grid"><div class="card">QC code<div class="v">{esc(qc)}</div></div><div class="card">Gate No.<div class="v">{esc(gate)}</div></div><div class="card">Dispatch No.<div class="v">NO</div></div><div class="card">QR payload<div class="v">{esc(pid+"|"+module+"|"+qc+"|"+gate+"|DISPATCH:NO")}</div></div></div><p>Dispatch remains NO until an explicit downstream dispatch event. QC/gate fields are production controls.</p></section>
<section><h2>Production lifecycle</h2><p><b>Input → Produce → QC → Gate → Package → Dispatch → downstream verification</b></p><p>Repository module: <code>{esc(module)}</code></p></section><section><a href="../../generated/public-production-command-center.html">Production Command Center</a> · <a href="../../generated/public-production-by-module.html">Module Production Map</a> · <a href="../../index.html">Main Hub</a></section></main>
<script>const meta=__META__;function produce(){{const x=document.getElementById('input').value.trim();const result={{product_id:meta.id,engine:meta.engine,status:x?'PRODUCED':'INPUT_REQUIRED',characters:x.length,words:x?x.split(/\\s+/).length:0,qc_code:meta.qc,gate_no:meta.gate,dispatch_no:'NO',produced_at:new Date().toISOString()}};document.getElementById('result').innerHTML='<pre>'+JSON.stringify(result,null,2)+'</pre>';}}</script></body></html>'''.replace("__META__",meta)
def main():
    if not CATALOG.exists(): raise SystemExit("catalog missing")
    data=json.loads(CATALOG.read_text(encoding="utf-8")); products=data.get("products",[]); OUT.mkdir(parents=True,exist_ok=True); created=existing=0; rows=[]
    for p in products:
        path=OUT/(p["id"].lower()+".html")
        if path.exists(): existing+=1
        else: path.write_text(page(p),encoding="utf-8"); created+=1
        rows.append({"product_id":p["id"],"name":p["name"],"engine":p.get("engine"),"family":p.get("family"),"asset_path":str(path.relative_to(ROOT)),"asset_state":"CONCRETE_PRODUCT_ASSET","qc_code":p.get("qc_code"),"gate_no":p.get("gate_no"),"dispatch_no":"NO"})
    INDEX.write_text(json.dumps({"version":1,"generated_at":datetime.now(timezone.utc).isoformat(),"product_count":len(rows),"created_this_cycle":created,"already_existing":existing,"asset_state":"CONCRETE_PRODUCT_ASSET","principle":"Product asset first; QC/gate/dispatch downstream.","products":rows},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"product_count":len(rows),"created_this_cycle":created,"already_existing":existing},ensure_ascii=False))
if __name__=="__main__": main()
