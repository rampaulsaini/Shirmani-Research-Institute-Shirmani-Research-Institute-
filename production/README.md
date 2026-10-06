# SHIRMANI Production Omniverse

Production-first layer for the Shirmani Research Institute.

## Four-level production mechanism

1. **Institute Discovery** — research ideas, signals, requirements and product opportunities are queued.
2. **Factory Production** — every production item becomes a concrete digital-product record with description, category, specification, price, offer, guarantee and QC metadata.
3. **QC Gate** — QC is a release gate attached to a produced item; it is not the purpose of Automission.
4. **Public Showroom** — released products are presented in a clean public catalog with category, price, offer and purchase destination.

## Production principle

Automation exists to create and improve products. Verification is downstream quality control of produced results.

The production engine is deliberately deterministic and auditable: every product has a stable product ID, factory batch, QC gate, release state and generated timestamp.

## Current implementation

- Multi-layer production workflow scheduled every 5 minutes.
- Seed catalog with concrete product records.
- Parametric product factory for continuous expansion.
- QC metadata embedded per product.
- Public showroom interface generated from the production catalog.
- Production status manifest for platform visibility.
- Existing store can be used as the purchase destination until a native checkout is connected.

## Important

A GitHub workflow run alone is not a product. The factory must emit an artifact/catalog entry. The showroom is the user-visible proof of production output.
