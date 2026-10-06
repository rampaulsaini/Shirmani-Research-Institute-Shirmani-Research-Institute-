#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import hashlib,html,json

ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"generated/1000-digital-products.json"
OUT=ROOT/"products/concrete"
MAN=ROOT/"generated/concrete-product-manifest.json"
STATUS=ROOT/"generated/concrete-product-production-status.json"

def esc(x): return html.escape(str(x),quote=True)
def fp(p): return hashlib.sha256(json.dumps(p,sort_keys=True,ensure_ascii=False).encode()).hexdigest()[:16].upper()

def js(engine):
    if engine in ("calculator","engineering"):
        return "const a=+v('a'),b=+v('b'),o=v('op');let r=o==='+'?a+b:o==='-'?a-b:o==='*'?a*b:o==='/'?(b? a/b:'DIV0'):o==='%'?(b?a%b:'DIV0'):a**b;show({type:'CALCULATION',a,b,operation:o,result:r});"
    if engine in ("text","nlp","knowledge"):
        return "const t=v('input');show({type:'TEXT_ANALYSIS',characters:t.length,words:(t.match(/\\S+/g)||[]).length,lines:t.split(/\\n/).length,uppercase:t.toUpperCase()});"
    if engine in ("seo","marketing","creator"):
        return "const t=v('title'),d=v('desc'),slug=t.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');show({type:'SEO_PACK',title:t,description:d.slice(0,160),slug});"
    if engine in ("data","files"):
        return "const t=v('input');try{show({type:'JSON',valid:true,data:JSON.parse(t)})}catch(e){let r=t.split(/\\n/).filter(Boolean).map(x=>x.split(','));show({type:'CSV',rows:r.length,columns:r[0]?.length||0,preview:r.slice(0,10)})}"
    if engine=="research":
        return "show({type:'EVIDENCE_RECORD',claim:v('title'),source:v('input'),evidence:v('answer'),verification:'NOT_INDEPENDENTLY_VERIFIED'});"
    if engine=="quiz":
        return "show({type:'QUIZ_RECORD',topic:v('title'),question:v('input'),answer:v('answer'),status:'DRAFT'});"
    if engine in ("productivity","time"):
        return "const m=Math.max(1,+v('input')||1);show({type:'TIMER',minutes:m,ends_at:new Date(Date.now()+m*60000).toISOString()});"
    if engine=="quantum":
        return "show({type:'QUANTUM_INSPIRED_SIMULATION',gate:v('input'),hardware_execution:false});"
    return "show({type:'STRUCTURED_PRODUCT_RECORD',input:v('input'),created_at:new Date().toISOString(),status:'DRAFT'});"

