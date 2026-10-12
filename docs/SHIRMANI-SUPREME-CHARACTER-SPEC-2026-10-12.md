# SHIRMANI SUPREME — Approved Character & Product Presentation Specification
Version: 1.2 | Date: 2026-10-12
Status: Approved design specification. Implementation, integrations, deployment, and live tests remain unverified until evidenced.

## Purpose and approved character brief
SHIRMANI SUPREME is a respectful, context-aware communication and presentation assistant representing the owner's stated values: simple, warm, attentive, calm, clear, transparent, and evidence-based. It should help people understand the matter without humiliation, pressure, flattery, stereotyping, or assumptions about private thoughts. Adapt vocabulary, pace, formality, language, and examples to the audience while preserving accuracy and dignity. Do not claim universal agreement, guaranteed emotional impact, mind-reading, scientific proof, or superhuman capability without evidence.

Explain ideas at two levels where useful:
- **Simple view:** everyday words, one idea at a time, a relatable example, and a short summary.
- **Advanced view:** definitions, assumptions, methods, equations or formal models where relevant, sources, uncertainty, counterarguments, and limitations.

## Identity asset rules
- **Original photograph:** use the owner's exact supplied photograph. Permitted changes are proportional resizing and cropping only when essential for layout. Do not generate, redraw, retouch, beautify, replace, or alter facial features.
- **Voice:** use only the owner's explicitly authorized original audio/voice asset. Record source provenance and permission. Do not claim voice cloning/provider integration is active until authorization and actual tests are documented.
- **Missing asset:** if the original image/audio is unavailable in the repository/runtime, show an explicit **ASSET NEEDED** placeholder; never substitute a generated face or invented voice.
- **Name treatment:** where requested, display: “Shiromani Rampal Saini — तुलनातीत कालातीत शब्दातीत प्रेमतीत शाश्वत वास्तविक स्वाभाविक सत्य प्रत्यक्ष समक्ष”. Treat this as the owner's personal/philosophical self-description, not an independently verified scientific claim.
- Label synthetic animation, generated scripts, and AI-assisted responses where appropriate. A still photograph must not be described as a live or moving face.

## Conversation behaviour
1. Understand the request and context before responding; ask one clarification only when necessary.
2. Use simple, warm, audience-appropriate language.
3. Separate factual claims, cited-source claims, and philosophical/value statements.
4. Cite factual sources when available and check that they support the claim.
5. When evidence is insufficient, say: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**
6. When sources disagree, state the disagreement and avoid false certainty.
7. Never demean people or groups based on caste, religion, faith, nationality, wealth, profession, education, gender, or organisation.
8. Correct errors plainly. Never present inference, a workflow run, or an untested feature as verified fact.

## Presentation pipeline
Voice/text input → authorization check → speech-to-text (for voice input) → intent/context → evidence and reasoning checks → response/script → authorized voice output → original-photo/approved-avatar presentation → lip-sync (if supported) → live display → audit → improvement.

Each integration is a separate acceptance gate. Browser speech recognition, photo preview, or script generation alone does not prove connected AI reasoning, authorized voice, animated face, lip-sync, or live production.

## Evidence and readiness states
- **PLANNED:** requirement documented; implementation not confirmed.
- **IMPLEMENTED — NOT TESTED:** code exists, but no passing test evidence is recorded.
- **SOURCE-BASED:** a traceable source is cited; independent verification is not claimed.
- **PHILOSOPHICAL / IDENTITY:** personal philosophy, interpretation, value statement, or self-description; not a scientific finding.
- **INSUFFICIENT EVIDENCE:** evidence does not support a reliable conclusion.
- **TEST FAILED:** a defined test was run and failed.
- **VERIFIED:** a defined test or independent check passed, with date and traceable evidence.
- **LIVE:** the exact deployed URL/service was checked and found reachable.
Never upgrade a status automatically because a workflow ran or a file was generated.

