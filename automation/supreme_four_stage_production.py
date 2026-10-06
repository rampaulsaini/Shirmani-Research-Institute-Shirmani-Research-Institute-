#!/usr/bin/env python3
"""SHIRMANI four-stage continuous production engine.
Institute discovery -> Factory production -> QC gate -> Public showroom.
Production is primary; QC/verification are downstream result controls.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, html

ROOT=Path(__file__).resolve().parents[1]
GEN=ROOT/"generated"/"four-stage-production"
PRODUCTS=GEN/"products"
STATE=GEN/"state.json"
SHOWROOM=ROOT/"supreme-public-production-showroom.html"
DISCOVERY_DIRS=["source","factory","automation","scripts","agents","schemas","docs","products"]
EXTS={".py",".js",".ts",".html",".md",".json",".yml",".yaml",".css"}
FAMILIES=[("research","Research & Evidence"),("ai","AI Tools"),("ml-nlp","ML/NLP Practitioner"),("automation","Automission"),("knowledge","Knowledge"),("publishing","Digital Publishing"),("audio","Audio & Media"),("creator","Creator Tools"),("commerce","Commerce"),("visual","Visual Production"),("education","Education"),("nature","Nature & Earth")]

def now(): return datetime.now(timezone.utc).isoformat()
def digest(s): return hashlib.sha256(s.encode("utf-8","ignore")).hexdigest()
def family(path):
    s=path.lower()
    for key,val in [("nlp","ml-nlp"),("ml","ml-nlp"),("audio","audio"),("music","audio"),("research","research"),("evidence","research"),("automation","automation"),("automission","automation"),("workflow","automation"),("factory","commerce"),("product","commerce"),("education","education"),("learn","education"),("visual","visual"),("image","visual"),("nature","nature"),("earth","nature"),("publish","publishing"),("content","publishing"),("agent","knowledge"),("knowledge","knowledge")]:
        if key in s: return val
    return "ai"

def discover():
    found=[]
    for d in DISCOVERY_DIRS:
        root=ROOT/d
        if not root.exists(): continue
        for p in root.rglob("*"):
            if p.is_file() and p.suffix.lower() in EXTS and ".git" not in p.parts and "generated" not in p.parts:
                found.append(p)
    return sorted(set(found))

def make_product(p):
    rel=p.relative_to(ROOT).as_posix()
    content=p.read_text(encoding="utf-8",errors="ignore")
    h=digest(rel+"|"+content); fam=family(rel); label=dict(FAMILIES)[fam]
    pid="SRI-"+h[:16].upper(); base=99+(int(h[:8],16)%7902); offer=max(49,round(base*.80))
    qc="QC-"+h[8:20].upper(); gate="GATE-"+h[20:26].upper()
    return {"product_id":pid,"name":f"SHIRMANI {label} Production {h[:8].upper()}","category":label,"family":fam,"source_module":rel,"source_hash":h,"description":f"Concrete production package derived from {rel}, with defined scope, customer-facing metadata and a reusable working module.","deliverables":["working module reference","product description","commercial metadata","QC passport","QR gate payload"],"price_inr":base,"offer_price_inr":offer,"offer":"LAUNCH -20%","guarantee":"Digital product correction window; delivery evidence retained","packing":"SUPREME DIGITAL PRIME PACK","qc_code":qc,"gate_no":gate,"dispatch":"NO","production_stage":"FACTORY_PRODUCED","qc_state":"READY_FOR_QC","verification":"DOWNSTREAM_RESULT_CONTROL","qr_payload":f"{pid}|QC:{qc}|GATE:{gate}|DISPATCH:NO|PRICE:{offer}","generated_at":now(),"source_size":len(content)}

def product_page(p):
    s=html.escape
    return f"""<!doctype html><html lang="hi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{s(p['name'])}</title><style>body{{margin:0;background:#071018;color:#eef5f8;font:16px system-ui;line-height:1.5}}main{{max-width:1000px;margin:auto;padding:20px}}section{{background:#101923;border:1px solid #354858;border-radius:18px;padding:18px;margin:12px 0}}h1,h2{{color:#ffd84a}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:9px}}.m{{background:#081019;padding:12px;border-radius:10px}}.price{{font-size:1.5rem;font-weight:900}}.offer{{color:#6ee7b7;font-weight:800}}a{{color:#67e8f9}}</style><body><main><section><h1>꙰ {s(p['name'])}</h1><p>{s(p['description'])}</p><p class="price">₹{p['offer_price_inr']:,} <del>₹{p['price_inr']:,}</del></p><p class="offer">{s(p['offer'])}</p></section><section><h2>Four-Stage Product Passport</h2><div class="grid"><div class="m">Institute<br><b>DISCOVERED</b></div><div class="m">Factory<br><b>PRODUCED</b></div><div class="m">QC<br><b>{s(p['qc_state'])}</b></div><div class="m">Dispatch<br><b>NO</b></div><div class="m">QC Code<br><b>{s(p['qc_code'])}</b></div><div class="m">Gate<br><b>{s(p['gate_no'])}</b></div><div class="m">Packing<br><b>{s(p['packing'])}</b></div><div class="m">Guarantee<br><b>{s(p['guarantee'])}</b></div></div><p>QR payload: <code>{s(p['qr_payload'])}</code></p></section><section><h2>Production Result</h2><p>Source module: <b>{s(p['source_module'])}</b></p><p>Production is the primary workload. QC and verification are downstream controls on the produced result.</p></section></main></body></html>"""

