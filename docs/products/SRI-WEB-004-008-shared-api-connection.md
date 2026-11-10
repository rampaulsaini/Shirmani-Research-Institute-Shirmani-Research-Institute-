# SRI-WEB-004–008 Shared API Connection

## Purpose
The five browser-local tools now share a small connection client for checking the existing Shirmani API. The client targets the already-existing Render API service; this change does not create a service, alter secrets, run a deployment, or migrate a database.

## Connection boundary
- API base: https://shirmani-research-institute-shirmani.onrender.com
- Health check: GET /health
- Health checks send no app records, credentials, or customer data.
- SRI-WEB-004 Lead Desk alone exposes an explicit, per-lead submission to POST /v1/enquiries.
- A lead is eligible for submission only when the operator separately checks the cloud-submission consent box and the record contains an email or phone number. The operator must then press "Send to server".
- The existing contact-permission field remains separate from cloud-submission consent. WhatsApp draft remains gated by contact permission.
- A successful server response is stored locally as a sync reference to reduce accidental duplicate submissions.

## Data intentionally kept local
SRI-WEB-005 stock/cost/pricing records, SRI-WEB-006 content drafts, SRI-WEB-007 income/expense entries, and SRI-WEB-008 resume details remain in browser storage. The shared API status panel does not upload or synchronize those records. This avoids sending financial, business, or personal information to a server without a separate authenticated account, retention/deletion controls, and explicit opt-in design.

## What this does not mean
- A health response is not proof that the API is configured for every browser origin or that database writes succeed.
- The Lead Desk submission has not yet been browser-tested against the live service.
- No payment provider, WhatsApp API, social publishing account, reminder scheduler, cloud backup, or customer account has been connected by this change.
- A server enquiry is not an order, payment, delivery, or recognized income.

## Verification required before release
1. Complete GitHub checks, including public local-link integrity.
2. Browser-test health status from the published GitHub Pages origin.
3. Submit a synthetic lead with test contact data and explicit cloud consent; verify the row is owner-only in the database, then remove the test record using the approved retention process.
4. Verify no lead data is sent when cloud consent is absent.
5. Test mobile layout and keyboard/screen-reader operation.
6. Keep deployment gated; no Render deployment is part of this PR.
