#!/usr/bin/env python3
import json,html
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]; GEN=ROOT/"generated"; OUT=ROOT/"products/concrete"; OS=__import__("os"); BATCH=int(OS.environ.get("CONCRETE_PRODUCT_BATCH_SIZE","250")); FORCE_REBUILD=OS.environ.get("CONCRETE_PRODUCT_REBUILD","0")=="1"
def now(): return datetime.now(timezone.utc).isoformat()
def esc(x): return html.escape(str(x or ""),quote=True)
def page(p):
    pid=p["id"]; name=esc(p["name"]); fam=esc(p.get("family")); eng=esc(p.get("engine")); price=int(p.get("offer_price_inr") or p.get("price_inr") or 0)
    qc="QC-PROD-"+pid; gate="GATE-PRODUCTION"
    return f'''<!doctype html><html lang="hi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{name} — SHIRMANI Production</title><style>body{{font:16px system-ui;background:#071019;color:#eee;max-width:1000px;margin:auto;padding:20px}}section{{background:#101923;border:1px solid #405466;border-radius:16px;padding:18px;margin:12px 0}}h1,h2{{color:#ffd84a}}.product-visual{{margin:0 0 18px;border:1px solid #405466;border-radius:16px;overflow:hidden;background:#050910}}.product-visual img{{display:block;width:100%;height:auto;aspect-ratio:16/9;object-fit:cover}}.m{{display:inline-block;background:#081019;padding:12px;margin:4px;border-radius:9px}}textarea{{width:100%;box-sizing:border-box;background:#081019;color:#fff;padding:10px;border:1px solid #405466;border-radius:8px;margin:5px 0}}button,a{{padding:10px 13px;background:#ffd84a;color:#111;border:0;border-radius:8px;font-weight:800;text-decoration:none}}pre{{white-space:pre-wrap;background:#060b10;padding:12px}}</style><main><section><div class="product-visual"><img src="../visuals/{pid.lower()}.svg" alt="{name} — unique SHIRMANI 4K product identity" width="3840" height="2160" loading="eager"></div><h1>꙰ {name}</h1><p>{esc(p.get("description") or "Concrete public digital product.")}</p><div class="m">ID<br><b>{pid}</b></div><div class="m">Category<br><b>{fam}</b></div><div class="m">Engine<br><b>{eng}</b></div><div class="m">Price<br><b>₹{price:,}</b></div></section><section><h2>QC / Gate / Dispatch</h2><div class="m">QC<br><b>{qc}</b></div><div class="m">Gate<br><b>{gate}</b></div><div class="m">Dispatch<br><b>NO</b></div><p>Dispatch remains NO until explicit release.</p></section><section><h2>Working Product Module</h2><textarea id="input" rows="7" placeholder="Enter product input / brief"></textarea><button onclick="produce()">Produce result</button><pre id="out">Ready.</pre></section><section><a href="../../supreme-showroom.html?id={pid}">Showroom</a> <a href="../../product-passport.html?id={pid}">Passport</a></section></main><script>function produce(){{let x=document.getElementById("input").value;document.getElementById("out").textContent=JSON.stringify({{product_id:"{pid}",engine:"{eng}",status:x?"PRODUCED":"INPUT_REQUIRED",characters:x.length,words:x?x.trim().split(/\\s+/).length:0,qc_code:"{qc}",gate_no:"{gate}",dispatch_no:"NO",produced_at:new Date().toISOString()}},null,2)}}</script></html>'''
def main():
    catalog=json.loads((GEN/"1000-digital-products.json").read_text())
    op=GEN/"concrete-production-overlay.json"
    old=json.loads(op.read_text()) if op.exists() else {"products":[]}
    previous={x["id"]:x for x in old.get("products",[])}
    done={}
    pending=[]
    for p in catalog["products"]:
        asset=OUT/(p["id"]+".html")
        if asset.is_file() and asset.stat().st_size >= 100:
            prior=previous.get(p["id"])
            if prior and prior.get("production_state")=="PRODUCED":
                done[p["id"]]=prior
            else:
                done[p["id"]]={"id":p["id"],"production_state":"PRODUCED","sale_state":"READY_FOR_ORDER","artifact_url":"products/concrete/"+p["id"]+".html","production_batch":"EXISTING-ASSET-SYNC","produced_at":now(),"qc_code":"QC-PROD-"+p["id"],"gate_no":"GATE-PRODUCTION","dispatch_no":"NO"}
        else:
            pending.append(p)
    if FORCE_REBUILD:
        pending=catalog["products"][:BATCH]
    else:
        pending=pending[:BATCH]
    batch="BATCH-"+datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"); ts=now(); OUT.mkdir(parents=True,exist_ok=True)
    for p in pending:
        (OUT/(p["id"]+".html")).write_text(page(p))
        done[p["id"]]={"id":p["id"],"production_state":"PRODUCED","sale_state":"READY_FOR_ORDER","artifact_url":"products/concrete/"+p["id"]+".html","production_batch":batch,"produced_at":ts,"qc_code":"QC-PROD-"+p["id"],"gate_no":"GATE-PRODUCTION","dispatch_no":"NO"}
    for p in catalog["products"]:
        if p["id"] in done:
            done[p["id"]]["artifact_url"]="products/concrete/"+p["id"]+".html"
    ordered=sorted(done.values(),key=lambda x:int(x["id"].split("-")[-1]))
    op.write_text(json.dumps({"schema_version":1,"generated_at":ts,"architecture":["INSTITUTE","FACTORY","QC","SHOWROOM_SALE"],"production_first":True,"verification_is_downstream":True,"batch":batch,"product_count":len(catalog["products"]),"produced_count":len(ordered),"remaining_count":len(catalog["products"])-len(ordered),"batch_size":len(pending),"products":ordered},ensure_ascii=False,indent=2)+"\n")
    (GEN/"continuous-production-batch-status.json").write_text(json.dumps({"generated_at":ts,"batch":batch,"catalog_products":len(catalog["products"]),"produced_total":len(ordered),"produced_this_cycle":len(pending),"remaining":len(catalog["products"])-len(ordered),"dispatch_released":0,"verification":"DOWNSTREAM"},ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"batch":batch,"produced_this_cycle":len(pending),"produced_total":len(ordered),"remaining":len(catalog["products"])}))
if __name__=="__main__": main()
