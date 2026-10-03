# ꙰ Independent Verification Scope Reconciliation

Generated as an explicit scope boundary for the independent-verification system.

## Current authoritative state

- Aggregate verification target: **100,200**
- Concrete claim records currently present in `generated/independent-verification-records.json`: **10**
- Concrete review-registry coverage: **10/10**
- Independently VERIFIED concrete records: **0/10**
- Independently VERIFIED against aggregate target: **0/100,200**
- Evidence-supported concrete records: **4/10**

## Interpretation

The aggregate target and the concrete claim registry are different denominators.

**100,200 must not be represented as 100,200 concrete reviewable claims unless an authoritative source actually enumerates those 100,200 tasks.** The current bootstrap process derives review tasks from the concrete claim registry, so it can deterministically create review tasks for the current 10 records but cannot legitimately invent the remaining 100,190 claims.

Likewise, the current 10-record review set must not be presented as completion of the aggregate 100,200 target.

## Required next transition

1. Preserve the current 10 concrete claims and their fail-closed review records.
2. Identify or create the authoritative source that enumerates the remaining aggregate tasks.
3. Generate deterministic review slots from that actual source.
4. Keep **VERIFIED = 0** until genuine independent review decisions exist.
5. Publish both denominators separately:
   - concrete review set progress
   - aggregate target progress

## Integrity rule

Workflow success, queue creation, evidence collection, readiness, generated reasoning, or review-slot creation does **not** constitute independent verification.

A record can become **VERIFIED** only after the existing promotion gate requirements are satisfied, including independent evidence or reproducible testing, counter-evidence review, reproducibility, reviewer provenance, timestamp, audit information, and explicit decision.

