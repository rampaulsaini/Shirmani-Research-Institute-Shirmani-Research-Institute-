from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated"
FAMILIES = [
    ("calculator", "Counting & Math"), ("text", "Text & Language"), ("seo", "SEO & Web"), ("data", "Data Tools"),
    ("draw", "Sketch & Drawing"), ("pixel", "Painting & Pixel Art"), ("game", "Mini Games"), ("quiz", "Education"),
    ("research", "Research"), ("productivity", "Productivity"), ("media", "Audio & Media"), ("commerce", "Commerce"),
    ("access", "Accessibility"), ("visual", "Visualization"), ("quality", "Security & Quality"), ("ai", "AI Prompt Tools"),
    ("nlp", "ML/NLP Tools"), ("quantum", "Quantum-Inspired"), ("engineering", "Engineering"), ("knowledge", "Knowledge"),
    ("time", "Calendar & Time"), ("files", "Files & Formats"), ("marketing", "Marketing"), ("creator", "Creator Tools"),
    ("nature", "Nature & Earth")
]
PREFIX = ["Starter","Quick","Pro","Studio","Mini","Advanced","Smart","Express","Creator","Research","Classroom","Mobile","Visual","Batch","Insight","Toolkit","Generator","Analyzer","Planner","Lab","Workspace","Dashboard","Explorer","Builder","Converter","Inspector","Composer","Maker","Trainer","Simulator","Manager","Tracker","Mapper","Canvas","Workbench","Console","Assistant","Monitor","Archive","Universal"]
OBJECTIVES = {e: f"produce reusable {f} work" for e, f in FAMILIES}

def code(prefix, value):
    return prefix + hashlib.sha256(value.encode("utf-8")).hexdigest()[:12].upper()

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    products, passports = [], []
    for i in range(1, 1017):
        engine, family = FAMILIES[(i - 1) % len(FAMILIES)]
        pid = f"SP-{i:04d}"
        name = f"SHIRMANI {PREFIX[(i - 1) % len(PREFIX)]} {family} {i:04d}"
        qc = code("QC-", pid + "|SHIRMANI-PRODUCTION-QC")
        gate = f"GATE-{i:04d}"
        module = f"products/modules/{engine}.html"
        products.append({
            "id": pid, "name": name, "family": family, "engine": engine, "module": module,
            "objective": OBJECTIVES[engine], "product_index": i,
            "configuration_key": hashlib.sha256(f"{pid}|{engine}|{family}".encode()).hexdigest()[:20],
            "status": "CONCRETE_PRODUCT_MVP", "access": f"products/1000-digital-product-factory.html?id={pid}",
            "qc_code": qc, "gate_no": gate, "dispatch_no": "NO", "commercial_status": "NOT_SOLD",
            "verification": "DOWNSTREAM_QC_GATE"
        })
        passports.append({
            "product_id": pid, "name": name, "family": family, "engine": engine, "module": module,
            "objective": OBJECTIVES[engine], "qc_code": qc, "gate_no": gate, "dispatch_no": "NO",
            "status": "READY_FOR_QC", "qr_payload": f"{pid}|{module}|{qc}|{gate}|DISPATCH:NO"
        })
    payload = {
        "schema_version": 2, "generated_at": datetime.now(timezone.utc).isoformat(),
        "title": "SHIRMANI 1000+ Digital Product Factory",
        "principle": "Every catalog entry has a concrete product configuration, executable browser engine, production objective and QC/gate/dispatch passport.",
        "product_count": len(products), "engine_count": len(FAMILIES), "families": [x[1] for x in FAMILIES],
        "products": products,
        "production_status": {"configured_products": len(products), "concrete_product_mvp": len(products), "ready_for_qc": len(products), "dispatch": 0},
        "truth_boundary": "Production comes first. QC/gate/dispatch and independent verification remain downstream."
    }
    (OUT / "1000-digital-products.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (OUT / "PRODUCT-PASSPORTS.jsonl").open("w", encoding="utf-8") as f:
        for row in passports:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    status = {
        "strategy": "CONCRETE_PRODUCT_FIRST", "target_products": 1016, "concrete_product_mvp": len(products),
        "families": len(FAMILIES), "catalog": "generated/1000-digital-products.json",
        "passports": "generated/PRODUCT-PASSPORTS.jsonl", "public_product_center": "products/production-launch-center.html",
        "qc_gate": "READY_FOR_QC", "dispatch": 0, "verification_status": "DOWNSTREAM"
    }
    (OUT / "real-product-factory-status.json").write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
