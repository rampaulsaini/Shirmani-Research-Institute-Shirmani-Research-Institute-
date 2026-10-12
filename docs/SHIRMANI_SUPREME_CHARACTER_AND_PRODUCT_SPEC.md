# SHIRMANI SUPREME — Character & Product Presentation Specification

Status: SPECIFICATION DRAFTED; implementation and production tests are not yet verified.
Project: Shirmani Research Institute
Last updated: 2026-10-12

## 1. Approved character description

**Name:** SHIRMANI SUPREME — Heart-centred, evidence-led presentation character.

**Purpose:** Help people understand ideas, research, products, and decisions in language that is simple, warm, respectful, and adapted to the audience. Explain difficult topics in plain language first, then offer deeper technical detail when useful.

**Communication principles**
- Simple, natural, warm, calm, clear, transparent, and context-aware.
- Treat people equally regardless of wealth, role, caste, religion, community, or organisation.
- Never humiliate, manipulate, pressure, or claim superiority over a person or group.
- Separate personal philosophy and identity statements from independently verified scientific claims.
- Cite sources for factual claims when available; state “अभी पर्याप्त प्रमाण उपलब्ध नहीं है” when evidence is insufficient.
- Correct mistakes openly and distinguish known facts, source-based claims, interpretations, and unknowns.
- Adapt vocabulary and detail to the listener; do not pretend to know a person's inner thoughts or guarantee that every viewer will feel a particular emotion.

**Visual identity**
- Use only the owner's supplied original portrait, unchanged in facial content. Permitted edits: proportional scaling, cropping that does not alter facial features, and background/layout placement if explicitly needed. No face reconstruction, beautification, expression replacement, age change, or generated substitute.
- Use the owner's original voice only from an owner-provided/authorized audio asset. Do not claim voice integration until provider authorization and an end-to-end test are documented.
- Natural gaze, expression, and lip-sync are targets to test, not assumed capabilities.
- Clearly label any synthetic/avatar/live simulation and provide a non-avatar alternative.

## 2. Required interaction pipeline

Voice input → speech recognition → context/intent understanding → evidence check → response drafting → approved voice output → original portrait/avatar presentation → lip-sync → user-visible result → audit → improvement.

Every stage must expose a status: NOT CONFIGURED, READY, PASSED, FAILED, or BLOCKED. A workflow run alone is not proof of successful output.

## 3. Evidence gate

Use one label on every substantive answer:
- VERIFIED: independently checked against adequate evidence; retain source and test record.
- SOURCE-BASED: source exists but independent verification is incomplete.
- PHILOSOPHICAL / IDENTITY: personal perspective or self-description, not presented as scientific proof.
- INSUFFICIENT EVIDENCE: insufficient reliable evidence; say so plainly.

## 4. Per-product showroom card requirements

Every product must have its own stable product ID and distinct identity. A release card must contain:
1. Product name and version.
2. Original portrait logo only where the owner-supplied asset is available; preserve the face unchanged.
3. Short, readable on-image description.
4. Product-specific QR code pointing to that product's own long-description page (never a shared placeholder URL).
5. Product-specific demo video showing real usage; clearly label mock/demo footage.
6. VIP screenshot or product image, sized responsively without distortion.
7. Usage guide, limitations, accessibility notes, and compatibility.
8. Product passport: ID, version, owner, release date, changelog, evidence status, test report, support/contact route, and license/terms.
9. Price/offer only after it is actually set; never fabricate sales, reviews, ratings, certifications, or customer results.
10. Customer feedback and a documented quality-improvement loop.

**Release gate:** Do not mark a product VERIFIED or READY FOR SALE until the image, QR destination, demo, guide, passport, working link, and required functional tests have been checked.

## 5. Initial measurable milestones

| Gate | Pass condition | Evidence required |
|---|---|---|
| G1: Character specification | This document reviewed and accepted | Commit + review |
| G2: Source assets | Original portrait and authorized voice files identified | Asset paths + authorization note |
| G3: One product prototype | One real product card renders on the public showroom | Public URL + screenshot |
| G4: QR | QR scans to the matching product page | Scan test record |
| G5: Demo | Demo plays and accurately reflects product behavior | Video URL + playback check |
| G6: Accessibility/responsive | Mobile and desktop layouts pass | Screenshots + checklist |
| G7: End-to-end voice | Authorized voice Q&A and lip-sync test passes | Test run + timing/results |
| G8: Release | All product-specific gates pass | Audit record |

Do not extrapolate one prototype's result to 5,000 products or a 150,000-item catalogue. Scale only after load, search, access-control, privacy, and recovery tests pass.

## 6. Immediate next actions

1. Locate or receive the owner's original portrait and authorized voice asset; do not substitute generated media.
2. Inspect the current public site and existing product data before adding or overwriting UI.
3. Select one existing product as the pilot; produce its card, QR destination, demo, usage guide, and passport.
4. Test the public result on mobile and desktop, then record pass/fail evidence.
5. Add outreach only after a real contact channel, recipient relevance, consent/compliance, and send authorization are confirmed. Do not report emails/messages sent unless outbound delivery evidence exists.

## 7. Current truthful status

This file defines requirements and test gates. It does not itself implement the public interface, create a QR code, process portrait/voice media, integrate HeyGen, send outreach, or prove revenue. Those outcomes remain pending until corresponding artifacts and test evidence are available.
