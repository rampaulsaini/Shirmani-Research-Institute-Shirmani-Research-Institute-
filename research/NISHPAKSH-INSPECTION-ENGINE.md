# निष्पक्ष समझ निरीक्षण इंजन — विस्तृत उत्पाद/स्वचालन अनुबंध

## 1. पहला प्रश्न: निरीक्षण किस चीज़ के लिए है?
हर session में purpose पहले चुना जाएगा, फिर उसी purpose के लिए न्यूनतम आवश्यक evidence और parameters तय होंगे:
- खुद का निष्पक्ष स्व-निरीक्षण
- “इंसान” होने के व्यक्तिगत/दार्शनिक self-reflection — **कानूनी या वैज्ञानिक सार्वभौमिक प्रमाण नहीं**
- शिक्षा/ज्ञान/कौशल
- रोजगार/किसी पद की competency
- मंत्री/PM/CM/न्यायिक/राष्ट्राध्यक्ष जैसे सार्वजनिक पद की **role-relevant competency**
- research/custom purpose

किसी व्यक्ति की मानव गरिमा या मानव-अधिकार को app score से निर्धारित नहीं किया जाएगा। सार्वजनिक पद के लिए assessment केवल प्रकाशित, वैध, role-specific criteria और उपलब्ध evidence तक सीमित रहेगा।

## 2. सदस्यता और session gate
**Purpose → Eligibility → Consent → Subscription → Evidence plan → Baseline → Analysis → Counter-evidence → Human review → Explainable report → Certificate**

Subscription केवल service access है; payment से assessment outcome प्रभावित नहीं होगा। Free/Trial/Active/Expired/Paused state स्पष्ट रहेगी।

## 3. निष्पक्ष निरीक्षण के मुख्य आयाम
### व्यक्ति/स्व-निरीक्षण
self-observation, attention, comprehension, reasoning, logical consistency, uncertainty handling, evidence-vs-experience separation, self-correction, communication, empathy/non-harm.

### शिक्षा/ज्ञान
conceptual knowledge, numeracy, source use, problem solving, reproducibility, domain-specific practical tasks.

### पद/भूमिका
role duties, applicable rules/law, decision transparency, evidence handling, conflict-of-interest disclosure, accountability, communication, crisis reasoning, resource stewardship, public-impact analysis. पद के नाम से अतिरिक्त गुण स्वतः नहीं मान लिए जाएंगे।

### प्रकृति/पृथ्वी/मानव सभ्यता
environmental impact, long-term risk recognition, resource stewardship, social-impact analysis, harm minimization, intergenerational considerations. इन्हें भी evidence-based और purpose-relevant रखा जाएगा।

## 4. Multimodal analysis
- Text: multilingual NLP, semantic normalization, ambiguity detection, contradiction/consistency, claim extraction, source traceability.
- Voice/audio: speech-to-text, language/meaning analysis, optional acoustic quality features; accent/voice identity को competence का स्वतः प्रमाण नहीं माना जाएगा।
- Document: OCR, structure, provenance, tamper/quality indicators.
- Image/video: consent-based object/context analysis; identity inference और sensitive-trait inference default नहीं.
- Eye/finger-vein: केवल explicit opt-in, supported hardware, purpose limitation; raw biometric retention default नहीं, जहाँ संभव हो device-side feature extraction.
- Additional future modalities: typing dynamics, interaction patterns, accessibility signals — केवल necessity/proportionality review के बाद।

## 5. “शब्दों को multi-angle” समझने का engine
हर महत्वपूर्ण statement के लिए:
1. literal meaning
2. contextual meaning
3. temporal meaning
4. domain meaning
5. ambiguity alternatives
6. implied assumptions
7. evidence required
8. counter-interpretation
9. contradiction check
10. confidence/uncertainty

AI किसी अस्पष्ट वाक्य को मनमाने अर्थ में बदलकर verdict नहीं देगा।

## 6. Evidence graph
हर claim को:
**claim → source → timestamp/version → evidence type → counter-evidence → reviewer → status**
से बाँधा जाएगा।

Possible statuses: DRAFT, DATA_READY, ANALYZED, COUNTERCHECKED, HUMAN_REVIEW, CERTIFIED, INSUFFICIENT_EVIDENCE, NEEDS_MORE_DATA, REJECTED.

AI-generated result अपने-आप VERIFIED/CERTIFIED नहीं बनेगा।

