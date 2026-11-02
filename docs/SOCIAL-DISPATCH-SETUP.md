# Social dispatch — safe setup and current truth

## Included
- Canonical directory of supplied social/store URLs; each is explicitly marked as link-only or not API-connected.
- Node.js webhook bridge that defaults to dry-run and selects only explicitly verified, dispatch-ready products.
- GitHub Actions workflow on manifest changes, manual trigger, and a five-minute schedule.
- Deterministic idempotency key per product/version.

## Not claimed
A saved URL is not an authenticated API connection. This code does not log into social accounts, obtain tokens, publish directly to every network, send WhatsApp messages, or prove an order/payment. The Make receiver and each platform's official API permissions must be configured and tested separately.

## Enable after testing
1. Repository Settings → Secrets and variables → Actions: add secret MAKE_WEBHOOK_URL.
2. Set repository variable DISPATCH_ENABLED to false while validating.
3. Configure Make to validate schema, allow-list destinations, record accepted/rejected events, and reject repeated idempotency keys.
4. Test using a private/non-public destination; confirm a repeated event is rejected.
5. Only after successful review set DISPATCH_ENABLED=true. Publishing must be authorized and opt-in.
6. Add official platform APIs separately with minimum permissions. Never put tokens in source files or logs.

## Product gate
A product is eligible only if dispatch is READY_FOR_DISPATCH and artifact_evidence is VERIFIED_IN_REPOSITORY. Existing PUBLIC, EXTERNAL_ROUTE, or unverified entries are not silently promoted.

## Payment gate
UPI IDs and PayPal contact details are payment instructions, not payment proof. Confirm payment from bank/provider records or a verified provider webhook before dispatching paid goods.
