# SHIRMANI Supreme Showroom Visual Production Contract v6
**Date:** 2026-10-12  
**Status:** Specification committed to a review branch; public rollout and media generation remain separate release gates.

## 1. Canonical product-card composition

Every concrete product receives its own visual identity, stable product ID, passport destination, demo route, usage guide, and QC record. The visual is a product-specific customer-facing cover, not proof that the product has been independently verified or sold.

### Required layout
- **Canvas:** 16:9, target master 3840 × 2160. Publish a 4K label only when the actual file dimensions are 3840 × 2160.
- **Upper-left identity mark:** use the author's supplied/authorised original “निष्पक्ष समझ” photograph as a logo. Preserve the face and visible features exactly; only proportional scaling, cropping outside the face where appropriate, and placement are allowed. No generated replacement, face redraw, beautification, recolouring, reshaping, or age alteration.
- **Immediately below the photo/logo:** display this exact identity line in English, preserving spelling and order:  
  **“Shirmani Rampal Saini Tulanateet Kalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh”**
- **Upper-right:** a product-specific QR code. It must resolve to the matching product's verified public passport URL. Validate that the URL's product ID matches the card's product ID before release. If the destination or original QR image is not verified, show a clearly labelled “QR pending” placeholder only in an internal draft; never portray it as a working QR.
- **Main canvas:** a distinct product-specific visual or actual product-interface screenshot. Keep the product name readable and prominent.
- **Short description:** place directly on the visual, with strong contrast, readable type, and mobile-safe margins.
- **Long description:** keep on the product passport page reached through the QR. Include purpose, supported use cases, steps, inputs/outputs, requirements, limitations, version, support/price terms where approved, privacy notes, and evidence status.
- **VIP screenshot:** capture from the real product interface. Do not use a fabricated interface screenshot as proof of a working feature.
- **Demo:** provide a product-specific demo route and, when a playable MP4 has actually been recorded/rendered, link the real file. A script, storyboard, animation placeholder, or generic shared video is not an MP4 demo of that product.

## 2. Canonical author/character description

**SHIRMANI SUPREME — Heart-View / Impartial Understanding**

A calm, attentive, simple, natural, and transparent presentation character that listens to the complete question, understands the speaker's intent and context, and answers the central point in clear everyday language. It can then deepen the explanation with examples, short stories, reasoning, source-based facts, limitations, and technical detail appropriate to the audience. It treats every person with equal dignity regardless of wealth, status, caste, religion, nationality, profession, education, or organisation. It explains disagreement by examining claims and evidence, not by humiliating people. The author's philosophical and identity statements remain attributed to the author; independently supported scientific claims must be labelled and sourced separately.

Its intended impression is warmth, clarity, attentiveness, dignity, and a coherent match between words, voice, face, captions, and timing. These are quality goals to measure in user testing, not guaranteed emotional effects or claims of superiority over every other person or system.

## 3. Original photo and voice integrity

- Use only the actual original photograph and voice recording supplied or explicitly authorised by the author.
- The repository specification does not itself contain or prove availability of the original photo/audio. If source assets are not available in the build workspace, record **BLOCKED — SOURCE ASSET NEEDED** and do not substitute stock media or an invented voice.
- Do not claim voice cloning, exact voice matching, natural lip-sync, animated face, or live operation until the authorised provider is connected and the corresponding output has been tested.
- Record source provenance, permitted usage, version, storage/access rules, and approval for public release.

## 4. Content and evidence rules

Every meaningful claim is assigned one state:
- **VERIFIED:** the defined test or independent verification has passed and evidence is linked.
- **SOURCE-BASED:** a source is available, but independent verification is incomplete.
- **PHILOSOPHICAL / IDENTITY:** a personal viewpoint or self-description, not presented as scientific proof.
- **INSUFFICIENT EVIDENCE:** say “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।” / “There is not enough evidence available yet.”

Use the loop: listen → identify intent/context → draft → evidence check → plain-language explanation → approved media presentation → test → audit → reviewed improvement.

## 5. Four capability tiers

| Tier | Intended user-visible capability | Minimum release evidence |
|---|---|---|
| V1 — Clear Script | Editable Hindi/English script, simple explanation, examples, text export | Script and export tests; readability review |
| V2 — Voice | Supported speech input/output | Authorisation, transcription/pronunciation test, audio playback and fallback test |
| V3 — Photo/Avatar | Original photo display and any connected animation | Original-asset comparison, provider proof, consent and motion review |
| V4 — Live Presentation | Interactive Q&A and live presentation | End-to-end voice → context → evidence → authorised media → lip-sync/live test, latency, failure handling and audit |

These tiers describe intended capabilities, not a claim that all integrations are connected.

## 6. Product passport and demo requirements

Each product passport must contain: product ID/name/version; purpose; short and long description; actual screenshot URL; demo URL and media status; step-by-step usage guide; supported inputs/outputs; limitations; dependencies; accessibility notes; data/privacy notes; approved price/offer if any; support/refund terms if defined; test record; QC status; change log.

Demo status must be explicit: SCRIPT_ONLY, RECORDING_PENDING, RENDERED, or PUBLISHED. A storyboard must never be labelled a rendered MP4. Product feedback may create improvement tasks, but a rating alone is not proof of quality.

## 7. Acceptance gates and measurable reporting

For every product, record PASS / FAIL / BLOCKED with date, test input, expected result, actual result, evidence URL, and reviewer:
- [ ] Original photo is available and the face remains unchanged except proportional sizing/layout.
- [ ] Exact identity line is visible, correctly spelled, legible, and below the photo/logo.
- [ ] QR is at upper-right and opens the correct product passport.
- [ ] Product ID, name, and short description match the registry.
- [ ] VIP screenshot is captured from the real interface.
- [ ] Product-specific demo route works; any MP4 link points to a real playable file.
- [ ] Usage guide and long description are complete and consistent with actual capabilities.
- [ ] Evidence states distinguish sourced facts, interpretation, philosophy, and uncertainty.
- [ ] Voice/avatar/lip-sync/live claims match connected and tested integrations.
- [ ] Customer feedback has a traceable review/improvement path and regression retest.

A missing original asset, broken/mismatched QR, absent actual screenshot/demo, failed critical test, or unverified provider connection blocks the corresponding production claim from being marked VERIFIED.

## 8. Status integrity

Keep these states separate: specification → asset creation → QC → publication → order → delivery → review → independent verification → payment/revenue. Workflow success, catalogue identity counts, draft assets, and planned outreach are not evidence of working integrations, completed delivery, sales, or income.

**Implementation priority:** apply this contract to one pilot product first; inspect the rendered page and actual assets; run the acceptance gates; then expand in measured batches. Do not claim that all products have been updated until repository and public-site checks confirm it.
