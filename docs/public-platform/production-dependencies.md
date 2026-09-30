# Production Dependencies and Launch Gates

GitHub Pages can host the public interface and static prototype, but a global multi-user platform requires additional production services.

## Required production layers
1. Identity/authentication — secure signup, login, recovery, sessions and abuse controls.
2. Database — shared durable storage, backups, migrations, access control and audit logs.
3. Object/media storage — images, audio, video and documents with scanning and lifecycle controls.
4. API/backend — authorization, publishing, search, marketplace, education, AI orchestration and moderation.
5. Payments/payouts — regulated provider, seller onboarding, refunds, receipts, taxes and payout controls.
6. Search/discovery — multilingual indexing, retrieval and transparent ranking policies.
7. AI/ML/NLP runtime — model serving, queues, rate limits, evaluations, cost controls and human escalation.
8. Trust & safety — reporting, moderation, appeals, fraud detection and high-impact human review.
9. Observability — uptime, errors, security events, workflow health and auditable receipts.
10. Automission federation — schedules, cross-repository dispatch, retry/recovery and fail-closed gates.

## Launch gates
BUILT → TESTED requires automated tests. TESTED → LIVE requires deployment, security/privacy review, monitoring and a demonstrated real user workflow. LIVE → AUTONOMOUS requires additional safety, rollback and human-oversight gates.

## Secret boundary
Repository credentials belong only in GitHub repository secrets or a secure secret manager. Never place tokens in source files, issues, pull requests, logs or chat.

## Economic boundary
A prototype listing or currency design is not a payment, sale, income result or deployed currency. Those states require real transaction evidence and applicable legal, security and deployment controls.
