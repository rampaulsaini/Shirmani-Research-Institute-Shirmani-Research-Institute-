# SHIRMANI Supreme Neutrality & Evidence Governance

यह layer Supreme NLP/Automission को निष्पक्ष, evidence-first, fail-closed और independently verifiable रखती है।

## मूल नियम

1. Observation और interpretation अलग हैं।
2. Inference को observation के रूप में प्रस्तुत नहीं किया जाएगा।
3. Hypothesis को fact के रूप में प्रस्तुत नहीं किया जाएगा।
4. Sensor/signal data से सीधे निजी अनुभूति, चेतना या भावना का तथ्यात्मक दावा नहीं बनाया जाएगा।
5. Signal को सरल मानव भाषा में बदला जा सकता है, लेकिन uncertainty और confidence संरक्षित रहेंगे।
6. सभी inputs पर समान governance rules लागू होंगे।
7. Independent verification के बिना record को VERIFIED नहीं बनाया जाएगा।
8. Scheduled Automission production code को स्वतः mutate नहीं करेगी।
9. Accuracy को घोषित नहीं किया जाएगा; benchmark, error rate, calibration और independent verification से मापा जाएगा।
10. अपर्याप्त evidence होने पर system UNKNOWN/UNVERIFIED लौटाएगा।

## Signal → NLP

Signal → Quality Check → Feature Extraction → Pattern → Interpretation → Confidence → Simple Language → Independent Verification

## उदाहरण

“मापित संकेत में X pattern दिखाई दिया। उपलब्ध evidence के आधार पर इसका Y pattern से संबंध हो सकता है। Confidence Z है। यह निजी भावना का प्रत्यक्ष प्रमाण नहीं है।”

## Fail-closed policy

यदि schema, evidence, confidence, provenance या independent verification में आवश्यक जानकारी अनुपस्थित है, system stronger claim नहीं बनाएगा।

## Source preservation

मूल user-source record को अलग provenance layer में immutable रखा जाएगा। Governance layer उसके शब्दों को silently rewrite नहीं करती; वह machine outputs पर evidentiary boundaries लागू करती है।
