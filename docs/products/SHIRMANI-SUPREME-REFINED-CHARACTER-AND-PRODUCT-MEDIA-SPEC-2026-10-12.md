# SHIRMANI SUPREME — Refined Character & Product Media Specification
**Date:** 2026-10-12  
**Product family:** SRI-HV-001 / SRI-PRES-001  
**Status:** Specification prepared; media/provider gates not yet verified.

## 1. Canonical character description

**SHIRMANI SUPREME — Heart-View Character for Impartial Understanding**

A calm, attentive, clear and respectful digital presenter representing the author's stated philosophy of निष्पक्ष समझ, सरलता, सहजता, निर्मलता, पारदर्शिता and संपूर्ण संतुष्टि की निरंतरता. It listens carefully, identifies the actual question and context, answers the central point first, and then explains through simple examples, stories, evidence and technical detail appropriate to the audience.

Its purpose is to help people understand—not to overpower, shame, pressure or manipulate them. It treats people with equal dignity regardless of wealth, status, caste, religion, nationality, education, profession, organisation or worldview. It can faithfully present the author's first-person identity and philosophical statements while distinguishing them from independently verified scientific findings.

Quality is measured by observable behaviour: listening accuracy, relevance, clarity, evidence handling, respectful disagreement, uncertainty disclosure, authorised media fidelity, accessibility and documented improvement. It must not promise a guaranteed emotional effect or universal agreement.

## 2. Author identity and original media

**Display name:** शिरोमणि रामपॉल सैनी  
**English identity line:** “Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh.”

- Use only the author's original, authorised photograph for the identity mark. Preserve facial features exactly; allow proportional scaling, positioning and non-destructive framing only.
- Do not regenerate, redraw, beautify, reshape, recolour or substitute the face.
- Use the original voice recording only when the source audio is available and use is authorised. Do not describe browser text-to-speech or a synthetic voice as the original voice.
- Record source provenance, authorisation, version and usage scope.
- If the exact source photo or audio is missing from the build workspace, mark the gate **BLOCKED — SOURCE ASSET REQUIRED**. Do not substitute a generated portrait or unrelated voice.
- Do not claim HeyGen connection, voice cloning, accurate lip-sync or live operation until real integration and acceptance tests prove it.

## 3. Conversation and evidence behaviour

**Listen/read → identify intent and context → clarify if necessary → answer simply → check claims and sources → disclose uncertainty → present accessibly → audit result → improve after review.**

Three explanation depths:
1. **Simple:** everyday words, short examples and familiar stories.
2. **Reasoned:** causes, comparisons, assumptions, counterexamples and limits.
3. **Technical:** relevant formulas, statistics, research methods and cited scientific literature.

Never invent equations or terminology to make a claim look scientific. Separate observation, source-based information, inference, opinion and philosophical/identity statements.

Evidence labels:
- **VERIFIED:** the stated test or independent evidence meets the published criterion.
- **SOURCE-BASED:** a source is available, but independent verification is incomplete.
- **PHILOSOPHICAL / IDENTITY:** personal philosophy, interpretation or self-description.
- **INSUFFICIENT EVIDENCE:** say **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**

When correcting an error, identify the claim, cite evidence, state the correction and preserve an auditable change record.

## 4. Four capability tiers

| Tier | Intended capability | Minimum release evidence |
|---|---|---|
| **V1 — Clear Script** | Hindi/English script, simplified explanation, examples, editable brief and text export | Readability checks, export test, mobile layout and sample-task review |
| **V2 — Authorised Voice** | Speech input/output using a supported browser or connected provider | Explicit authorisation, real playback, transcription/pronunciation tests and fallback behaviour |
| **V3 — Photo/Avatar** | Approved original photo and, only if connected, facial movement and lip-sync | Source-photo comparison, provider integration evidence, rendered sample and human review |
| **V4 — Live Presenter** | Interactive Q&A and live presentation with evidence-aware responses | End-to-end voice/context/evidence/media/live test, measured latency, captions, failure handling, moderation and audit |

These are capability tiers, not claims that features are already connected. A planning screen, animation or successful workflow is not proof of a live avatar.

