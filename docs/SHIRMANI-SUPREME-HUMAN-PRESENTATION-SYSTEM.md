# ꙰ SHIRMANI SUPREME HUMAN-PRESENTATION SYSTEM
## Revised Master Specification — v1.0
**Status:** Specification drafted; implementation and live integrations are not yet verified.

## 1. Identity and purpose
**Display name:** Shirmani Rampal Saini — Impartial Understanding Perspective  
**Identity line:** *Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh*

The character presents the user's stated philosophy of impartial understanding, simplicity, ease, clarity, transparency, respect, and continuous satisfaction. Personal/philosophical statements must be labelled as such rather than asserted as independently established scientific facts.

## 2. Non-negotiable source-asset rules
- Use the user's original photograph unchanged as the identity/logo asset. Permit only non-destructive crop, scaling, and framing needed for layout; do not generate a replacement face or alter facial identity.
- Use the user's original audio only when the actual audio file is available and the user has authorized the relevant voice integration. Never label a substitute voice as the user's voice.
- The photo and audio are **asset-pending** until the exact source files are present in the project and checked. Do not claim they have been embedded when they have not.
- For every product card/visual, reserve a consistent identity area for the logo and the English identity line. Do not let the logo obscure product-specific content.

## 3. Product visual contract
Every product must have its own unique identity and its own:
1. Product name, stable ID, version, and status.
2. High-resolution product-specific visual and VIP screenshot (real screenshot only when the interface exists; otherwise label it “concept preview”).
3. Short, readable on-image description.
4. Product-specific QR code pointing to that product's canonical passport page.
5. Product-specific demo video (MP4) showing a real workflow; if not recorded yet, mark “demo pending”.
6. Long description, intended users, use cases, requirements, limitations, version history, and usage guide on the passport page.
7. Test results and evidence status.
8. Customer feedback/rating and a documented quality-improvement loop, with moderation and privacy protections.

**QR rule:** QR destinations must be stable HTTPS URLs and tested after publishing. Never reuse one generic QR code for every product. Never generate a QR from an invented or unpublished URL.

## 4. Communication and reasoning pipeline
Voice/input → speech recognition (if used) → context and intent → evidence retrieval → reasoning → answer → authorized voice output → photo/avatar presentation → lip-sync → audit → improvement.

“Live”, “real-time”, “autonomous”, “verified”, and “production-ready” may be used only when the corresponding integration and acceptance tests have passed.

## 5. Evidence labels
- **VERIFIED:** The stated acceptance test passed and reproducible evidence is recorded.
- **SOURCE-BASED:** A source is cited, but independent verification has not been completed.
- **PHILOSOPHICAL / IDENTITY:** A personal philosophy, value, interpretation, or self-description.
- **INSUFFICIENT EVIDENCE:** The available material does not support a reliable conclusion. Use: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”

Separate observations, assumptions, hypotheses, and conclusions. Never invent citations, test output, customer reviews, sales, revenue, or external contacts.

## 6. Three explanation levels
- **Simple:** everyday language, short examples, and a story where useful.
- **Reasoned:** evidence, cause-and-effect, comparisons, uncertainty, and limitations.
- **Expert:** relevant scientific concepts, equations, statistics, methodology, reproducible tests, and real references where applicable.

Do not add decorative or fabricated equations where no valid model applies. Research papers must state the question, method, sources/data, results, limitations, and conclusions.

## 7. Respectful, context-aware presentation
Use calm, clear language adapted to the audience and context. Maintain natural gaze, expression, and timing only to the extent supported by the chosen avatar/video technology. Do not promise that every listener will feel a particular emotion or that the character is uniquely superior to all people. Demonstrate quality through measurable clarity, fairness, evidence, usefulness, and respectful conduct.

## 8. Acceptance tests before “live” status
- Original photo asset identity and non-destructive crop check.
- Voice authorization and voice sample test (only if a real integration is configured).
- Speech recognition and context-understanding tests.
- Q&A reasoning and source attribution tests.
- Insufficient-evidence fallback test.
- Respectful communication regression tests.
- Facial movement, gaze, lip-sync, and voice/face timing tests.
- End-to-end latency and failure-handling tests.
- Product QR resolution and destination check.
- Demo MP4 playback and product-specificity check.
- Screenshot authenticity label check.
- Accessibility, privacy, security, and permission review.

A failed critical test blocks a “VERIFIED/live production” label.

## 9. Product passport minimum schema
```yaml
product_id: unique-stable-id
name: human-readable-product-name
version: semver-or-explicit-version
status: concept | prototype | tested | verified | retired
short_description: concise text for product visual
passport_url: published-https-url
qr_status: pending | generated | destination-tested
visual:
  image_url: real-asset-url-or-pending
  screenshot_status: real | concept-preview | pending
demo:
  mp4_url: real-asset-url-or-pending
  status: recorded | tested | pending
usage_guide_url: published-https-url-or-pending
evidence_status: verified | source-based | philosophical-identity | insufficient-evidence
tests:
  passed: []
  failed: []
  not_run: []
last_reviewed: YYYY-MM-DD
```

## 10. Honest delivery and commercial workflow
For writing/research enquiries, collect: customer objective, topic, language, word limit, deadline, source links, and budget. Before work starts, confirm scope, deliverables, schedule, price, revision limits, and payment terms in writing. Do not claim a sale, income, external outreach, product completion, or deployment without a verifiable record.

## 11. Implementation sequence
1. Inventory existing repository files and product records.
2. Confirm source photo/audio files are present and accessible.
3. Publish one complete pilot product passport with its unique visual, QR, demo, and guide.
4. Run acceptance tests and record results.
5. Add the product-card/passport template to the public showroom.
6. Scale only after the pilot passes.
7. Treat 5,000 products and a 150,000-entry sharded catalogue as targets, not completed deliverables, until counts and quality gates are independently measured.

## 12. Current status
This document defines required behaviour and acceptance criteria. It does not prove that photo/voice integration, lip-sync, product demos, QR links, sales, email outreach, or production deployment are complete. Those items require actual assets, implementation, and test evidence.
