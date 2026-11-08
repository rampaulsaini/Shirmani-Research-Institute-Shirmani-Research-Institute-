# Free-first hosting policy

**Decision date:** 2026-11-08  
**Applies to:** Shirmani Research Institute public showroom, enquiry/API and data services  
**Budget rule:** ₹0 recurring platform spend until the platform records verified customer income and the owner explicitly approves a paid service.

## 1. Vercel retirement

Vercel is not an approved hosting, build, preview, deployment or status-check dependency for this platform.

- Do not connect this repository to a Vercel project.
- Do not create or retry Vercel deployments.
- Do not upgrade a Vercel plan or add a payment method for Vercel.
- Do not make Vercel a required GitHub status check.
- Treat any Vercel deployment/rate-limit status as external and non-blocking; do not represent it as a product-code failure.
- Historical references in generated research/archive records are provenance, not active deployment configuration, and should not be rewritten as if they never existed.

The inspected repository root contains no active `vercel.json` configuration. The existing `.github/workflows/github-pages.yml` is a route guard, and `.github/workflows/pages-deployed-root-smoke.yml` targets the GitHub Pages URL. The route-guard workflow explicitly says it does not deploy. The canonical publisher must be inspected independently before claiming a release.

**Important boundary:** this repository inspection cannot disconnect an external Vercel GitHub App installation or delete a Vercel account/project. Those account-level actions must be completed in the Vercel dashboard/GitHub App settings by the account owner. Until then, the repository policy is “no use”; an external status context may still appear.

## 2. Preferred ₹0 architecture

| Layer | Preferred option | Reason / boundary |
|---|---|---|
| Public showroom (now) | Existing GitHub Pages | Already configured in this public repository; supports static HTML/CSS/JS on GitHub Free. Keep current public URL unless a separately verified migration is needed. |
| Static-host fallback | Cloudflare Pages Free | Optional alternative, not an automatic migration. Free limits include 500 builds/month, 20,000 files/site and 25 MiB per file. |
| API / lightweight server logic | Cloudflare Workers Free | Up to 100,000 requests/day and 10 ms CPU per invocation on the Free plan. Suitable for lightweight enquiry APIs; not long-running background jobs. |
| Relational data | Cloudflare D1 Free | Up to 10 databases, 500 MB per database, 5 GB total, 5 million rows read/day and 100,000 rows written/day. Requests stop returning query results when daily limits are exhausted. |
| Postgres alternative | Neon Free | Use only if existing Node/Postgres application compatibility makes it the lower-risk option: 1 GB/project, 100 CU-hours/project/month, 5 GB public transfer/project/month; compute scales to zero after inactivity. |
| Supabase alternative | Supabase Free | Optional, not primary: 2 active projects, 500 MB database and projects may pause after a week of low activity. |
| Render | Not the default free production choice | Free web services spin down after 15 minutes idle and can take about a minute to wake; free Postgres expires after 30 days and has no backups. |

## 3. Migration safety gates

Do not rewrite the current Node API or move customer data solely to adopt a new provider. Before any migration:

1. Inventory the current API routes, runtime dependencies, secrets, database schema, scheduled jobs, uploads and webhook requirements.
2. Confirm the chosen free runtime supports every required dependency and execution pattern.
3. Create a schema/data export and verify a restore into a test database.
4. Implement consent, validation, rate limiting, CORS allow-list, abuse protection and secret handling.
5. Test health, readiness, authenticated/authorised writes, read-after-write, error paths and backup restore.
6. Run a public smoke test against the exact deployed URL.
7. Keep the previous service untouched until the replacement passes all checks; do not delete data or disable a working service during migration.

For this project, the least-change path is to keep the existing GitHub Pages showroom and assess Cloudflare Workers + D1 against the actual Node API before changing backend infrastructure. If Node/Postgres compatibility makes a rewrite unsafe, assess Neon Free as the Postgres option. A free tier is quota-limited and must never be described as unlimited or guaranteed 24/7.

## 4. Spend and truth controls

- No paid plan, paid add-on, custom domain purchase, or payment method is authorised by this policy.
- Do not silently switch to a paid tier or allow overage billing.
- Configure alerts/limits where available; stop or degrade safely when a free quota is exhausted.
- Keep data exports/backups independent of the hosting provider.
- Distinguish “configured”, “deployed”, “smoke-tested”, “durable”, and “verified” in every status report.
- Income remains ₹0 until a genuine provider-confirmed payment and the agreed customer acceptance evidence are both recorded.

## 5. Official plan references checked on 2026-11-08

- GitHub Pages availability on GitHub Free public repositories: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
- Cloudflare Workers limits: https://developers.cloudflare.com/workers/platform/limits/
- Cloudflare Pages limits: https://developers.cloudflare.com/pages/platform/limits/
- Cloudflare D1 pricing/quotas: https://developers.cloudflare.com/d1/platform/pricing/
- Neon Free plan quotas: https://neon.com/blog/neon-free-plan-1-gb-per-project
- Supabase Free plan and inactivity pause: https://supabase.com/docs/guides/platform/billing-on-supabase and https://supabase.com/kb/faqs/platform/free-project-pausing
- Render Free plan limitations: https://render.com/docs/free

**Decision:** Vercel is retired from active platform use. GitHub Pages remains the public static host. Cloudflare Workers + D1 is the first backend candidate to evaluate at ₹0; Neon Free is the Postgres fallback. No migration or deployment is claimed by this policy document.
