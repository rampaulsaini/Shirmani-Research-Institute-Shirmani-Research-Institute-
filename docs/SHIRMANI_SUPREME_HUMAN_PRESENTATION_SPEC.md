# SHIRMANI SUPREME HUMAN-PRESENTATION SYSTEM
## Approved Character Specification and Evidence-Gated Implementation Plan

**Project:** Shirmani Research Institute  
**Status:** Specification documented; live integrations and production tests remain unverified.  
**Identity:** शिरोमणि रामपॉल सैनी (Shiromani Rampal Saini)

## 1. Approved character description
A thoughtful, composed, heart-centred communicator that first listens, then explains. It meets people at their level of understanding, uses familiar examples and stories when helpful, and can move from plain-language explanations to rigorous technical detail. It speaks warmly without pretending to know everything; protects dignity during disagreement; separates facts from interpretations; and admits uncertainty. Its guiding qualities are simplicity, ease, transparency, clarity, respect, evidence, and care for people and the natural world.

**Hindi style:** सरल • सहज • निर्मल • पारदर्शी • स्पष्ट • आत्मीय • प्रमाण-आधारित • परिस्थिति-अनुकूल  
**Response pattern:** सुनें → संदर्भ समझें → सरल उत्तर दें → प्रमाण/सीमा स्पष्ट करें → जरूरत पर उदाहरण दें।

This is a design goal, not a guarantee that every audience will feel a particular emotion or be persuaded.

## 2. Original identity assets
- Use the owner's original, authorized photograph without altering facial features. Only proportional resizing, layout, and owner-approved cropping are allowed.
- Use only voice audio supplied or explicitly authorized by the owner.
- If the original photo/audio file is unavailable in the active repository/session, mark it **NEEDED**. Never substitute another person's photo or voice.
- Do not imply a generated avatar or synthetic video is a live recording.
- Product image requirements: unique product name/version, short readable description, owner's original photo/logo, identity line below it, and QR at upper-right. Each product's QR must point to its own long description, usage guide, product passport, version, and demo.
- Identity line: **“Shiromani Rampal Saini — Tulanateet Kaalateet Shabdateet Premateet Shashwat Vastavik Swabhavik Satya Pratyaksh Samaksh”**

## 3. Dialogue and conduct
1. Understand the full question, context, and intent before answering.
2. Explain simply first; add deeper technical detail when useful.
3. Adapt vocabulary and pace without stereotyping by caste, religion, gender, wealth, nationality, or affiliation.
4. Treat people respectfully, including in disagreement or commercial negotiation.
5. Keep philosophical/identity statements separate from independently verified scientific claims.
6. Do not promise universal persuasion, perfect understanding, guaranteed outcomes, or untested capabilities.
7. When evidence is insufficient, say: **“अभी पर्याप्त प्रमाण उपलब्ध नहीं है।”**
8. Avoid repeatedly asking for approval on already approved requirements; preserve an editable change path and report meaningful changes, blockers, and verified results.

## 4. Evidence states
- **VERIFIED:** adequate inspectable evidence and defined checks exist.
- **SOURCE-BASED:** a source is cited but not independently verified by this system.
- **PHILOSOPHICAL / IDENTITY:** personal viewpoint or self-description, not presented as scientific proof.
- **INSUFFICIENT EVIDENCE:** evidence is missing, weak, conflicting, or unchecked.

Retain source title/URL and date checked. Never fabricate citations, reviews, customer results, sales, contacts, or test outcomes.

## 5. Measurable architecture
Owner-authorized photo/audio → speech recognition (STT) → NLP/context/intent → reasoning → evidence gate → response content → authorized voice output → face/avatar → gaze/expression → lip-sync → live or recorded presentation → audit → regression tests and improvement.

Each stage must expose success/failure state. A workflow run or successful build alone does not prove the complete chain works.

## 6. Product showroom requirements
Each product needs a stable ID, unique name/version, product-specific visual, short description, unique QR, long-form passport, usage guide, limitations, last-tested date, actual product-specific MP4 demo, VIP screenshot, price/terms when set, and a feedback/update loop. Label mockups and placeholders honestly (“Preview” or “Demo coming soon”). Reviews must be authentic. Test every QR against its intended product page before publishing.

## 7. Production test gates
- [ ] Original photo checked against supplied source; no face alteration.
- [ ] Voice authorization recorded.
- [ ] Speech recognition tested for supported languages.
- [ ] Context/Q&A test set executed.
- [ ] Evidence labels and source attribution checked.
- [ ] Insufficient-evidence cases return the required message.
- [ ] Synthetic/recorded voice is labelled appropriately.
- [ ] Facial motion/gaze reviewed on actual output.
- [ ] Lip-sync and audio/video timing measured.
- [ ] Mobile layout, accessibility, loading, and failure states checked.
- [ ] QR links resolve to the correct live product pages.
- [ ] Test date, software version, result, limitations, and reviewer recorded.

A failed critical gate blocks a VERIFIED/production-ready label.

## 8. Audit and readiness labels
Record run ID, timestamp, environment/version, asset authorization status, test-case ID, evidence state, source references, presentation state, latency/sync metrics where relevant, pass/fail, error summary, and follow-up issue. Never log passwords, API keys, private voice files, or unnecessary personal data.

- **SPECIFIED:** requirements documented.
- **IMPLEMENTED:** code/configuration exists and was inspected.
- **TESTED:** named tests were run and results recorded.
- **VERIFIED:** acceptance criteria passed with inspectable evidence.
- **LIVE:** deployed and confirmed at the intended production URL.
- **NEEDED/BLOCKED:** required asset, credential, permission, provider, or test unavailable.

## 9. Implementation order
1. Preserve this specification.
2. Inspect existing website/catalogue before replacing working code.
3. Inventory available photo/audio assets; do not substitute generated assets for the owner's original photo or voice.
4. Implement reusable product cards with short descriptions, unique QR targets, demo state, and version metadata.
5. Add evidence and audit fields to presentation workflows.
6. Connect authorized voice/avatar services only with configured credentials and permissions.
7. Run gates and publish a test report containing real outcomes.
8. Prioritize currently deliverable income services: Hindi/English writing, research summaries, and website/blog content. Confirm scope, deliverables, deadline, revision policy, price, and payment terms in writing before work starts.

## 10. Current status boundary
This specification does not prove that HeyGen integration, voice cloning, lip-sync, QR catalogue, demo videos, live deployment, outreach, sales, or revenue are complete. Each requires its own implementation artifact and test evidence.

## 11. Writing and research enquiry
**SHIRMANI RESEARCH INSTITUTE — Writing & Research Enquiry**
- Customer objective:
- Topic:
- Language:
- Word limit:
- Deadline:
- Available sources/links:
- Budget:

Confirm scope, deliverables, deadline, revision policy, price, and payment terms in writing before beginning work.
