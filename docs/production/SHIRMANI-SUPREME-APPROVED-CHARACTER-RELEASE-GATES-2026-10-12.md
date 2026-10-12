# SHIRMANI SUPREME — Approved Character Implementation Gate
Date: 2026-10-12
Status: SPECIFICATION RECORDED; production integrations remain unverified
Product ID: SRI-PRES-001
Owner identity: शिरोमणि रामपॉल सैनी (Shiromani Rampal Saini)

## Approved character decision
The user approved the character description and authorised continuation under these constraints:
- Dialogue is simple, warm, evidence-based, and adapted to the actual context.
- Use the user's exact original portrait; only proportional size adjustment and placement are allowed. Do not redraw, beautify, reshape, replace, or synthesize the face.
- Use only the user's original voice recording or a voice integration explicitly authorised by the rights holder. Do not claim voice cloning or exact voice match until an actual authorised integration and comparison test pass.
- Never report a feature as complete without an executable test and inspectable evidence.

## Public character description
“नमस्कार। मैं शिरोमणि रामपॉल सैनी के ‘निष्पक्ष समझ’ दृष्टिकोण को सरल, आत्मीय, परिस्थिति-अनुकूल और प्रमाण-सचेत भाषा में प्रस्तुत करने वाला डिजिटल प्रस्तुति किरदार हूँ। मैं पहले प्रश्न और संदर्भ को समझने की कोशिश करता हूँ। जहाँ विश्वसनीय स्रोत उपलब्ध हैं, वहाँ स्रोत और उसकी सीमा बताता हूँ; जहाँ बात व्यक्तिगत दर्शन या पहचान की है, उसे उसी रूप में स्पष्ट करता हूँ; और जहाँ पर्याप्त प्रमाण नहीं हैं, वहाँ साफ़ कहता हूँ—‘अभी पर्याप्त प्रमाण उपलब्ध नहीं है।’ मेरा उद्देश्य किसी व्यक्ति या समुदाय को नीचा दिखाना या किसी खास भावना के लिए दबाव डालना नहीं, बल्कि बात को स्पष्ट, सम्मानजनक और समझने योग्य बनाना है।”

## Evidence labels
1. INDEPENDENTLY VERIFIED — adequate evidence and a recorded test/review trail exist.
2. SOURCE-BASED — named source exists; independent verification is not complete.
3. PHILOSOPHICAL / PERSONAL PERSPECTIVE — a personal identity, interpretation, value, or worldview.
4. INSUFFICIENT EVIDENCE — explicitly say: “अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”

## Portrait and voice asset gate
- Portrait source: NOT VERIFIED IN THIS REPOSITORY REVIEW. The source asset must be located and checked before production output can use it.
- Voice source: NOT VERIFIED IN THIS REPOSITORY REVIEW. The original recording must be located and checked before production output can use it.
- Allowed portrait transform: proportional scaling and positioning only.
- No fabricated preview may be described as the user's real face or voice.
- If source assets or authorization are unavailable, mark the render BLOCKED — SOURCE ASSET / AUTHORIZATION NEEDED.

## Four capability versions
- V1 — Clear Script: character brief, scripts, Q&A response format and rehearsal; can be prepared with the existing browser-local studio.
- V2 — Authorized Voice: V1 plus real authorized speech input/output; BLOCKED until provider/model is connected and audio tests pass.
- V3 — Portrait + Lip-sync: V2 plus the exact approved portrait, facial animation and measured lip-sync; BLOCKED until actual asset and end-to-end tests pass.
- V4 — Live Presenter: V3 plus live Q&A, latency handling, moderation, privacy controls and audit; BLOCKED until a live integration passes all release gates.

A version label describes a target capability, not proof that the capability is connected.

## Required end-to-end release tests
Record test date, tester, test inputs, output evidence, result and defect ID for each:
- Intent/context understanding and ambiguity handling.
- Plain-language comprehension (at least 4 of 5 readers can paraphrase the core answer).
- Evidence labels correctly distinguish sourced claims, philosophy and insufficient evidence.
- Unsupported claims produce the required Hindi uncertainty statement.
- Respectful communication regression test passes without stereotyping or demeaning groups.
- Original portrait identity preserved; only proportional scaling/placement changed.
- Original voice or authorised voice integration verified using actual audio samples.
- Captions/transcript and mobile accessibility reviewed.
- Lip-sync timing reviewed against real audio/video.
- Privacy, retention, deletion and consent notices reviewed.
- Live latency, failure handling and rollback tested for V4.
- Product passport, demo URL, usage guide, known limitations and release version are published.

## Product media release gate
Every product must have a unique product ID and distinct product identity. Before marking its media pack complete, record:
- Product-specific cover image with logo/portrait treatment permitted by the asset gate.
- Short description visible on the cover.
- A real QR code pointing to that product's long description or canonical product page (not placeholder text).
- Actual demo video URL or explicit status “DEMO VIDEO NOT YET RECORDED”.
- Usage guide, product passport, version, QC result, limitations and last-tested date.
- VIP screenshot captured from the real product UI, or explicit status “SCREENSHOT NOT YET CAPTURED”.
- Customer feedback and improvement loop, once actual customer feedback exists.

A storyboard is not a video. A QR placeholder is not a scannable QR. A test checklist is not a passed test. A browser-local prototype is not a hosted AI service.

## Current verified state from this repository review
- Public repository exists and is accessible: rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-.
- Existing Heart-View Character Studio is a browser-local brief/rehearsal tool.
- The existing character specification explicitly says live avatar, voice cloning, lip-sync, streaming and MP4 rendering are not proven implemented by that specification.
- The repository README lists existing product media tools that prepare covers/QR destinations/passports/storyboards; it explicitly distinguishes these from actual MP4 rendering, publishing, payments and sales.
- Original portrait and original voice were not verified in the inspected repository files.
- No claim is made here that a new photo/video was rendered, a voice integration passed, any organisation was contacted, or income/sales occurred.

## Next execution order
1. Locate and verify the original portrait and original audio recording.
2. Audit the product catalogue for missing actual QR images, demo-video URLs, VIP screenshots and usage guides.
3. Produce one complete pilot product media pack end-to-end and run its release tests before scaling to the catalogue.
4. Integrate authorised voice/avatar providers only after credentials, consent, privacy and rollback are defined.
5. Track every product through DISCOVERY → BUILD → QC → PUBLISHED; only passing evidence moves a product to PUBLISHED.
