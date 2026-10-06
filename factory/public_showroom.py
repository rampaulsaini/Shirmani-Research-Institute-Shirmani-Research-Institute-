from pathlib import Path
from datetime import datetime, timezone
import json

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "generated" / "1000-digital-products.json"
TEMPLATE = ROOT / "products.html"

def build(url: str) -> str:
    return TEMPLATE.read_text(encoding="utf-8").replace("__CATALOG_URL__", url)

def main():
    if not CATALOG.exists():
        raise SystemExit("production catalog not found")
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    products = data.get("products", [])
    target = ROOT / "products" / "production-launch-center.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(build("../generated/1000-digital-products.json"), encoding="utf-8")
    status = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "showroom": "products.html",
        "launch_center": "products/production-launch-center.html",
        "catalog": "generated/1000-digital-products.json",
        "product_count": len(products),
        "commercial_fields": ["price", "offer", "description", "guarantee", "packing"],
        "qc_fields": ["qc_code", "gate_no", "dispatch_no", "qr_payload"],
        "production_first": True,
        "payment_state": "UI_READY_PAYMENT_PROVIDER_REQUIRED",
    }
    (ROOT / "generated" / "public-showroom-status.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

if __name__ == "__main__":
    main()
