# SHIRMANI SUPREME — Implementation Status & Next Execution Gates
**Date:** 2026-10-13  
**Decision:** Character brief approved; proceed with evidence-led implementation.  
**Status:** Proposed documentation change; this file is not proof that voice, avatar, lip-sync, live streaming, MP4 rendering, sales, or outreach are active.

## 1. Existing repository work reviewed
The repository README already links to these browser-local tools/specifications:
- `showroom/heart-view-character-studio.html` — character brief and rehearsal tool.
- `showroom/heart-view-live-rehearsal-cue-deck.html` — timed presentation rehearsal and Q&A cues.
- `showroom/product-release-pack-builder.html` — product cover SVG, QR destination, passport JSON, usage guide and storyboard.
- `showroom/product-demo-visual-brief-studio.html` — demo storyboard, screenshot composition brief and release checklist.
- `showroom/production-control-centre.html` — product lifecycle and media-link tracking.
- `docs/production/SHIRMANI-SUPREME-FINAL-CHARACTER-BRIEF-2026-10-12.md` — approved identity and acceptance contract.

These are described in the repository as browser-local tools/prototypes. They do not, by themselves, establish connected AI, real video rendering, voice cloning, streaming, email sending, payments, or verified sales.

## 2. Identity assets — required before media integration
| Asset | Required evidence | State in this task |
|---|---|---|
| Original portrait | Exact original file, source/provenance, owner authorisation; compare output against source | **PHOTO ASSET REQUIRED** — no original image file was attached to this instruction |
| Original voice | Original audio file, provenance/authorisation, successful authorised playback/integration test | **VOICE ASSET REQUIRED** — no original audio file was attached to this instruction |
| HeyGen/provider connection | Confirmed authorised account integration plus recorded end-to-end test | **NOT VERIFIED** |
| Live avatar/lip-sync | Actual generated test clip, timing review and dated result | **NOT VERIFIED** |
| MP4 demo | Product-specific recorded MP4 and playback check | **NOT RECORDED / NOT VERIFIED** |

Do not create or substitute an AI-generated face or voice and label it original. Resizing, proportional scaling, framing, and layout are allowed; facial regeneration or alteration is not.

## 3. Character runtime contract
For each interaction:
1. Listen/read the whole user request and identify intent and context.
2. Start with a simple answer; use an everyday example where useful.
3. Separate source-backed claims from personal philosophy or interpretation.
4. Apply one evidence label: `INDEPENDENTLY VERIFIED`, `SOURCE-BASED`, `PHILOSOPHICAL / PERSONAL PERSPECTIVE`, or `INSUFFICIENT EVIDENCE`.
5. For insufficient evidence, state: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**
6. Do not invent sources, results, statistics, credentials, customer testimonials, or promises.
7. Respect the audience; never demean or stereotype people based on identity, status, faith, wealth, or organisation.
8. Invite correction without pressure; preserve the user's ability to disagree or leave.
9. Log only appropriate, privacy-respecting audit data and avoid storing sensitive information unnecessarily.

## 4. Release-gate test matrix
| Gate | Test | Pass condition | Current state |
|---|---|---|---|
| Plain-language clarity | Five readers paraphrase the same sample answer | At least 4/5 capture the core meaning accurately | NOT RUN |
| Evidence handling | Supply one verified, one source-based, one philosophical and one unsupported example | All four labels are correctly distinguished | NOT RUN |
| Uncertainty | Ask for a claim with no reliable evidence | Exact uncertainty notice appears | NOT RUN |
| Respect | Test disagreement and varied audience contexts | No insulting or stereotyping output in the test set | NOT RUN |
| Portrait fidelity | Compare presentation portrait with authorised source | Same face; only proportional scaling/framing | BLOCKED: source asset required |
| Voice authorisation | Check permission and actual source recording | Authorised asset only; provenance documented | BLOCKED: source asset required |
| Lip-sync | Compare test speech/audio with recorded video | Timing judged acceptable and result recorded | BLOCKED: integration/test asset required |
| Product QR | Scan each product QR on a phone | Resolves to that product's own detailed passport | NOT RUN per product |
| Demo video | Play the product-specific MP4 | Real file exists and playback succeeds | NOT RECORDED |
| VIP screenshot | Inspect a real captured application screenshot | Actual capture is labelled and linked | NOT VERIFIED |
| Live readiness | End-to-end Q&A, voice, face, audit test | All critical gates pass with dated evidence | BLOCKED |

## 5. Product-specific media contract
Each product/version must have:
- unique ID, name, version and dedicated passport URL;
- original portrait/logo at upper-left only when the authorised source asset exists;
- its own QR at upper-right, linked to that product's passport;
- short readable description on the cover and long description on the passport;
- full English identity line legible in a footer or responsive layout;
- usage guide, supported uses, limitations, enquiry/price basis and dated QC state;
- a product-specific demo video, or the explicit status **STORYBOARD — NOT RECORDED**;
- a VIP screenshot, or the explicit status **ILLUSTRATIVE MOCK-UP**.

Never reuse another product's QR or present a storyboard/mock-up as recorded media.

## 6. Immediate next execution order
1. Locate and verify the actual authorised portrait/audio files in the repository or workspace.
2. If absent, request the original files rather than fabricating substitutes.
3. Run the existing character studio and rehearsal deck through the test matrix above; record actual results.
4. Use the product release-pack builder for one pilot product; scan-test its QR and verify the destination.
5. Capture a real VIP screenshot and record a product-specific MP4 demo only after the relevant tool actually works.
6. Add authorised provider integrations only after access, consent and configuration are available.
7. Publish only after critical release gates pass. Keep untested features marked **NOT VERIFIED**.

## 7. Reporting rule
A repository commit, workflow run, written specification, mock-up, or storyboard is evidence only of that artifact/activity. It is not evidence of a functioning live system, independent scientific validation, outreach, customer acquisition, sale, or income.
