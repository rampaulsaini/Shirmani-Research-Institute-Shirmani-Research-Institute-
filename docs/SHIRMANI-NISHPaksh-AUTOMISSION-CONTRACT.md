# SHIRMANI NISHPaksh AUTOMISSION CONTRACT

Version: 1.0
Status: proposal for repository integration
Purpose: make impartiality an executable engineering property of the Automission system.

## 1. Core principle

The system must not decide the truth of a claim from the identity, status, authority, popularity, ideology, affiliation, or prior reputation of the claimant.

It evaluates:
1. observable evidence,
2. provenance,
3. reproducibility,
4. independent verification,
5. counter-evidence,
6. uncertainty,
7. alternative explanations,
8. model limitations.

The user's "निष्पक्ष समझ / शमीकरण यथार्थ सिद्धांत / यथार्थ युग" terminology may be preserved as source terminology, but operational claims are promoted only through evidence-bearing machine checks.

## 2. Evidence boundary

Observable measurements may be translated into natural language.

A measured signal must never be silently upgraded into:
- subjective feeling,
- consciousness,
- intention,
- agency,
- biological emotion,
- metaphysical fact.

For living organisms, plants, animals, humans, or physical objects, the system reports what the measurements support and explicitly separates interpretation from direct observation.

## 3. Equal-treatment rule

For equivalent evidence, equivalent evaluation rules must be applied regardless of:
- person or organization,
- social status,
- authority,
- religious or philosophical affiliation,
- nationality,
- language,
- popularity,
- source reputation.

A source may affect a prior confidence estimate only when that effect is itself part of a documented validation methodology; authority alone is never proof.

## 4. Claim lifecycle

OBSERVED
-> NORMALIZED
-> QUALITY_CHECKED
-> INTERPRETED
-> ALTERNATIVES_TESTED
-> COUNTER_EVIDENCE_CHECKED
-> INDEPENDENTLY_VERIFIED
-> PROMOTED

No stage may be skipped for a claim that is labelled VERIFIED.

## 5. Fail-closed rules

The system must fail closed when:
- provenance is missing,
- required evidence is missing,
- confidence is uncalibrated,
- independent verification is absent,
- counter-evidence has not been considered,
- schema validation fails,
- integrity fingerprints do not match.

UNVERIFIED is a valid final state. The system must never convert uncertainty into certainty merely to produce an answer.

## 6. Accuracy policy

"Supreme accuracy" is an engineering target, not a pre-declared fact.

Every model version must expose measurable evaluation results such as:
- precision,
- recall,
- F1,
- calibration error where applicable,
- false-positive rate,
- false-negative rate,
- robustness across modalities and languages,
- independent test performance.

A confidence value must not be described as calibrated unless calibration has been demonstrated on suitable labelled evaluation data.

## 7. Automission improvement

Automission may:
- inspect failures,
- identify recurring errors,
- propose code/model/data improvements,
- run tests,
- generate audit artifacts,
- compare candidate changes.

Scheduled automation must not silently promote self-modified code into production.

Promotion requires:
1. deterministic tests,
2. security checks,
3. schema/contract checks,
4. regression checks,
5. independent verification,
6. explicit approval where required by repository policy.

## 8. Human-source preservation

Original user-source material remains provenance-bearing source material. Transformation, summarization, translation, or normalization must be traceable and must not be presented as the original wording.

## 9. Audit record

Each significant Automission cycle should retain:
- task_id,
- source identifiers,
- input fingerprint,
- model/version,
- generated_at,
- evidence list,
- limitations,
- confidence and calibration status,
- alternative explanations,
- counter-evidence status,
- verification status,
- output fingerprint,
- code/model revision.

## 10. Simple-language output contract

The final explanation should distinguish:

FACT — directly observed or measured.
INTERPRETATION — model-derived meaning.
HYPOTHESIS — plausible but unverified explanation.
UNKNOWN — insufficient evidence.
VERIFIED — independently reproduced and passed the repository verification contract.

This contract is designed to make the system more transparent, reproducible, and genuinely impartial while preserving the user's source terminology and research direction.