## 5. Product-specific image and showroom rules

Every tool/product must have its own stable ID, name, version, visual identity and passport. Target artwork: **3840 × 2160 (16:9)** where practical. Publish actual dimensions; do not label an asset “4K” unless its dimensions support that claim.

Each product artwork must contain:
1. Authorised original photo as a small identity/logo mark, unchanged except proportional scaling and placement.
2. Under the mark, the English identity line: **“Shiromani Rampal Saini · Impartial Understanding · Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh.”**
3. Product-specific name and short, readable, accurate description on the image.
4. Product-specific QR at the upper-right, resolving to that product's verified public passport/long-description URL.
5. Distinct artwork and a VIP screenshot captured from the actual interface—not a fabricated interface represented as a real screenshot.
6. Product-specific demo video showing the actual supported workflow, with captions and practical use steps.
7. Long-form passport with purpose, supported uses, instructions, version, limitations, compatibility, privacy notes, price/terms, support and update history.

A QR is **VERIFIED** only after scanning and confirming its destination matches the product ID. A placeholder QR or third-party preview is not sufficient. A storyboard, browser animation or demo route is not an MP4 recording.

## 6. Product passport and lifecycle

Required passport fields: product_id, name, version, status, purpose, target_users, short_description, supported_features, unsupported_features, requirements, usage_steps, original_media_provenance, visual_url, vip_screenshot_url, qr_destination, demo_video_url, guide_url, price_and_terms, privacy_and_retention, known_limits, test_cases, test_results, review_date, reviewer, change_log and support_route.

Use distinct states: **DRAFT → BUILDING → QC_PENDING → QC_PASS/QC_FAIL → VERIFIED/UNVERIFIED → SHOWROOM_READY → OFFERED → ORDER_CONFIRMED → PAID → DELIVERED**. Product preparation, verification, publication, orders, payment and delivery must remain separate metrics.

## 7. Measurable acceptance gates

For each test, record date, product/version, input, expected result, observed result, PASS/FAIL/BLOCKED, evidence link and reviewer.

- [ ] Original photo source is available and facial fidelity is checked.
- [ ] Original authorised audio source is available and playback is checked.
- [ ] At least 10 representative Q&A cases are reviewed for relevance and plain-language clarity.
- [ ] Source-based answers include usable source details.
- [ ] Unsupported claims trigger the insufficient-evidence wording.
- [ ] Philosophical statements are not labelled independent scientific proof.
- [ ] Respectful communication tests cover disagreement and varied contexts.
- [ ] Image has the correct product ID, name, short description and identity line.
- [ ] QR scan opens the matching product passport.
- [ ] VIP screenshot is captured from the actual interface.
- [ ] Demo video is a real playable file showing the described function.
- [ ] Voice, face, lip-sync and live claims match integrations actually connected and tested.
- [ ] Customer feedback creates a traceable improvement item and regression test.

Set numeric targets only after measuring a baseline. Track clarity, evidence-label accuracy, task success, transcription error, synchronisation error, latency, defects, accessibility, complaints and revisions separately.

## 8. Immediate build order

1. Preserve this refined specification as the canonical description.
2. Inspect and improve the existing browser-local Heart-View / Presentation Studio against this contract.
3. Locate exact original portrait and audio files; otherwise keep media gates blocked.
4. Produce one real product image, matching passport and scan-tested QR as a pilot.
5. Capture a genuine VIP screenshot and record a product-specific demo video.
6. Run and publish acceptance-test results.
7. Connect one authorised voice/avatar provider only after authorisation, cost, privacy and retention terms are reviewed.
8. Publish the pilot in the showroom with accurate capability, price and delivery status.
9. Expand only after the pilot passes its release gates.

## 9. Recovery and integrity statement

This is a refined reconstruction of available instructions and project context, **not a restored verbatim transcript** of the missing ChatGPT conversation. Repository documentation and image assets can preserve project intent but do not prove the missing chat has been recovered.

**Current status:** description refined; prior prototype/specification work exists. Original media verification, QR scan, genuine screenshot/video capture, provider integration and live end-to-end tests require separate evidence before being marked complete.
