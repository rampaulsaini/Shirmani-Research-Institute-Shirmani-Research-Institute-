# Free-first hosting policy

**Decision date:** 2026-11-08  
**Budget rule:** ₹0 recurring platform spend until verified customer income exists and the owner explicitly approves any paid service.

## 1. Vercel retirement

Vercel is not an approved hosting, build, preview, deployment or required-check dependency for Shirmani.

- No Vercel project connection, deployment retry, paid upgrade or payment method.
- Do not make a Vercel check required for pull requests.
- Ignore Vercel deployment-rate-limit results as external integration noise, not product-code failures.
- Preserve historical/archive references as provenance; do not erase historical evidence.

Repository inspection found no active `vercel.json` in the root and no Vercel-specific workflow in the inspected Pages workflows. GitHub code search on the default branch found Vercel references in generated research/archive artifacts, not an active platform deployment configuration.

**External disconnect remains outstanding:** a Vercel bot posted a deployment-failure comment on PR #3670 with an upgrade link. Repository commits cannot uninstall an external GitHub App. The account owner must open GitHub Settings → Applications → Installed GitHub Apps, locate Vercel, and uninstall it for this account/repository (or remove this repository from its access). Also disconnect the Git repository from any Vercel project if one remains connected. No account-level uninstall is claimed here.

## 2. Preferred ₹0 architecture — Render + Neon + GitHub Pages

| Layer | Selected service | Current evidence / limit |
|---|---|---|
| Public static showroom | GitHub Pages | Existing Pages publisher workflow; static site stays separate from backend. |
| Node.js API | Render Free: `shirmani-social-api-node` | Account inspection: service exists, Node runtime, free plan, not suspended; latest retrieved deploy status was `live` for commit `c5d54496e4fb877ec0514d9afd9de19bffe47c14` (2026-11-06). This is deployment evidence, not a current health/readiness smoke test. |
| PostgreSQL | Neon Free: `shirmani-income-db-lifetime` | Account inspection: Free subscription, project exists in Singapore region, default branch `main` is ready; reported logical size about 31 MB. The inspected branch currently exposes only `public.yatharth_accounts`; it is not yet proven to contain the complete application schema/data. |
| Legacy/temporary database | Render Free Postgres: `shirmani-income-db` | Account inspection: available, but expiration is 2026-12-02. Do not treat it as permanent storage. Read-only table inspection was blocked because its IP allowlist does not permit the connector. |

### Render Free is not lifetime always-on hosting

Render's official Free plan documentation states:
- Free web services spin down after 15 minutes without inbound traffic and take about a minute to wake.
- 750 free instance-hours are shared per workspace per calendar month.
- Free Postgres is limited to 1 GB, expires 30 days after creation, and has no backups.
- If no payment method is present, included-usage exhaustion suspends services or pauses new builds rather than silently billing; if a payment method is present, excess bandwidth/build usage can incur charges.

Therefore: keep the existing Render Node API as the current low-cost runtime while it remains useful, but do not promise uninterrupted 24/7 availability. Do not use Render Free Postgres as the long-term income database.

### Neon Free is the preferred durable Postgres candidate

Neon's current official Free plan is $0/month and has no published fixed expiry date, but it is not an unconditional lifetime guarantee or unlimited production plan. Current published limits include:
- 100 projects;
- 10 branches per project;
- 100 CU-hours per project per month;
- 1 GB Postgres storage per project (20 GB account-wide);
- 5 GB public network transfer per project per month;
- compute scales to zero after 5 minutes of inactivity; Free cannot disable this.
- Free-plan quota exhaustion suspends compute until the monthly reset or an upgrade; no overage billing is applied on the Free plan.

**Interpretation:** Neon is the best current ₹0 Postgres choice for the platform, subject to its quotas and terms. “Lifetime free” cannot be guaranteed by us; the provider can change plan terms. Do not add paid billing or upgrade automatically.

## 3. Migration order — do not switch the production database yet

The current Neon project is real and ready, but its inspected branch lists only `public.yatharth_accounts`. The Render Postgres database expires on 2026-12-02, but its contents could not be inspected because of its IP allowlist. The app's `server/sql/schema.sql` and migration files define a broader application schema.

Before changing Render's `DATABASE_URL` to Neon:

1. Restore read-only access to the current Render database using a permitted owner-controlled route; do not expose credentials in chat or Git.
2. Inventory all tables, indexes, constraints, migrations, row counts and critical records.
3. Create a secure database export and verify that it can be restored.
4. Apply the reviewed application schema/migrations to Neon without overwriting its existing `yatharth_accounts` data.
5. Import the verified Render data and compare table counts and critical records.
6. Test API health, readiness, authentication, enquiry writes, read-after-write, payment webhook signature checks, and backup/restore.
7. Only after a verified cutover, update Render's secret `DATABASE_URL` to Neon and run an end-to-end smoke test.
8. Keep the old Render database untouched until backup and cutover are verified; note its 2026-12-02 expiry and export before that date.

Do not print, commit, or send database connection strings, JWT secrets, webhook secrets, or passwords. No migration, secret change or deployment was performed by this policy update.

## 4. Spend and truth controls

- Keep all active services on explicitly selected Free plans.
- Do not add a payment method or enable automatic paid upgrades without separate approval.
- Monitor quota usage; when a Free quota is exhausted, degrade safely and report it.
- Keep independent exports/backups; a provider's free tier is not a backup guarantee.
- Distinguish configured, deployed, smoke-tested, durable and verified.
- Income remains ₹0 until authentic payment-provider confirmation and customer acceptance evidence are both recorded.

## 5. Official plan references checked 2026-11-08

- GitHub Pages: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
- Render Free limits: https://render.com/docs/free
- Render billing/usage FAQ: https://render.com/docs/faq
- Neon Free plan: https://neon.com/blog/neon-free-plan-1-gb-per-project
- Neon plan details: https://github.com/neondatabase/website/blob/main/content/docs/introduction/plans.md

**Decision:** Vercel is retired from active platform use. GitHub Pages remains the static showroom. Render Free remains the current Node API runtime with cold-start/quota limits. Neon Free is the preferred PostgreSQL destination after a verified schema-and-data migration. No paid service, migration, deployment, or live health claim is made by this document.
