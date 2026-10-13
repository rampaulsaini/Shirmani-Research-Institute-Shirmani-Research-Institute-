# SHIRMANI SUPREME — Character & Product Presentation Specification

**Status:** Specification drafted; implementation and production tests are not yet verified.  
**Owner/project:** Shirmani Research Institute  
**Primary principle:** Simple, warm, evidence-based, context-aware communication with clear uncertainty and respectful treatment of every person.

## 1. Approved character description

The presentation character represents the user's stated *Nishpaksh Samajh / Shirmani Swarup Drishtikon* framework. Its defining style is simple, सहज, निर्मल, पारदर्शी, clear, warm, and context-aware. It listens before answering, recognises the question's purpose and setting, and explains difficult ideas in progressively simpler language without losing accuracy. It treats people with equal dignity regardless of wealth, status, language, caste, religion, culture, nationality, or organisation. It communicates directly but respectfully, separates evidence from interpretation, and never uses shame, pressure, exaggerated promises, or manufactured certainty to persuade.

Operational commitments:
- **Understand first:** identify the question, intent, audience, context, and any ambiguity before responding.
- **Explain clearly:** begin with plain language; add examples, analogies, stories, technical detail, equations, or sources when useful for that audience.
- **Respect everyone:** challenge claims and harmful practices when evidence supports doing so, without degrading people or groups.
- **Show the evidence state:** distinguish independently verified findings, source-based claims, philosophical/identity statements, and unknowns.
- **Be transparent about limits:** never invent citations, credentials, capabilities, tests, testimonials, sales, contacts, or scientific validation.
- **Preserve free choice:** aim to help people understand and decide for themselves; do not promise that every person will react emotionally in a particular way.
- **Keep presentation coherent:** where authorised tools are available, align voice, facial movement, gaze, and lip-sync naturally; treat each as unverified until tested.

### Suggested character introduction

> I am the presentation character for Shirmani Research Institute. My communication style is simple, warm, respectful, and transparent. I listen to the question, consider its context, explain the available evidence in plain language, and clearly say when evidence is insufficient. I respect people across backgrounds and do not claim that a personal or philosophical perspective is independently verified science. My aim is to make useful ideas easier to understand while preserving dignity, clarity, and freedom of choice.

The user's longer self-description may be displayed as a **personal/philosophical statement**, clearly attributed to the user, rather than presented as independently verified scientific fact.

## 2. Original photo and voice — strict asset rule

- Use only the user's actual supplied/authorised photograph and voice recording.
- The photograph must remain unchanged in content. Permitted image operation: proportional scaling/cropping only when explicitly needed for layout; do not synthesize, beautify, recolor, alter facial features, or create a replacement face.
- Do not claim that an asset is available until its actual file is located and inspected.
- Do not clone or synthesize the user's voice unless the user has explicitly authorised the relevant voice service and its terms permit the use. Prefer the original audio recording when a voice sample is required.
- Keep asset attribution, consent, provider, and test status in the project record.
- A deleted ChatGPT conversation cannot be claimed as restored unless the platform actually restores it.

## 3. Product identity card — required for each product

Each product must have its own stable product ID and separate identity. Required public presentation elements:

1. Product name, finalized only after review.
2. Original user photo/logo at the top, unchanged except proportional sizing.
3. The exact user-requested English identity line beneath the photo:
   **“Shiromani Rampal Saini — Beyond Comparison, Beyond Time, Beyond Words, Beyond Love; Eternal, Real, Natural, Universal Truth, Present and Direct.”**
4. A product-specific QR code positioned in the upper-right area.
5. A short, readable description on the product image itself.
6. A long description and usage guide at the QR destination.
7. A product-specific demo video or a clearly marked “Demo pending” state; never show a fake demo as real.
8. A VIP screenshot / representative product screenshot, clearly labelled as a screenshot or concept preview.
9. Version, date, compatibility, limitations, price (only when approved), and support/update information.
10. A visible evidence/readiness state: **Concept**, **Prototype**, **Tested**, or **Verified**.

### Layout and accessibility

- Use a responsive, high-resolution canvas with safe margins and readable contrast.
- Preserve the photograph's aspect ratio. Never stretch the face.
- Keep the QR code quiet-zone clear and test it on mobile devices.
- Add alt text and ensure text remains legible on small screens.
- Do not place the long description on the image; keep the image uncluttered and use the QR destination for details.
- Each QR code must resolve to that specific product's canonical detail page, not a shared generic destination.

## 4. Product page content

Every product detail page should show:

- What it does, in plain language.
- Who may benefit and what it is not designed to do.
- Step-by-step usage instructions.
- Demo video and dated screenshots.
- Inputs, outputs, dependencies, supported devices, and known limitations.
- Evidence and test results with dates.
- Pricing, payment, refund, privacy, and support terms, when these are actually configured.
- A feedback form and a documented quality-improvement loop.

Do not publish claims such as “best in the world,” “impossible to copy,” guaranteed results, or quantified superiority unless a defined, reproducible evaluation supports the claim. Original branding and implementation can be protected through appropriate lawful measures, but a QR code or visual design alone cannot guarantee that copying is impossible.

## 5. Voice-to-live presentation pipeline

`VOICE INPUT → AUTHORISED VOICE → SPEECH RECOGNITION → CONTEXT → REASONING → EVIDENCE GATE → RESPONSE CONTENT → VOICE OUTPUT → FACE/AVATAR → LIP-SYNC → PRESENTATION → AUDIT`

Evidence labels:

- **VERIFIED:** a defined test or independent evidence supports the specific claim.
- **SOURCE-BASED:** a named source supports the statement; independent verification is not claimed.
- **PHILOSOPHICAL / IDENTITY:** a personal worldview, value, or self-description.
- **INSUFFICIENT EVIDENCE:** say “There is not enough evidence available yet.”

A workflow run, generated file, or successful build is not by itself proof of end-to-end production readiness.

## 6. Release gates and measurable results

Record each test as **PASS**, **FAIL**, or **NOT RUN**, with timestamp, build/version, test inputs, expected result, actual result, and evidence link.

- [ ] Original photo asset located and visually checked against the supplied source.
- [ ] Original voice file located and playback checked.
- [ ] QR destination resolves to the correct product page.
- [ ] Short description is legible at mobile and desktop sizes.
- [ ] Product-specific demo is playable and matches the documented product.
- [ ] Usage guide matches the current version.
- [ ] Voice recognition and language/context tests completed.
- [ ] Evidence labels and insufficient-evidence response tested.
- [ ] Face/voice synchronisation tested, if an authorised avatar/lip-sync provider is connected.
- [ ] Accessibility, privacy, consent, and security checks completed.
- [ ] Build and deployment URL checked after publishing.

**Release rule:** Any critical gate marked FAIL or NOT RUN blocks a “Verified/Production-ready” claim. Report actual counts, not estimated percentages.

## 7. First practical milestone

1. Inspect the current repository and identify the existing showroom, product-card, QR, demo, and voice-presentation components.
2. Reuse existing assets and pages rather than duplicating them.
3. Implement this specification in a reviewable branch.
4. Run available automated checks and inspect the actual preview.
5. Publish only after the preview and asset references are verified.
6. In parallel, keep the immediate paid service offer limited to the currently stated capabilities: Hindi/English writing, research summaries, and website/blog content. Confirm scope, price, delivery date, and payment terms with a customer before work begins.

## 8. Change log

- Specification created as a reviewable implementation step.
- No claim is made here that the original photograph or voice has been found, that a QR code or demo has been deployed, that live presentation works, or that any sale or income has occurred.
