#!/usr/bin/env python3
"""Concrete production engine for rotating repository modules."""
from __future__ import annotations
import hashlib,html,json,re
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
GEN=ROOT/"generated"; OUT=GEN/"module-products"
QUEUE=GEN/"production-work-queue.jsonl"
REG=GEN/"module-product-registry.json"; STATUS=GEN/"production-engine-status.json"
BASE="https://rampaulsaini.github.io/Shirmani-Research-Institute-Shirmani-Research-Institute-/"
SKIP={".git",".github","generated","node_modules","__pycache__",".venv","dist","build"}
EXT={".html",".md",".py",".json",".yml",".yaml"}
LANES={
"ai-ml-nlp":("nlp","ml","ai-","automission","agent","model","language"),
"research":("research","paper","evidence","study","science"),
"economic":("income","employment","economic","store","market","product","business"),
"content":("content","blog","copy","writing","article"),
"social-media":("social","youtube","facebook","instagram","podcast"),
"federation":("federation","repository","integration","network"),
"security-quality":("security","quality","qc","schema","governance"),
"automation":("workflow","factory","automation","orchestrator","worker"),
}
OBJECTIVES={
"ai-ml-nlp":"Concrete AI/ML/NLP module output",
"research":"Concrete research/evidence work product",
"economic":"Concrete lawful product/service/livelihood asset",
"content":"Concrete publishable content asset",
"social-media":"Concrete distribution-ready media asset",
"federation":"Concrete integration/bridge asset",
"security-quality":"Concrete QC/provenance/resilience asset",
"automation":"Concrete automation/control asset",
"platform":"Concrete public module/product surface"}

def digest(s): return hashlib.sha256(s.encode()).hexdigest()
def lane(p):
 s=str(p).lower()
 for n,keys in LANES.items():
  if any(k in s for k in keys): return n
 return "platform"
def title(p,s):
 m=re.search(r"<title[^>]*>(.*?)</title>",s,re.I|re.S)
 if m:
  t=re.sub(r"\s+"," ",re.sub("<[^>]+>","",m.group(1))).strip()
  if t:return t[:140]
 for x in s.splitlines():
  x=re.sub(r"^\s*#+\s*","",x).strip()
  if x and not x.startswith(("{","[","import ","from ","<")):return x[:140]
 return p.stem.replace("-"," ").replace("_"," ").title()
def discover():
 out=[]
 for p in ROOT.rglob("*"):
  if p.is_file() and p.suffix.lower() in EXT and not any(x in p.parts for x in SKIP):
   rel=p.relative_to(ROOT).as_posix()
   if rel=="factory/supreme_production_engine.py":continue
   out.append((rel,p.suffix[1:],lane(p),p.read_text(encoding="utf-8",errors="ignore")))
 return {x[0]:x[1:] for x in out}
