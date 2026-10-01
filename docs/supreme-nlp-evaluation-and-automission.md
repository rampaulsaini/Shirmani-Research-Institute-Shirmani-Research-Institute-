# SHIRMANI Supreme NLP — Evaluation & Automission Gate

## उद्देश्य

Supreme NLP को केवल अधिक complex नहीं, बल्कि **मापनीय, reproducible, fail-closed और continuously auditable** बनाना।

## Evaluation contract

हर NLP record में अलग fields रहने चाहिए:

- measured signal
- model inference
- interpretation
- confidence
- evidence
- uncertainty
- provenance
- verification state

**Signal ≠ inference ≠ interpretation ≠ proof.**

किसी biological, plant, environmental या non-living signal को plain language में बदलना अनुमत है, लेकिन detected pattern को अपने-आप subjective feeling, consciousness या intention का प्रमाण नहीं बनाया जाएगा।

## Quality metrics

हर evaluation cycle कम-से-कम structural pass rate, confidence validity, provenance completeness, evidence-state completeness, uncertainty completeness, prohibited-claim detection और verification-state validity जाँचेगा।

**100% structural pass rate** केवल record-contract checks पास होने का अर्थ है; यह scientific truth या universal model accuracy का दावा नहीं है।

## Continuous loop

Observe → Collect → Normalize → Analyze → Reason → Translate → Test → Verify → Audit → Learn → Improve

Regression आने पर publication gate **FAIL/CLOSED** रहेगा।

## Five-minute Automission boundary

GitHub Actions का 5-minute schedule quality evaluation चला सकता है। यह अपने-आप किसी external model, sensor या production service को continuously available या fully accurate सिद्ध नहीं करता। बाहरी execution की उपलब्धता अलग evidence के रूप में दर्ज होगी।

## Maturity

Contract → Fixtures → Evaluation → Regression → Evidence → Independent Verification → Production Gate

यह layer मौजूदा Research Institute architecture को replace नहीं करती; यह उसके ऊपर measurable quality-control layer जोड़ती है।