## 7. निष्पक्षता और सुरक्षा
- protected/sensitive traits को scoring में स्वतः शामिल नहीं किया जाएगा।
- political persuasion, ideology, religion, caste, ethnicity, disability आदि को competence का hidden proxy नहीं बनाया जाएगा।
- conflict-of-interest को केवल घोषित, evidence-backed facts के आधार पर handle किया जाएगा।
- high-impact/public-office assessments में human review और appeal/contestation record अनिवार्य होगा।
- हर assessment का purpose, version, criteria, evidence scope और limitations certificate/report में दिखाई दें।

## 8. Certificate architecture
Certificate का अर्थ होगा:
**“इस घोषित purpose के लिए, इस version के criteria और इस उपलब्ध evidence के आधार पर यह assessment/report जारी हुई।”**

यह “पूर्ण सत्य”, “श्रेष्ठ व्यक्ति”, “अयोग्य मानव” या universal moral/scientific certificate नहीं होगा।

## 9. 850 करोड़-scale architecture
850 करोड़ users को **future target scale** माना जाएगा, current capacity नहीं। इसके लिए:
- tenant-isolated accounts
- regional deployment/data-residency controls
- encryption in transit/at rest
- key rotation
- rate limits/abuse controls
- audit logs
- consent/retention/deletion workflows
- model/version registry
- asynchronous queues
- horizontally scalable inference
- human-review queues
- disaster recovery
- independent security testing
- accessibility and low-bandwidth mode
- multilingual UI
- offline/device-assisted capture जहाँ lawful and appropriate

Scale बढ़ने पर safety gates हटाए नहीं जाएंगे।

## 10. आगे जोड़े जाने वाले parameters
self-reflection depth, epistemic humility, source reliability, numerical reasoning, causal reasoning, counterfactual reasoning, temporal consistency, calibration, decision reversibility, uncertainty communication, privacy awareness, cybersecurity hygiene, environmental externalities, accessibility, language fairness, model-bias checks, reviewer disagreement, appeal outcome, reproducibility, auditability.

## 11. Human agency
App व्यक्ति को सोचने, evidence देखने, counter-case देखने और correction/appeal का अवसर देगा। AI निर्णय-सहायक/विश्लेषक रहेगा; अंतिम high-impact certification में accountable human/audit gate रहेगा।


## 12. Purpose-first decision matrix — अनिवार्य प्रारम्भिक चयन
App का पहला स्क्रीन/चरण कोई score नहीं दिखाएगा। पहले उपयोगकर्ता से पूछा जाएगा:
**“आप निष्पक्ष निरीक्षण किस उद्देश्य से करना चाहते हैं?”**

| Purpose | क्या जाँचा जा सकता है | क्या नहीं निकाला जाएगा |
|---|---|---|
| खुद का निष्पक्ष निरीक्षण | self-observation, reasoning, evidence-vs-experience, consistency, uncertainty handling | मानव-मूल्य/गरिमा का universal score |
| शिक्षा | syllabus/domain knowledge, reasoning, practical tasks, source use | व्यक्ति की सम्पूर्ण बुद्धिमत्ता का दावा |
| रोजगार/पद | प्रकाशित job/role competencies, task simulation, communication, evidence handling | personality/biometric से hidden hiring score |
| मंत्री/PM/CM/राष्ट्राध्यक्ष | लागू कानून/संविधान/प्रकाशित eligibility और role-relevant competencies | राजनीतिक पसंद, ideology या भविष्य का चुनावी परिणाम |
| न्यायिक/संस्थागत भूमिका | प्रकाशित legal/professional criteria, reasoning, ethics rules, case-handling evidence | private sensitive traits से suitability inference |
| शोध-दावा | claim definition, evidence, counter-evidence, reproducibility, audit trail | AI output को स्वतः scientific proof |
| custom | user-defined, versioned criteria | अस्पष्ट/छिपे criteria |

**महत्वपूर्ण:** “खुद को इंसान सिद्ध करना” को app में self-reflection/identity-understanding purpose के रूप में लिया जा सकता है, लेकिन app किसी व्यक्ति की मानवता को कानूनी/वैज्ञानिक सार्वभौमिक certificate से तय नहीं करेगा। मानव गरिमा और मूल अधिकार assessment से सशर्त नहीं होंगे।

## 13. Parameter selection engine
Purpose चुने जाने के बाद केवल आवश्यक parameters सक्रिय होंगे:
**purpose → criteria version → minimum evidence → optional modules → tests → countertests → review level → report/certificate type.**
अनावश्यक biometric या sensitive data collection default रूप से बंद रहेगी।

