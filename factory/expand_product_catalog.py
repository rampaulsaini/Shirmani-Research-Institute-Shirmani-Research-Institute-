#!/usr/bin/env python3
"""Deterministically expand the runnable digital-product catalog to 5,000 entries.

The existing 1,016 records are preserved byte-for-byte at the data level.
Additional records are functional product variants built from the repository's
existing browser engines; they are not claims of independent scientific proof,
external-service deployment, sales, or payment completion.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "generated/1000-digital-products.json"
TARGET = 5000

TIERS = ["Starter", "Quick", "Smart", "Pro", "Studio", "Advanced", "Expert", "Supreme"]
FOCUS = [
    "Daily", "Professional", "Creator", "Research", "Education", "Business",
    "Nature", "Knowledge", "Language", "Accessibility", "Commerce", "Security",
    "Analytics", "Planning", "Publishing", "Marketing", "Media", "Engineering",
    "AI", "ML", "NLP", "Quantum-Inspired", "Productivity", "Visualization", "Global",
]
PRICE_BY_ENGINE = {
    "calculator": 99, "text": 149, "seo": 199, "data": 199, "draw": 199,
    "pixel": 299, "game": 199, "quiz": 299, "research": 499, "productivity": 149,
    "time": 149, "audio": 399, "media": 399, "creator": 499, "ai": 699,
    "ml": 799, "nlp": 799, "quantum": 999, "engineering": 499, "knowledge": 299,
    "calendar": 149, "files": 199, "marketing": 499, "nature": 399, "visual": 299,
    "accessibility": 199, "quality": 399, "security": 499,
}

def fp(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, ensure_ascii=False).encode("utf-8")
    ).hexdigest()[:16].upper()

def main() -> None:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    products = list(data.get("products", []))
    if len(products) >= TARGET:
        data["product_count"] = len(products)
        data["catalog_target"] = TARGET
        data["catalog_generation"] = "5K_READY"
        CATALOG.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"catalog_count": len(products), "added": 0, "target": TARGET}))
        return

    existing = {p["id"] for p in products}
    families = list(data.get("families", []))
    seeds = [p for p in products if p.get("engine")]
    n = len(products) + 1

    while len(products) < TARGET:
        seed = seeds[(n - len(seeds) - 1) % len(seeds)]
        engine = seed.get("engine", "structured")
        family = seed.get("family", "Knowledge")
        tier = TIERS[(n - 1) % len(TIERS)]
        focus = FOCUS[(n - 1) % len(FOCUS)]
        pid = f"SP-{n:04d}"
        if pid in existing:
            n += 1
            continue
        base = PRICE_BY_ENGINE.get(engine, 299)
        multiplier = 1.0 + (((n * 17) % 5) * 0.1)
        price = int(round(base * multiplier / 10) * 10)
        offer = "SUPREME 10% OFFER" if n % 5 == 0 else (
            "LAUNCH 15% OFFER" if n % 3 == 0 else "PUBLIC LAUNCH PRICE"
        )
        offer_price = int(round(price * (0.9 if n % 5 == 0 else 0.85 if n % 3 == 0 else 1.0) / 10) * 10)
        name = f"SHIRMANI {tier} {focus} {family} {n:04d}"
        product = {
            "id": pid,
            "product_index": n,
            "name": name,
            "family": family,
            "engine": engine,
            "description": f"Concrete public digital product {pid}: {focus} workflow for {family}, powered by the repository's {engine} engine.",
            "status": "QUEUED_FOR_CONCRETE_PRODUCTION",
            "production_state": "QUEUED",
            "sale_state": "PAYMENT_ROUTE_CONFIGURED",
            "price_inr": price,
            "offer_price_inr": offer_price,
            "pricing_status": "PUBLISHED_LAUNCH_PRICE",
            "offer": offer,
            "commercial_status": "NOT_SOLD",
            "verification": "FUNCTIONAL_BROWSER_BEHAVIOUR_ONLY",
            "generation": "DETERMINISTIC_CATALOG_VARIANT",
            "source_engine_product": seed["id"],
            "fingerprint": fp({"id": pid, "engine": engine, "family": family, "focus": focus, "tier": tier}),
            "payment_routes": ["PAYTM_UPI", "PAYPAL"],
        }
        products.append(product)
        existing.add(pid)
        n += 1

    data["products"] = products
    data["product_count"] = len(products)
    data["catalog_target"] = TARGET
    data["catalog_generation"] = "5K_READY"
    data["integrity"] = {
        "existing_records_preserved": True,
        "new_records_are_deterministic_variants": True,
        "external_service_claim": False,
        "sales_claim": False,
        "payment_claim": False,
        "independent_verification_claim": False,
    }
    data["families"] = sorted(set(families) | {p.get("family") for p in products if p.get("family")})
    CATALOG.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"catalog_count": len(products), "added": len(products) - len(seeds), "target": TARGET}))

if __name__ == "__main__":
    main()
