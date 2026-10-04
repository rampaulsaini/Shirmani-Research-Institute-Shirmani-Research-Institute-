# ꙰ SHIRMANI Independent Review Intake — v1

## Purpose

This intake converts the existing concrete verification queue into explicit independent-review work without manufacturing VERIFIED decisions.

## Current scale

- Authoritative target: **100,200 VERIFIED records**
- Concrete claim records currently instantiated: **10**
- Concrete review slots: **10**
- Independently VERIFIED: **0**
- Review-slot coverage: **100% of the instantiated 10-record layer**
- VERIFIED completion against the 100,200 target: **0%**

These are intentionally separate scales.

## Fail-closed rule

Workflow success, queue generation, evidence collection, packet generation, QC success, or AI/model agreement is **not** an independent verification decision.

A record may be promoted to VERIFIED only when the registry contains, at minimum:

1. A precise operational claim/test definition.
2. Independent evidence or a reproducible independent test/observation.
3. Reproducible result and artifacts.
4. Explicit counter-evidence review.
5. Reviewer identity and role.
6. Review timestamp.
7. Immutable task/audit hash.
8. Explicit independent reviewer decision.

## Current review slots

| Claim | Review ID | Current state |
|---|---|---|
| IV-001 | REVIEW-IV-001-independent-review-v1 | PENDING_REVIEW |
| IV-002 | REVIEW-IV-002-independent-review-v1 | PENDING_REVIEW |
| IV-003 | REVIEW-IV-003-independent-review-v1 | PENDING_REVIEW |
| IV-004 | REVIEW-IV-004-independent-review-v1 | PENDING_REVIEW |
| IV-005 | REVIEW-IV-005-independent-review-v1 | PENDING_REVIEW |
| IV-006 | REVIEW-IV-006-independent-review-v1 | PENDING_REVIEW |
| IV-007 | REVIEW-IV-007-independent-review-v1 | PENDING_REVIEW |
| IV-008 | REVIEW-IV-008-independent-review-v1 | PENDING_REVIEW |
| IV-009 | REVIEW-IV-009-independent-review-v1 | PENDING_REVIEW |
| IV-010 | REVIEW-IV-010-independent-review-v1 | PENDING_REVIEW |

## Operational path

Source → Claim → Evidence → Independent Test → Reproducible Result → Counter-Evidence → Audit → Independent Decision → VERIFIED

Automation may prepare, validate, measure, and audit this path. It must not impersonate the independent reviewer.

## Next measurable milestone

The first milestone is not more workflow runs. It is:

**1 independently completed review → 1 independently VERIFIED record, if and only if the fail-closed gate passes.**

Then the same controlled process can scale toward the 100,200-record target.
