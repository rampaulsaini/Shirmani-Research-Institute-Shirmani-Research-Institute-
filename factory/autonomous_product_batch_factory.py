#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import os,json,html
ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/"generated/1000-digital-products.json"; OUT=ROOT/"products/concrete"; OVL=ROOT/"generated/concrete-production-overlay.json"; STATE=ROOT/"generated/live-production-state.json"; PASS=ROOT/"generated/PRODUCT-PASSPORTS.jsonl"
def J(p,d):
 try:return json.loads(p.read_text(encoding="utf-8"))
 except:return d
def esc(x):return html.escape(str(x or ""),quote=True)
def main():
 rows=J(CAT,{}).get("products",[]); OUT.mkdir(parents=True,exist_ok=True)
 existing={p.stem.upper() for p in OUT.glob("SP-*.html")}; batch=max(1,min(500,int(os.getenv("PRODUCT_BATCH","100"))))
 now=datetime.now(timezone.utc); bid="BATCH-"+now.strftime("%Y%m%dT%H%M%SZ"); made=[]
 for i,p in enumerate(rows):
  if len(made)>=batch:break
  pid=str(p.get("id") or f"SP-{i+1:04d}")
  if not pid.startswith("SP-"):pid=f"SP-{i+1:04d}"
  if pid in existing:continue
  name=p.get("name") or pid; fam=p.get("family") or p.get("category") or "Digital Product"; eng=p.get("engine") or "browser"; desc=p.get("short_description") or p.get("description") or "Customer-facing digital product."
  price=p.get("offer_price_inr",p.get("price_inr",0)) or 0
  body=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(name)} · {pid}</title><style>body{{margin:0;background:#060b12;color:#f5f7fb;font:16px/1.6 system-ui}}main{{max-width:1000px;margin:auto;padding:28px}}section{{background:#101a27;border:1px solid #32475d;border-radius:20px;padding:24px;margin:14px 0}}h1,h2{{color:#e8c65b}}.id{{color:#63e7ff;font-weight:900}}a{{display:inline-block;background:#e8c65b;color:#111;padding:10px 14px;border-radius:10px;text-decoration:none;font-weight:900;margin:4px}}</style></head><body><main><section><div class="id">{esc(pid)}</div><h1>{esc(name)}</h1><p><b>{esc(fam)} · {esc(eng)}</b></p><p>{esc(desc)}</p><p><b>Price / offer:</b> ₹{int(price):,}</p><a href="../../product-passport.html?id={pid}">Product Passport</a><a href="../../showroom-public-interface.html">Showroom</a></section><section><h2>How to use</h2><ol><li>Read the product passport.</li><li>Open the demo route when available.</li><li>Use the product according to its instructions.</li><li>Submit customer feedback for future improvement.</li></ol></section><section><h2>Production state</h2><p>Institute → Factory → QC/Gate → Public Showroom</p><p>Batch: {bid}<br>QC code: QC-PROD-{pid}<br>Gate: GATE-PRODUCTION<br>Dispatch: NO</p><p>Production artifact does not itself claim independent scientific verification.</p></section></main></body></html>'''
  (OUT/(pid+".html")).write_text(body,encoding="utf-8")
  made.append({"id":pid,"name":name,"category":p.get("category") or fam,"family":fam,"engine":eng,"artifact_url":"products/concrete/"+pid+".html","production_batch":bid,"produced_at":now.isoformat(),"qc_code":"QC-PROD-"+pid,"gate_no":"GATE-PRODUCTION","dispatch_no":"NO","production_state":"PRODUCED","sale_state":"READY_FOR_ORDER","price_inr":price,"short_description":desc})
 old=J(OVL,{"schema_version":1,"architecture":["INSTITUTE","FACTORY","QC","SHOWROOM_SALE"],"production_first":True,"verification_is_downstream":True,"products":[]}); d={x.get("id"):x for x in old.get("products",[]) if isinstance(x,dict)}
 for x in made:d[x["id"]]=x
 allp=list(d.values()); old.update({"generated_at":now.isoformat(),"batch":bid,"product_count":len(rows),"produced_count":len(allp),"remaining_count":max(0,len(rows)-len(allp)),"batch_size":batch,"products":allp}); OVL.write_text(json.dumps(old,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 with PASS.open("a",encoding="utf-8") as f:
  for x in made:f.write(json.dumps({"id":x["id"],"name":x["name"],"category":x["category"],"family":x["family"],"engine":x["engine"],"short_description":x["short_description"],"artifact_url":x["artifact_url"],"price_inr":x["price_inr"],"qc_code":x["qc_code"],"gate_no":x["gate_no"],"dispatch_no":"NO","production_batch":bid,"produced_at":x["produced_at"],"demo_route":"product-specific-demo","long_description_route":"product-passport.html?id="+x["id"],"truth_boundary":"Production artifact; not independent scientific verification."},ensure_ascii=False)+"\n")
 s=J(STATE,{}); total=len(allp); s.update({"generated_at":now.isoformat(),"catalog_identities":len(rows),"concrete_repository_assets":total,"current_catalog_pending":max(0,len(rows)-total),"five_thousand_scale_target":5000,"remaining_to_scale_target":max(0,5000-total),"concrete_materialization_percent_of_catalog":round(100*total/max(1,len(rows)),2),"concrete_materialization_percent_of_scale_target":round(100*total/5000,2),"module_products_generated":total,"dispatch_released":0,"sales_claimed":0,"payment_claimed":0,"independent_verification_claimed":0,"state":"PRODUCTION_IN_PROGRESS","last_batch_created":len(made),"last_batch_id":bid}); STATE.write_text(json.dumps(s,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print({"batch":bid,"created":len(made),"concrete_total":total,"remaining_to_5000":max(0,5000-total)})
if __name__=="__main__":main()
