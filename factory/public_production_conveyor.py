#!/usr/bin/env python3
"""SHIRMANI public production conveyor: produce concrete result manifests and public telemetry."""
from __future__ import annotations
import hashlib,json,os
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; GEN=ROOT/"generated"; CAT=GEN/"1000-digital-products.json"
OUT=GEN/"production-results"; STATUS=GEN/"public-production-status.json"; CENTER=GEN/"public-production-command-center.json"
BATCH=int(os.environ.get("PUBLIC_PRODUCTION_BATCH","100"))
def now(): return datetime.now(timezone.utc)
def digest(x): return hashlib.sha256(x.encode("utf-8",errors="ignore")).hexdigest()
def main():
    catalog=json.loads(CAT.read_text(encoding="utf-8")); products=catalog.get("products",[])
    OUT.mkdir(parents=True,exist_ok=True); stamp=now(); cycle=stamp.strftime("%Y%m%dT%H%M%SZ")
    offset=((stamp.year*366+stamp.timetuple().tm_yday)*288+stamp.hour*12+stamp.minute//5)*BATCH % max(1,len(products))
    selected=[products[(offset+i)%len(products)] for i in range(min(BATCH,len(products)))]
    rows=[]
    for p in selected:
        asset=ROOT/p.get("asset",""); module=ROOT/p.get("module","")
        at=asset.read_text(encoding="utf-8",errors="ignore") if asset.exists() else ""
        mt=module.read_text(encoding="utf-8",errors="ignore") if module.exists() else ""
        engine=p.get("engine","package")
        rt={"calculator":"interactive calculation module","text":"text/NLP analysis module","nlp":"ML/NLP production module","research":"research/QC record module","seo":"SEO production package","data":"data inspection module","visual":"visual production specification","game":"interactive game module","quantum":"quantum-inspired classical simulation module"}.get(engine,"interactive digital production module")
        rows.append({"production_id":"PR-"+digest(cycle+"|"+p["id"])[:16].upper(),"cycle":cycle,"product_id":p["id"],"name":p["name"],"family":p.get("family"),"engine":engine,"production_state":"PRODUCED","result_type":rt,"asset_path":p.get("asset"),"module_path":p.get("module"),"asset_bytes":len(at.encode()),"module_bytes":len(mt.encode()),"asset_hash":digest(at)[:32],"module_hash":digest(mt)[:32],"qc_code":p.get("qc_code"),"gate_no":p.get("gate_no"),"dispatch_no":"NO","price_inr":p.get("price_inr"),"offer_price_inr":p.get("offer_price_inr"),"offer":p.get("offer"),"guarantee":p.get("guarantee"),"packing":p.get("packing"),"showroom_url":"supreme-marking-hub.html?id="+p["id"],"product_url":p.get("asset"),"produced_at":stamp.isoformat()})
    text="\n".join(json.dumps(x,ensure_ascii=False) for x in rows)+"\n"; (OUT/f"{cycle}.jsonl").write_text(text,encoding="utf-8"); (OUT/"latest.jsonl").write_text(text,encoding="utf-8")
    families={}; engines={}
    for p in rows: families[p["family"]]=families.get(p["family"],0)+1; engines[p["engine"]]=engines.get(p["engine"],0)+1
    status={"generated_at":stamp.isoformat(),"cycle":cycle,"production_first":True,"batch_size":len(rows),"catalog_total":len(products),"family_total":catalog.get("family_count",0),"engine_total":catalog.get("engine_count",0),"produced_this_cycle":len(rows),"production_state":"PRODUCED","qc_state":"READY_DOWNSTREAM","dispatch_no":len(rows),"dispatch_yes":0,"verification":"DOWNSTREAM_RESULT_QUALITY","families_this_cycle":families,"engines_this_cycle":engines,"continuity":"scheduled workflow; chat not required"}
    STATUS.write_text(json.dumps(status,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    CENTER.write_text(json.dumps({"generated_at":stamp.isoformat(),"pipeline":["INSTITUTE_DISCOVERY","FACTORY_PRODUCTION","QC_GATE","PUBLIC_SHOWROOM_SALE"],"catalog":{"products":len(products),"families":catalog.get("family_count",0),"engines":catalog.get("engine_count",0)},"cycle":status,"latest_results":"generated/production-results/latest.jsonl","showroom":"supreme-marking-hub.html","command_center":"generated/public-production-command-center.html","module_map":"generated/public-production-by-module.html"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(status,ensure_ascii=False))
if __name__=="__main__": main()