def page(rel,kind,ln,src,t):
 pid="MOD-"+digest(rel)[:12].upper(); fp=digest(src); name=title(Path(rel),src)
 qc="QC-"+digest(pid+"|"+fp)[:12].upper(); gate="GATE-"+str(int(digest(rel)[:6],16)%900+100)
 excerpt=" ".join(src.split())[:1600]
 return f'''<!doctype html><html lang="hi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>꙰ SHIRMANI Product — {html.escape(name)}</title><style>body{{margin:0;background:#080b12;color:#eef2f7;font-family:system-ui,sans-serif;line-height:1.55}}main{{max-width:1050px;margin:auto;padding:24px 16px 70px}}h1,h2{{color:#e7c45f}}section{{background:#111722;border:1px solid #334155;border-radius:18px;padding:20px;margin:14px 0}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px}}.m{{font-size:1.2rem;font-weight:900;color:#e7c45f}}.l{{color:#94a3b8;font-size:.75rem}}.ok{{color:#7ee2a8}}pre{{white-space:pre-wrap;background:#070a0f;padding:14px;border-radius:8px;overflow:auto}}a{{color:#67e8f9}}</style></head><body><main><section><h1>꙰ {html.escape(name)}</h1><p><b>Concrete module production output</b> generated from repository source.</p><div class="grid"><div><div class="l">Product ID</div><div class="m">{pid}</div></div><div><div class="l">Lane</div><div class="m">{html.escape(ln)}</div></div><div><div class="l">Cycle</div><div class="m">{t.get("cycle","")}</div></div><div><div class="l">State</div><div class="m">PRODUCED</div></div></div></section><section><h2>Production objective</h2><p>{html.escape(OBJECTIVES[ln])}</p><p class="ok">A concrete public module-product page has been materialized.</p></section><section><h2>Source binding</h2><p><b>Module:</b> <code>{html.escape(rel)}</code></p><p><b>Type:</b> {html.escape(kind)}</p><p><b>Fingerprint:</b> <code>{fp[:32]}</code></p><p><b>Work unit:</b> <code>{html.escape(t.get("task_id",""))}</code></p></section><section><h2>Build output</h2><p>source → normalize → build → publish → measure → iterate</p><pre>{html.escape(excerpt)}</pre></section><section><h2>QC / Gate / Dispatch</h2><div class="grid"><div><div class="l">QC code</div><div class="m">{qc}</div></div><div><div class="l">Gate No.</div><div class="m">{gate}</div></div><div><div class="l">Dispatch No.</div><div class="m">NOT-DISPATCHED</div></div><div><div class="l">Result state</div><div class="m">QC-READY</div></div></div><p>ये production-control fields हैं; इन्हें independent verification का विकल्प नहीं माना जाता।</p></section><section><a href="../public-production-index.html">Production Results</a> · <a href="../public-production-by-module.html">Module Map</a> · <a href="../../products.html">Catalog</a> · <a href="../../index.html">Main Hub</a></section></main></body></html>'''
def main():
 GEN.mkdir(exist_ok=True); OUT.mkdir(exist_ok=True)
 mods=discover(); tasks=[]
 if QUEUE.exists():
  for x in QUEUE.read_text(encoding="utf-8",errors="ignore").splitlines():
   try:tasks.append(json.loads(x))
   except:pass
 old={}
 if REG.exists():
  try:old=json.loads(REG.read_text(encoding="utf-8")).get("products",{})
  except:pass
 made=[]
 for t in tasks:
  rel=t.get("module")
  if rel not in mods:continue
  kind,ln,src=mods[rel]; pid="MOD-"+digest(rel)[:12].upper()
  (OUT/(pid.lower()+".html")).write_text(page(rel,kind,ln,src,t),encoding="utf-8")
  made.append({"product_id":pid,"module":rel,"lane":ln,"cycle":t.get("cycle"),"task_id":t.get("task_id"),"status":"PRODUCED","public_url":BASE+"generated/module-products/"+pid.lower()+".html","source_fingerprint":digest(src)[:32],"qc_code":"QC-"+digest(pid+"|"+digest(src))[:12].upper(),"gate_no":"GATE-"+str(int(digest(rel)[:6],16)%900+100),"dispatch_no":"NOT-DISPATCHED","verification":"DOWNSTREAM"})
 for x in made:old[x["product_id"]]=x
 REG.write_text(json.dumps({"schema_version":1,"generated_at":datetime.now(timezone.utc).isoformat(),"principle":"Production first; QC/gate/dispatch downstream.","discovered_modules":len(mods),"produced_this_cycle":len(made),"total_materialized_module_products":len(old),"products":dict(sorted(old.items()))},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 STATUS.write_text(json.dumps({"generated_at":datetime.now(timezone.utc).isoformat(),"cycle":max([x.get("cycle",0) for x in tasks],default=0),"discovered_modules":len(mods),"selected_work_units":len(tasks),"concrete_module_products_this_cycle":len(made),"total_materialized_module_products":len(old),"lane_outputs":dict(Counter(x["lane"] for x in made)),"autonomous_continuity":"scheduled GitHub Actions; chat is not required for a scheduled cycle","verification_position":"downstream","quantum_boundary":"quantum-inspired only unless a real quantum backend is configured"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(json.dumps({"discovered_modules":len(mods),"produced_this_cycle":len(made),"total_materialized_module_products":len(old)},ensure_ascii=False))
if __name__=="__main__":main()
