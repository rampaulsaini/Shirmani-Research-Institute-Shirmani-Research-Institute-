# Independent Verification System v2

## Objective
Move the research queue through a strict, auditable lifecycle:
**QUEUED → EVIDENCE COLLECTION → INDEPENDENT TEST → REPRODUCIBLE RESULT → COUNTER-EVIDENCE REVIEW → AUDIT → VERIFIED / NOT_VERIFIED / CONTRADICTED / INCONCLUSIVE**

The system is fail-closed. Automation can prepare evidence and execute tests, but automation success is never itself an independent verification decision.

## Verification packet

A claim may be promoted to VERIFIED only when the record contains:
1. Precise claim text.
2. Operational definition.
3. Independent source(s) or a reproducible experiment.
4. Test/observation procedure.
5. Reproducible result and relevant artifacts/hashes.
6. Counter-evidence review.
7. Explicit result.
8. Reviewer identity and role.
9. Review timestamp.
10. Explicit decision.

## Independence controls
- Author-authored material is provenance, not independent confirmation.
- A GitHub Actions green check is not proof.
- A generated report is evidence packaging, not a review decision.
- Source-backed does not automatically mean the complete claim is verified.
- Conflicting or insufficient evidence must remain visible.
- A claim must never become VERIFIED merely because all automated jobs passed.

## Continuous Automission

After each cycle:
1. Discover queued claims.
2. Normalize and assign stable IDs.
3. Collect independent evidence.
4. Generate a test plan.
5. Execute deterministic tests where possible.
6. Store outputs and SHA-256 hashes.
7. Search for counter-evidence.
8. Run independent review gates.
9. Promote only records satisfying every required field.
10. Audit the registry.
11. Re-queue failed/inconclusive claims with the blocking reason.
12. Repeat.

## Accuracy model

Do not use an unsupported universal 100% accuracy claim. Track measurable metrics instead:
- test pass rate
- reproducibility rate
- evidence coverage
- contradiction rate
- false-positive/false-negative rates where a labelled benchmark exists
- reviewer agreement
- regression rate
- provenance completeness

## Current state

The existing registry intentionally remains at 0% independently verified until actual independent review decisions exist. The purpose of v2 is to make that transition technically enforceable rather than to manufacture a verification result.