#!/usr/bin/env python3
import argparse, hashlib, html, json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"generated/1000-digital-products.json"
OUT=ROOT/"generated"
ART=OUT/"products"
STATE=OUT/"production-state.json"
BATCH=100200

def code(seed,prefix): return prefix+"-"+hashlib.sha256(seed.encode()).hexdigest()[:12].upper()
def price_for(n):
    base=99+(n*47)%7901
    offer=max(49,round(base*(0.68+((n*11)%18)/100)))
    return base,offer

def build_artifact(p,row):
    pid=p["id"]; s=html.escape
    return f'''<!doctype html><html lang="hi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>꙰ {s(p["name"])} — SHIRMANI Product</title>
<style>body{{margin:0;background:#071018;color:#eef5f8;font:16px system-ui;line-height:1.55}}main{{max-width:1100px;margin:auto;padding:20px 14px 70px}}.hero,.card{{background:#101923;border:1px solid #354858;border-radius:18px;padding:18px;margin:12px 0}}.hero{{border:2px solid #ffd84a}}h1,h2{{color:#ffd84a}}.tag{{display:inline-block;border:1px solid #5ee7ff;border-radius:99px;padding:3px 9px;color:#5ee7ff;font-size:.75rem}}.price{{font-size:1.6rem;color:#ffd84a;font-weight:900}}.offer,.ok{{color:#6ee7b7;font-weight:800}}.passport{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:8px}}.passport div{{background:#081019;border-radius:10px;padding:10px}}code{{color:#ffd84a}}iframe{{width:100%;height:620px;border:1px solid #405466;border-radius:12px;background:#fff}}a{{color:#67e8f9}}</style></head><body><main>
<section class="hero"><span class="tag">PRODUCED PRODUCT • {s(p["family"])} • {s(p["engine"])}</span><h1>꙰ {s(p["name"])}</h1>
<p>{s(p.get("description") or ("SHIRMANI "+p["family"]+" digital product."))}</p>
<p class="price">₹{row["offer_price_inr"]:,} <del>₹{row["price_inr"]:,}</del></p><p class="offer">{s(row["offer"])}</p></section>
<section class="card"><h2>Product Passport</h2><div class="passport">
<div>ID<br><b>{pid}</b></div><div>Production Unit<br><b>{row["unit_no"]}</b></div><div>QC Code<br><b>{row["qc_code"]}</b></div><div>Gate No.<br><b>{row["gate_no"]}</b></div><div>Dispatch<br><b>NO</b></div><div>Sale State<br><b>OFFERED</b></div><div>Packing<br><b>{s(row["packing"])}</b></div><div>Guarantee<br><b>{s(row["guarantee"])}</b></div></div></section>
<section class="card"><h2>QR / Gate Payload</h2><p id="payload"></p><p class="ok">Production result is primary. QC and gate are downstream product controls; Dispatch remains NO until an explicit downstream release.</p></section>
<section class="card"><h2>Live Product Module</h2><iframe src="../products/1000-digital-product-factory.html?id={pid}" title="{s(p["name"])}"></iframe></section>
<section class="card"><a href="../supreme-marking-hub.html?id={pid}">Supreme Marking Hub</a> · <a href="../supreme-production-showroom.html?id={pid}">Showroom</a> · <a href="../products/production-launch-center.html?id={pid}">Production Launch Center</a></section>
</main><script>
const payload={{product_id:"{pid}",qc_code:"{row["qc_code"]}",gate_no:"{row["gate_no"]}",dispatch:"NO",price_inr:{row["offer_price_inr"]}}};
document.getElementById("payload").textContent=JSON.stringify(payload);
</script></body></html>'''

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--batch-size",type=int,default=250); a=ap.parse_args()
    src=json.loads(SRC.read_text(encoding="utf-8")); products=src.get("products",[])
    if not products: raise SystemExit("No canonical products")
    state={"cursor":0,"cycle":0,"produced_ids":[]}
    if STATE.exists():
        state=json.loads(STATE.read_text(encoding="utf-8"))
    produced=set(state.get("produced_ids",[]))
    cursor=int(state.get("cursor",0))%len(products)
    cycle=int(state.get("cycle",0))+1
    selected=[]
    for i in range(len(products)):
        p=products[(cursor+i)%len(products)]
        if p["id"] not in produced:
            selected.append(p)
            if len(selected)>=a.batch_size: break
    stamp=datetime.now(timezone.utc).isoformat()
    ART.mkdir(parents=True,exist_ok=True)
    rows=[]
    for n,p in enumerate(selected,1):
        pid=p["id"]; idx=int(pid.split("-")[-1]); base,offer=price_for(idx)
        row=dict(p)
        row.update({"production_batch":BATCH,"unit_no":f"{BATCH}.{idx:04d}","qc_code":code(pid+str(BATCH),"QC"),
                    "gate_no":f"GATE-{((idx-1)//max(1,a.batch_size))+1:04d}","dispatch_no":"NO",
                    "production_state":"PRODUCED","qc_state":"READY","sale_state":"OFFERED",
                    "price_inr":base,"offer_price_inr":offer,"offer":"Launch offer",
                    "guarantee":"30-day product-access/defect support policy; subject to final commercial terms",
                    "packing":"SUPREME_DIGITAL_PRIME","artifact_url":f"generated/products/{pid}.html",
                    "passport_url":f"product-passport.html?id={pid}","showroom_url":f"supreme-marking-hub.html?id={pid}",
                    "production_url":f"products/1000-digital-product-factory.html?id={pid}","generated_at":stamp})
        (ART/f"{pid}.html").write_text(build_artifact(p,row),encoding="utf-8")
        rows.append(row); produced.add(pid)
    next_cursor=(cursor+max(1,len(selected)))%len(products)
    newstate={"schema_version":2,"generated_at":stamp,"cursor":next_cursor,"cycle":cycle,
              "batch_size":len(rows),"catalog_count":len(products),"produced_count":len(produced),
              "remaining_count":len(products)-len(produced),"produced_ids":sorted(produced),
              "latest_batch":[x["id"] for x in rows]}
    STATE.write_text(json.dumps(newstate,ensure_ascii=False,indent=2),encoding="utf-8")
    allrows=[]
    for p in products:
        pid=p["id"]
        if pid in produced:
            idx=int(pid.split("-")[-1]); base,offer=price_for(idx)
            allrows.append({"id":pid,"name":p["name"],"family":p.get("family"),"engine":p.get("engine"),
             "unit_no":f"{BATCH}.{idx:04d}","qc_code":code(pid+str(BATCH),"QC"),
             "gate_no":f"GATE-{((idx-1)//max(1,a.batch_size))+1:04d}","dispatch_no":"NO",
             "production_state":"PRODUCED","qc_state":"READY","sale_state":"OFFERED",
             "price_inr":base,"offer_price_inr":offer,"offer":"Launch offer",
             "artifact_url":f"generated/products/{pid}.html","showroom_url":f"supreme-marking-hub.html?id={pid}",
             "production_url":f"products/1000-digital-product-factory.html?id={pid}"})
    registry={"schema_version":3,"generated_at":stamp,"architecture":["INSTITUTE","FACTORY","QC","SHOWROOM_SALE"],
              "production_first":True,"verification_is_downstream":True,"batch":BATCH,
              "catalog_count":len(products),"produced_count":len(produced),"remaining_count":len(products)-len(produced),
              "engine_count":src.get("engine_count",0),"family_count":len(set(x.get("family") for x in products)),
              "products":allrows}
    (OUT/"production-registry.json").write_text(json.dumps(registry,ensure_ascii=False,indent=2),encoding="utf-8")
    q=[{"product_id":p["id"],"work":"PRODUCE","state":"PRODUCED" if p["id"] in produced else "QUEUED",
        "production_url":f"products/1000-digital-product-factory.html?id={p['id']}"} for p in products]
    (OUT/"production-work-queue.jsonl").write_text("\n".join(json.dumps(x,ensure_ascii=False) for x in q)+"\n",encoding="utf-8")
    status={"generated_at":stamp,"architecture":["INSTITUTE","FACTORY","QC","SHOWROOM_SALE"],
            "catalog_count":len(products),"product_count":len(produced),"produced":len(produced),
            "remaining":len(products)-len(produced),"qc_ready":len(produced),"offered":len(produced),
            "dispatch_no":len(produced),"dispatch_yes":0,"batch_produced":len(rows),
            "production_cycle":cycle,"verification_scope":"DOWNSTREAM_PRODUCT_RESULT",
            "next_work":"continue multi-lane product artifact production; verification follows produced results"}
    (OUT/"production-status.json").write_text(json.dumps(status,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(status,ensure_ascii=False))

if __name__=="__main__": main()
