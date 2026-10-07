#!/usr/bin/env python3
"""Build the public showroom visual-production manifest.

Production-first: this records customer-facing visual readiness and routes.
It does not claim scientific verification.
"""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
registry = json.loads((ROOT / "showroom-products.json").read_text(encoding="utf-8"))
state = json.loads((ROOT / "generated/live-production-state.json").read_text(encoding="utf-8"))
products = registry.get("products", [])

def identity(pid: str) -> str:
    return "SRI-VIS-" + hashlib.sha256(pid.encode("utf-8")).hexdigest()[:12].upper()

items = []
for p in products:
    pid = str(p.get("id", "PRODUCT"))
    long_url = p.get("store_url") or p.get("artifact_url") or f"showroom-product.html?id={pid}"
    items.append({
        "product_id": pid,
        "visual_identity": identity(pid),
        "visual_format": "3840x2160 SVG / 16:9 / contain",
        "short_description_on_image": True,
        "long_description_qr": True,
        "long_description_route": long_url,
        "price_inr": p.get("price_inr", 0),
        "category": p.get("category", "digital-product"),
        "source_status": p.get("status", "CATALOG"),
    })

out = {
    "schema_version": 1,
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "production_first": True,
    "visual_standard": {
        "resolution": "3840x2160",
        "aspect_ratio": "16:9",
        "scaling": "contain / center / no crop",
        "identity": "deterministic product-specific visual identity",
        "image_short_description": True,
        "qr_long_description": True,
    },
    "platform_snapshot": {
        "catalog_identities": state.get("catalog_identities", 0),
        "concrete_repository_assets": state.get("concrete_repository_assets", 0),
        "concrete_materialization_percent": state.get("concrete_materialization_percent_of_scale_target", 0),
        "production_modules": state.get("module_products_generated", 0),
    },
    "showroom_seed_products": len(items),
    "products": items,
    "truth_boundary": "Visual production readiness is not independent scientific verification.",
}
(ROOT / "generated/showroom-visual-manifest.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
md = [
    "# SHIRMANI Showroom Visual Production Manifest",
    "",
    f"- Generated: {out['generated_at']}",
    f"- Catalog identities: {out['platform_snapshot']['catalog_identities']:,}",
    f"- Concrete repository assets: {out['platform_snapshot']['concrete_repository_assets']:,}",
    f"- Concrete materialization: {out['platform_snapshot']['concrete_materialization_percent']:.2f}%",
    f"- Production modules: {out['platform_snapshot']['production_modules']:,}",
    f"- Seed products with product-specific visual routes: {len(items):,}",
    "",
    "## Visual standard",
    "- 3840×2160 SVG, 16:9.",
    "- Centered contain scaling; no forced crop.",
    "- Deterministic product-specific visual identity.",
    "- Short description printed on the visual.",
    "- QR route opens the long product description/product page.",
    "",
    "Production output is separate from independent scientific verification.",
]
(ROOT / "generated/showroom-visual-manifest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