def main():
    GEN.mkdir(parents=True,exist_ok=True); PRODUCTS.mkdir(parents=True,exist_ok=True)
    files=discover(); state={"cycle":0,"cursor":0,"produced":{}}
    if STATE.exists():
        try: state=json.loads(STATE.read_text(encoding="utf-8"))
        except Exception: pass
    cursor=int(state.get("cursor",0)); cycle=int(state.get("cycle",0))+1; batch_size=250; selected=[]
    for i in range(len(files)):
        p=files[(cursor+i)%len(files)]; content=p.read_text(encoding="utf-8",errors="ignore")
        pid="SRI-"+digest(p.relative_to(ROOT).as_posix()+"|"+content)[:16].upper()
        if pid not in state["produced"]:
            selected.append(p)
            if len(selected)>=batch_size: break
    for p in selected:
        row=make_product(p); state["produced"][row["product_id"]]=row
        (PRODUCTS/(row["product_id"]+".html")).write_text(product_page(row),encoding="utf-8")
    if files: state["cursor"]=(cursor+len(selected))%len(files)
    state["cycle"]=cycle; state["updated_at"]=now(); STATE.write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding="utf-8")
    allp=list(state["produced"].values()); public=allp[-5000:]
    catalog={"schema_version":1,"generated_at":now(),"four_levels":["INSTITUTE_DISCOVERY","FACTORY_PRODUCTION","QC_GATE","PUBLIC_SHOWROOM_SALE"],"production_first":True,"discovered_modules":len(files),"produced_products":len(allp),"new_this_cycle":len(selected),"products":public}
    (GEN/"catalog.json").write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding="utf-8")
    status={"generated_at":now(),"cycle":cycle,"institute":{"modules_discovered":len(files)},"factory":{"products_produced_total":len(allp),"new_products_this_cycle":len(selected)},"qc":{"ready_for_qc":len(allp),"dispatch_yes":0,"dispatch_no":len(allp)},"showroom":{"listed":len(public),"priced":len(public),"with_offer":len(public)},"automission":{"schedule":"every 5 minutes","continuous":True},"principle":"Produce first; QC/verification evaluate produced results downstream."}
    (GEN/"status.json").write_text(json.dumps(status,ensure_ascii=False,indent=2),encoding="utf-8")
    cards=[]
    for p in reversed(public):
        cards.append(f'<article><small>{html.escape(p["category"])}</small><h2>{html.escape(p["name"])}</h2><p>{html.escape(p["description"])}</p><strong>₹{p["offer_price_inr"]:,}</strong> <del>₹{p["price_inr"]:,}</del><p>QC {html.escape(p["qc_code"])} · Gate {html.escape(p["gate_no"])} · Dispatch NO</p><a href="generated/four-stage-production/products/{p["product_id"]}.html">Open product</a></article>')
    SHOWROOM.write_text(f"""<!doctype html><html lang="hi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>꙰ SHIRMANI Supreme Public Production Showroom</title><style>body{{margin:0;background:#050b12;color:#eef5f8;font:16px system-ui}}header,main{{max-width:1400px;margin:auto;padding:22px}}header{{background:linear-gradient(135deg,#10233a,#071018);border-bottom:2px solid #ffd84a}}h1,h2{{color:#ffd84a}}.stats,.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px}}.stat,article{{background:#101923;border:1px solid #354858;border-radius:16px;padding:16px}}.num{{font-size:2rem;font-weight:900}}article strong{{font-size:1.35rem;color:#ffd84a}}a{{display:inline-block;padding:9px 12px;background:#ffd84a;color:#101010;border-radius:8px;text-decoration:none;font-weight:800}}</style><header><h1>꙰ SHIRMANI Supreme Public Production Showroom</h1><p>Institute → Factory → QC Gate → Public Showroom / Sale</p><div class="stats"><div class="stat">Modules discovered<div class="num">{len(files):,}</div></div><div class="stat">Products produced<div class="num">{len(allp):,}</div></div><div class="stat">Current public window<div class="num">{len(public):,}</div></div><div class="stat">Dispatch YES<div class="num">0</div></div></div><p>हर product के साथ price, offer, description, QC code, Gate No., QR payload और dispatch state है। Production automission हर 5 मिनट चलता है।</p></header><main><h2>Latest Production</h2><section class="grid">{''.join(cards)}</section></main></html>""",encoding="utf-8")
    print(json.dumps(status,ensure_ascii=False))

if __name__=="__main__": main()
