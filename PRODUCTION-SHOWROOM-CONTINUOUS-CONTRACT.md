# ꙰ SHIRMANI Supreme Continuous Production Contract

## Production-first rule
Automission continuously produces customer-visible digital products and supporting assets. Verification is downstream; workflow success is never promoted as independent verification.

## Four-stage production chain
1. Institute — research, discovery, specification and product identity.
2. Factory — concrete browser-executable product artifact.
3. QC / Gate — deterministic quality/package checks, QC code, gate number and dispatch state.
4. Public Showroom — product visual, short description, QR for long description, demo route, product-specific media, price/offer, passport and customer review path.

## Continuous cycle
- 5-minute autonomous cadence.
- Product batch rotates through the remaining catalogue.
- 4K-ready product-specific visual identity is generated.
- Product-specific MP4 demo and VIP screenshot are generated where the media toolchain is available.
- Demo manifest and showroom visual manifest are refreshed.
- Customer reviews/ratings remain production-quality improvement signals.
- No sale, payment, dispatch or scientific verification is claimed merely because an artifact exists.

## Media contract
Each concrete product should resolve to:
- products/visuals/<product-id>.svg
- products/demos/<product-id>.mp4 when MP4 production succeeds
- products/vip-screenshots/<product-id>.png
- product-demo.html?id=<product-id>
- product-passport.html?id=<product-id>

The public interface must never point at a different path than the factory actually writes.

## Scale
The catalogue may scale to 5,000 concrete products first and to larger sharded catalogues afterward. Production output must remain source-bound and publicly inspectable.

## Independence
Scheduled Actions continue without a new chat message. Chat is not the execution trigger. The repository remains the durable production state.
