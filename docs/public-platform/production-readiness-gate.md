# Production Readiness Gate

This is the repository-side gate before a real deployment is declared.

## State discipline

BUILT means code exists. TESTED means reproducible checks pass. DEPLOYMENT READY means production infrastructure is configured and reachable. LIVE means the actual HTTPS service is deployed and serving users. AUTONOMOUS means routine operation is automated with rollback, observability, abuse controls and human oversight for high-impact decisions.

Passing GitHub Actions checks establishes only the tested repository state. Status checks report validation state; they do not prove an external service is globally deployed or that a philosophical or scientific claim is independently verified.

## Production configuration

The deployment environment must provide, as applicable:

- DATABASE_URL
- JWT_SECRET
- CORS_ORIGIN
- PORT
- PAYMENT_WEBHOOK_SECRET only after payment integration and compliance review
- media/object-storage credentials
- AI-provider credentials
- monitoring and alerting configuration

Secrets must remain in protected deployment or GitHub environment storage. Never commit or paste secrets into source, issues, pull requests, logs or chat.

## Infrastructure gate

Before LIVE status, verify HTTPS/domain routing, managed PostgreSQL backups and restore, media storage access controls, authentication and recovery, authorization, privacy export/deletion/correction, rate limiting, abuse prevention, moderation and appeals, payment/refund/payout controls where applicable, monitoring, incident response, rollback, retention and user-facing legal/privacy notices.

## Human-impact gate

Human review remains required for decisions that can materially affect account access or termination, financial settlement or payout, safety escalation, disputes or justice pathways, and independent research verification.

Automission may prepare, classify, route, retry and audit tasks, but high-impact or ambiguous decisions must escalate.

## Verification boundary

These do not constitute independent verification: successful CI runs, workflow completion, generated documents, hashes, API health, QC status, AI output, publication, website availability, or author testimony alone.

Independent verification requires the evidence contract defined by the Yatharth research system and appropriate independent human review.

## Deployment workflow

Use a protected GitHub environment such as production for actual deployment. GitHub environments can restrict deployment branches, protect secrets, and require approval before a deployment job proceeds.

No workflow should silently label a build LIVE merely because CI succeeded.

## Current status

Repository readiness gate: IMPLEMENTED.

Production LIVE: NOT ESTABLISHED by this repository-side gate.

Independent verification: SEPARATE evidence-and-human-review process.
