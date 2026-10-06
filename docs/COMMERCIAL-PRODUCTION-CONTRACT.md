# SHIRMANI Commercial Production — Order-to-Delivery Contract

## Purpose

Move the 1,016 concrete digital-product assets from **READY_FOR_ORDER** into a traceable commercial workflow without confusing product production with a completed sale.

## State machine

`REQUEST_RECEIVED → CATALOG_VALIDATED → PAYMENT_PENDING → PAYMENT_REVIEWED → FULFILMENT_STARTED → DELIVERED → DELIVERY_EVIDENCE_RECORDED → SETTLED → AUDITED`

Exceptional states:

- `INVALID_PRODUCT`
- `PAYMENT_REJECTED`
- `FULFILMENT_BLOCKED`
- `DISPUTED`
- `CANCELLED`

## Integrity rules

- Product asset ≠ sale.
- Payment route ≠ payment received.
- Payment received ≠ fulfilment complete.
- Delivery message ≠ delivery evidence.
- Sale ≠ scientific verification.
- No payment credentials, OTPs, passwords or card numbers belong in GitHub issues.

## Automission

The purchase-request issue form is the intake surface. The purchase-intake workflow:

1. validates the Product ID against `generated/1000-digital-products.json`;
2. creates a durable `generated/orders/ORD-xxxxxx.json` pending-order record;
3. records `PAYMENT=PENDING`, `FULFILMENT=NOT_STARTED`, and `DELIVERY=NOT_DELIVERED`;
4. comments the order ID back to the issue;
5. never upgrades the record to PAID, DELIVERED, SETTLED or VERIFIED automatically.

## Remaining production engineering

For full end-to-end commerce, the next bounded layers are:

1. secure payment webhook / transaction reference;
2. human or policy-gated payment reconciliation;
3. entitlement and fulfilment worker;
4. delivery artifact / access record;
5. settlement ledger;
6. dispute and refund handling;
7. audit trail and customer-quality feedback loop.

The public product factory remains responsible for production; the commercial layer is downstream.
