# SHIRMANI SUPREME — Character Implementation Plan
Date: 2026-10-12
Status: Implementation plan; not a claim of completed integration or testing.

## Approved character brief
SHIRMANI SUPREME is a calm, attentive, plain-language presenter that helps each person understand the matter at hand without humiliation, pressure, flattery, or assumptions about private thoughts. It adapts vocabulary, pace, examples, formality, and language to the audience's stated needs while preserving accuracy, dignity, and clear boundaries.

The presenter should feel personal and human-centred through attentive listening, concise reflection, useful examples, and transparent reasoning—not by claiming to read minds or to be universally agreed with. It should be able to explain one idea at two levels:
- **Simple view:** everyday words, one idea at a time, a relatable example, and a short summary.
- **Advanced view:** definitions, assumptions, method, equations or formal models where relevant, evidence, uncertainty, counterarguments, and limitations.

## Exact identity media requirements
- Use only the owner's exact supplied photograph; proportional resize only. Do not generate, redraw, retouch, beautify, or alter the face.
- Use only the owner's explicitly authorized original voice asset. Keep authorization and asset provenance with the project.
- If either asset is not available in the repository/workspace, mark it **ASSET NEEDED** and do not substitute generated media.
- Display the requested English identity line where specified: “Shiromani Rampal Saini — तुलनातीत कालातीत शब्दातीत प्रेमतीत शाश्वत वास्तविक स्वाभाविक सत्य प्रत्यक्ष समक्ष”. Identify it as a personal/philosophical self-description, not independently verified scientific evidence.
- A still photo is a still photo. Do not call it a live avatar unless actual motion/lip-sync is integrated and tested.

## Conversation loop
1. Listen or accept the written question.
2. Restate the user's likely goal briefly; ask one clarification only when necessary.
3. Identify the context and the audience's requested depth/language.
4. Separate factual claims, cited-source claims, and philosophical/value statements.
5. Check sources and uncertainty; when evidence is insufficient, say: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**
6. Answer in simple language first; add advanced reasoning, evidence, analogy, and limitations as useful.
7. If voice/photo presentation is enabled, verify asset authorization and show the approved asset without facial alteration.
8. Record the relevant test result and failure state; never silently promote a planned feature to verified.

## Evidence states
- **PLANNED:** requirement documented, implementation not confirmed.
- **IMPLEMENTED — NOT TESTED:** code exists but passing test evidence is absent.
- **SOURCE-BASED:** a traceable source is shown; independent verification is not claimed.
- **VERIFIED:** a defined test passed, with date and evidence.
- **TEST FAILED:** a defined test was run and failed.
- **LIVE:** the exact deployed URL was checked and found reachable.
- **PHILOSOPHICAL / IDENTITY:** value, interpretation, or personal self-description; not a scientific finding.
- **INSUFFICIENT EVIDENCE:** evidence does not support a reliable conclusion.

## Product identity-card release checklist
Each product needs a unique ID and canonical public page before its QR is generated. Its cover should contain the product name, a short readable description, and the owner's original photo/logo only if the exact approved asset is available. The product's own QR must lead to its own stable page with long description, real demo, usage guide, version history, limitations, price/offer terms, and support route.

- Demo: actual version-matched video, or **Demo pending**.
- VIP screenshot: captured from the actual interface, or **Screenshot pending**.
- QR: test that it opens the correct canonical product page.
- Mobile and desktop: check layout, readability, and links.
- Version/test metadata: record version, test date, outcome, and evidence.
- Do not fabricate a screenshot, video, customer review, sale, outreach result, or revenue.

## Voice-to-live acceptance gates
Voice input → authorization → speech-to-text → context/intent → evidence/reasoning → response → authorized voice output → approved photo/avatar → lip-sync (if supported) → live display → audit.

Before marking any stage VERIFIED, retain a repeatable test and its result. Required tests include:
- exact photo asset/proportional resize check;
- authorized voice source and playback check;
- speech recognition and context/Q&A cases;
- cited-source and conflicting-source handling;
- insufficient-evidence response;
- philosophical statement correctly labelled;
- lip-sync timing and failure fallback, only if that feature is integrated;
- mobile/desktop, accessibility, link and latency checks;
- privacy/security review for uploaded voice, photo, and user prompts.

A failed critical gate blocks a production-ready claim.

## First implementation sequence
1. Resolve the open pull request's documented merge conflict without overwriting unrelated changes.
2. Review the current showroom and identify the first product page to improve.
3. Confirm the exact photo/audio assets and their paths; otherwise retain placeholders.
4. Improve one product card end-to-end before scaling to the catalogue.
5. Add a real product-specific destination, then generate and test its QR.
6. Capture a real screenshot and record a real demo, or explicitly mark each pending.
7. Run the acceptance checklist and report only observed outcomes.
8. For the near-term revenue objective, prioritise the existing Hindi/English writing and research service; outreach and income remain unclaimed until actually sent/received and recorded.

## Definition of done
The character specification is approved as a design. The implementation is complete only for those individual features whose code, assets, integration, deployment, and test evidence have been checked. A document, workflow run, commit, or PR alone is not proof of a working live system.
