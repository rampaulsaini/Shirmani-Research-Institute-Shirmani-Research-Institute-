# SHIRMANI SUPREME — Implementation Plan and Release Gates

**Specification version:** 1.0.0  
**Decision:** Character description approved  
**Status:** IMPLEMENTATION PLAN — NOT A CLAIM OF LIVE COMPLETION

## 1. Approved character

The character communicates in a simple, warm, attentive, impartial, transparent, and context-sensitive manner. It listens to the full question, identifies the user's practical intent, answers in accessible language, gives an example when useful, explains reasoning and limits, cites reliable sources for factual claims, and distinguishes known facts from interpretation.

The user's philosophical vocabulary—including “निष्पक्ष समझ”, “शमीकरण यथार्थ सिद्धांत”, “यथार्थ युग”, and “संपूर्ण संतुष्टि की निरंतरता”—may be presented respectfully as the user's own philosophical framework. It must not be presented as independently verified scientific fact without suitable evidence. If evidence is insufficient, say: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**

The character must not shame, manipulate, stereotype, or promise control over another person's thoughts or feelings. Its goal is that people feel heard and understand the subject more clearly, while retaining their autonomy.

## 2. Identity and asset integrity

- Preserve the user's original photograph exactly; allow proportional scaling and layout placement only.
- Do not generate, retouch, beautify, reconstruct, or substitute a face.
- Use only the user's original voice recording or a voice provider that the user has explicitly authorized.
- Do not infer authorization from a login to a third-party app.
- If the original image/audio asset is not available in the authorized project workspace, mark the integration **BLOCKED — SOURCE ASSET REQUIRED**.
- Approved English identity line:

  **Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh**

## 3. Required end-to-end architecture

`Input voice/text → speech recognition (if voice) → intent/context → reasoning → evidence gate → response content → authorized voice output → photo/avatar presentation → lip-sync → live delivery → audit → feedback/improvement`

Each stage must expose a status and test result. A workflow run or a saved design is not proof that an end-to-end interaction works.

## 4. Evidence states

| State | Meaning | Required behavior |
|---|---|---|
| VERIFIED | A defined test passed with a recorded result and adequate evidence | Show test ID, date, result, and evidence reference |
| SOURCE-BASED | A reliable source supports the statement, but independent verification is not complete | Cite the source and retain the qualification |
| PHILOSOPHICAL / IDENTITY | A personal belief, self-description, or philosophical concept | Attribute it as such; do not label it scientific proof |
| INSUFFICIENT EVIDENCE | Evidence is missing or inadequate | Say “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।” |

## 5. Product card and product passport contract

Every product that is actually ready for public listing must have its own:
1. unique name and stable product ID/version;
2. product-specific screenshot, not a generic placeholder;
3. short description on the product visual;
4. QR code linking to that product's long description/passport;
5. usage guide and supported-use statement;
6. product-specific demo video (MP4 or a clearly stated supported format);
7. test record, known limitations, and version/change history;
8. customer feedback and quality-improvement path.

The original photo and approved English identity line may appear in the product visual according to the brand layout. QR codes must be generated from the canonical product-passport URL and tested by scanning. Do not print decorative QR-like artwork as if it were functional.

A missing demo, screenshot, valid QR destination, usage guide, or required test must block the product's **READY FOR SALE** status. Use **IN DEVELOPMENT** or **BLOCKED** instead.

## 6. Minimum acceptance tests

- Character profile JSON/metadata validates against the repository schema.
- Photo integrity: source file hash recorded; displayed version differs only by proportional scaling/layout.
- Voice authorization: provider/asset and permission are documented.
- Speech recognition: test phrases produce inspectable transcripts and error metrics.
- Context/Q&A: representative easy, ambiguous, multilingual, and specialist questions are tested.
- Evidence gate: verified, source-based, philosophical, and insufficient-evidence examples are correctly classified.
- Voice output: authorized voice is confirmed through an actual sample playback test.
- Lip-sync: spoken test clip and visual timing are inspected together.
- Product visual: screenshot, short description, identity line, and QR are readable at mobile size.
- QR: scan resolves to the correct product passport, not a placeholder or another product.
- Demo: product-specific demo plays and demonstrates the stated use.
- Accessibility and privacy: controls, disclosures, and collection of customer data are reviewed.
- Regression: respectful communication, uncertainty handling, and identity-integrity tests pass.

Record **PASS**, **FAIL**, or **BLOCKED** for every test. Never convert a missing result into PASS.

## 7. Release states and metrics

Track separate counts for:
- planned products;
- products with an implementation artifact;
- products with screenshot and working QR;
- products with demo and usage guide;
- products with passing tests;
- products approved for sale.

Report numerator, denominator, and measurement date. Do not claim 100% readiness or revenue without auditable evidence. Sales outreach, customer replies, orders, payments, and delivery are separate states and must each have their own evidence.

## 8. First implementation sequence

1. Locate and validate the original photo and authorized voice asset.
2. Validate the character profile and English identity line.
3. Build one reference product end-to-end before scaling to the full catalogue.
4. Generate that product's real screenshot, passport page, scannable QR, usage guide, and demo.
5. Run the acceptance tests and publish only if all required gates pass.
6. Use the reference product as the template for catalogue automation.
7. Add customer feedback, versioning, and auditable improvement records.

## 9. Current boundary

This file records the approved implementation contract and test gates. It does **not** establish that original media assets have been found, that an avatar/voice/lip-sync pipeline is connected, that any product demo has been produced, or that any product has passed production testing. Those states must change only after the relevant artifact and test evidence exist.
