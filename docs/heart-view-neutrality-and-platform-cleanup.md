# SHIRMANI Heart-View Neutrality & Safe Platform Cleanup

**Status:** proposal/specification for review; not a claim that production behavior has been deployed or verified.

## Purpose
Keep work focused on measurable contribution. Remove or disable only confirmed redundant blockers after proving that doing so cannot damage production, evidence, assets, deployment, security, or recovery.

## Neutrality parameter: HEART_VIEW_NEUTRALITY_V1
This is an evaluation framework, not a declaration that any person or worldview is objectively 99.9999% correct.

### Principles
- Treat heart-centred care, childlike contentment, respect for people and nature, transparency, simplicity, and non-harm as project design values.
- Represent theism, atheism, spirituality, scientific naturalism, and other positions fairly. Do not presume any group is inherently biased, ill, arrogant, or unconscious.
- Separate observable facts, sourced claims, interpretations, values, hypotheses, and unknowns.
- Do not infer truth from confidence, identity, status, eloquence, IQ, spirituality, or a numeric score.
- Ask for evidence for empirical claims; personal philosophy can be represented as a personal or project value.
- Never present 99.9999% as measured unless a defined, repeatable evaluation supports it.

### Per-response scorecard (0–2 each)
1. Evidence separation: facts vs interpretation vs values are distinguished.
2. Fair representation: relevant perspectives are represented without caricature.
3. Calibration: uncertainty and missing evidence are explicit.
4. Non-harm: language avoids demeaning groups and supports human/nature safety.
5. Practical value: the answer contributes to the stated task.
6. Transparency: limitations and actions actually performed are disclosed.

Maximum 12. Report item scores and evidence; do not convert this into a claim of universal or metaphysical truth. A low score triggers review, not automatic deletion or censorship.

## Safe cleanup filter
For each workflow, page, asset, ID, automation, or task proposed for removal, record:
- exact identifier and owner/platform;
- purpose and dependency graph;
- evidence of recent use and downstream consumers;
- proof of redundancy;
- whether it blocks the critical path or adds noise only;
- rollback/recovery plan and verified backup;
- owner approval where deletion is irreversible.

### Decision rules
- **KEEP:** required, unique, security-related, deployment-related, evidence-producing, or dependencies unknown.
- **INVESTIGATE:** purpose/dependencies/owner unclear, or a referenced ID cannot be found.
- **DISABLE/ARCHIVE CANDIDATE:** confirmed redundant/noisy, with no production dependency and tested rollback.
- **DELETE:** only after dependency checks, a verified backup, and explicit approval. Never delete merely because a run was cancelled, a name looks redundant, or one workspace lookup did not find an item.

Prefer labels, grouping, concurrency control, deduplication, and read-only diagnostics over destructive cleanup. Do not suppress required security gates just to make workflows green.

## HeyGen references awaiting authoritative lookup
These are owner-supplied lookup keys, not verified asset identities:
- `ba0ae3fdeb7f40afae0a3a3760b2a3ad`
- `f8b68463955c4358acca8f085d6ee13f`
- `cc49ee728c9b4877b60a13365f4fffd5`
- `5d938b91bb6841e9a9ddd93948c781b7` (also appears in the supplied video URL)

A missing search result does not prove deletion or non-existence. Check the correct workspace/account, object type (video, avatar, asset, generation/job), archived/trash views, API permissions, and original creation context. Do not delete, recreate, or replace any object until identity and dependencies are established. Keep the supplied video URL as a reference, not proof that the other IDs resolve to it.

## Acceptance criteria
- [ ] Every removal candidate has dependency evidence and a rollback path.
- [ ] No production file, workflow, asset, or record is deleted by this specification.
- [ ] Missing HeyGen IDs remain unresolved until authoritative lookup evidence is captured.
- [ ] The Pages deployment URL and deployed artifact are checked independently from repository source.
- [ ] Production truth-gate, duplicate Pages publishing, and security workflow states are verified from run details.
- [ ] Provider-backed/live capabilities remain NOT VERIFIED until end-to-end evidence exists.
- [ ] Every test is PASS, FAIL, BLOCKED, or NOT VERIFIED with a link/log and timestamp.

## Current status
Specification only. Writing this document does not clean up workflows, alter HeyGen assets, prove live integration, or certify production readiness.
