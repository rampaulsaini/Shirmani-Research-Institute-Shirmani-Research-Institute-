# Character Studio V1–V4 executable acceptance plan

Canonical contract: specs/shirmani-supreme/canonical-character-specification.md.

## What this change makes executable

- scripts/character_release_gate.py validates a real-run evidence packet, checks that V1–V4 use one immutable build, calculates nearest-rank p50/p95 from at least five latency samples, and fails closed on missing proof.
- tests/test_character_studio_v1_v4_acceptance.py runs deterministic V1 contract checks and tests release-gate positive/negative behavior.
- Example URLs in test fixtures are fake test data, not product evidence. Never submit them as a real release packet.

## Run local contract tests

    python -m unittest tests/test_character_studio_v1_v4_acceptance.py -v

Validate a real evidence packet collected separately from provider/runtime tests:

    python scripts/character_release_gate.py path/to/real-evidence-packet.json --write-report path/to/release-gate-report.json

Exit code 0 means only ELIGIBLE_FOR_HUMAN_REVIEW. Exit code 1 means BLOCKED. Invalid/missing JSON exits 2.

## Required real evidence

### V1 — Character Studio
- Run browser/unit checks against a recorded commit SHA.
- Attach Hindi and English prompt results, evidence-state checks, exact insufficient-evidence notice, and original-photo policy check.
- Static source inspection alone is not a browser behavior test.

### V2 — Authorized voice
- Record actual provider-side authorization evidence and a successful generated audio artifact.
- Include provider/reference (never credentials), response status, duration, and real artifact URL.
- A configured voice ID is not authorization proof.

### V3 — Original face and lip-sync
- Record the original source asset's actual SHA-256; do not invent a hash.
- Link the real rendered video and reviewer notes.
- Supply measured non-negative audio/video offsets in milliseconds, the declared threshold, and enough samples to reproduce the result.

### V4 — Live Q&A and audit
- Run Hindi and English questions through the complete connected pipeline on the same release candidate.
- Capture at least five measured end-to-end latency samples; the gate calculates nearest-rank p50/p95.
- Record passing timeout, rate-limit, network-disconnect, provider-outage, and insufficient-evidence tests.
- Redact secrets and avoid unnecessary personal data in logs.

## Evidence packet contract

Top-level keys: release_candidate and tiers.
The release candidate requires build_id, reviewed=true, and security_checks_passed=true.
Each tier requires status=PASS, the same build_id, and actual evidence_urls. V2–V4 additionally require the fields enforced by the release-gate script.

## Current status (not inferred from tests)

- V1 source/contract tests: added by this change; CI must run them against the actual branch before calling them passed.
- V2 voice authorization/audio: BLOCKED / NOT VERIFIED until provider-side proof and real audio exist.
- V3 original asset/render/lip-sync: BLOCKED / NOT VERIFIED until real asset identity, rendered video, and measurements exist.
- V4 live Q&A/latency/failure paths: BLOCKED / NOT VERIFIED until real end-to-end runs exist.
- Production release: BLOCKED until all four tiers pass on the same build and a human reviews the evidence.

This gate validates packet structure and consistency; it cannot independently verify an evidence URL or provider claim. Reviewers must inspect linked artifacts.
