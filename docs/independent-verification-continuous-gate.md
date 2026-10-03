# SHIRMANI Independent Verification — Continuous Gate

## Current measurable state

The repository preserves the distinction between:

- source preservation;
- evidence-supported records;
- QC / automation execution;
- independent verification.

The current verification registry records **10 queued propositions and 0 independently verified records**. This is an intentional fail-closed state, not a missing success value.

## Continuous gate

`factory/independent_verification_gate.py` measures the registry every five minutes through GitHub Actions.

A record is never promoted to VERIFIED by workflow execution alone.

The gate reports:

- total registry records;
- records eligible for an independent review;
- independently verified records, if an actual qualifying decision exists;
- blocked/incomplete records;
- input SHA-256;
- timestamp and deterministic rule.

## Promotion requirement

A VERIFIED result requires an actual independent review decision with:

1. precise claim;
2. operational definition;
3. independent source or reproducible experiment;
4. evidence and counter-evidence review;
5. reviewer identity/role;
6. timestamp and provenance;
7. explicit verification decision.

## Target map

Current target: **100,200 independently verified records**.

`0 / 100,200 = 0%` is the current measured verification progress.

The system must not increase that percentage merely because an Actions run succeeds.

## Operating principle

**Observe → Measure → Review → Verify → QC → Publish → Audit**

If independent evidence is absent, the correct state remains **NOT_VERIFIED**.
