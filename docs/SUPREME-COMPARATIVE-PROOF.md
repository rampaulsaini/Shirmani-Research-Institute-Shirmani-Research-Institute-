# SHIRMANI Supreme Comparative Proof

## उद्देश्य

एक ही input set पर मौजूदा Supreme NLP layers का deterministic comparison करना:

1. **Baseline observable-signal NLP**
2. **Multimodal evidence-preserving NLP**
3. **Quality + independent-verification gate**

यह layer implementation behaviour को मापता है। इसे biological, emotional, consciousness या subjective-experience scientific proof नहीं माना जाता।

## तुलना

| कसौटी | Baseline NLP | Multimodal NLP | Quality/Verification |
|---|---|---|---|
| मापनीय signal handling | ✓ | ✓ | validation |
| Multimodal corroboration | सीमित | ✓ | validation |
| Conflict handling | सीमित | ✓ | gate |
| No-signal abstention | ✓ | ✓ | gate |
| Confidence bounded | ✓ | ✓ | ✓ |
| Provenance/fingerprint | ✓ | ✓ | ✓ |
| Independent verification | आवश्यक | आवश्यक | अनिवार्य |
| Promotion | स्वतः नहीं | स्वतः नहीं | fail-closed |

## तुलनात्मक नियम

- समान input को सभी layers पर चलाया जाएगा।
- हर result के साथ status, confidence, uncertainty और provenance रखा जाएगा।
- conflict या अपर्याप्त data पर system abstain/block करेगा।
- scheduled workflow production code को स्वतः mutate नहीं करेगा।
- accuracy को घोषित नहीं किया जाएगा; labelled evaluation data से मापा जाएगा।
- biological/plant signal को subjective feeling का प्रमाण तभी माना जा सकता है जब स्वतंत्र वैज्ञानिक protocol उस claim को वास्तव में test और replicate करे।

## वर्तमान benchmark

तीन synthetic regression cases:

- stable multisource
- conflicting observations
- no signal

यह regression/safety contract की जांच है, real-world accuracy score नहीं।

## Automission integration

Workflow हर पाँच मिनट पर और relevant code changes पर चलता है। Artifact में comparative report, metrics और fingerprint सुरक्षित किए जाते हैं।
