# SHIRMANI Product Media Production Contract

## Production objective

Every public product identity progressively receives its own customer-facing media package:

1. Product-specific 4K-ready visual identity.
2. Heart-View logo/photo.
3. English identity line.
4. Short description directly on the visual.
5. QR route to the long Product Passport / description.
6. Product-specific VIP screenshot.
7. Product-specific demo route and MP4 when the media factory completes it.
8. Usage steps explaining what the tool/product does, where it is used, and how to use it.
9. Price/offer when a catalog record supplies it.
10. QC / Gate / Dispatch fields remain explicit release metadata.

## Automation

- VIP screenshot factory: `.github/workflows/shirmani-vip-screenshot-factory.yml`
- Demo video factory: `.github/workflows/shirmani-product-specific-demo-videos.yml`
- Both are scheduled independently of an active chat session.
- The VIP factory works in bounded batches so the catalogue can scale without one oversized run.
- The demo factory remains bounded because MP4 generation is materially heavier.

## Production truth

A workflow run is not itself a product. A product becomes production-visible when its concrete artifact/media exists and is published into the showroom/catalogue.

Customer reviews and ratings are inputs to continuous quality improvement. They are not treated as a substitute for product production, payment, dispatch, or independent scientific verification.

## Scale targets

- Current public-production scale target: 5,000 concrete products.
- Long-term catalogue vision: 150,000 products.
- The 150,000 target is an expansion target, not a claim that all 150,000 already exist.

## External platform mapping

The platform may maintain official links to external technology/platform providers for appropriate product categories. This is a directory/reference relationship only unless an authorized integration or commercial agreement exists.

Lawful outreach automation must never claim that an organisation has been contacted unless an authorized outbound channel actually executed the contact.
