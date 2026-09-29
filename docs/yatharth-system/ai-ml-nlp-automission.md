# AI / ML / NLP / Automission Layer

## उद्देश्य
AI को सत्य का निर्णायक नहीं, बल्कि research infrastructure का सहायक बनाया जाए।

## NLP pipeline
1. Source ingestion
2. sentence / proposition segmentation
3. claim candidate extraction
4. terminology normalization
5. entity / concept linking
6. duplicate and contradiction detection
7. evidence-source retrieval
8. comparison candidate generation
9. reviewer packet generation
10. provenance and hash attachment

## ML / reasoning layer
मॉडल निम्न कार्य कर सकते हैं:
- semantic clustering
- claim similarity
- source classification
- contradiction candidate detection
- missing-evidence detection
- uncertainty tagging
- comparison suggestions
- regression checks on research schemas

मॉडल का generated conclusion independent verification नहीं माना जाएगा।

## Automission layers
### L1 — Intake Agent
नए source को सुरक्षित archive में दर्ज करे।

### L2 — Claim Agent
स्थिर claim IDs बनाए या existing IDs से जोड़े।

### L3 — Evidence Agent
विश्वसनीय स्रोत और counter-evidence candidates खोजे।

### L4 — Comparison Agent
दस्तावेजित दर्शन, विज्ञान और अन्य frameworks से neutral comparison बनाए।

### L5 — Audit Agent
provenance, schema, hashes, links और status transitions जाँचे।

### L6 — Verification Gate
देखे कि independent reviewer evidence contract पूरा हुआ या नहीं।

### L7 — Federation Agent
अन्य repositories / creative systems से machine-readable tasks और receipts का आदान-प्रदान करे।

### L8 — Public Presentation Agent
verified, evidence-supported, author-source और unresolved सामग्री को स्पष्ट रूप से अलग करके public pages बनाए।

## सुरक्षा नियम
- secrets कभी source, issue, log या generated page में नहीं।
- external person पर आरोप को independent fact की तरह publish नहीं करना।
- private identity/health-bearing records को public research layer में अनावश्यक रूप से नहीं डालना।
- generated text को source wording का replacement नहीं बनाना।
- हर transformation traceable होना चाहिए।

## Acceptance principle
Automation accelerates research; it does not manufacture verification.
