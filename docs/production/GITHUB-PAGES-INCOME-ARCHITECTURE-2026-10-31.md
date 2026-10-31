# Shirmani Research Institute — GitHub Pages Income Architecture

Date: 2026-10-31
Status: architecture decision and deployment checklist; not evidence of a live API, customer, payment, or automated production worker.

## Decision

The public website is hosted on GitHub Pages. GitHub Pages serves static HTML, CSS, JavaScript, and assets; it does not run the repository's Express/Node.js API process or host PostgreSQL. Keep the existing Pages site as the public storefront and deploy the existing `server/` application to a separate Node.js-capable hosting provider. Use a separately managed PostgreSQL database.

Do not put database credentials, JWT secrets, payment secrets, or private customer data in the Pages repository's public client-side code.

## Existing repository evidence

- `server/package.json` defines an Express API with `npm start`, `npm run check`, and `npm test`.
- `server/src/index.js` includes a `/health` route, registration/login routes, profile/feed endpoints, and capability status.
- Production startup explicitly requires `CORS_ORIGIN`, `JWT_SECRET`, and `DATABASE_URL`.
- `server/.env.example` is a configuration template, not evidence that production secrets or a deployment exist.
- `server/sql/schema.sql` includes account/profile, listings, transactions, and order tables. The schema comment explicitly leaves payment-provider integration deployment-gated.
- The current Writing & Research enquiry page links to WhatsApp. A click-through is not a server-side enquiry record or a verified customer lead.
- `income/runtime-state.json` currently records `observed_state: CONTROL_PLANE_READY`, no heartbeat, no active workers, zero verified opportunities, and zero verified income.

## Required production topology

1. **GitHub Pages:** static public showroom, service descriptions, samples, and enquiry entry point.
2. **Node.js API host:** deploy only the existing `server/` application; expose HTTPS; configure a health check at `/health`.
3. **Managed PostgreSQL:** create a private database and apply `server/sql/schema.sql`.
4. **Secrets:** configure `DATABASE_URL`, a long random `JWT_SECRET`, `NODE_ENV=production`, and the exact Pages origin in `CORS_ORIGIN` using the hosting provider's secret manager. Never commit real values.
5. **Enquiry workflow:** add a validated, rate-limited server-side enquiry endpoint and persistent enquiry table; connect the static enquiry page to the deployed API only after the API URL and CORS origin are verified.
6. **Human-reviewed sales workflow:** record enquiry, qualification, written scope/quote, payment receipt verification, delivery manifest, and customer acceptance as separate states.
7. **Payment integration:** select a compliant payment provider only after the API is deployed; verify payment through provider callbacks/webhooks and reconcile with the provider dashboard. Never mark an order paid from a browser redirect or client-side claim.
8. **Production telemetry:** emit real timestamped heartbeats and cycle outcomes from an actually running worker. Keep desired state separate from observed state. Do not display a 24/7 claim until monitoring proves uptime.

## Release gates

- [ ] Node.js host and deployment URL selected.
- [ ] PostgreSQL provisioned; schema applied successfully.
- [ ] Secrets configured outside Git; exact Pages origin configured for CORS.
- [ ] Deployed `GET /health` returns HTTP 200 with database READY and auth CONFIGURED.
- [ ] Registration/login smoke tests pass against the deployed API.
- [ ] Enquiry endpoint persists a test enquiry and rejects malformed or abusive requests.
- [ ] Public Pages form successfully submits to the API; no secrets are exposed in browser assets.
- [ ] Payment provider webhook signature verification and test-mode reconciliation pass before accepting real payments.
- [ ] Delivery and acceptance evidence can be exported without exposing private customer data.
- [ ] Monitoring demonstrates actual worker heartbeats before any continuous-operation claim.

## Income-first execution order

1. Preserve existing static tools and samples; do not rebuild the catalogue.
2. Deploy the API and database foundations.
3. Make one Writing & Research service enquiry persist reliably.
4. Manually qualify the first real enquiry and send a written, scope-limited quote.
5. Verify payment in the provider account before starting paid work.
6. Deliver one clearly scoped product and record acceptance.
7. Only then automate follow-ups and production cycles with human approval and auditable records.

## Current truth boundary

As of this document's creation, this repository inspection does not establish a selected API host, provisioned production database, deployed API URL, persisted customer enquiry, payment-provider integration, verified payment, or continuously running production worker. The current verified-income figure remains the value reported by the runtime state: zero. This document records the architecture and gates; it does not claim that any gate has passed.
