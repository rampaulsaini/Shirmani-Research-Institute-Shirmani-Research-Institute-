# Governance State Model

The control plane uses explicit state transitions so that automation cannot silently convert a proposal into an authoritative public decision.

## Proposal lifecycle

`DRAFT → EVIDENCE_MAPPED → IMPACT_REVIEW → HUMAN_DECISION → REVIEW_WINDOW → IMPLEMENTED → AUDITED`

Possible exits:
- `REJECTED`
- `RETURNED_FOR_REVISION`
- `APPEALED`
- `SUSPENDED`

## Decision contract

A high-impact decision record should contain:

- unique decision ID;
- jurisdiction;
- policy/rule ID and version;
- proposer;
- decision authority;
- affected population/category;
- evidence references;
- counter-evidence references;
- impact assessment;
- effective date;
- expiry/review date;
- appeal path;
- audit event ID.

## Automation restrictions

Automission may:
- validate schema;
- check policy prerequisites;
- detect missing evidence;
- route work;
- run simulations;
- calculate disclosed metrics;
- generate drafts;
- monitor service health;
- open alerts.

Automission may not:
- appoint itself as authority;
- suppress appeals;
- alter evidence history;
- declare a contested research claim independently VERIFIED;
- create legal currency;
- impose irreversible high-impact action without the required human/legal authorization.

## Emergency mode

Emergency mode must include:
- reason;
- start time;
- explicit scope;
- authorized actor;
- automatic expiry;
- review checkpoint;
- full audit trail.

An emergency flag must never become permanent by omission.
