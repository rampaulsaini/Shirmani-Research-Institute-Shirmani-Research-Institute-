# Public Platform Integration Runbook

## Current implementation

PR #491 contains:
- public platform hub
- local-first public platform MVP
- browser console prototype
- machine-readable capability registry
- multi-user API server scaffold
- PostgreSQL schema for accounts, profiles, posts, self-interviews and marketplace listings
- OpenAPI contract
- production dependency and launch gates

## To make the multi-user platform genuinely live

1. Deploy the API server from `server/` to a managed HTTPS runtime.
2. Provision PostgreSQL and apply `server/schema.sql`.
3. Set `DATABASE_URL`, `JWT_SECRET`, `CORS_ORIGIN`, and `PORT` as deployment secrets/environment variables.
4. Configure the public MVP's API URL to the deployed HTTPS API.
5. Run registration, login, feed and marketplace integration tests.
6. Add object/media storage before accepting user uploads.
7. Add payment/payout provider only after legal, tax, fraud, refund and webhook controls are implemented.
8. Add moderation, reporting, appeals, deletion/export and audit logging before broad public exposure.
9. Add AI/ML/NLP workers behind authenticated queues, rate limits, evaluation and human escalation.
10. Keep independent verification separate from automated QC and from successful API/workflow execution.

## Security rules

- Never commit credentials, tokens or passwords.
- Use HTTPS in production.
- Keep database credentials server-side only.
- Use short-lived credentials where appropriate and rotate secrets.
- Do not treat client-side localStorage as production authentication.
- Do not expose private user data through public endpoints.
- Validate authorization on every write.
- Log security-relevant events without storing unnecessary secrets.

## Truth/status rule

A code path is **BUILT** when implemented, **TESTED** after reproducible tests, and **LIVE** only after real deployment plus security/privacy/monitoring gates. **AUTONOMOUS** additionally requires rollback, safety and human-oversight controls.

A listing is not proof of payment, sale, delivery, employment, income or customer satisfaction. AI output is not independent verification.
