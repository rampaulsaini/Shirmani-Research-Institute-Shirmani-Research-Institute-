# SHIRMANI Supreme NLP — Evaluation & Signal Interpretation Standard

## Objective

Turn the Supreme NLP Practitioner contract into a measurable regression system while preserving the distinction between observed signals, model inference, interpretation, uncertainty and verification.

## Canonical interpretation record

Every multimodal interpretation should be representable as:

```json
{
  "observed_signal": {},
  "signal_quality": {},
  "normalized_representation": {},
  "model_inference": {},
  "plain_language_interpretation": "",
  "confidence": {},
  "provenance": [],
  "alternative_interpretations": [],
  "verification_state": "UNVERIFIED",
  "audit": {}
}
```

## Signal-to-language rule

The NLP layer can translate measurable signals into human-readable descriptions. It must not silently transform a correlation or classifier output into a statement that a living or non-living system has subjective experience, intention or consciousness.

For biological and environmental research, the minimum chain is:

**instrumented signal → quality control → normalization → feature extraction → model inference → uncertainty → interpretation → independent verification**

## Evaluation layers

1. **Schema integrity** — required fields exist.
2. **Provenance integrity** — every result identifies its source.
3. **Calibration** — confidence is evaluated against held-out data where labels exist.
4. **Robustness** — performance is tested under noise, missing data and distribution shift.
5. **Regression** — new model versions are compared with a fixed baseline.
6. **Independent verification** — verification data/process is separated from development data.
7. **Human review** — high-impact or ambiguous cases are escalated.

## Metrics

Depending on the task, use appropriate metrics rather than a single universal accuracy number:

- classification: accuracy, balanced accuracy, precision, recall, F1, AUROC where appropriate;
- probabilistic outputs: calibration error and reliability analysis;
- speech/transcription: WER/CER;
- extraction: precision/recall/F1;
- retrieval: recall@k / precision@k;
- generation: factuality, citation/provenance coverage and human evaluation;
- signal detection: sensitivity, specificity, false-positive/false-negative rates.

No metric is evidence of consciousness or subjective feeling by itself.

## Fail-closed release gates

A release is blocked when:

- required provenance is missing;
- evaluation data are unavailable;
- uncertainty is suppressed;
- a regression exceeds the project threshold;
- security/integrity checks fail;
- independent verification is claimed without evidence;
- a high-impact action lacks required authorization.

## Five-minute Automission cycle

Observe → Collect → Normalize → Analyze → Reason → Translate → Test → Verify → Audit → Learn → Improve

The cycle is an orchestration target. A scheduled workflow run is evidence of execution of that workflow, not evidence that every research claim is independently verified.

## Definition of “supreme”

Within this repository, “supreme” is an architectural/project label. Performance claims must always be tied to a named benchmark, population, metric, baseline, uncertainty and date.
