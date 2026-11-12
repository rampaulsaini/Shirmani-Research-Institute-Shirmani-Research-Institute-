# Supreme NLP — Independent Scientific Validation Protocol v3

यह protocol measurable signals से language/NLP interpretation को scientifically testable बनाता है। मूल Heart-View/Yatharth framework की भाषा और propositions preservation layer में रह सकती हैं; यह protocol empirical proposition के लिए data क्या दिखाता है, उसे अलग से test करता है।

## तीन स्तर

1. Observation — sensor/measurement से वास्तव में क्या दर्ज हुआ।
2. Interpretation / hypothesis — उस pattern का संभावित अर्थ।
3. Verification — independent test में hypothesis कितनी बार और किन controls के साथ पुनरुत्पादित हुई।

इन स्तरों को merge नहीं किया जाएगा।

## जीव और वनस्पति

Plant research में electrical, chemical, hydraulic, calcium और ROS-related signalling जैसे measurable mechanisms documented हैं। इसलिए system इन signals को collect, align, classify और plain-language में describe कर सकता है। Signal का अस्तित्व अपने-आप subjective feeling, consciousness, intention या किसी विशिष्ट inner experience को सिद्ध नहीं करता।

## Experimental design

जहाँ लागू हो:
- pre-registered hypothesis और primary endpoint
- sensor calibration और timestamp synchronization
- randomized stimulus/control assignment
- sham/negative controls
- blinded acquisition और/or analysis
- multiple biological samples
- repeated trials
- independent replication by a separate source/lab
- fixed analysis plan + versioned code
- raw data, metadata, exclusions और preprocessing provenance
- effect size + uncertainty interval
- calibration metrics for probabilistic models
- adversarial/null tests
- reproducible artifact

## Promotion rule

OBSERVED → INTERPRETED → REVIEWED → INDEPENDENT_REPLICATION → VERIFIED

MODEL_CONFIDENCE कभी VERIFIED का substitute नहीं है।

## NLP contract

हर output में observed measurements, derived features, interpretation, uncertainty, provenance, confidence/calibration और verification state अलग fields में रहें।

Evidence insufficient होने पर model ABSTAIN / INSUFFICIENT_DATA करे; fluent prose evidence नहीं है।

## Automission

हर 5-minute cycle:
ingest → schema validation → deterministic baseline → optional ML/NLP → calibration → contradiction/null tests → independent-verification queue → audit → status publication

Automission preparation और testing कर सकता है; unverified proposition को silently verified नहीं बना सकता।
