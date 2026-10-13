# SHIRMANI SUPREME — Acceptance Test Matrix

**Purpose:** Turn the approved character brief into measurable, evidence-backed implementation gates.  
**Status at creation:** Test plan created; tests are not run by this document.  
**Rule:** Never mark a gate PASS without a dated result, reproducible steps, and an evidence/artifact reference.

## A. Character behaviour tests

| ID | Test | Pass condition | Evidence required |
|---|---|---|---|
| CHAR-01 | Plain-language answer | A non-specialist can restate the main point after reading the answer | Test prompt, answer, reviewer result |
| CHAR-02 | Layered explanation | Answer provides simple explanation first and technical depth only when useful | Input/output transcript |
| CHAR-03 | Context adaptation | Tone and detail fit the stated audience without changing factual meaning | At least 3 audience test cases |
| CHAR-04 | Respectful language | No insult, stereotype, coercion, or demeaning treatment of a person/group | Regression test log |
| EVID-01 | Evidence labels | Claims are distinguished as independently verified, source-based, philosophical/personal perspective, or insufficient evidence | Labelled test transcript |
| EVID-02 | Missing evidence | System states “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।” where support is inadequate | Prompt, output, pass/fail record |
| EVID-03 | Citation integrity | Every cited source exists and supports the attached claim; no fabricated citations | Source ledger and reviewer check |

## B. Original identity asset gates

| ID | Test | Pass condition | Evidence required |
|---|---|---|---|
| ASSET-01 | Original photo found | Actual owner-supplied image is available with a traceable path/reference | Asset reference and authorization note |
| ASSET-02 | Face identity preserved | Only proportional resize/display scaling or framing; no generated replacement, retouching, recolouring, beautification, or reshaping | Before/after files and transformation log |
| ASSET-03 | Original voice found | Actual owner-supplied or explicitly authorized audio is available | Audio reference and authorization record |
| ASSET-04 | Voice playback | Authorized audio plays correctly in the target integration | Test recording, configuration reference, result |
| ASSET-05 | Honest missing-asset state | Missing media is labelled “PHOTO ASSET REQUIRED” or “VOICE ASSET REQUIRED”; no substitute is mislabelled original | UI screenshot and test result |

## C. Live presentation gates

| ID | Test | Pass condition | Evidence required |
|---|---|---|---|
| LIVE-01 | Speech recognition | Test utterances are transcribed within an explicitly recorded accuracy threshold | Test set, transcripts, measured score |
| LIVE-02 | Context/Q&A | System identifies intent and answers the actual question across the agreed test set | Test cases and results |
| LIVE-03 | Authorized voice path | Voice provider/configuration is authorized and end-to-end playback passes | Provider/configuration reference and playback evidence |
| LIVE-04 | Lip-sync | Measured audio/video alignment meets a predeclared threshold on test clips | Clip, measurement method, result |
| LIVE-05 | Timing/latency | End-to-end latency is measured against a declared target | Timestamped run log |
| LIVE-06 | Live smoke test | Input → response → authorized voice/visual → audit record completes without critical failure | Reproducible run ID and artifact links |

## D. Product media release gates

| ID | Test | Pass condition | Evidence required |
|---|---|---|---|
| MEDIA-01 | Product identity | Unique stable ID, product name, version and canonical page are assigned | Product record |
| MEDIA-02 | Cover and short description | Product-specific cover includes readable short description and the approved original-photo logo only if the real authorized asset is available | Actual image file and visual review |
| MEDIA-03 | QR destination | QR is unique to the product, decodes successfully and opens the intended canonical passport page | QR image, decode output, destination URL |
| MEDIA-04 | Real demo video | Video shows the actual product and supported functionality; storyboard/placeholders do not count | MP4 or published video URL and playback check |
| MEDIA-05 | VIP screenshot | Screenshot is captured from the real interface and matches the released version | Original screenshot and version reference |
| MEDIA-06 | Usage guide | Inputs, outputs, steps, limitations and troubleshooting are documented | Guide URL/file and checklist |
| MEDIA-07 | QC/review loop | Defects, user feedback, fixes and retest results are recorded | Issue/review log and retest evidence |
| MEDIA-08 | Commercial path | Price or quote basis, scope, terms and enquiry/order route are visible and accurate | Published page capture and test enquiry |

## E. Release decision

Use only these states:
- **PLANNED:** defined but not implemented.
- **IMPLEMENTED — NOT TESTED:** code or artifact exists; no passing test recorded.
- **TEST-PASSED:** listed acceptance criteria passed with linked evidence.
- **INDEPENDENTLY VERIFIED:** a separate reviewer/test process confirmed the result.
- **LIVE/DEPLOYED:** accessible in the intended environment and smoke-tested there.
- **BLOCKED:** a critical gate failed or required asset/configuration is missing.

Do not combine these states. Workflow success, file creation, a mockup, a storyboard, or a QR preview is not proof that a live product works.

## F. First execution order

1. Inventory the actual authorized photo and voice assets; record missing items without substitution.
2. Run the character/evidence behaviour tests on a small fixed test set.
3. Select one concrete product and verify its real UI, cover, QR, guide and demo assets.
4. Run end-to-end smoke tests and record failures.
5. Publish only after all critical release gates pass.

**Current test status:** NOT RUN by this specification.  
**Current live integration status:** NOT VERIFIED by this specification.  
**Income, sales, outreach and customer outcomes:** Must be evidenced separately; no outcome is implied by this document.
