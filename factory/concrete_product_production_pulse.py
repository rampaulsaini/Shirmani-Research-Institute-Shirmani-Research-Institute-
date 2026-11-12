#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import json,html,os
ROOT=Path(__file__).resolve().parents[1]
OV=ROOT/"generated/concrete-production-overlay.json"; LIVE=ROOT/"generated/live-production-state.json"
OUT=ROOT/"products/concrete"; CAT=ROOT/"generated/public-production-catalog.json"
def page(p):
 pid=str(p["id"]); name=str(p.get("name") or "SHIRMANI Digital Product"); desc=str(p.get("short_description") or p.get("description") or "Customer-facing digital product.")
 price=p.get("offer_price_inr",p.get("price_inr",0)); qc=p.get("qc_code",f"QC-PROD-{pid}"); gate=p.get("gate_no","GATE-PRODUCTION")
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(name)} · SHIRMANI</title><meta name="description" content="{html.escape(desc[:155],quote=True)}"><style>body{{margin:0;background:#050910;color:#f5f7fb;font:16px/1.6 system-ui}}main{{max-width:1100px;margin:auto;padding:24px}}section{{background:#0c1722;border:1px solid #304457;border-radius:20px;padding:24px;margin:14px 0}}h1,h2{{color:#e7c85b}}a{{display:inline-block;padding:11px 15px;background:#e7c85b;color:#111;border-radius:10px;text-decoration:none;font-weight:900;margin:5px}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}}.m{{background:#07111a;border:1px solid #304457;border-radius:14px;padding:15px}}</style></head><body><main><section><h1>{html.escape(name)}</h1><p>{html.escape(desc)}</p><a href="../product-demo.html?id={pid}">Demo</a><a href="../product-passport.html?id={pid}">Product Passport</a></section><section><h2>How to use</h2><ol><li>Open the demo.</li><li>Enter the required task or input.</li><li>Run the product module.</li><li>Inspect and reuse the result.</li><li>Submit customer feedback for improvement.</li></ol></section><section class="grid"><div class="m"><b>Product ID</b><br>{html.escape(pid)}</div><div class="m"><b>Rate</b><br>₹{html.escape(str(price))}</div><div class="m"><b>QC</b><br>{html.escape(str(qc))}</div><div class="m"><b>Gate</b><br>{html.escape(str(gate))}</div></section><section><h2>Production boundary</h2><p>Concrete showroom artifact. Payment, dispatch and independent verification remain separate states.</p></section></main></body></html>'''
def main():
 data=json.loads(OV.read_text()); rows=data["products"]; batch=max(1,min(500,int(os.getenv("CONCRETE_PRODUCT_BATCH","250")))); OUT.mkdir(parents=True,exist_ok=True)
 selected=[]
 for p in rows:
  pid=str(p.get("id","")); path=OUT/f"{pid}.html"
  if pid and not path.exists(): selected.append((p,path))
 for p,path in selected[:batch]:
  path.write_text(page(p),encoding="utf-8"); p.update(production_state="PRODUCED",sale_state=p.get("sale_state","READY_FOR_ORDER"),artifact_url=f"products/concrete/{p['id']}.html",produced_at=datetime.now(timezone.utc).isoformat(),qc_code=p.get("qc_code",f"QC-PROD-{p['id']}"),gate_no=p.get("gate_no","GATE-PRODUCTION"),dispatch_no=p.get("dispatch_no","NO"))
 produced=sum((OUT/f"{p.get('id','')}.html").exists() for p in rows); now=datetime.now(timezone.utc).isoformat(); total=len(rows)
 data.update(generated_at=now,produced_count=produced,remaining_count=total-produced,batch_size=batch,production_first=True,verification_is_downstream=True)
 OV.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
 LIVE.write_text(json.dumps({"schema_version":2,"generated_at":now,"production_first":True,"catalog_identities":total,"concrete_repository_assets":produced,"current_catalog_pending":total-produced,"five_thousand_scale_target":5000,"remaining_to_scale_target":max(0,5000-produced),"concrete_materialization_percent_of_scale_target":round(produced/50,2),"module_products_generated":produced,"dispatch_released":0,"sales_claimed":0,"payment_claimed":0,"independent_verification_claimed":0,"last_cycle_concrete_results":len(selected[:batch]),"state":"PRODUCTION_COMPLETE_FOR_CATALOG" if produced>=total else "PRODUCTION_IN_PROGRESS","truth_boundary":"Concrete production is customer-visible output; payment, dispatch and independent verification remain separate states."},ensure_ascii=False,indent=2)+"\n")
 CAT.write_text(json.dumps({"schema_version":2,"generated_at":now,"production_first":True,"product_count":total,"produced_count":produced,"remaining_count":total-produced,"products":rows},ensure_ascii=False,indent=2)+"\n")
 print(json.dumps({"catalog":total,"produced":produced,"created_this_cycle":len(selected[:batch]),"remaining":total-produced}))
if __name__=="__main__": main()
