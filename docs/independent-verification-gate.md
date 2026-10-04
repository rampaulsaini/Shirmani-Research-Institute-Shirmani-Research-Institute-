# SHIRMANI Independent Verification Gate

## Purpose

Convert the repository's existing integrity boundary into an executable, fail-closed verification gate.

## State rule

Automation activity, workflow success, QC PASS, benchmark PASS and operational health do not equal independent verification.

A record may enter **VERIFIED** only when its evidence explicitly identifies an independent verifier and an independently reproducible verification result.

## Verification states

REGISTERED → UNVERIFIED → REVIEW → VERIFIED

BLOCKED is terminal until the blocker is resolved.

## Required independent-verification fields

- record_id
- subject
- evidence_hash
- verifier_id
- verifier_scope
- verification_method
- verification_timestamp
- reproducibility_reference
- verdict

## Fail-closed rule

Missing verifier identity/scope, method, evidence hash, reproducibility reference or explicit PASS verdict keeps the record UNVERIFIED or BLOCKED.

The gate never converts scheduled workflow runs into VERIFIED records.

## Target

The repository may track a target such as 100,200 VERIFIED records, but the target counter must remain zero until qualifying independent evidence exists.
