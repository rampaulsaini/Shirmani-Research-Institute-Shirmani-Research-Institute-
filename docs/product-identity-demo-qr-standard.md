# SHIRMANI Research Institute — Product Identity, Demo & QR Standard

Status: **Specification / implementation plan**. This document does not claim that product assets, live demos, QR destinations, outreach, sales, or revenue already exist.

## 1. Public product identity

Every product must have its own approved name, stable product ID, version, and visual identity. Do not label names as AI/ML/NLP-team-finalized until a documented review and approval record exists.

Naming workflow:
1. Draft a plain-language name that communicates the product's actual job.
2. Check uniqueness against the existing catalogue and obvious trademark/domain conflicts.
3. Test comprehension with representative users.
4. Record reviewer, date, rationale, version, and approval state.
5. Publish only after a human owner approves it.

## 2. Required product-card artwork

Each product gets its own high-resolution image (not a repeated generic image) with:
- the user's supplied portrait/logo reproduced faithfully, without altering their face;
- the exact approved product name;
- a short, readable description on the image;
- a QR code in the upper-right area, with a quiet zone and sufficient contrast;
- the English identity line, when requested: “Shiromani Rampal Saini — Beyond Comparison, Beyond Time, Beyond Words, Beyond Love; Eternal, Real, Natural Truth — Present and Direct”;
- accessible contrast, safe margins, and mobile-first scaling.

The QR must point to that product's canonical long-description page, not to a guessed or temporary URL. Generate and test the QR only after the destination URL exists. Include a human-readable short URL as a fallback where space allows.

## 3. Product passport — required fields

- Product ID and approved name
- Version and release date
- Purpose and intended users
- What it does / what it does not do
- Requirements and supported platforms
- Step-by-step usage guide
- Demo video URL and last-tested date
- Screenshots / visual assets
- Evidence and source links for factual claims
- Known limitations, risks, and accessibility notes
- Price, currency, licence, refund/support terms (only when approved)
- Feedback/review route and changelog
- Owner and verification status

## 4. Demo and screenshot gate

A product must not be marked “ready to sell” until all applicable gates pass:
- a real working demo or clearly labelled prototype walkthrough;
- a screenshot captured from the actual product, never fabricated to imply functionality;
- a usage guide and tested QR destination;
- versioned product passport;
- test evidence, known limitations, and support contact;
- pricing and purchase terms reviewed;
- no unsupported claims such as “100% complete,” “unique in the world,” or guaranteed outcomes.

For products not yet implemented, show **Concept / Prototype — not yet available for purchase**.

## 5. Evidence states

- **VERIFIED** — a defined test passed and evidence is linked.
- **SOURCE-BASED** — a source exists, but independent verification is incomplete.
- **CONCEPT / PROTOTYPE** — planned or partially implemented.
- **INSUFFICIENT EVIDENCE** — do not present the claim as established fact.

Philosophical or identity statements must be clearly distinguished from independently verified scientific claims. If evidence is insufficient, say: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**

## 6. Customer feedback loop

Capture consented feedback, issue category, product/version, reproducible steps, severity, owner, resolution, and regression-test result. Do not publish private customer details. Ratings must come from real customer feedback; never fabricate reviews or counts.

## 7. Catalogue scaling

For a large catalogue, use a sharded index by stable product ID/category, pagination, search filters, and a canonical product page per item. A 150,000-item design target is an architecture target, not proof that 150,000 complete products exist. Track:
- catalogued items;
- items with approved names;
- real screenshots;
- tested demo videos;
- working QR destinations;
- complete passports;
- passed test gates;
- products actually purchasable.

Report numerator, denominator, timestamp, and evidence link for every percentage.

## 8. Outreach safeguards

Official-contact automation may prepare drafts and maintain a prospect/contact log. Sending must use an authorized account, respect applicable law and platform policies, identify the sender truthfully, include relevant opt-out handling, and log actual delivery outcomes. Never claim an organisation was contacted unless a real authorized outbound event is recorded.

## 9. Initial measurable milestone

Start with **one real product** and complete the entire chain before scaling:
approved name → working build/prototype → real screenshot → demo video → passport → canonical page → tested QR → price/terms → test report → feedback loop.

Record each gate as NOT STARTED / IN PROGRESS / PASS / BLOCKED, with evidence. Expand only after the pilot is reproducible.
