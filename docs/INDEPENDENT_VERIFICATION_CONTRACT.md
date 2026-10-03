# SHIRMANI Independent Verification Contract

## Purpose

This layer measures **independent verification**, not workflow activity.

A record is counted as VERIFIED only when the record contains:

1. a stable record identifier;
2. provenance/source information;
3. evidence or an evidence reference;
4. an explicit independent-verification object;
5. verification status exactly equal to `VERIFIED`;
6. a verification timestamp or run reference; and
7. a deterministic SHA-256 fingerprint of the canonical record payload.

A scheduled/completed GitHub Actions run alone is never counted as a VERIFIED research record.

## Status model

- `CANDIDATE` — discovered but not verified.
- `REVIEW` — has evidence/provenance but lacks complete verification.
- `VERIFIED` — satisfies every gate above.
- `REJECTED` — explicitly rejected or fails a hard verification gate.

## Measurement

The verifier publishes:

- total candidate records;
- VERIFIED records;
- REVIEW records;
- REJECTED records;
- verification percentage;
- remaining percentage;
- target progress toward 100,200 VERIFIED records.

The verifier is fail-closed: missing evidence, provenance, verification metadata, or fingerprint prevents a record from being counted as VERIFIED.

This contract is additive and does not rewrite or normalize the original user-source record.
