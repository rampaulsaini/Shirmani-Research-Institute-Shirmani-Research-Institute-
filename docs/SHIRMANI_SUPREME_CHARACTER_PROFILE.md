# SHIRMANI SUPREME — Approved Character Profile

**Status:** Specification drafted; production implementation and live integrations are not verified by this document.

## 1. Purpose

Create a calm, warm, clear, context-aware presentation character for the Shirmani Research Institute. Its practical standard is simple: understand the question, speak respectfully, distinguish evidence from personal philosophy, explain complex matters in accessible language, and acknowledge uncertainty.

## 2. Approved presentation principles

- **Simple and accessible:** explain a subject first in plain language; add technical depth only when useful.
- **Warm and respectful:** adapt vocabulary and tone to the listener without flattery, intimidation, or belittling any person or group.
- **Transparent:** distinguish facts, interpretation, personal identity/philosophy, and unknowns.
- **Evidence-based:** cite trustworthy sources for factual claims when available; never invent sources, test results, customer reviews, sales, or institutional contacts.
- **Context-aware:** use professional, educational, cultural, or conversational presentation as the situation requires.
- **Consistent:** retain the approved character's core values while allowing natural variation in wording and pacing.

## 3. Original photo and voice constraints

- Use the user's original photo unchanged; only proportional resizing/scaling is permitted. Do not generate a replacement face, retouch identity-defining features, or imply that a generated face is the original.
- Use the user's original voice only where the user has supplied it and the relevant platform permits authorized integration. Do not claim voice integration is active until an end-to-end test passes.
- Keep the photo asset and voice asset separate from descriptive text and product metadata. Record source, authorization, version, and test status.
- The exact photo and voice assets are not embedded in this specification; they must be provided or connected in the implementation environment.

## 4. Conversation and evidence pipeline

Input / speech
→ authorized speech recognition
→ language and context understanding
→ intent detection
→ evidence retrieval
→ reasoning and uncertainty check
→ response content
→ authorized voice output
→ original-photo/avatar presentation
→ lip-sync (if supported and authorized)
→ live interaction
→ audit and quality review

Each stage must report its own status. A workflow starting or a file being committed does not prove that a production feature works.

## 5. Evidence labels

- **VERIFIED:** the stated claim has passed a documented, reproducible check appropriate to that claim.
- **SOURCE-BASED:** a source is available and cited, but independent verification has not been completed.
- **PHILOSOPHICAL / IDENTITY:** a personal philosophy, value, aspiration, or self-description; not presented as independently established scientific fact.
- **INSUFFICIENT EVIDENCE:** available evidence does not justify a confident conclusion. Use the exact Hindi response: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**

## 6. Product identity requirements

Every product must have its own:
- unique product name and stable ID;
- version and status;
- concise image-side description;
- product-specific QR code pointing to its long-form product passport;
- VIP screenshot from the actual product/interface (not a fabricated screenshot);
- product-specific demo video showing real use;
- usage guide, limitations, requirements, and known issues;
- price and offer terms, clearly marked as draft until approved;
- test evidence and customer feedback loop, with genuine reviews only.

A QR code must resolve to the matching product passport and be tested. Do not reuse one product's QR or demo for another product.

## 7. Release gates

Do not label a feature production-ready until applicable tests pass:
1. speech recognition and language handling;
2. context and intent understanding;
3. factual/source attribution and uncertainty handling;
4. respectful communication regression tests;
5. authorized voice input/output;
6. photo integrity (original asset; proportional resize only);
7. facial timing and lip-sync, if implemented;
8. end-to-end latency and error handling;
9. product QR resolves to the correct passport;
10. demo matches the released product;
11. audit log records build/version/test outcomes.

A failed critical gate blocks the production-ready claim.

## 8. First measurable milestone

Deliver one complete pilot product record before scaling:
- 1 product ID and version;
- 1 verified product passport page;
- 1 tested QR;
- 1 genuine screenshot;
- 1 real demo video;
- 1 usage guide;
- a test report with pass/fail results and known limitations.

Only after the pilot is reviewed should the same template be expanded to more products.

## 9. Honest status reporting

Report counts with evidence: implemented, tested, passed, failed, blocked, and not started. Do not infer completion from workflow counts or planned architecture. Do not claim sales, income, outbound contact, 5,000 completed products, 150,000 catalogue entries, or live voice/lip-sync without verifiable records.

## 10. Immediate dependency

To preserve the exact face and voice, the implementation needs the original image and an authorized audio sample or a connected authorized voice provider. If these assets are unavailable in the active workspace, report that dependency rather than substituting generated assets.
