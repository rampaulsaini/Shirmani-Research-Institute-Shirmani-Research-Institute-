# Social Auto-Dispatch — safe setup

## What this change does
- Reads the canonical `showroom-products.json` manifest; it does not hard-code a product count.
- Runs validation on manifest changes, manual runs, and a five-minute scheduled check.
- Defaults to dry-run. A scheduled run does **not** publish content unless live dispatch is explicitly enabled.
- Sends one selected product to the configured Make.com HTTPS webhook. A stable idempotency key lets the receiving scenario suppress duplicate requests.
- Reports webhook acceptance separately from actual publication on Facebook, Instagram, LinkedIn, X, Pinterest, WhatsApp, YouTube, or Blogger.

## Enable safely
1. Create a Make.com scenario with a Custom Webhook trigger.
2. In GitHub repository Settings → Secrets and variables → Actions, add secret `MAKE_WEBHOOK_URL`.
3. Add repository variable `DISPATCH_ENABLED` with value `true` only after testing the scenario.
4. Keep the Make.com scenario idempotent: persist `idempotency_key` and reject duplicate keys before any external post.
5. For a manual test, run **Supreme Social Dispatch Gateway** with an exact `product_id`. The selected manifest record must explicitly set `dispatch_ready: true`.
6. Begin with platform-specific test destinations. Enable each platform only after its official API authorization, account/page permissions, content format, and publication response are confirmed.

## Important boundaries
- Never put access tokens, passwords, payment secrets, or personal credentials in source files or logs. Use GitHub Actions secrets.
- A Facebook share URL or profile URL is not a Page access token. WhatsApp Channel and group links do not grant WhatsApp Business API access. YouTube channels do not automatically authorize uploads. API access and permissions must be granted by the account owner on each official platform.
- This gateway currently integrates with the Make.com webhook only. It does not claim direct posting to all social networks, Take App order notifications, payment confirmation, or verified income.
- The workflow runs every five minutes for validation/eligible queue checks; it does not repeatedly blast the same item to every network. The receiving webhook must enforce idempotency and per-platform rate limits.
- Existing manifest records are not automatically marked dispatch-ready. This prevents accidental publication of unreviewed catalogue entries.

## Evidence required for a successful end-to-end test
Record separately: webhook accepted; platform API accepted; public post URL returned; public post independently checked; customer enquiry received; order agreed; payment provider confirmed payment; delivery evidence recorded. A workflow green check alone is not proof of any later stage.
