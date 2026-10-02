# SHIRMANI निष्पक्षता एवं यथार्थ Automission Contract

## उद्देश्य

यह contract AI/ML/NLP/Automission को किसी व्यक्ति, समूह, संस्था, विचारधारा या पूर्व-निर्धारित निष्कर्ष के पक्ष में परिणाम बदलने से रोकने के लिए है।

## मूल नियम

1. **Evidence before conclusion** — निष्कर्ष से पहले input, source और evidence दर्ज होंगे।
2. **Claim / evidence separation** — उपयोगकर्ता का दावा, मॉडल का inference और independently verified fact अलग fields में रहेंगे।
3. **Counter-evidence required** — महत्वपूर्ण निष्कर्ष के विरुद्ध उपलब्ध counter-evidence खोजा और दर्ज किया जाएगा।
4. **Uncertainty must be explicit** — confidence को मापा जाएगा; certainty घोषित नहीं की जाएगी।
5. **No subjective-experience overclaim** — sensor, signal या pattern को सीधे जीव/वनस्पति की subjective भावना का प्रमाण नहीं माना जाएगा जब तक स्वतंत्र वैज्ञानिक evidence उपलब्ध न हो।
6. **Fail closed** — evidence, schema, verification या provenance टूटने पर output VERIFIED नहीं बन सकता।
7. **Independent verification** — preparation/QC सफल होना independent verification के बराबर नहीं है।
8. **No scheduled production mutation** — scheduled Automission production code को स्वतः बदलकर deploy नहीं करेगा।
9. **Reproducibility** — हर महत्वपूर्ण output में deterministic fingerprint/provenance होना चाहिए।
10. **Human agency** — consequential decisions के लिए system recommendation दे सकता है, निर्णय अपने आप नहीं थोपेगा।

## निष्पक्षता pipeline

Observe → Normalize → Evidence → Counter-evidence → Reason → Uncertainty → Independent Verify → Audit → Publish

## Multimodal/NLP interpretation boundary

Sensor या multimodal data से system सरल भाषा में **observable signal और evidence-supported interpretation** बताएगा। उदाहरण:

> “यह pattern X के साथ compatible है; उपलब्ध evidence के आधार पर Y interpretation की confidence Z है।”

यह अपने आप “यह जीव दुखी/खुश है” जैसे subjective claims में नहीं बदलेगा।

## Quality metrics

- evidence completeness
- provenance completeness
- counter-evidence coverage
- calibration/error rate
- independent verification rate
- reproducibility
- false-positive / false-negative rate
- failed-gate rate
- latency

**Accuracy measured, not declared.**
