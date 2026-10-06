#!/usr/bin/env python3
"""SHIRMANI Institute -> Factory -> QC -> Showroom production controller."""
from __future__ import annotations
import json, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN = ROOT / "generated"
PY = sys.executable
STEPS = ["factory/public_module_inventory.py","factory/real_product_factory.py","factory/materialize_all_product_assets.py","factory/concrete_product_modules.py","factory/product_asset_expander.py","factory/production_queue_builder.py","factory/supreme_production_engine.py","factory/public_production_materializer.py","factory/product_qc_gate.py"]

def run(path: str) -> dict:
    r = subprocess.run([PY, str(ROOT / path)], cwd=ROOT, text=True, capture_output=True, check=False)
    return {"step": path, "exit_code": r.returncode, "output": (r.stdout + r.stderr)[-1600:]}

def read_json(name: str) -> dict:
    p = GEN / name
    if not p.exists(): return {}
    try: return json.loads(p.read_text(encoding="utf-8"))
    except Exception: return {}

def main() -> None:
    GEN.mkdir(exist_ok=True)
    started = datetime.now(timezone.utc).isoformat()
    report = {"generated_at": started, "mode": "CONTINUOUS_FOUR_STAGE_PRODUCTION", "chat_required_for_continuity": False, "principle": "Production first; QC is the release gate; downstream verification evaluates results.", "stages": []}

    stage1 = run(STEPS[0]); inv = read_json("public-module-inventory.json")
    report["stages"].append({"stage":1,"name":"INSTITUTE_DISCOVERY","status":"PASS" if stage1["exit_code"]==0 else "FAIL","modules_discovered":inv.get("module_count",0),"lane_counts":inv.get("lane_counts",{}),"run":stage1})

    factory_steps=[]; factory_failed=False
    for path in STEPS[1:8]:
        r=run(path); factory_steps.append(r)
        if r["exit_code"]!=0: factory_failed=True
    # Resilient production: one lane failure does not suppress later production lanes.
    report["stages"].append({"stage":2,"name":"FACTORY_PRODUCTION","status":"PASS" if not factory_failed and stage1["exit_code"]==0 else "FAIL","steps":factory_steps,"catalog":read_json("real-product-factory-status.json"),"asset_status":read_json("concrete-product-asset-status.json"),"module_engine":read_json("production-engine-status.json")})

    qc_run=run(STEPS[-1]); qc=read_json("product-qc-gate.json")
    report["stages"].append({"stage":3,"name":"PRODUCT_QC_GATE","status":"PASS" if qc_run["exit_code"]==0 else "FAIL","qc":qc,"run":qc_run})

    showroom = "supreme-showroom.html"
    showroom_exists=(ROOT/showroom).exists()
    catalog=read_json("1000-digital-products.json")
    registry=read_json("production-registry.json")
    production_ok=not factory_failed and stage1["exit_code"]==0
    qc_ok=qc_run["exit_code"]==0
    report["stages"].append({"stage":4,"name":"PUBLIC_SHOWROOM","status":"READY" if showroom_exists and production_ok and qc_ok else "BLOCKED","showroom":showroom if showroom_exists else None,"catalog_products":catalog.get("product_count",0),"produced_products":registry.get("produced_count",registry.get("total_materialized_module_products",catalog.get("product_count",0))),"qc_passed":qc.get("qc_passed",0),"dispatch_default":"NO","public_sale_claim":False,"entry_fee_config":"generated/showroom-entry-fees.json"})

    report["production_contract"]={"stage_1_institute":"continuous module/product discovery","stage_2_factory":"continuous concrete product and module production","stage_3_qc":"deterministic product structure/asset/passport gate","stage_4_showroom":"public catalog with product, description, price, offer, QR/passport, time-based showroom entry and dispatch state","dispatch":"NO by default until explicit downstream release","verification":"downstream result-quality/promotion layer, not the production objective","schedule":"every 5 minutes","continuity_without_chat":True,"quantum_boundary":"quantum-inspired orchestration only unless a real quantum backend is configured"}

    module_status=read_json("production-engine-status.json")
    asset_status=read_json("concrete-product-asset-status.json")
    throughput={
        "generated_at": started,
        "cycle_mode": "CONTINUOUS_FOUR_STAGE_PRODUCTION",
        "chat_required_for_continuity": False,
        "stages": [{"stage":x["stage"],"name":x["name"],"status":x["status"]} for x in report["stages"]],
        "institute_modules_discovered": report["stages"][0].get("modules_discovered",0),
        "catalog_products": catalog.get("product_count",0),
        "concrete_product_assets": asset_status.get("concrete_product_assets",asset_status.get("product_assets",0)),
        "module_products_this_cycle": module_status.get("concrete_module_products_this_cycle",0),
        "module_products_total": module_status.get("total_materialized_module_products",0),
        "qc_passed": qc.get("qc_passed",0),
        "dispatch_released": 0,
        "verification": "DOWNSTREAM",
        "production_priority": "MULTI-LAYER CONTINUOUS OUTPUT",
        "schedule": "5-minute GitHub Actions cycle"
    }
    (GEN/"production-throughput.json").write_text(json.dumps(throughput,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (GEN/"four-stage-production-status.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    public={"generated_at":report["generated_at"],"stages":[{"stage":s["stage"],"name":s["name"],"status":s["status"]} for s in report["stages"]],"products":{"catalog":catalog.get("product_count",0),"produced":registry.get("produced_count",registry.get("total_materialized_module_products",catalog.get("product_count",0))),"qc_passed":qc.get("qc_passed",0),"dispatch":0},"showroom":"supreme-showroom.html","entry_fees":"generated/showroom-entry-fees.json","principle":"Production → QC gate → Showroom → downstream verification"}
    # Keep public showroom telemetry bound to concrete production data.
    production_status = {
        "schema_version": 1,
        "generated_at": report["generated_at"],
        "source": "generated/production-registry.json",
        "catalog_products": catalog.get("product_count", 0),
        "produced": registry.get("produced_count", registry.get("total_materialized_module_products", catalog.get("product_count", 0))),
        "qc_ready": qc.get("qc_passed", 0),
        "dispatch_yes": sum(1 for p in registry.get("products", []) if p.get("dispatch_no") == "YES"),
        "dispatch_default": "NO",
        "engine_count": registry.get("engine_count", 0),
        "family_count": registry.get("family_count", 0),
        "production_first": True,
        "verification_position": "DOWNSTREAM",
        "showroom": "supreme-showroom.html",
        "chat_required_for_continuity": False
    }
    (GEN/"production-status.json").write_text(json.dumps(production_status,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (GEN/"production-release-map.json").write_text(json.dumps(public,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False))
    if any(s["status"]=="FAIL" for s in report["stages"]): raise SystemExit(1)

if __name__=="__main__": main()
