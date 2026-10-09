# Product Passport & QC Gate
**Version:** 0.1.0 · **Status:** Specification template

## Purpose
A standard record for product identity, version, intended use, price, deliverables, limitations, demo status, and release checks.

## Required passport fields
- Stable product ID, name, version, and change history
- Intended users and usage instructions
- Deliverables, price/currency, and offer expiry if applicable
- Demo-video status and product visual
- QC checklist, findings, and reviewer
- Known limitations and feedback route
- Release state: DRAFT, FACTORY, QC_HOLD, QC_PASS, SHOWROOM, WITHDRAWN

## Gate rules
1. Missing artifact or guide → QC_HOLD.
2. Broken links or material unsupported claims → QC_HOLD.
3. A checklist alone is not independent certification.
4. Mark QC_PASS only after checks actually run and results are recorded.
5. Preview listings must disclose readiness and limitations.
6. Do not imply paid checkout, QR generation, or video rendering exists until implemented and tested.

This is a specification, not yet an automated QC service, checkout, QR/passport generator, or live inventory backend.
