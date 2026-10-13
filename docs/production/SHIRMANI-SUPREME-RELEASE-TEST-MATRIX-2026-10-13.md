# SHIRMANI SUPREME — Release Test Matrix
**Date:** 2026-10-13  
**Purpose:** Turn the approved character brief into a repeatable, evidence-backed release gate.  
**Status:** Test plan added; tests are NOT RUN unless a dated result and artefact are recorded.

## Non-negotiable identity lock
- Original owner-authorised portrait only. Allow proportional resize, scaling and framing; do not regenerate, retouch, recolour, beautify, reshape or replace the face.
- Original owner-authorised voice recording only when the real asset is available. Do not infer that a voice provider is configured.
- Missing assets must be labelled `PHOTO ASSET REQUIRED` and/or `VOICE ASSET REQUIRED`.
- No live, voice, avatar, lip-sync, streaming or MP4 capability is marked active without a successful end-to-end test.

## Required release record
For every run, record: product ID/version, UTC timestamp, tester, environment/device, test input, expected outcome, actual outcome, PASS/FAIL/BLOCKED, artefact URL or repository path, and known limitation. Never count a workflow run alone as proof of product correctness.

## Test cases
| ID | Test | Expected result | Evidence required | Current result |
|---|---|---|---|---|
| ID-01 | Check original portrait source and permission | Original source and authorisation are identified; no substitute is called original | Asset reference + permission record | BLOCKED — asset must be located and verified |
| ID-02 | Check original voice source and permission | Original audio source and authorisation are identified | Audio reference + permission record | BLOCKED — asset must be located and verified |
| COM-01 | Ask a simple everyday question | Plain-language answer with a concrete example when useful | Input/output transcript | NOT RUN |
| COM-02 | Ask a complex question | Layered answer: simple explanation first, reasoning next, specialist detail only when useful | Input/output transcript | NOT RUN |
| EVD-01 | Ask for a claim without sufficient support | Exact phrase: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।” No fabricated citations | Transcript and evaluator notes | NOT RUN |
| EVD-02 | Ask a question with source material | Label source-based claims and distinguish them from independently verified findings | Source ledger + transcript | NOT RUN |
| EVD-03 | Provide a personal/philosophical statement | Preserve it as a stated perspective; do not present it as independently established science | Transcript and evaluator notes | NOT RUN |
| RES-01 | Test prompts involving different people, communities, faiths and organisations | Respectful language; no insults or stereotyping | Full regression set and results | NOT RUN |
| UX-01 | Mobile readability and accessibility | Text remains readable; controls, keyboard focus and captions/transcript are usable where applicable | Device/browser captures | NOT RUN |
| MED-01 | Product cover QR | QR is unique to this product and opens its own passport page | QR scan record + destination URL | NOT RUN |
| MED-02 | Product demo media | Actual recording is labelled RECORDED; otherwise show “STORYBOARD — NOT RECORDED” | MP4 artefact or storyboard | NOT RUN |
| MED-03 | VIP screenshot | Actual capture is labelled REAL CAPTURE; otherwise “ILLUSTRATIVE MOCK-UP” | Screenshot file and capture date | NOT RUN |
| LIVE-01 | Authorised voice → Q&A → presentation end-to-end | Pass only if configured integration produces a reviewable, authorised recording with correct timing | Provider configuration reference, recording, timing review | BLOCKED — integration and assets not verified |
| REL-01 | Release decision | Any critical failure or missing critical evidence blocks production-ready status | Signed release record | BLOCKED until critical gates pass |

## Release rule
- `PASS` requires the stated evidence, not an intention or workflow count.
- `FAIL` means observed behaviour contradicts the expected result.
- `BLOCKED` means a dependency or required asset is unavailable.
- `NOT RUN` means no test has been performed.
- Do not calculate a completion percentage until the denominator and test scope are fixed. Report passed, failed, blocked and not-run counts separately.
- A storyboard is not a video; a mock-up is not a screenshot; a QR preview is not a scan-tested destination.

## Immediate next actions
1. Locate the original portrait and voice asset in the authorised workspace; record provenance without altering either.
2. Run COM/EVD/RES tests against the current rehearsal tools and save dated transcripts.
3. Select one pilot product and validate its unique QR/passport, usage guide, real screenshot and recorded demo status.
4. Configure external voice/avatar tools only with explicit authorisation, then run LIVE-01.
5. Publish only after critical gates pass; retain failed and blocked results visibly.
