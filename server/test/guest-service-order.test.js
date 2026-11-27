import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const read = path => fs.readFileSync(new URL(path, import.meta.url), "utf8");

test("guest conversion is owner-only, consent-linked, exact-scope and idempotent", () => {
  const source = read("../src/index.js");
  const route = source.slice(source.indexOf('app.post("/api/owner/enquiries/:enquiryId/convert-to-service-order"'));
  for (const contract of [
    "dbRequired, auth, ownerOnly",
    "written_acceptance_reference",
    "Number.isSafeInteger(amountMinor)",
    'body.currency !== "INR"',
    "revisionLimit < 0",
    "for update",
    "where enquiry_id=$1",
    "duplicate: true",
    "guest_service_order_created"
  ]) assert.ok(route.includes(contract), "missing guest conversion contract: " + contract);
});

test("guest payment proof copies the exact quote and cannot verify without owner bank match", () => {
  const source = read("../src/index.js");
  const migration = read("../sql/migrations/005_guest_service_order_lifecycle.sql");
  assert.ok(source.includes('app.post("/api/owner/service-orders/:orderId/payment-proof"'));
  assert.ok(source.includes('app.post("/api/owner/service-payment-proofs/:proofId/verify"'));
  assert.ok(source.includes("confirm_bank_match !== true"));
  assert.ok(source.includes("verification_method='owner_bank_statement'"));
  assert.ok(source.includes("String(p.amount_minor) !== String(p.order_amount)"));
  assert.ok(migration.includes("payment_reference text not null unique"));
  assert.ok(migration.includes("customer_consent boolean not null check (customer_consent = true)"));
  assert.ok(migration.includes("customer_consent_reference text not null"));
  assert.ok(source.includes("customer_consent_reference"));
  assert.ok(migration.includes("private://"));
});

test("guest delivery and acceptance are sequential and require private evidence", () => {
  const source = read("../src/index.js");
  const migration = read("../sql/migrations/005_guest_service_order_lifecycle.sql");
  assert.ok(source.includes('app.post("/api/owner/service-orders/:orderId/deliver"'));
  assert.ok(source.includes('app.post("/api/owner/service-orders/:orderId/customer-acceptance"'));
  assert.ok(source.includes("SERVICE_ORDER_MUST_BE_PAID_BEFORE_DELIVERY"));
  assert.ok(source.includes("SERVICE_ORDER_MUST_BE_DELIVERED_BEFORE_ACCEPTANCE"));
  assert.ok(migration.includes("delivery_reference"));
  assert.ok(migration.includes("customer_acceptance_reference"));
});

test("public status includes guest verified INR payments without customer PII", () => {
  const source = read("../src/index.js");
  assert.ok(source.includes("guest_service_payment_proofs"));
  assert.ok(source.includes("guest_paid_orders"));
  assert.ok(source.includes("verification_status='verified' and customer_consent=true and currency='INR'"));
  const status = source.slice(source.indexOf('app.get("/api/status"'), source.indexOf('const csvCell'));
  assert.doesNotMatch(status, /select .*email|select .*phone|select .*name/i);
});

test("public income separates owner-attested bank matches from provider-verified payments", () => {
  const source = read("../src/index.js");
  assert.ok(source.includes("owner_attested_bank_match_inr_minor"));
  assert.ok(source.includes("provider_verified_payment_inr_minor"));
  assert.ok(source.includes("verification_method='owner_bank_statement'"));
  assert.ok(source.includes("verification_method='provider_verified'"));
  assert.ok(source.includes("Owner bank-statement matches are owner-attested, not independently audited."));
});
