# Make Custom App — Module 1: Get Live Production State

Status: implementation specification; not yet installed in a Make account.

## Goal

Read the public production snapshot from the Shirmani Research Institute repository. This module is read-only. It must not dispatch products, publish social posts, create orders, claim sales, or record payments.

## Connection

- App name: Shirmani Research Institute
- API base URL: https://api.github.com
- Authentication: none for these public repository reads
- Repository: rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-

## Module 1 request

- Method: GET
- URL: /repos/rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-/contents/generated/live-production-state.json
- Headers:
  - Accept: application/vnd.github.raw+json
  - X-GitHub-Api-Version: 2022-11-28

Expected response: raw JSON from the repository's default branch.

## Module 2 request — independent verification

- Method: GET
- URL: /repos/rampaulsaini/Shirmani-Research-Institute-Shirmani-Research-Institute-/contents/generated/independent-verification-status.json
- Headers: same as Module 1.

## Required truth rules

1. Display the source timestamp (`generated_at`) and repository path.
2. Keep catalog materialization, dispatch, sales, payments, and independent verification as separate counters.
3. Never infer dispatch, sales, or payment from generated assets, workflow runs, listing drafts, clicks, or social engagement.
4. A verification record is VERIFIED only when the source registry and the required independent/human review evidence say so. Prepared review packets are not verified records.
5. If either request fails, JSON is invalid, or the source timestamp is stale, show UNKNOWN/STALE and do not reuse an old value as live.
6. This app is a read-only status viewer until separately approved and tested write-capable modules exist.

## Snapshot fields to expose

From `live-production-state.json`:
- `generated_at`
- `catalog_identities`
- `concrete_repository_assets`
- `dispatch_released`
- `sales_claimed`
- `payment_claimed`
- `independent_verification_claimed`
- `state`
- `qc_state`

From `independent-verification-status.json`:
- `generated_at`
- `queue_total`
- `prepared_review_records`
- `verified_records`
- `unverified_records`
- `verification_policy`
- `state`

## Acceptance test

- Both GET requests return HTTP 200.
- Both bodies parse as JSON.
- The UI shows each source timestamp.
- The UI shows zero dispatch/sales/payment when the source values are zero.
- The UI labels review preparation separately from independent verification.
- No external write action is present in this module.

## Not included

No Amazon, Flipkart, Meesho, Shopify, Instagram, YouTube, payment gateway, affiliate, advertising, grant, CSR, or customer messaging connection is activated by this read-only module. Each requires its own authorized connection, provider approval, and end-to-end test.
