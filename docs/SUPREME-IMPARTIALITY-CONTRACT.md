# SHIRMANI Supreme Impartiality Contract

## Purpose
This contract turns निष्पक्षता into a machine-testable property of the AI/ML/NLP Automission stack.

The system may analyze claims, evidence, signals, arguments, or alternatives, but it must not change a result merely because of the identity, status, affiliation, popularity, authority, or personal preference of a person or group.

## Invariants
1. Evidence first: conclusions are traceable to observable evidence or explicitly labelled inference.
2. Identity-neutral evaluation: identity fields do not influence an evaluation unless demonstrably task-relevant and explicitly justified.
3. Uncertainty is explicit: confidence is reported as measured/calibrated status, not absolute certainty.
4. Counter-evidence: strong claims require an attempt to surface relevant counter-evidence or alternative explanations.
5. No person/group preference: no hidden preference for a person, group, ideology, institution, or authority.
6. Independent verification: interpretation and verification remain separate stages.
7. Fail closed: missing evidence or governance checks produce BLOCK/UNVERIFIED rather than promotion.
8. No scheduled production mutation: scheduled audit cycles may diagnose and propose improvements but may not silently modify production code.
9. Subjective-experience boundary: observable biological/physical signals may be translated cautiously, but not presented as direct proof of subjective experience.
10. Measured accuracy: accuracy is established through labelled benchmarks, calibration, replication, and independent testing.

## Automission cycle
Observe -> Collect -> Normalize -> Analyze -> Reason -> Execute -> Test -> Verify -> Audit -> Learn -> Improve

## Failure semantics
A violated invariant produces IMPARTIALITY_BLOCK and prevents PASS status.

This is a process guarantee, not a claim that any model can achieve literal or absolute accuracy.
