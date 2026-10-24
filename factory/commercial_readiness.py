from pathlib import Path
from datetime import datetime, timezone
import json, re
R=Path(__file__).resolve().parents[1]; G=R/"generated"
def J(p,d={}):
    try:return json.loads(p.read_text(encoding="utf-8"))
    except:return d
c=J(R/"factory/product-catalog.json"); t=J(G/"concrete-product-truth.json"); v=J(G/"verification-status.json"); cfg=J(R/"config/independent-verification-target.json")
offers=[o for l in c.get("lanes",[]) for o in l.get("offers",[])]
paid=[o for o in offers if o.get("price_inr",0)]
prod=int(t.get("concrete_produced",0)); total=int(t.get("catalog_count",0)); verified=int(t.get("independent_verification_claimed",v.get("verified_records",0))); target=int(cfg.get("verification_target",100200))
w=list((R/".github/workflows").glob("*.y*ml"))
classes={k:0 for k in ["production","product","nlp","evidence","verification","quality","other"]}
for p in w:
 s=p.read_text(encoding="utf-8",errors="ignore").lower(); hit=False
 for k,terms in {"production":["production","concrete","factory"],"product":["product","catalog","showroom"],"nlp":["nlp","language"],"evidence":["evidence"],"verification":["verification","verify"],"quality":["quality","benchmark","evaluation","reality"]}.items():
  if any(x in s for x in terms): classes[k]+=1; hit=True
 if not hit: classes["other"]+=1
out={"generated_at":datetime.now(timezone.utc).isoformat(),"catalog_offers":len(offers),"paid_offers":len(paid),"concrete_products":prod,"concrete_target":total,"concrete_percent":round(prod*100/total,2) if total else 0,"sales_evidenced":int(t.get("sales_claimed",0)),"payments_evidenced":int(t.get("payment_claimed",0)),"independent_verified":verified,"verification_target":target,"verification_percent":round(verified*100/target,6) if target else 0,"workflow_count":len(w),"workflow_classes":classes,"truth_rule":"workflow success != sale != payment != independent verification"}
G.mkdir(exist_ok=True); (G/"commercial-readiness.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,ensure_ascii=False,indent=2))
