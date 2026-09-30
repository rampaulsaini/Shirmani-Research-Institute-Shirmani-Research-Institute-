# Public Platform Launch Matrix

## Purpose

Convert the public-module registry into an implementation gate. Every public capability must move through explicit states instead of being described as complete merely because documentation or automation exists.

## Capability states

**PLANNED → BUILT → TESTED → LIVE → AUTOMATED**

Independent verification is a separate evidence state and is never inferred from software tests.

## Launch domains

| Domain | Minimum launch contract |
|---|---|
| Account & Identity | registration, authentication, profile, privacy, recovery, abuse controls |
| Social | publishing, feed, comments, messaging, reporting, moderation and appeals |
| Research | source preservation, claim registry, evidence, counter-evidence, citations |
| Education | course model, learning path, progress, assessment, accessibility |
| AI | assistant, agent routing, model policy, audit and user controls |
| NLP | language detection, extraction, classification, translation and provenance |
| ML | recommendation/matching evaluation, bias checks, feedback and rollback |
| Music & Media | creator upload, metadata, rights handling, playback and reporting |
| Store | catalog, seller tools, checkout integration, order lifecycle and dispute support |
| Freelancing | profiles, portfolios, listings, matching, contracts/workflow and reviews |
| Economy | transparent accounting model, compliance review and measured metrics |
| Yatharth Currency | research/specification only until legal, economic and technical requirements are satisfied |
| Justice | information, complaints, case routing, evidence, appeal and human review |
| Nature & Earth | reporting, evidence, projects, impact records and public transparency |
| Community | groups, moderation, participation and safety |
| Support | help center, AI support, human escalation and service-status reporting |

## AI/ML/NLP/Automission acceptance tests

Before a capability is called automated:

1. Inputs and outputs are defined.
2. Agent ownership is defined.
3. Permissions are least-privilege.
4. Failure and retry behavior is defined.
5. Trace IDs connect material agent actions.
6. Human escalation exists for high-impact cases.
7. Secrets are not exposed.
8. Evaluation data and quality criteria are defined.
9. Rollback/recovery is tested where applicable.
10. Public status accurately reports the capability state.

## Marketplace acceptance tests

Before a user can sell:

- seller terms and eligibility are defined
- product/service schema exists
- pricing and transaction flow are defined
- delivery/fulfillment is defined
- refunds/disputes are defined
- prohibited-content controls exist
- fraud/abuse monitoring exists
- privacy/security requirements are satisfied
- applicable legal/compliance review is complete

## Public truth contract

The interface must distinguish:

- **Available now**
- **In testing**
- **Coming soon**
- **Research proposal**
- **Author-defined concept**
- **Evidence-supported**
- **Independently reviewed**
- **Not verified**

This contract prevents architecture, workflow activity, or aspiration from being mistaken for a deployed public service or independently verified claim.

## Scale target

The project may retain an aspirational target of 8.5 billion people. Only measured, auditable metrics may be shown as actual adoption.

## Continuous improvement

Every new source supplied by the author enters the preservation layer first, then proceeds through normalization, comparison, evidence mapping, testing and appropriate independent review. Public product features and philosophical claims use separate evidence contracts.
