#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; GEN=ROOT/"generated"; OUT=GEN/"supreme-production"
DIRS=("agents","factory","automation","source","scripts","schemas","products","research","docs")
EXTS={".py",".js",".mjs",".ts",".html",".htm",".css",".md",".json",".yml",".yaml",".txt",".svg"}
PRICE={".py":499,".js":399,".mjs":399,".ts":499,".html":299,".htm":299,".css":199,".md":149,".json":249,".yml":199,".yaml":199,".txt":99,".svg":299}
def now(): return datetime.now(timezone.utc).isoformat()
def digest(s): return hashlib.sha256(s.encode("utf-8",errors="ignore")).hexdigest()
def lane(p):
 s=str(p).lower()
 if "research" in s or "source" in s:return "research"
 if "agent" in s or "nlp" in s or "ml" in s or "ai" in s:return "ai-ml-nlp"
 if "automation" in s or "factory" in s or "workflow" in s:return "automation"
 if "schema" in s or "qc" in s or "quality" in s:return "security-quality"
 if "product" in s or "commerce" in s or "income" in s:return "economic"
 return "platform"
def qc(p,c,sku):
 checks=[("EXISTS",p.exists()),("NON_EMPTY",len(c.strip())>=40),("NOT_GENERATED","generated" not in p.parts)]
 if p.suffix.lower()==".json":
  try: json.loads(c); checks.append(("JSON_PARSE",True))
  except: checks.append(("JSON_PARSE",False))
 elif p.suffix.lower()==".py":
  try: compile(c,str(p),"exec"); checks.append(("PY_COMPILE",True))
  except: checks.append(("PY_COMPILE",False))
 elif p.suffix.lower() in {".html",".htm"}: checks.append(("HTML_MARKUP",bool(re.search(r"<(html|main|body|section|div|article)\b",c,re.I))))
 else: checks.append(("CONTENT",bool(c.strip())))
 ok=all(v for _,v in checks); code="QC-"+digest(sku+"|"+"|".join(f"{a}:{int(b)}" for a,b in checks))[:12].upper()
 return ok,code,checks
def modes():
 p=GEN/"1000-digital-products.json"
 if not p.exists(): return []
 try:
  d=json.loads(p.read_text(encoding="utf-8")); out=[]
  for x in d.get("products",[]):
   y=dict(x); y.update(product_class="runnable-product-mode",production_stage="FACTORY",qc_gate="MODE-CATALOG",qc_code="CATALOG-QC",dispatch="NO",commercial_state="CATALOG_LISTED"); out.append(y)
  return out
 except:return []
def main():
 GEN.mkdir(exist_ok=True); OUT.mkdir(exist_ok=True)
 files=[]
 for d in DIRS:
  root=ROOT/d
  if root.exists(): files += [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in EXTS and "generated" not in p.parts and ".git" not in p.parts and "node_modules" not in p.parts]
 files=sorted(set(files)); batch="BATCH-"+datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"); products=[]; qcrows=[]
 for i,p in enumerate(files,1):
  c=p.read_text(encoding="utf-8",errors="ignore"); rel=p.relative_to(ROOT).as_posix(); h=digest(c); sku="SRI-"+h[:10].upper(); ok,code,checks=qc(p,c,sku)
  products.append({"product_id":"SPM-"+h[:16],"sku":sku,"name":"SHIRMANI "+p.stem.replace("_"," ").replace("-"," ").title(),"category":lane(p),"product_class":"module-production-package","source_module":rel,"source_hash":h[:32],"production_batch":batch,"production_stage":"FACTORY","description":"Concrete production package generated from "+rel,"deliverables":["source-bound package","description","QC record","showroom record"],"list_price_inr":PRICE.get(p.suffix.lower(),199),"offer":{"type":"LAUNCH","discount_percent":20,"display":"20% launch offer"},"packing":"DIGITAL-PRIME-PACK","qc":{"gate_no":f"GATE-{i:06d}","qc_code":code,"status":"PASS" if ok else "FAIL","checks":dict(checks)},"dispatch":"YES" if ok else "NO","showroom":"LISTED","commercial_state":"SALE_READY_LISTING" if ok else "QC_HOLD","created_at":now()})
  qcrows.append({"gate_no":f"GATE-{i:06d}","sku":sku,"qc_code":code,"status":"PASS" if ok else "FAIL","source_module":rel})
 m=modes(); allp=products+m; cp={"schema_version":1,"generated_at":now(),"production_batch":batch,"four_levels":["INSTITUTE_DISCOVERY","FACTORY_PRODUCTION","QC_GATE","PUBLIC_SHOWROOM"],"principle":"Production first; QC evaluates produced results.","module_product_count":len(products),"runnable_mode_count":len(m),"total_catalog_count":len(allp),"qc_summary":{"pass":sum(x["qc"]["status"]=="PASS" for x in products),"fail":sum(x["qc"]["status"]=="FAIL" for x in products)},"products":allp}
 (GEN/"supreme-product-catalog.json").write_text(json.dumps(cp,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 (OUT/"production-batch.jsonl").write_text("\n".join(json.dumps(x,ensure_ascii=False) for x in products)+"\n",encoding="utf-8")
 (OUT/"qc-gates.jsonl").write_text("\n".join(json.dumps(x,ensure_ascii=False) for x in qcrows)+"\n",encoding="utf-8")
 st={"generated_at":now(),"batch":batch,"institute_discovery":{"modules_found":len(files)},"factory_production":{"concrete_module_products":len(products)},"qc_gate":cp["qc_summary"],"showroom":{"listed_total":len(allp),"dispatch_yes":sum(x["dispatch"]=="YES" for x in products),"dispatch_no":sum(x["dispatch"]=="NO" for x in products)},"runnable_catalog_modes":len(m),"production_first":True}
 (GEN/"supreme-production-status.json").write_text(json.dumps(st,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(json.dumps(st,ensure_ascii=False))
if __name__=="__main__":main()
