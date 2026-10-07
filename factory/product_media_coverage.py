#!/usr/bin/env python3
"""Measure customer-facing media coverage for concrete digital products.

Production-first rule:
catalog identity != concrete product != media asset.
This report measures published assets only; it is not independent scientific verification.
"""
from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "product-media-coverage.json"

def load_products():
    for rel in ("generated/1000-digital-products.json",
                "generated/production-registry.json",
                "generated/concrete-production-overlay.json"):
        p = ROOT / rel
        if not p.exists():
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        rows = data.get("products", [])
        if rows:
            return rows, rel
    return [], "NONE"

def exists(rel: str) -> bool:
    return bool(rel) and (ROOT / rel).exists()

def main():
    products, source = load_products()
    rows = []
    for p in products:
        pid = str(p.get("id", "")).strip()
        if not pid:
            continue
        slug = pid.lower()
        concrete = str(p.get("artifact_url") or f"products/concrete/{pid}.html")
        checks = {
            "concrete_artifact": exists(concrete),
            "visual": exists(f"products/visuals/{slug}.svg"),
            "vip_screenshot": exists(f"products/demos/vip/{slug}.svg") or exists(f"products/vip-screenshots/{slug}.svg"),
            "mp4": exists(f"products/demos/products/{slug}.mp4"),
            "demo_route": exists("product-demo.html"),
            "passport_route": exists("product-passport.html"),
        }
        score = sum(checks.values())
        rows.append({
            "product_id": pid,
            "name": p.get("name"),
            "coverage_score": score,
            "coverage_percent": round(score / len(checks) * 100, 2),
            **checks,
        })
    total = len(rows)
    summary = {
        k: sum(1 for r in rows if r[k])
        for k in ("concrete_artifact","visual","vip_screenshot","mp4","demo_route","passport_route")
    }
    payload = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "catalog_source": source,
        "product_count": total,
        "summary": summary,
        "coverage_percent": {k: round(100*v/total,2) if total else 0 for k,v in summary.items()},
        "complete_media_package_count": sum(1 for r in rows if r["coverage_score"] == 6),
        "complete_media_package_percent": round(100*sum(1 for r in rows if r["coverage_score"] == 6)/total,2) if total else 0,
        "truth_boundary": "Production-media coverage is customer-facing production telemetry, not independent scientific verification.",
        "products": rows,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "product_count": total,
        "complete_media_package_count": payload["complete_media_package_count"],
        "coverage_percent": payload["coverage_percent"],
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
