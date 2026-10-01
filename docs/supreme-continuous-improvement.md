# SHIRMANI Supreme Continuous Improvement

## Objective
A continuously audited AI/ML/NLP/Automission layer for measurable quality improvement.

## Pipeline
Observe -> Collect -> Clean -> Analyze -> Reason -> Translate -> Verify -> Audit -> Improve.

## NLP boundary
The system may translate observable or encoded signals into human-readable language.
It must not silently convert signal patterns into proof of subjective experience.

## Quality dimensions
- accuracy on labelled evaluation data
- calibration and confidence
- evidence quality
- cross-modality agreement
- independent-source agreement
- drift detection
- reproducibility
- provenance
- regression safety
- security

## Automission rule
Scheduled audits may diagnose and propose improvements. Production code mutation remains blocked
unless an explicit reviewed change path and validation gates permit it.

## Verification rule
A passing workflow is not itself independent verification. Independent verification remains a
separate evidence boundary.

## Operational cadence
The GitHub Actions layer requests a five-minute audit cadence. GitHub-hosted schedules can be
delayed or throttled, so the cadence is an intended trigger frequency, not a guarantee of exact
five-minute execution.
