#!/usr/bin/env python3
"""Continuous multi-function product production controller."""
from __future__ import annotations
import json, os, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; GEN=ROOT/"generated"; PY=sys.executable
def run(path, env=None):
    e=os.environ.copy(); e.update({k:str(v) for k,v in (env or {}).items()})
    p=subprocess.run([PY,str(ROOT/path)],cwd=ROOT,text=True,capture_output=True,check=False,env=e)
    return {"step":path,"exit_code":p.returncode,"output":(p.stdout+p.stderr)[-1800:]}
def load(name):
    p=GEN/name
    if not p.exists(): return {}
    try:return json.loads(p.read_text(encoding="utf-8"))
    except Exception:return {}
def main():
    GEN.mkdir(exist_ok=True)
    v=os.getenv("VISUAL_BATCH","250"); q=os.getenv("QR_BATCH","250"); vip=os.getenv("VIP_BATCH","250"); demo=os.getenv("DEMO_BATCH","10")
    steps=[
      run("factory/public_module_inventory.py"),
      run("factory/real_product_factory.py"),
      run("factory/materialize_all_product_assets.py"),
      run("factory/product_visual_identity_factory.py",{"VISUAL_BATCH":v}),
      run("factory/product_qr_asset_factory.py",{"QR_BATCH":q}),
      run("factory/vip_screenshot_factory.py",{"VIP_SCREENSHOT_BATCH":vip}),
      run("factory/product_specific_demo_video_factory.py",{"PRODUCT_DEMO_BATCH":demo}),
      run("factory/public_production_materializer.py")]
    failed=[x for x in steps if x["exit_code"]!=0]
    cat=load("1000-digital-products.json"); st=load("concrete-product-asset-status.json"); media=load("product-specific-demo-video-manifest.json"); vm=load("vip-screenshot-assets.json")
    report={"schema_version":1,"generated_at":datetime.now(timezone.utc).isoformat(),"mode":"CONTINUOUS_MULTI_FUNCTION_PRODUCT_PRODUCTION","chat_required_for_continuity":False,"production_first":True,
      "targets":{"catalog_identities":cat.get("product_count",0),"visual_batch":int(v),"qr_batch":int(q),"vip_batch":int(vip),"demo_batch":int(demo)},
      "results":{"concrete_products":st.get("concrete_product_assets",st.get("product_assets",0)),"catalog_products":cat.get("product_count",0),"real_mp4":media.get("real_mp4_count",0),"vip_screenshots":vm.get("vip_screenshot_assets",vm.get("vip_screenshot_count",0))},
      "steps":steps,"cycle_state":"PARTIAL_FAILURE" if failed else "PRODUCED",
      "truth_boundary":"Production output is not sale, payment, dispatch or independent scientific verification."}
    (GEN/"multi-function-production-cycle.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False))
    if len(failed)==len(steps): raise SystemExit(1)
if __name__=="__main__": main()
