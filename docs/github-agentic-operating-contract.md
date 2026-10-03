# GitHub Agentic Operating Contract

## Purpose
Connect the repository's existing Automission architecture with GitHub's agentic development surfaces without confusing software automation with independent research verification.

## Control map

| Surface | Role | Boundary |
|---|---|---|
| Copilot cloud agent | Research, planning, implementation, PR creation | Changes remain reviewable PRs |
| Copilot code review | Review code changes | Review is not scientific verification |
| Repository instructions | Persistent project rules | Must preserve evidence-first contract |
| MCP | Context/tools for agents | Least privilege; read-only by default |
| GitHub Actions | Deterministic execution | Workflow success is operational evidence |
| repository_dispatch / webhooks | Event ingress | Validate payloads; no secrets in payload |
| Environments | Protected execution/promotion boundary | Human/protection rules remain external configuration |
| Codespaces | Reproducible development workspace | Not a production runtime |
| Cloud agent environment | Ephemeral build/test environment | Treat outputs as review artifacts |

## Canonical lifecycle

`Issue/Plan → Agent Research → Agent Implementation → PR → Automated Tests → Copilot Code Review → Human Review → Merge → Actions → Evidence/Telemetry`

For research outputs:

`Source → Claim → Evidence → Independent Verification → QC → Publication`

These two lifecycles must not be conflated.

## MCP policy

Repository MCP configuration is a GitHub settings capability, not a substitute for source files. When enabled:
- allowlist the minimum tools;
- prefer read-only tools for Copilot code review;
- never place API credentials in the repository;
- review third-party MCP servers before enabling them;
- record configuration/provenance separately from research evidence.

## Webhook/event policy

Use `repository_dispatch` or configured webhooks only for explicit event ingress. Validate event type and payload before work begins. Events may request work; they do not authorize unsafe production mutation or convert unverified research into verified results.

## Verification gate

The following state transitions are mandatory:

`REGISTERED → EVIDENCE_PENDING → VERIFIED → QC → PUBLISHED`

No automation run may skip `VERIFIED` for claims requiring independent verification.

## Success metrics

Track separately:
- workflow runs;
- successful/failed runs;
- generated artifacts;
- reproducible test results;
- code-review findings;
- independent verification records;
- published records.

Do not combine these counts into one unsupported accuracy percentage.
