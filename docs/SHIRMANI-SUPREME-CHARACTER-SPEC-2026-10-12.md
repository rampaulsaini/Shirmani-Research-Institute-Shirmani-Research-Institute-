# SHIRMANI SUPREME — Approved Character & Product Presentation Specification
Date: 2026-10-12
Status: Approved specification. Implementation/live integrations remain unverified until tested.

## Approved character brief
The presentation character represents the user's stated values: simple, warm, respectful, clear, transparent, context-aware, and evidence-based. Explain ideas without humiliating or stereotyping people or groups. Do not claim universal agreement, guaranteed emotional impact, scientific proof, or superhuman capability without evidence.

## Identity asset rules
- Use the user's original photograph unchanged in identity and appearance. Permitted operation: proportional resizing/cropping only when necessary for layout; no face alteration, beautification, replacement, or generative reconstruction.
- Use only the user's original voice recording or a voice integration explicitly authorized by the user and provider. Do not imply a provider connection is active until a real test passes.
- If original photo/audio is unavailable in the repository/runtime, show an explicit “asset required” placeholder; never substitute a generated face or invented voice.
- Label synthetic animation, generated scripts, and AI-assisted responses where appropriate.

## Conversation behaviour
1. Understand the request and context before responding.
2. Use simple, warm, audience-appropriate language.
3. Separate personal philosophy/identity statements from independently verified scientific claims.
4. Cite sources for factual claims when available.
5. When evidence is insufficient, say: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”
6. Never present inference, an untested workflow, or an unverified claim as verified fact.
7. Do not demean people or groups based on caste, religion, faith, wealth, profession, education, or organisation.
8. Correct errors plainly and retain uncertainty.

## Presentation pipeline
Voice/input → speech recognition or text input → intent/context → reasoning → evidence gate → script → authorized voice output → original-photo/approved-avatar presentation → lip-sync → live output → audit → improvement.

Each integration is a separate gate. Browser speech recognition, photo preview, or script generation alone does not prove connected AI reasoning, authorized voice, animated face, lip-sync, or live production.

## Evidence states
- VERIFIED: independent checks and recorded tests support the exact claim.
- SOURCE-BASED: a source is cited, but the platform has not independently verified the claim.
- PHILOSOPHICAL / IDENTITY: personal viewpoint or self-description.
- INSUFFICIENT EVIDENCE: available material does not support the claim.
Never upgrade a status automatically because a workflow ran or a file was generated.

## Per-product public showroom requirements
Every product needs its own:
- stable unique product ID and distinct product name;
- product-specific visual/screenshot;
- concise short description visible on the visual;
- QR code resolving to that product's canonical long description/passport/usage guide;
- demo video, or explicit “Demo pending” status until a real demo exists;
- usage guide, supported inputs/outputs, limitations, version and update history;
- configured price/offer and a clear enquiry/purchase route;
- QC state, test evidence, release date and review/quality-feedback route.

Generate QR codes from real canonical URLs; decorative/placeholder QR images are not functional. A screenshot is not a substitute for a real demo.

## Acceptance tests before production claims
- Confirm original image identity is preserved and only resize/crop transformations are applied.
- Confirm original voice asset/provider authorization.
- Test representative Hindi and English Q&A.
- Test evidence labels, including insufficient-evidence cases.
- Confirm sources open and support their claims.
- Measure face/voice timing and lip-sync on actual rendered output.
- Confirm each product QR opens the correct product page on mobile and desktop.
- Confirm demo playback or show “Demo pending”.
- Match visual, name, description, QR, passport, guide and version to the same product ID.
- Test accessibility, mobile layout, broken links, privacy and security.
- Record test date, tested version, outcome and unresolved failures.

## Reporting rule
Report separately: implemented, locally tested, deployed, externally integrated, independently verified. Do not claim revenue, customer outreach, sales, live operation, or completion without evidence from the relevant real system.

## Current caveat
This specification does not prove that the original photograph/audio is available, an external voice provider is connected, or lip-sync/live streaming works. Those require asset inspection and end-to-end tests.
