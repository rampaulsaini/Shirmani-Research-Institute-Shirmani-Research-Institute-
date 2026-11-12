# SHIRMANI Research Institute — Copilot Operating Instructions

## Mission
Work on this repository as an evidence-first research/automation platform. Preserve existing author-source records and public content. Improve software, automation, reproducibility, observability, and verification without turning workflow success into scientific proof.

## Required architecture
Follow:
`input → normalize → claims → sources → evidence → formulation/test → independent verification → QC → publication → archive`

For automation:
`observe → collect → normalize → analyze → reason → execute → test → verify → audit → learn → improve`

## Non-negotiable integrity rules
- Do not fabricate sources, evidence, measurements, verification, agent execution, income, corpus coverage, or completion states.
- `PASS`, `READY`, workflow success, benchmark execution, or QC success are operational states, not independent scientific verification.
- Keep measured signal, model inference, interpretation, confidence, uncertainty, provenance, and verification state separate.
- Unverified claims remain `UNVERIFIED`/blocked from promotion.
- Scheduled production-code mutation is disabled unless an explicit human-authorized workflow permits it.
- High-impact actions require human review and an auditable trail.
- Preserve historical failure records.
- Never silently rewrite or normalize immutable user-source records.

## Repository orientation
- `PROJECT-CONTINUITY.md` is the continuity contract.
- `README.md` documents the public architecture and integrity boundaries.
- `factory/` contains deterministic orchestration and QC.
- `agents/` contains agent contracts and interpretation layers.
- `schemas/` contains machine-readable contracts.
- `generated/` contains derived telemetry/artifacts, never authoritative source truth.
- `.github/workflows/` contains scheduled/event-driven automation.
- `docs/` contains operating contracts and architecture.
- `tests/` contains deterministic hardening tests.

## Change discipline
1. Read `PROJECT-CONTINUITY.md` and the relevant contract before changing code.
2. Prefer small, reviewable pull requests.
3. Run the narrowest relevant deterministic tests first, then broader validation.
4. Validate generated JSON against its schema where a schema exists.
5. Include provenance for generated artifacts.
6. Fail closed when required evidence/contracts are missing.
7. Do not add credentials or secrets to source control.
8. Do not claim that GitHub Copilot, MCP, web access, Codespaces, or a cloud agent is active merely because configuration files exist; verify the actual capability/status.

## GitHub agentic ecosystem
The repository may use GitHub Copilot cloud agent, Copilot code review, repository instructions, MCP tools, GitHub Actions, repository_dispatch events, environments, Codespaces, and external webhooks. Treat these as separate control surfaces:
- Copilot/cloud agent: planning and implementation through reviewed pull requests.
- Code review: review evidence and regression/security findings; do not treat approval as scientific verification.
- MCP: expose only the minimum required tools; prefer read-only tools for review.
- Actions: deterministic execution and telemetry.
- repository_dispatch/webhooks: event ingress; validate payloads and keep credentials out of payloads.
- Environments: use protected deployment/verification boundaries where available.
- Codespaces: reproducible development environment, not a production runtime.

## Completion criterion
A task is not complete merely because code was generated. Completion requires:
`implemented → tested → reviewed → evidenced → traceable`
and, for research claims:
`independent evidence → independent verification → QC → eligible publication`.
