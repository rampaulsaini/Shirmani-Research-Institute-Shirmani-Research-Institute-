# SHIRMANI SUPREME — Character & Product Acceptance Specification
**Status:** Approved specification; implementation and production verification remain separate states  
**Date:** 2026-10-12

## 1. Approved character direction
The presentation system must be simple, warm, respectful, context-aware and evidence-based. Explain difficult topics in plain language first, then provide deeper technical detail when useful. Distinguish observable facts, cited source-based claims, philosophical/identity statements, and unknowns. Never demean or stereotype a person or group based on caste, religion, belief, organisation, wealth, status, or another personal/protected characteristic.

### Identity and media constraints
- Use the user's original photograph unchanged except proportional resizing/cropping needed by the layout. Do not regenerate, retouch, beautify, alter facial features, or synthesize a replacement face.
- Use the user's original voice only where the actual recording is available and its use is authorized. Do not claim integration without an authorized asset and a successful end-to-end test.
- If the photo or authorized voice is unavailable in the execution environment, mark **BLOCKED — SOURCE ASSET REQUIRED**. Never substitute an AI-generated likeness or unapproved voice.
- Never imply a deleted ChatGPT conversation was restored unless an actual restoration can be demonstrated.

## 2. Evidence gate
Every substantive answer must have one state:
- **VERIFIED** — the relevant check was actually run and its result recorded.
- **SOURCE-BASED** — a credible source is cited, but independent verification is incomplete.
- **PHILOSOPHICAL / IDENTITY** — a personal or interpretive statement, not represented as independently established scientific fact.
- **INSUFFICIENT EVIDENCE** — say: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”

Do not treat aspirations, estimates, workflow activity, generated content, or a successful build as proof of real-world effectiveness, sales, income, adoption, or production readiness.

## 3. Presentation pipeline
Voice input → authorization check → speech-to-text → language/context understanding → reasoning → evidence gate → response content → authorized voice output → original-photo presentation → lip-sync (only with a tested provider) → live interaction → audit record → quality improvement.

Each stage must expose NOT_CONFIGURED, BLOCKED, READY_FOR_TEST, PASS, or FAIL. PASS requires a recorded test result. Missing providers, credentials, permissions, assets, or approvals remain explicit blockers. Never commit secrets.

## 4. Product release requirements
Every product/tool in the public showroom needs its own:
1. Stable name, ID, and version.
2. Product-specific VIP screenshot.
3. Short readable description on the product image.
4. QR code resolving to that product's own long-form passport.
5. Genuine product-specific demo video; until recorded, label **Demo pending**.
6. Usage guide, supported use cases, limitations, requirements, and known issues.
7. Accurate price/offer terms only when deliberately configured.
8. Test report with timestamp, test cases, result, and known failures.
9. Feedback/review route and traceable quality-improvement record.

Standard image layout: approved original photo/logo at the top (proportional resizing only); below it the English identity line:
“Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh”
and the product-specific QR in the upper-right where legible. Never reuse another product's QR, demo, screenshot, or passport. Do not present a QR as active until its destination has been checked.

## 5. Acceptance tests
### Character and communication
- [ ] Plain-language response test.
- [ ] Layered explanation: simple summary plus optional technical detail.
- [ ] Context adaptation across education, research, professional, and public/cultural settings.
- [ ] Respectful disagreement test; no group-based denigration.
- [ ] Evidence-state test for all four states.
- [ ] Unknown-answer test uses the exact Hindi insufficiency message.
- [ ] Original-photo integrity check confirms only allowed resizing/cropping.
- [ ] Authorized voice test with a supplied recording; record provider/configuration/result.
- [ ] Lip-sync and latency tests only if a real integration is configured.
- [ ] End-to-end test records input, output, evidence state, presentation state, latency, and failure state.

### Product and showroom
- [ ] Unique product ID/name/version.
- [ ] Genuine product-specific screenshot.
- [ ] QR opens the correct product passport.
- [ ] On-image short description is readable.
- [ ] Demo demonstrates real functionality or is explicitly pending.
- [ ] Usage guide and limitations exist.
- [ ] Automated checks and manual acceptance result are recorded.
- [ ] Feedback ties to the exact product/version.
- [ ] No unsupported sales, revenue, customer, outreach, or production-readiness claim.

## 6. Measurable reporting
Report from actual repository/test data: products with complete passports / products listed; valid product-specific QR / products listed; genuine demos / products listed; screenshots / products listed; tests passed / tests executed; blockers by category; actual enquiries, paid orders, and collected revenue only when supported by records. An empty test suite or workflow-run count cannot imply 100%. A test that did not execute is NOT RUN, not PASS.

## 7. Implementation sequence
1. Inspect existing architecture and avoid duplicating canonical components.
2. Identify the public showroom entry point and product metadata schema.
3. Add/validate a minimum product passport schema using one real product.
4. Generate or verify the QR only after its passport URL exists.
5. Attach a genuine screenshot, usage guide, and real demo—or mark missing assets as blockers.
6. Run repository checks and report commit, commands, outputs, and blockers.
7. Scale only after the first product passes.

## 8. Status note
This file records the approved acceptance specification only. It does NOT establish that voice, lip-sync, live presentation, QR destinations, demos, sales, or production deployment are implemented or verified. Each requires separate evidence and test results.
