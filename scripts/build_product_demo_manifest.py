#!/usr/bin/env python3
"""Build the customer-facing demo-video manifest for every catalog product."""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / "generated" / "1000-digital-products.json"
OUT = ROOT / "generated"

def main() -> None:
    data = json.loads(CAT.read_text(encoding="utf-8"))
    products = data.get("products", [])
    items = []
    for p in products:
        pid = str(p.get("id", ""))
        engine = str(p.get("engine", "package"))
        items.append({
            "product_id": pid,
            "name": p.get("name"),
            "family": p.get("family", p.get("category")),
            "engine": engine,
            "demo_route": f"product-demo.html?id={pid}",
            "preferred_video_asset": f"products/demos/{engine}.mp4",
            "fallback_demo": True,
            "usage_steps": [
                "Open the product",
                "Enter the task/input",
                "Run the product module",
                "Review the output",
                "Reuse or submit feedback for improvement",
            ],
            "status": "DEMO_ROUTE_READY",
        })
    stamp = datetime.now(timezone.utc).isoformat()
    engines = sorted({x["engine"] for x in items})
    out = {
        "schema_version": 2,
        "generated_at": stamp,
        "catalog_count": len(items),
        "engine_count": len(engines),
        "engines": engines,
        "demo_standard": {
            "short_description_on_product_visual": True,
            "long_description_qr": True,
            "video_route_required": True,
            "engine_video_preferred": True,
            "animated_fallback_required": True,
            "truth_boundary": "Demo readiness demonstrates product usage flow; it is not scientific verification.",
        },
        "products": items,
    }
    (OUT / "product-demo-video-manifest.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    md = [
        "# SHIRMANI Product Demo Video Manifest",
        "",
        f"- Generated: {stamp}",
        f"- Catalog products: {len(items):,}",
        f"- Distinct engines: {len(engines):,}",
        "- Every product has a stable public product-demo.html?id=... route.",
        "- Engine-level MP4 assets are preferred when present.",
        "- The browser-generated animated demo is the fallback, so a missing MP4 never removes the customer-facing demo route.",
        "",
        "## Production boundary",
        "Demo/video readiness is a customer-facing production state. It is not independent scientific verification.",
    ]
    (OUT / "product-demo-video-manifest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps({"catalog_count": len(items), "engine_count": len(engines), "status": "DEMO_MANIFEST_READY"}))

if __name__ == "__main__":
    main()
