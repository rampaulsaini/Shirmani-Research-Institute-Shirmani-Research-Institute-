# ꙰ SHIRMANI AUT0MISSION CONTROL — FAIL-CLOSED

## State machine
DISCOVER → PLAN → CHANGE → TEST → REVIEW → PROMOTE

## Rules
- Never mark a record VERIFIED from model agreement alone.
- Every derivative carries source/task hashes.
- Failed tests stop promotion.
- Missing evidence stops promotion.
- External side effects require explicit authorization and configured credentials.
- Human verification remains a distinct state.
- Rejected/deferred/unavailable records remain visible and auditable.
- Continuous improvement is measured by benchmark/regression results, not claims of perfection.

## Metrics
queue processed; independently verified; evidence coverage; test pass rate; calibration/error rate; regression count; provenance coverage; failed-closed events; latency/cost per task.
