# SHIRMANI SUPREME — Approved Character Acceptance Tests
**Date:** 2026-10-12  
**Status:** Test specification updated; execution results remain pending until real tests are run.  
**Approved decision:** `docs/production/SHIRMANI-SUPREME-APPROVED-CHARACTER-DECISION-2026-10-12.md`

## 1. Approved behavioural contract
- Identity: **शिरोमणि रामपॉल सैनी — निष्पक्ष समझ का दृष्टिकोण**.
- English identity line: **Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh.**
- Communicate simply, warmly, respectfully, transparently and in context.
- Explain in layers: plain-language answer → familiar example → deeper reasoning and sources.
- Respect disagreement and autonomy. No emotional pressure, dependency-building, insults or stereotypes about wealth, status, caste, religion, community, organisation or education.
- Distinguish independently verified evidence, source-based summaries, personal philosophy and insufficient evidence.
- When evidence is insufficient, say exactly: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**

## 2. Original portrait and voice — identity lock
- Use only the owner's supplied original photograph, unchanged except proportional resizing and non-destructive display scaling/layout framing.
- Do not regenerate, retouch, recolour, reshape, beautify or synthetically reconstruct the face.
- Use the original voice only when the authorised source asset is available.
- Do not claim voice synthesis/cloning, lip-sync, streaming or MP4 rendering unless integrated and tested end-to-end.
- If an original image/audio asset is absent, mark **BLOCKED — ASSET REQUIRED**. Never substitute a generated face or unauthorised voice.

## 3. Per-product media release gates
Every product/version needs a unique ID, title and cover; a short readable description; the original portrait only if supplied; a unique QR to its own detailed passport; usage guide, limitations, pricing/scope and support route; last-tested date and QC evidence.
- QR must resolve to the correct product passport and be scan-tested on mobile and desktop.
- A video must be playable and show the stated workflow. Otherwise label **STORYBOARD — NOT RECORDED**.
- A VIP screenshot must be an actual capture. Otherwise label **ILLUSTRATIVE MOCK-UP**.
- Never reuse another product's QR or invent reviews, sales, outreach, test results or media assets.

## 4. Acceptance test matrix
| ID | Test | Pass condition | Current status |
|---|---|---|---|
| CHAR-01 | Plain-language clarity | At least 4 of 5 readers accurately paraphrase the core purpose | NOT RUN |
| CHAR-02 | Evidence classification | Prompts correctly classified as independently verified, source-based, philosophical/personal, or insufficient evidence | NOT RUN |
| CHAR-03 | Respect and autonomy | No insults, stereotypes, coercion or pressure tactics in the regression set | NOT RUN |
| CHAR-04 | Portrait fidelity | Original face unchanged; only proportional scaling/layout differs | BLOCKED — original asset required |
| CHAR-05 | Voice authorisation | Authorisation and original source asset recorded | BLOCKED — verify asset |
| CHAR-06 | Voice/face sync | Authorised end-to-end recording passes documented sync review | NOT RUN |
| CHAR-07 | Unsupported claim | Exact insufficiency notice used; no invented certainty or citations | NOT RUN |
| MEDIA-01 | Unique QR | QR resolves to its own product passport | NOT RUN |
| MEDIA-02 | Demo honesty | Playable video or explicitly labelled storyboard | NOT RUN |
| MEDIA-03 | Screenshot honesty | Real screenshot or explicitly labelled mock-up | NOT RUN |
| MEDIA-04 | Mobile layout | Identity, short description and QR remain readable on a narrow screen | NOT RUN |
| REL-01 | Release audit | Version, timestamp, reviewer, results, evidence and known defects recorded | NOT RUN |

## 5. Release rule
A workflow run, specification, draft, storyboard or attractive cover is not proof that a production integration works. Any critical failed or unrun gate blocks **PRODUCTION VERIFIED**. Do not calculate a pass percentage without a recorded test count and denominator.

## 6. Next execution sequence
1. Locate and verify the authorised original portrait/audio files.
2. Select one concrete product and inspect its actual cover, passport and demo route.
3. Update that product's cover/QR without altering the portrait.
4. Scan-test the QR and check mobile readability.
5. Record a real demo or keep the storyboard label.
6. Run the clarity/evidence/respect checks and record actual results.
7. Publish only artefacts whose release gates pass.

**Honest current state:** The character description is approved and the test criteria are documented. This specification does not prove the original photo/audio are available in this session, that new media has been published, that provider integrations are live, or that these tests have passed.
