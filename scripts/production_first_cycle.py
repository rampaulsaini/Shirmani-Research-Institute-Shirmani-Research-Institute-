#!/usr/bin/env python3
"""Build production-first operational telemetry without timestamp-only churn."""
import json
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]


def write_if_changed(path: Path, payload: dict) -> bool:
    """Write telemetry only when meaningful fields differ from the current JSON."""
    try:
        previous = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(previous, dict):
            old_semantic = {key: value for key, value in previous.items() if key != "generated_at"}
            new_semantic = {key: value for key, value in payload.items() if key != "generated_at"}
            if old_semantic == new_semantic:
                print("Production operations state unchanged; skipping timestamp-only update.")
                return False
    except (OSError, json.JSONDecodeError):
        pass
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return True


def main() -> None:
    cat = json.loads((root / "generated/1000-digital-products.json").read_text(encoding="utf-8"))
    products = cat.get("products", [])
    priority = {"AI Prompt Tools": 1, "ML/NLP Tools": 1, "Research": 1, "Education": 2, "Creator Tools": 2, "Commerce": 2, "Security & Quality": 2, "Nature & Earth": 2, "Quantum-Inspired": 3}
    goal = {"AI Prompt Tools": "reusable prompt packs, examples and export", "ML/NLP Tools": "real text/data transformations and repeatable examples", "Research": "structured research workspaces and reproducible outputs", "Education": "exercises, scoring, explanations and export", "Creator Tools": "creation, preview, export and templates", "Commerce": "catalogue, offers, order-intent and product copy", "Security & Quality": "deterministic checks and remediation reports", "Nature & Earth": "calculators, trackers and educational tools", "Quantum-Inspired": "classical simulations with explicit boundaries"}
    rows = []
    for product in products:
        family = product.get("family", "")
        rows.append({
            "product_id": product.get("id"), "name": product.get("name"), "family": family,
            "engine": product.get("engine"), "priority": priority.get(family, 4),
            "action": "DEPTH_UPGRADE",
            "goal": goal.get(family, "product-specific examples, richer inputs/outputs, export and customer guidance"),
            "public_route": product.get("artifact_url") or "products/1000-digital-product-factory.html?id=" + str(product.get("id", "")),
        })
    rows.sort(key=lambda row: (row["priority"], row["family"], row["product_id"] or ""))
    produced = sum(1 for product in products if product.get("status") == "PRODUCED_PUBLIC" or product.get("production_state") == "PRODUCED")
    priced = sum(1 for product in products if product.get("pricing_status") == "PUBLISHED_LAUNCH_PRICE")
    payload = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "PRODUCTION_FIRST",
        "pipeline": ["INSTITUTE_RESEARCH", "FACTORY_PRODUCTION", "QC_GATE", "PUBLIC_SHOWROOM_SALE"],
        "production": {
            "catalog_products": len(products), "produced_public": produced, "pricing_published": priced,
            "sold_evidence": sum(1 for product in products if product.get("commercial_status") == "SOLD"),
            "next_scale_target": 5000, "remaining_to_scale_target": max(0, 5000 - produced),
        },
        "customer_loop": ["DISCOVER", "BUILD", "QC/GATE", "SHOW", "USE", "REVIEW/RATE", "IMPROVE", "BUILD_AGAIN"],
        "verification_boundary": "Independent verification is downstream and is not a substitute for production.",
        "next_work_units": rows[:100],
        "summary": {"families": len(cat.get("families", [])), "priority_units": sum(1 for row in rows[:100] if row["priority"] == 1)},
    }
    changed = write_if_changed(root / "generated/production-operations-status.json", payload)
    print(("production operations state updated: " if changed else "production operations state unchanged: "), len(products), "catalog products,", produced, "produced public")


if __name__ == "__main__":
    main()
