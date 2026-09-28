# निष्पक्ष समझ निरीक्षण इंजन — v1

## पहला अनिवार्य चरण: निरीक्षण किस लिए है?
- human_self_understanding — स्वयं को समझने/मानवीय आत्म-निरीक्षण के लिए
- education — शिक्षा और सीखने के लिए
- employment — काम/पद के कौशल के लिए
- public_service_role — प्रकाशित सार्वजनिक-सेवा criteria के विरुद्ध
- ministerial_role / pm_role / cm_role — संबंधित प्रकाशित eligibility/role criteria के विरुद्ध
- institutional_role — संस्था-विशिष्ट criteria
- research_claim — किसी दावे का evidence audit
- custom — स्पष्ट user-defined purpose

पद का नाम अपने-आप assessment criteria नहीं है। Criteria पहले source-bound और version-locked होंगे।

## निरीक्षण pipeline
Purpose → Consent → Profile → Claims/Answers → Evidence → Multi-angle Analysis → Tests → Countercases → Verification → Human Review → Certificate/Report → Appeal → Audit Archive

## मुख्य parameters
भाषा/NLP: शब्दार्थ, संदर्भ, बहुअर्थी शब्द, contradiction, temporal consistency, translation cross-check, ambiguity.
Reasoning: premises, inference, counterexample, causality, quantitative/unit consistency, uncertainty, reproducibility.
Knowledge/capability: domain knowledge, practical tasks, scenario simulation, communication, source literacy, numerical reasoning, safety.
Vision/audio: OCR, document integrity, image quality, transcription, cross-modal consistency.
Multi-angle semantic analysis: literal, contextual, domain, temporal, comparative और translation views.
Accessibility: visual/audio interaction quality और assistive pathways.

## Optional biometric layer — privacy first
Finger-vein, fingerprint, iris/eye और liveness signals केवल स्पष्ट consent, lawful basis और supported device पर optional security/provenance inputs होंगे।

इन signals से truthfulness, intelligence, mental state, moral character, political preference, religion या human worth infer नहीं किया जाएगा। Raw biometric data public archive में default रूप से नहीं रखा जाएगा। जहाँ संभव हो on-device processing और minimal derived attestations होंगे।

Eye analysis interaction usability, document/visual consistency और accessibility तक सीमित रहेगा; eye movement से honesty या मानसिक स्थिति का निष्कर्ष नहीं निकलेगा।

## Certificate
Certificate record: purpose → criteria → evidence → tests → verification → reviewer → decision → validity → provenance.
Statuses: DRAFT | EVIDENCE_PENDING | ASSESSED | HUMAN_REVIEW | CERTIFIED | NOT_CERTIFIED | EXPIRED | DISPUTED.
AI-generated assessment official/legal certificate नहीं है जब तक अधिकृत संस्था वास्तव में certificate जारी न करे।

## Subscription
Subscription service access, storage, assessment credits, reports या optional features के लिए हो सकती है। Certificate खरीदना, score बदलना या eligibility bypass करना subscription से संभव नहीं होगा।

## Scale architecture
850 करोड़ संभावित users को capacity target मानकर stateless assessment services, regional language packs, queues, tenant isolation, rate limits, privacy deletion, audit logs और graceful degradation रखे जाएंगे। यह वर्तमान usage या guarantee नहीं है।

## Governance
Consent, purpose limitation, data minimization, encryption, retention/deletion, appeal, independent audit, role-specific legal criteria, no hidden scoring और no biometric-only decision अनिवार्य gates हैं।

## निष्पक्षता
किसी व्यक्ति, पद, धर्म, संस्था, विचारधारा, जाति, भाषा या सामाजिक स्थिति को पहले से योग्य/अयोग्य मानकर scoring नहीं होगी। Criteria assessment के बाद बदले जाने पर versioned audit record बनेगा।