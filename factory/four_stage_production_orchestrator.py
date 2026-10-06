#!/usr/bin/env python3
"""SHIRMANI Institute -> Factory -> QC -> Showroom production controller."""
from __future__ import annotations
import json, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; GEN=ROOT/"generated"; PY=sys.executable
STEPS=["factory/public_module_inventory.py","factory/real_product_factory.py","factory/materialize_all_product_assets.py",
"factory/concrete_product_modules.py","factory/product_asset_expander.py","factory/production_queue_builder.py",
"factory/supreme_production_engine.py","factory/public_production_materializer.py","factory/product_qc_gate.py"]
def run(p):
 r=subprocess.run([PY,str(ROOT/p)],cwd=ROOT,text=True,capture_output=True,check=False)
 return {"step":p,"exit_code":r.returncode,"output":(r.stdout+r.stderr)[-1200:]}
def main():
 GEN.mkdir(exist_ok=True); started=datetime.now(timezone.utc).isoformat(); report={"generated_at":started,
 "mode":"CONTINUOUS_FOUR_STAGE_PRODUCTION","chat_required_for_continuity":False,"stages":[]}
 for i,p in enumerate(STEPS,1):
  r=run(p)
  if i==1:
   inv=json.loads((GEN/"public-module-inventory.json").read_text()) if (GEN/"public-module-inventory.json").exists() else {}
   report["stages"].append({"stage":1,"name":"INSTITUTE_DISCOVERY","status":"PASS" if r["exit_code"]==0 else "FAIL",
                            "modules_discovered":inv.get("module_count",0),"lane_counts":inv.get("lane_counts",{}),"run":r})
  elif i<=8:
   if not any(s["name"]=="FACTORY_PRODUCTION" for s in report["stages"]):
    report["stages"].append({"stage":2,"name":"FACTORY_PRODUCTION","status":"PASS","steps":[]})
   report["stages"][-1]["steps"].append(r)
  else:
   q=json.loads((GEN/"product-qc-gate.json").read_text()) if (GEN/"product-qc-gate.json").exists() else {}
   report["stages"].append({"stage":3,"name":"PRODUCT_QC_GATE","status":"PASS" if r["exit_code"]==0 else "FAIL","qc":q,"run":r})
  if r["exit_code"]!=0:
   report["stages"][-1]["status"]="FAIL"; break
 cat=json.loads((GEN/"1000-digital-products.json").read_text()) if (GEN/"1000-digital-products.json").exists() else {}
 report["stages"].append({"stage":4,"name":"PUBLIC_SHOWROOM","status":"READY" if (ROOT/"supreme-production-showroom.html").exists() else "MISSING",
 "showroom":"supreme-production-showroom.html","catalog_products":cat.get("product_count",0),"families":cat.get("family_count",0),
 "dispatch_policy":"NO until authorized downstream dispatch"})
 report["production_contract"]={"institute":"continuous discovery","factory":"continuous product/module production",
 "qc":"deterministic product release gate","showroom":"public catalog and sale surface","dispatch":"NO by default",
 "independent_verification":"downstream result-quality layer","schedule":"every 5 minutes","continuity_without_chat":True}
 (GEN/"four-stage-production-status.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(json.dumps(report,ensure_ascii=False))
 if any(s["status"]=="FAIL" for s in report["stages"]): raise SystemExit(1)
if __name__=="__main__": main()
