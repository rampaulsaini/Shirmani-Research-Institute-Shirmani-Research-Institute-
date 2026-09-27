# निष्पक्ष समझ निरीक्षण App — implementation contract

यह layer किसी व्यक्ति के बारे में अंतिम सत्य घोषित करने के बजाय एक traceable inspection protocol उपलब्ध कराती है।

## Required first question
हर run से पहले purpose तय होगा: स्वयं, शिक्षा, कार्य/पद, सार्वजनिक दायित्व, अनुसंधान या अन्य अधिकृत उद्देश्य। एक ही score को सभी contexts में reuse नहीं किया जाएगा।

## Evidence pipeline
Input → Normalize → Claims → Definitions → Sources → Evidence → Countercases → Formulation/Test → Verification → Uncertainty → Human Review → Process Certificate → Archive

## Multi-angle NLP
Literal meaning, context, ambiguity, claim/opinion/question classification, provenance, internal consistency, countercases, temporal scope, translation drift, uncertainty, conflicts and appeal/accessibility को अलग dimensions माना जाएगा।

## Sensor boundary
Fingerprint, vein और eye/liveness signals केवल consent-based authentication/liveness जैसे सीमित प्रयोजन के लिए हैं। वे सत्य, नैतिकता, चरित्र, intelligence, competence, mental state या human-ness के प्रमाण नहीं हैं। Raw biometric templates public records में नहीं जाएंगे।

## Certificate boundary
Certificate केवल PROCESS_ONLY होगा: protocol, timestamp, evidence references और verification state का रिकॉर्ड। UNIVERSAL personhood/value certificate नहीं।

## Scale architecture
850 करोड़ users जैसे लक्ष्य के लिए stateless clients, regional queues, idempotency keys, encrypted private evidence vaults, public provenance store, model/version registry, human-review queues, rate limits, accessibility, multilingual support, disaster recovery, independent audit logs और retention/deletion controls चाहिए।

## Fail closed
Missing → DEFERRED; UNVERIFIED → UNVERIFIED. Model confidence स्वतः evidence/verification में promote नहीं होगा।

## Subscription
Subscription service-access/retention/advanced-review सुविधा हो सकती है; outcome या evidence quality खरीदने का साधन नहीं।

## Governance
High-impact contexts में applicable law, institutional authority, due process, human review, accessibility, security, privacy, appeal और independent validation gates आवश्यक हैं।
