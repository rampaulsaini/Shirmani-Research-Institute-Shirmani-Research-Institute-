#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "production" / "PRODUCTION-MANIFEST.json"
OUT = ROOT / "generated" / "PRODUCTION-RELEASE-REGISTRY.json"

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
records, errors = [], []

for n, engine in enumerate(manifest["actual_engine_inventory"], 1):
    entry = ROOT / engine["entrypoint"]
    if not entry.exists():
        errors.append({"engine_id": engine["engine_id"], "error": "MISSING_MODULE_ENTRYPOINT", "path": engine["entrypoint"]})
        continue
    product_id = f"SP-ENG-{n:03d}"
    batch_no = f"100200.{n:03d}"
    source = f"{product_id}|{engine['engine_id']}|{engine['module']}|{engine['entrypoint']}|{batch_no}"
    qc_code = "QC-" + hashlib.sha256(source.encode()).hexdigest()[:12].upper()
    gate_no = f"GATE-{n:03d}"
    dispatch_no = f"DISPATCH-PENDING-{n:03d}"
    qr_payload = f"SHIRMANI|{product_id}|{batch_no}|{qc_code}|{gate_no}|{dispatch_no}"
    records.append({
        "product_id": product_id,
        "product_name": f"SHIRMANI {engine['name']}",
        "engine_id": engine["engine_id"],
        "module": engine["module"],
        "module_path": engine["entrypoint"],
        "version": "1.0.0",
        "batch_no": batch_no,
        "qc_code": qc_code,
        "gate_no": gate_no,
        "dispatch_no": dispatch_no,
        "qr_payload": qr_payload,
        "status": "RELEASE_READY",
        "created_at": datetime.now(timezone.utc).isoformat()
    })

status = "PASS" if records and not errors else "CHECK"
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps({
    "version": 1,
    "status": status,
    "batch_target": manifest["batch_model"]["batch_target"],
    "batch_sequence_start": ".001",
    "independent_product_engines": len(records),
    "errors": errors,
    "records": records
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": status, "records": len(records), "errors": len(errors)}))
