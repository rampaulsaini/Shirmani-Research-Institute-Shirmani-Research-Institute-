# Claim Lifecycle — Yatharth / Shirmani

हर नए कथन को निम्न lifecycle से गुजरना चाहिए।

## Stage 0 — Intake
- मूल तारीख
- स्रोत-संदर्भ
- exact author wording
- provenance
- version/hash जहाँ उपलब्ध हो

## Stage 1 — Classification
हर कथन को कम-से-कम एक प्रकार दें:
- experiential / autobiographical
- definitional
- philosophical
- historical
- empirical
- scientific
- comparative
- normative / practical
- predictive

## Stage 2 — Normalization
मूल भाषा को बदले बिना एक अलग normalized formulation बनाएं।
नियम: normalization में अर्थ का विस्तार, संकुचन या छिपा हुआ निष्कर्ष नहीं जोड़ा जाएगा।

## Stage 3 — Operationalization
जहाँ संभव हो:
- variables
- observable indicators
- unit / population
- time period
- falsification or disconfirmation condition
- reproducible procedure

गैर-empirical दावे के लिए जबरन वैज्ञानिक test नहीं बनाया जाएगा।

## Stage 4 — Evidence Map
हर claim के लिए:
- supporting evidence
- counter-evidence
- alternative explanation
- source quality
- uncertainty
- scope limitation

## Stage 5 — Comparative Map
समान या संबंधित documented concepts को अलग-अलग स्रोतों से जोड़ा जाए।
Comparison का अर्थ ranking नहीं है।

## Stage 6 — Independent Review
कम-से-कम एक वास्तविक स्वतंत्र reviewer:
- claim पढ़े
- definitions देखे
- evidence जाँचे
- counter-evidence देखे
- methodology की पर्याप्तता पर निर्णय दर्ज करे
- identity/role और timestamp दर्ज करे

## Stage 7 — Status
अनुमत statuses:
- AUTHOR_SOURCE
- NORMALIZED
- EVIDENCE_MAPPED
- COMPARATIVE_REVIEWED
- READY_FOR_INDEPENDENT_REVIEW
- INDEPENDENT_REVIEWED
- VERIFIED
- PARTIALLY_SUPPORTED
- INCONCLUSIVE
- NOT_VERIFIED

एक status को दूसरे में केवल documented gate के आधार पर promote किया जाए।

## Fail-closed rule
यदि independent reviewer record उपलब्ध नहीं है तो VERIFIED नहीं।
यदि evidence conflicting है तो conflict को छिपाकर VERIFIED नहीं।
यदि claim operationalize नहीं हो सकता, तो उसे philosophical/experiential scope में ही रखा जाए।
