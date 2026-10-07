# SHIRMANI Supreme Showroom — Visual Production Contract

## Product-card identity

Every public product card is required to expose the same visual identity layer:

1. **Product-specific 3840×2160 (4K) visual master** — generated from the product's own stable ID/name.
2. **SHIRMANI Heart-View photo/logo** — upper-left brand mark.
3. **English identity line** directly with the brand mark:
   **Shiromani Rampal Saini · Beyond Comparison · Beyond Time · Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present**
4. **Short description** — rendered on the visual itself.
5. **QR code** — upper-right, resolving to the product passport / long description route.
6. **Product identity** — stable product ID remains visible.
7. **Commercial fields** — published rate/offer are separate from production/QC state.
8. **QC / Gate / Dispatch** — shown from the product passport; no fabricated sale or dispatch state.

## Production semantics

- A workflow run is **not** a product.
- A runtime visual engine is **not** a claim that a raster photograph/VIP screenshot has already been materialized.
- `3840×2160` SVG output is a 4K visual master; raster/VIP screenshots remain separately counted.
- A QR route is a navigation mechanism, not independent scientific verification.
- Customer reviews/ratings feed product improvement and are independent of the research verification ledger.
- Production work remains the primary automation objective; verification remains a downstream quality/integrity state.

## Four-level path

**Institute → Factory → QC Gate → Public Showroom**

The showroom is the final public presentation layer for products that have a concrete artifact or an explicitly labelled delivery route.

## Scale

The current live production state reports **5,000 catalog identities** and **1,516 concrete repository assets**. The current target is to materialize the remaining concrete production work continuously. No number of catalog identities is silently treated as an equivalent number of completed sales.

## Implementation

- `assets/product-visuals.js` — 3840×2160 product visual engine.
- `showroom-product-visuals.js` — showroom identity/QR overlay layer.
- `showroom-public-interface.html` — public catalog, telemetry and customer-facing controls.
- `generated/PRODUCT-PASSPORTS.jsonl` — product identity/QC metadata source.
- `product-passport.html` — long-description and passport destination.
