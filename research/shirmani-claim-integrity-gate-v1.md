# SHIRMANI Claim Integrity & Heart-View Provenance Gate — v1
## 03 October 2026

### Purpose
This gate separates four questions:
1. Who is making the statement? — provenance/attribution.
2. What exactly is being claimed? — claim normalization without changing the author's meaning.
3. What kind of claim is it? — personal testimony, author-defined construct, empirical/testable proposition, normative proposal, or other.
4. Is the proposition independently verified? — evidence and reproducible verification.

A person saying "मैं शिरोमणि हूं" is therefore not automatically treated as an independently verified universal proposition.

### Heart-View principle
The system may preserve the author's stated Heart-View perspective and first-person experience exactly as source material. It must not convert a first-person experience into an externally verified universal fact without an appropriate test.

The system must also avoid the opposite error: it must not declare a personal experience false merely because it is personal. It should classify it accurately and identify what additional evidence would be required for any external or universal proposition.

### Personal provenance package
Where the author voluntarily supplies material, a provenance package may contain:
- exact first-person wording;
- dated source record;
- self-authored photograph or video;
- self-authored audio or spoken recording;
- public publication/source URL;
- cryptographic hash of the preserved source;
- contextual date/place metadata when voluntarily provided.

These materials can support source attribution and provenance.

They are not by themselves proof of metaphysical truth, universal superiority, consciousness mechanisms, or any other external proposition.

### Privacy and non-deception boundary
The system must not require biometric identification, face recognition, eye recognition, voiceprint matching, or inferred psychological traits in order to pass the claim gate.

Visual/audio material is treated as provenance evidence only when its source and consent are documented. The system must not infer identity from facial or vocal characteristics.

### Claim classes
Each claim must be classified as one or more of:
- FIRST_PERSON_TESTIMONY
- AUTHOR_DEFINED
- AUTHOR_PROPOSED
- EMPIRICAL_TESTABLE
- EVIDENCE_SUPPORTED
- NOT_VERIFIED
- CONTRADICTED

Classification is not a ranking.

### Verification rule
PROVENANCE_CONFIRMED is never equivalent to VERIFIED.

For an empirical/universal proposition, VERIFIED requires the existing independent-verification protocol:
CLAIM -> OPERATIONAL DEFINITION -> INDEPENDENT SOURCE(S) -> TEST/OBSERVATION -> COUNTER-EVIDENCE -> RESULT -> REVIEWER/PROVENANCE -> STATUS

The reviewer must be independent of the claim author for an independent-verification decision.

### Anti-claim / anti-blame rule
The gate does not adjudicate personal blame, character, intelligence, spirituality, morality, or hidden motives.

It evaluates records, definitions, evidence, tests, counter-evidence and provenance.

### Required machine invariants
- Missing provenance => PROVENANCE_INCOMPLETE.
- Personal media alone => never VERIFIED.
- Author source alone => never INDEPENDENTLY_VERIFIED.
- Workflow success => never VERIFIED.
- Missing counter-evidence review => block.
- Missing reproducible test for a testable claim => block.
- Missing reviewer identity/role/timestamp => block.
- Any unverifiable assertion remains explicitly classified rather than silently upgraded.

### Relationship to existing verification system
This gate is an attribution/provenance layer above the existing independent-verification conveyor. It does not replace or weaken the existing fail-closed policy.