def page(p):
    e=p.get("engine","structured"); name=p["name"]; pid=p["id"]
    if e in ("calculator","engineering"): controls="<input id='a' type='number' value='10'><input id='b' type='number' value='5'><select id='op'><option>+</option><option>-</option><option>*</option><option>/</option><option>%</option><option>^</option></select>"
    elif e in ("seo","marketing","creator"): controls="<input id='title' placeholder='Title'><textarea id='desc' placeholder='Description'></textarea>"
    elif e in ("research","quiz"): controls="<input id='title' placeholder='Topic / claim'><input id='input' placeholder='Source / question'><textarea id='answer' placeholder='Evidence / answer'></textarea>"
    elif e=="quantum": controls="<select id='input'><option>H</option><option>X</option><option>Z</option><option>CNOT</option></select>"
    else: controls="<textarea id='input' rows='8' placeholder='Enter input…'></textarea>"
    price=p.get('offer_price_inr',p.get('price_inr',0)); base_price=p.get('price_inr',0); offer=p.get('offer','PUBLIC LAUNCH PRICE'); qc=p.get('qc_code','QC-PENDING'); gate=p.get('gate_no','GATE-PRODUCTION'); dispatch=p.get('dispatch_no','NO'); sale=p.get('sale_state','PAYMENT_ROUTE_CONFIGURED'); desc=p.get('description','Concrete public digital product.');
    return f"""<!doctype html><html lang='hi'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><meta name='description' content='{esc(desc)}'><title>{esc(name)} · SHIRMANI</title><style>body{{margin:0;background:#080c13;color:#eef2f7;font-family:system-ui,sans-serif}}main{{max-width:900px;margin:auto;padding:24px 16px}}.card{{background:#111827;border:1px solid #334155;border-radius:16px;padding:18px;margin:14px 0}}h1,h2{{color:#e7c45f}}input,textarea,select{{width:100%;box-sizing:border-box;margin:7px 0;padding:10px;background:#0b1220;color:#fff;border:1px solid #475569;border-radius:9px}}button,a{{padding:10px 14px;border-radius:9px;background:#e7c45f;color:#111;font-weight:800;text-decoration:none;border:0}}pre{{white-space:pre-wrap;background:#070a0f;padding:12px;color:#bdefff}}.muted{{color:#aeb8c8}}</style></head><body><main><section class='card'><h1>꙰ {esc(name)}</h1><p>{esc(desc)}</p><div><span class='m'><b>Product ID</b><br>{esc(pid)}</span><span class='m'><b>Family</b><br>{esc(p.get('family'))}</span><span class='m'><b>Engine</b><br>{esc(e)}</span><span class='m'><b>Price</b><br>₹{int(price):,}</span><span class='m'><b>Offer</b><br>{esc(offer)}</span></div><p><b>Base price:</b> ₹{int(base_price):,} · <b>Sale state:</b> {esc(sale)}</p><a href='../../products.html'>Catalog</a> <a href='../../products/1000-digital-product-factory.html?id={esc(pid)}'>Factory</a> <a href='../../showroom.html#products'>Showroom</a></section><section class='card'><h2>Run Product</h2>{controls}<button onclick='run()'>Run / Produce Output</button><pre id='out'>Ready.</pre></section><section class='card'><h2>Customer-facing production record</h2><p><b>QC:</b> {esc(qc)} · <b>Gate:</b> {esc(gate)} · <b>Dispatch:</b> {esc(dispatch)}</p><p><b>Payment:</b> Public payment routes are configured at the platform level; this page does not claim payment completion.</p><p>PRODUCED ≠ SOLD · PRODUCED ≠ PAID · PRODUCED ≠ INDEPENDENTLY VERIFIED.</p></section><script>const v=i=>document.getElementById(i).value,show=x=>document.getElementById('out').textContent=JSON.stringify(x,null,2);function run(){{{js(e)}}}</script></main></body></html>"""

def main():
    data=json.loads(CAT.read_text(encoding="utf-8")); products=data["products"]; OUT.mkdir(parents=True,exist_ok=True)
    rows=[]
    for p in products:
        (OUT/(p["id"]+".html")).write_text(page(p),encoding="utf-8")
        rows.append({"id":p["id"],"name":p["name"],"family":p.get("family"),"engine":p.get("engine"),"asset":"products/concrete/"+p["id"]+".html","status":"CONCRETE_PRODUCED","commercial_status":"NOT_SOLD","verification":"FUNCTIONAL_BROWSER_BEHAVIOUR_ONLY","fingerprint":fp(p)})
    now=datetime.now(timezone.utc).isoformat()
    MAN.write_text(json.dumps({"generated_at":now,"target":len(products),"concrete_product_count":len(rows),"materialization_percent":round(100*len(rows)/len(products),2),"products":rows,"integrity":{"sales_claim":False,"payment_claim":False,"independent_verification_claim":False}},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    STATUS.write_text(json.dumps({"generated_at":now,"target":len(products),"concrete_produced":len(rows),"concrete_production_percent":round(100*len(rows)/len(products),2),"remaining":len(products)-len(rows),"status":"COMPLETE","next_layer":"QC → packaging → commercial listing → delivery evidence → independent review"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"target":len(products),"concrete_produced":len(rows),"percent":100*len(rows)/len(products)}))
if __name__=="__main__": main()