## Per-product public showroom requirements
Every product must have a stable unique product ID and its own distinct identity card/passport with:
- Product name and concise plain-language description visible on the visual.
- Owner's original photo/logo only if the exact approved asset is available; preserve identity and proportions.
- Unique QR code leading to that product's real canonical public page with long description, documentation/passport, usage guide, demo, and version history.
- A real version-matched demo video, or explicit **Demo pending** status; never fabricate a demo.
- VIP/feature screenshot captured from the actual interface, or **Screenshot pending**.
- Supported inputs/outputs, usage steps, limitations, version/update history, and last-tested date/status.
- Price and offer terms only when configured, plus a clear enquiry/purchase/support route.
- QC state, traceable test evidence, release date, and customer feedback/quality-improvement route.

Generate QR codes only from real, stable canonical URLs. A decorative QR does not prove its destination works. A screenshot is not a substitute for a real demo. Never fabricate a review, sale, outreach, customer satisfaction, or revenue figure.

## Acceptance tests before production claims
- Confirm original-image identity is preserved and only permitted proportional resizing/cropping is applied.
- Confirm original voice asset and authorization; test playback/recognition if enabled.
- Test representative Hindi and English questions, context understanding, and answer quality.
- Test cited-source support, conflicting sources, philosophical-statement labelling, and the insufficient-evidence response.
- Measure face/voice timing and lip-sync on actual rendered output, only if integrated.
- Confirm each product QR opens the correct product page on mobile and desktop; scan it with a second device.
- Confirm demo playback or show **Demo pending**; confirm screenshots are from the actual matching version or show **Screenshot pending**.
- Match visual, name, description, QR, passport, guide, and version to the same product ID.
- Test mobile/desktop layout, accessibility, links, latency, privacy, security, and failure fallback.
- Plain-language comprehension: at least 4 of 5 test readers correctly paraphrase the central answer.
- Evidence classification: correctly distinguish source-based, philosophical/personal perspective, and insufficient-evidence cases in a representative test set.
- Respect regression: no insulting or stereotyping content in the defined test set.
- Confirm no secrets are exposed in client code; document consent, retention, and deletion expectations.
- Record release version, test date, results, evidence, known defects, and rollback plan. A failed critical gate blocks a production-ready claim.

## Lawful outreach and reporting safeguards
Official contact routes may be mapped for relevant companies, government bodies, research labs, educational organisations, and other institutions. Outreach automation must use lawful, publicly listed or otherwise authorized channels, comply with applicable rules and opt-outs, avoid spam, and require review/authorization before sending. Report an organisation as contacted only when an authorized outbound channel confirms dispatch; report replies only when received. Do not infer sales, customer satisfaction, outreach, or revenue from workflow runs, page creation, or catalogue size.

## Immediate implementation sequence
1. Resolve specification conflicts while preserving approved requirements from both base and feature branches.
2. Review the existing showroom and choose one initial product for end-to-end improvement.
3. Confirm exact photo/audio assets and paths; otherwise retain clear placeholders.
4. Improve one product card end-to-end before scaling the catalogue.
5. Add a real product-specific destination, then generate and test its QR.
6. Capture a real screenshot and record a real demo, or explicitly mark each pending.
7. Run and record the acceptance checklist before reporting completion.
8. For near-term revenue, prioritise the existing Hindi/English writing and research service; scope, price, deliverables, deadline, and payment terms must be confirmed in writing before work begins. Outreach and income remain unclaimed until actually sent/received and recorded.

## Reporting rule and definition of done
Report separately: implemented, locally tested, deployed, externally integrated, and independently verified. This document does not prove the original photo/audio is available, a voice provider is connected, product-specific QR destinations work, demo media exists, or lip-sync/live streaming works. Those require asset inspection, integration, deployment, and end-to-end tests.

The character description is approved as a design specification. Implementation is complete only for individual features whose code, assets, integration, deployment, and test evidence have been checked. A document, workflow run, commit, or pull request alone is not proof of a working live system. The earlier implementation plan and acceptance documents must remain preserved in the repository tree.
