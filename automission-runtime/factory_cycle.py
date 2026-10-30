import json
from datetime import datetime, timezone
from pathlib import Path

from product_factory import DigitalProductFactory
from product_catalog import STAGES

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def run_factory_cycle(catalog, requests):
    """Process product requests without publishing or claiming sales."""
    factory = DigitalProductFactory(catalog)
    results = []
    for request in requests:
        title = str(request.get("title", "")).strip()
        product_type = str(request.get("product_type", "")).strip()
        if not title or not product_type:
            results.append({"status": "REJECTED", "reason": "title_and_product_type_required"})
            continue
        try:
            product_id, spec = factory.create_blueprint(
                title, product_type, request.get("description", ""),
                request.get("languages"),
            )
            manifest = factory.package(
                product_id, {**spec, "version": request.get("version", "1.0.0")},
                request.get("files", []), request.get("version", "1.0.0"),
            )
            results.append({
                "status": "BLUEPRINT_READY",
                "product_id": product_id,
                "stage": catalog.get(product_id)["stage"],
                "spec_hash": spec["spec_hash"],
                "manifest_hash": manifest["manifest_hash"],
                "agents": spec["agents"],
                "created_at": utc_now(),
            })
        except (ValueError, KeyError) as exc:
            results.append({"status": "REJECTED", "reason": str(exc)})
    return results

def load_requests(path: Path):
    path = Path(path)
    if not path.exists():
        return []
    data = json.loads(path.read_text())
    if not isinstance(data, list):
        raise ValueError("factory request file must contain a list")
    return data
