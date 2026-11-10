# Payment proof format — SRI first pilot

This document is an internal review checklist. A screenshot or customer message alone is **not** verified income.

## 1. Payment reference

- Service: `SRI-SVC-001 — Hindi/English Writing & Research`
- Agreed amount: INR ______
- Currency: INR
- Customer / enquiry reference: ______
- Payment channel: UPI / PayPal
- Payment date and time (IST): ______
- UPI UTR / transaction ID or PayPal transaction ID: ______
- Recipient shown inside the payment app: ______

## 2. Evidence supplied by the customer

Attach privately to the relevant enquiry/order record:

- UPI or PayPal transaction screenshot showing amount, date, status and transaction reference.
- Transaction ID / UTR copied as text.
- Corresponding bank SMS or bank-app transaction entry showing the debit.

Before sharing, redact unrelated transactions, full account numbers, balances, addresses and other private data. Never request or store a UPI PIN, OTP, password, card CVV or bank login. Do not upload unredacted bank evidence to a public GitHub issue, commit, repository or public ledger.

## 3. Human verification checklist

A designated owner/reviewer must:

1. Open the recipient's own bank / UPI / PayPal account independently; do not rely only on a forwarded screenshot or SMS.
2. Match the recipient account, amount, currency, date/time and transaction ID / UTR against the actual credited transaction.
3. Confirm the transaction is successful, not pending, reversed, refunded or duplicated.
4. Record reviewer identity, review time, evidence reference and outcome in the private payment record.
5. Keep the enquiry, accepted written proposal, payment and delivery/acceptance as separate states.

## 4. Status rules

- `PENDING_PROOF`: customer has supplied evidence; not yet checked.
- `REJECTED_OR_UNMATCHED`: mismatch, pending, failed, reversed, refunded or unverifiable.
- `VERIFIED_PAYMENT`: actual credit independently matched in the recipient account by the authorized reviewer.
- `DELIVERED`: agreed deliverable handed over.
- `CUSTOMER_ACCEPTED`: customer confirms receipt / acceptance.

**Income VERIFIED** may be counted only after the real credit is matched and recorded by an authorized human reviewer. Payment verification does not itself prove delivery or customer acceptance. Do not mark a payment verified from a GitHub Actions run, enquiry submission, customer screenshot alone, or an unverified webhook.

## 5. Privacy and retention

Keep evidence in access-controlled private storage with the minimum necessary access and retention period. The public showroom may show aggregate verified totals only; never publish customer names, phone numbers, email addresses, bank SMS, screenshots or transaction IDs.
