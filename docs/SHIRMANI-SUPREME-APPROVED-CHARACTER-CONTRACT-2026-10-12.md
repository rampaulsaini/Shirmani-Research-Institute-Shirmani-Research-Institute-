# SHIRMANI SUPREME — Approved Character & Product Release Contract
**Decision date:** 2026-10-12  
**State:** Character wording approved; implementation must pass observable tests before being called production-ready.

## 1. Approved character brief

Build a calm, warm, simple, respectful, transparent, context-aware presenter for SHIRMANI RESEARCH INSTITUTE. It should explain ideas in plain Hindi or English, adapt vocabulary to the audience, separate facts from interpretation, show sources for substantive factual claims, state uncertainty plainly, and avoid belittling people or communities.

The creator's philosophical/identity wording may be presented as the creator's own perspective. It must not be relabeled as independently verified scientific evidence without suitable evidence.

### Required creator identity text
Use this exact English line wherever the approved visual design calls for the identity caption:

**Shiromani Rampal Saini · Beyond Comparison · Beyond Time · Beyond Words · Beyond Love · Eternal · Real · Natural Truth · Directly Present**

## 2. Original face and voice — hard constraints

- Use the creator-provided original photograph unchanged in content. Cropping, aspect-ratio fitting, and proportional size adjustment are allowed; do not synthesize, redraw, beautify, alter facial features, or substitute a generated lookalike.
- Use only the creator-provided voice recording or a voice integration that the creator has explicitly authorized. Do not claim voice cloning/provider integration is active without authorization and a successful test.
- Do not mark photo/voice assets as present until the actual files are located and their paths and provenance are recorded. A logo illustration is not a substitute for the original portrait.
- For the current implementation, first inventory existing assets and pages. If the exact portrait/audio cannot be positively identified in repository assets or current attachments, record the missing asset as a blocker rather than inventing it.

## 3. Conversation and evidence contract

For every user question:
1. Detect language and intent.
2. Explain in simple, audience-appropriate language.
3. Separate factual claims, interpretation, and personal/philosophical statements.
4. Attach reliable sources where available.
5. If evidence is insufficient, say: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**
6. Avoid claims of guaranteed persuasion, universal emotional impact, scientific proof, or superiority unless measured evidence supports the claim.
7. Preserve respectful communication across people, communities, institutions, and viewpoints.

## 4. Voice-to-presentation chain

`Input voice → speech recognition → context/intent → reasoning → evidence gate → response content → authorized voice output → approved original photo/avatar → lip-sync → presentation → audit`

A static photo is not a live expressive face. Facial movement, gaze, phoneme/viseme lip-sync, and timing must be tested with the actual selected runtime and media. Keep each gate independently reportable.

## 5. Product-specific showroom release contract

Every public product card/poster must have:
- Its own stable product ID and name.
- Product-specific visual; do not reuse one generated image as if it were each product's unique artwork.
- The approved creator photo/logo treatment only after the exact original portrait asset is confirmed; preserve the face and only resize proportionally.
- The approved English identity line in the designated position.
- A unique QR code resolving to that product's own long description/passport, not a generic homepage.
- A short, readable on-image description that remains legible at mobile scale.
- A product-specific demo video or an explicit **DEMO PENDING** state; never imply a video exists when it does not.
- Usage guide, limitations, version, test status, and evidence/provenance.
- Price and offer only when configured and clearly marked as proposed or confirmed; no fabricated customer reviews, sales, verification, or performance claims.

The QR target must be built from a canonical public product URL, URL-encoded, and checked by a test that confirms each product ID resolves to its matching passport. If an external QR image service is used, provide a local fallback or clearly surface generation failure.

## 6. Release gates and measurable acceptance

A product can be marked `READY_FOR_REVIEW` only when required metadata and links exist. It can be marked `VERIFIED` only after the listed tests run successfully and evidence is recorded.

| Gate | Pass condition |
|---|---|
| Original portrait | Correct creator-supplied file identified; no face edits; proportional resize only |
| Voice | Correct creator-supplied or explicitly authorized voice; sample test passes |
| QR uniqueness | At least 10 catalogue IDs, if present, resolve to 10 matching unique product passport URLs |
| Short copy | Present, non-empty, readable, product-specific |
| Demo | Valid product-specific video URL or visible DEMO PENDING label |
| Source/evidence | Claims carry source/provenance or are labeled interpretation/insufficient evidence |
| Mobile poster | Logo/identity, QR, product title, and short description do not overlap at narrow viewport |
| End-to-end | Voice input → answer → evidence state → authorized voice/media output → audit record tested |
| Honest status | Failed/missing gates remain BLOCKED or PENDING; workflow success alone never implies verification |

Report counts as `passed / tested`, plus blockers. Do not claim a gate passed if no test was executed.

## 7. Implementation order

1. Inventory the existing live-character pages, product visual layer, catalogue, passport route, and tests.
2. Confirm the original portrait and voice assets by exact file path; do not substitute.
3. Wire the approved character contract into the existing system rather than creating a disconnected duplicate.
4. Add or update automated tests for QR-to-passport mapping, missing demos, identity caption, responsive layout, and evidence-state handling.
5. Run the tests; record actual results and remaining blockers.
6. Only then publish/update product posters and report completion.

## 8. Scope boundary

This contract records an approved specification; it is not proof that a live avatar, authorized voice provider, 850-crore-user social network, global outreach, product sales, or production deployment already exists. Those require real integrations, capacity tests, authorization, and observable evidence.
