# SHIRMANI Product Media Production Standard

## Customer-facing production contract

Every saleable or publicly presented digital product should have:

1. **Unique product identity** — stable Product ID and product-specific visual.
2. **VIP product view** — product-passport.html?id=PRODUCT_ID.
3. **4K-ready visual** — 3840×2160, 16:9, product name, short description, SHIRMANI perspective logo, English identity line and QR for the long description.
4. **Long description** — product passport/detail route behind the QR.
5. **Demo video** — product-specific MP4 when produced; browser demo remains the fallback.
6. **Usage guide** — clear HOW TO USE / WHERE TO USE / RESULT steps.
7. **QC package** — QC code, Gate No., Dispatch No. and production state.
8. **Public review loop** — customer review/rating is an input to quality improvement, not a substitute for production.
9. **Commercial truth** — price/offer can be shown only from the product record; no fabricated sale, dispatch or external-contact claim.

## Four-stage production

**Institute → Factory → QC → Public Showroom/Sale**

Verification is downstream result-quality work. It does not replace production.

## Media batch policy

The demo-video factory is bounded per cycle so GitHub Actions remains operational. Missing product videos are generated in order across scheduled cycles until the catalogue is covered.

## Scale policy

The public catalogue is designed for sharded growth:

- current production target: **5,000 concrete products**
- long-term catalogue architecture: **150,000+ product identities**
- sharding prevents a single giant JSON document from becoming the delivery bottleneck
- public showroom reads index + shard rather than requiring every product to be embedded in one HTML document

## External organisations

GitHub, NVIDIA, government, science and enterprise organisations may receive product-package links through authorised outreach channels. The platform must never claim that an organisation was contacted unless an actual authorised outbound action occurred.