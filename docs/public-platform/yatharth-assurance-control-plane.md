# Yatharth Assurance Control Plane

## Purpose

The Assurance Control Plane is the next layer above ordinary CI/QC and Automission execution.

Its job is not to generate more activity. Its job is to prevent the platform from confusing:

- documentation with implementation,
- workflow success with service availability,
- automation with truth,
- an author claim with independent verification,
- a recorded transaction with real income,
- an architectural capability with a live capability.

## Assurance chain

Source Registry → API Capability Surface → Evidence Rules → Consistency Checks → Assurance Report → Human Review where required

The control plane is intentionally read-only. It does not deploy, publish, verify research claims, mint currency, authorize payments, or make high-impact decisions.

## Gate rules

### 1. Registry integrity

Every declared domain must have exactly one declared capability state, and every state must belong to the registry's status model.

### 2. Operational-state parity

Capabilities declared at MVP or above must be represented by the public capability status endpoint. A missing operational representation is a gate failure rather than an assumption.

### 3. Verification boundary

INDEPENDENTLY_VERIFIED cannot be declared merely because tests, QC, generated artifacts, workflow runs, or Automission succeeded. Independent verification requires a separate evidence record and review process.

### 4. Production boundary

LIVE requires external deployment evidence. A workflow that only proves repository-side readiness cannot promote a capability to LIVE.

### 5. Automation boundary

AUTOMATED is meaningful only after the underlying capability is operational and its automation path is itself observable and auditable.

### 6. No silent promotion

The assurance script never upgrades a capability. It only detects contradictions and missing evidence.

## Failure semantics

A failure means the repository contains a contradiction that should be resolved before the affected state is treated as trustworthy.

A warning means the architecture is explicit but still requires external evidence or human review.

The report is evidence about the repository state at a point in time; it is not independent scientific verification.

## Automission relationship

Automission remains:

Observe → Understand → Plan → Execute → Validate → Record → Audit → Recover/Escalate → Learn

The Assurance Control Plane sits beside that lifecycle as a constraint layer. It should be able to say: execution succeeded, but the capability is still not LIVE/VERIFIED.

## Security posture

The assurance workflow requests read-only repository contents and uses workflow concurrency to prevent redundant overlapping checks. It performs no arbitrary remote execution and does not require production secrets.

GitHub's security guidance recommends least-privilege workflow permissions, immutable action references where third-party actions are used, and concurrency controls for workflows that must not overlap.

## Current interpretation

The existing public capability registry is the source of declared capability state. The assurance gate validates that declaration against the repository's API capability surface.

This is deliberately conservative: an absent deployment or independent-verification record remains absent rather than being inferred.
