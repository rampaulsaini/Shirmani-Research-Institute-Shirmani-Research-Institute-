# Customer Experience, Community, Reminders and Rewards — Delivery Contract

Status: **UI preview and requirements defined; production activation pending**.

## Existing entry points
- `account-access.html` already provides a signup/login UI and fails closed when `SHIRMANI_AUTH_API_BASE` is not configured.
- `index.html` already links to account access and community/social sections.
- This change adds `customer-experience-hub.html` as a single customer-experience entry point. Its actions are explicitly local preview actions, not shared production records.

## Required production modules

### Identity and account
- Register/signup, login/logout, email verification, recovery, profile, session revocation and account deletion/export.
- Server-side password hashing; secure HTTP-only cookies or an equivalent reviewed session design; CSRF protection where applicable; rate limits and abuse controls.
- Never store credentials or session secrets in browser local storage.

### Community and social graph
- Authenticated, authorized, durable records for share events, reactions/likes, comments, reviews/ratings, follows and subscriptions.
- Stable IDs, actor/resource IDs, timestamps, idempotency, moderation status, report/block controls, spam limits and audit references.
- A share click is not proof that a recipient viewed content. A subscribe action requires clear consent and unsubscribe.

### Vision-aware reminders
- Save only user-provided goals/topics and explicit reminder preferences.
- Opt-in delivery, timezone, quiet hours, frequency caps, unsubscribe, deletion/export and delivery-failure status.
- Do not infer sensitive traits or send messages until a scheduler and delivery provider are configured.

### Watch time and rewards
- First proposed milestone: **100 eligible hours**.
- Browser tab-open time or a local timer is not eligible evidence. Server-side session/content events, foreground/activity rules, anti-fraud checks, deduplication and an auditable eligibility ledger are required.
- Publish reward value/type, eligibility, expiry, funding, redemption, dispute and tax/legal terms before launch. Do not promise a cash reward until the reward is funded and payout path is verified.
- Keep engagement healthy: prioritize user value and learning, not manipulative or compulsive time maximization.

## Launch gates
1. UI reviewed and accessible on mobile.
2. API contracts and database migrations implemented.
3. Authentication, authorization, rate limiting, moderation and privacy tests pass.
4. Scheduler and delivery provider tested in sandbox, including opt-out and quiet hours.
5. Watch-time event integrity and reward fraud controls tested; reward funding and redemption rules published.
6. End-to-end staging tests pass, deployment is verified, monitoring/backup/restore are evidenced.
7. Public counters distinguish UI preview interactions from authenticated unique users, persisted social events, eligible watch time, approved rewards, redemptions, inquiries, payments and accepted deliveries.

## Income-first rule
Do not let the customer-feature expansion delay the existing first-paid-service path. Keep service enquiry → human-reviewed quote → explicit acceptance → verified payment → accepted delivery as separate states. Do not record revenue from page views, signups, likes, subscriptions, catalogue entries or workflow counts.
