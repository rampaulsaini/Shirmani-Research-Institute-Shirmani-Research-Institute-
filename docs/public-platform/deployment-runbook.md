# Public Platform Deployment Runbook

This runbook turns the repository-side readiness contract into an explicit deployment sequence. It does not declare the service LIVE by itself.

## 1. Build

From `server/`:

```bash
npm install
npm test
npm run check
```

Build the container:

```bash
docker build -t shirmani-social-api:local ./server
```

## 2. Provision

Provide a managed PostgreSQL database and an HTTPS-capable runtime. Configure secrets only through the deployment provider:

- `DATABASE_URL`
- `JWT_SECRET`
- `CORS_ORIGIN`
- `PORT`
- `PAYMENT_WEBHOOK_SECRET` only after a real payment provider integration is reviewed
- object/media storage credentials when media upload is enabled
- AI-provider credentials only for enabled providers

Never commit real secret values.

## 3. Database

Apply the baseline schema using a protected database connection:

```bash
psql "$DATABASE_URL" -f server/sql/schema.sql
```

Before a production release, test backup restoration against a disposable environment.

## 4. Smoke test

After deployment, check:

```bash
curl -i https://YOUR_API_HOST/health
curl -i https://YOUR_API_HOST/v1/platform/readiness
curl -i https://YOUR_API_HOST/v1/capabilities/status
```

A successful response proves endpoint reachability only. It does not prove global availability, payment readiness, or independent verification.

## 5. Security gate

Confirm:

- HTTPS and domain routing
- production CORS allow-list
- strong secret storage and rotation procedure
- PostgreSQL network restrictions and backups
- authentication and authorization tests
- rate limiting and abuse controls
- privacy export/deletion/correction flow
- moderation, reports, disputes and appeals
- audit logging and monitoring
- rollback procedure

## 6. Payments and media

Payment webhooks remain disabled until a provider is configured and signed-event verification is tested. Media records currently store metadata; binary object storage requires a separate provider and access-control policy.

## 7. Production LIVE status

Only an authorized maintainer may declare LIVE after the external deployment evidence is recorded. Repository CI success alone must never set LIVE.

## 8. Independent verification

Research verification remains separate. CI, deployment health, AI output, generated documents and author testimony are not independent verification. Claim status changes require the evidence contract and qualifying independent human review.
