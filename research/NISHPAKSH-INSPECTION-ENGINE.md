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