## 14. Multi-angle word/meaning engine — विस्तार
हर statement को कम-से-कम इन कोणों से देखा जा सके:
literal, grammatical, contextual, temporal, speaker-intent-as-stated, domain, cultural/language variant, translation, ambiguity, presupposition, contradiction, evidence burden, counter-interpretation, causal claim, quantitative/unit consistency, source provenance, uncertainty.
यह engine “व्यक्ति क्या वास्तव में सोच रहा है” जैसी अदृश्य मानसिक अवस्था को certainty के साथ घोषित नहीं करेगा।

## 15. Biometric/visual safeguards
Finger-vein, fingerprint, iris/eye, face, voice और liveness को तीन अलग श्रेणियों में रखा जाएगा:
1. **Security/provenance** — access/identity continuity जहाँ वैध और आवश्यक हो।
2. **Capture quality** — image/scan/audio quality, liveness, document readability.
3. **Assessment evidence** — केवल validated, purpose-relevant measurements।
तीसरी श्रेणी में कोई modality तभी आएगी जब उसका वैज्ञानिक validation, documented limitations और lawful purpose उपलब्ध हो।
“आँख देखकर सच”, “finger-vein देखकर चरित्र”, “आवाज़ देखकर बुद्धिमत्ता” जैसे unsupported inference निषिद्ध होंगे।

## 16. Certificate levels
- **Participation/Session Report:** केवल session completion और collected evidence.
- **Assessment Report:** criteria + findings + uncertainty + evidence.
- **Verified Assessment:** independent verification और human/audit review के बाद.
- **Official Certificate:** केवल वास्तविक अधिकृत संस्था/authority द्वारा जारी होने पर।
किसी subscription से certificate outcome नहीं खरीदा जा सकेगा।

## 17. Appeal / correction
हर high-impact assessment में:
**view evidence → challenge finding → add evidence → request re-review → reviewer decision → immutable audit trail**
की प्रक्रिया होगी। पुराने result को चुपचाप overwrite नहीं किया जाएगा; नया version बनेगा।

## 18. Fairness test suite
हर model/version पर pre-release और periodic checks:
- language parity
- translation consistency
- false-positive/false-negative analysis
- accessibility
- calibration
- reviewer disagreement
- drift
- missing-data sensitivity
- counterfactual robustness
- biometric non-inference guard
- sensitive-trait leakage tests
- adversarial/prompt-injection tests.

## 19. Nature/Earth/civilization module
यदि user purpose में यह चुने, तो evidence-based dimensions हो सकते हैं:
environmental externalities, resource efficiency, long-term risk, public-impact analysis, biodiversity/ecosystem considerations, disaster resilience, intergenerational effects, reversibility of decisions.
यह किसी व्यक्ति को “प्रकृति का रक्षक” घोषित करने का universal moral score नहीं होगा; यह घोषित criteria पर evidence report होगा।

## 20. 850 करोड़ target — architecture rule
850 करोड़ को **design target / future scale scenario** माना जाएगा, वर्तमान user count नहीं।
Scale test में केवल throughput नहीं, बल्कि privacy, auditability, model consistency, disaster recovery, regional latency, deletion propagation, abuse resistance और human-review capacity भी शामिल होंगे।


## 21. v2 AI/ML/NLP Automission विस्तार
### Purpose-first router
Purpose selection is a hard gate. No score is produced before purpose, criteria version and evidence policy are fixed.

### Candidate parameter registry
Epistemic humility, experience-vs-fact separation, self-correction, uncertainty calibration, source reliability, causal and counterfactual reasoning, temporal consistency, decision reversibility, privacy awareness, cybersecurity hygiene, environmental externalities, accessibility, language fairness, model-bias checks, reviewer disagreement, appeal outcomes, reproducibility and auditability are available as purpose-bound parameters.

### Multimodal contract
Eye/finger-vein/fingerprint/iris/face/voice/liveness are not general truth detectors. They may be used only for lawful security/provenance or capture-quality purposes unless a separate validated measurement contract exists. Raw biometric retention is not the default.

### Automission contract
Agents can validate schemas, generate evidence/review packets, version criteria, route queues, run safety tests, detect stale evidence and archive receipts. Agents cannot self-certify, bypass consent, bypass human review or turn unsupported biometric inference into a decision.

### Subscription contract
Subscription changes access/credits/storage/features only. It cannot buy eligibility, alter assessment results or bypass verification.

### Public-office neutrality
Minister/PM/CM/judge/president flows are role-competency/evidence assessments against published, versioned criteria. The system must not infer political preference, ideology, religion, caste, ethnicity or electoral outcome.

### Scale
850 crore is a future architecture target, not a current capacity claim. Scale tests must include privacy, deletion propagation, regional latency, model drift, abuse resistance, disaster recovery and human-review throughput.
