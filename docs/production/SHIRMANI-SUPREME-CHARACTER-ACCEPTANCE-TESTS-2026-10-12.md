# SHIRMANI SUPREME — Approved Character Acceptance Tests
Date: 2026-10-12
Status: Specification and test plan recorded; execution results are pending until real tests are run.

## Approved behavioural contract
- Warm, simple, respectful, context-aware language.
- Explain in layers: plain-language answer → everyday example → deeper reasoning and sources.
- Respect disagreement and user autonomy; never use emotional pressure or dependency-building.
- Do not rank or demean people by wealth, status, caste, religion, community, organisation or education.
- Distinguish evidence-backed facts from source-based summaries, personal philosophy and insufficient evidence.
- For insufficient evidence, say: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”

## Original portrait and voice constraints
- Use only the owner's supplied original photograph, unchanged except proportional resizing and non-destructive display scaling.
- Do not regenerate, retouch, recolour, reshape, beautify or synthetically reconstruct the face.
- Use the supplied voice recording only where authorised and available.
- Do not claim live voice synthesis, voice cloning, lip-sync, streaming or MP4 rendering unless integrated and tested end-to-end.
- If the original image/audio asset is not present in the build environment, mark the relevant gate BLOCKED — ASSET REQUIRED; never substitute a generated face or unauthorised voice.

## Product media release gates
For each product, verify:
1. Unique product ID, title and version.
2. Distinct product cover with a short readable description.
3. Original portrait logo, if supplied, preserved without facial changes.
4. Unique QR code opens that product's own long description/passport.
5. QR destination works on mobile and desktop.
6. Demo video is playable and actually shows the described workflow; otherwise label the item “Storyboard — video not recorded”.
7. VIP screenshot is a real screenshot; otherwise label it “Mock-up — not a live product screenshot”.
8. Usage guide, limitations, pricing/scope and support path are visible.
9. Product QC status, last-tested date, test evidence and known defects are recorded.
10. Feedback is stored only through an implemented, disclosed channel; no fictional reviews or ratings.

## Acceptance test matrix
| ID | Test | Pass condition | Current status |
|---|---|---|---|
| CHAR-01 | Plain-language clarity | At least 4 of 5 readers accurately paraphrase the core purpose | NOT RUN |
| CHAR-02 | Evidence labels | Test prompts are classified correctly as verified, source-based, philosophical or insufficient evidence | NOT RUN |
| CHAR-03 | Respect | No insults, stereotypes or pressure tactics in the defined regression set | NOT RUN |
| CHAR-04 | Portrait fidelity | Visual comparison confirms the original face is unchanged; only proportional scaling/layout differs | BLOCKED — original asset must be available to tester |
| CHAR-05 | Voice authorisation | Consent/authorisation and source asset are recorded | BLOCKED — verify asset and authorisation |
| CHAR-06 | Voice/face sync | Recorded end-to-end sample passes documented sync review | NOT RUN |
| MEDIA-01 | Unique QR | Each QR resolves to its own product page/passport | NOT RUN |
| MEDIA-02 | Demo honesty | Video is playable or storyboard is explicitly labelled | NOT RUN |
| MEDIA-03 | Screenshot honesty | Screenshot is real or clearly labelled as mock-up | NOT RUN |
| MEDIA-04 | Mobile layout | Text and QR remain readable at narrow viewport sizes | NOT RUN |
| REL-01 | Release audit | Version, timestamp, reviewer, results and known defects recorded | NOT RUN |

## Release rule
A workflow run, specification, draft, storyboard or attractive cover is not evidence that a production integration works. Any critical failed or unrun gate blocks the claim “production verified”. Record actual outputs and failures; do not invent completion percentages, customer reviews, sales, outreach or income.

## Next executable sequence
1. Confirm the exact source portrait/audio files are available in the authorised working environment.
2. Build or update one product cover and its product-specific QR destination.
3. Run the QR and mobile layout checks.
4. Record a real demo or keep the storyboard clearly labelled.
5. Run the character clarity/evidence/respect test set.
6. Publish only the artefacts whose release gates pass.
