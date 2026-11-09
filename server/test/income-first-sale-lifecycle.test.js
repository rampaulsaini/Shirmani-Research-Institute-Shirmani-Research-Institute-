import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const read = path => fs.readFileSync(new URL(path, import.meta.url), "utf8");

test("verified payment atomically moves an eligible order to paid", () => {
  const source = read("../src/index.js");
  const start = source.indexOf('app.post("/api/owner/payment-proofs/:proofId/verify"');
  const end = source.indexOf('app.post("/api/owner/orders/:orderId/deliver"', start);
  assert.ok(start >= 0 && end > start, "payment verification route must exist");
  const route = source.slice(start, end);
  for (const contract of [
    'body?.confirm_bank_match !== true',
    'begin',
    "update paid_orders set verification_status='verified'",
    "update orders set status='paid'",
    'await client.query("commit")',
    'await client.query("rollback")',
    'owner_attested_bank_match_not_independent_audit'
  ]) assert.ok(route.includes(contract), "missing payment transition: " + contract);
});

test("delivery requires a paid order and private delivery evidence", () => {
  const source = read("../src/index.js");
  const start = source.indexOf('app.post("/api/owner/orders/:orderId/deliver"');
  const end = source.indexOf('app.post("/api/owner/orders/:orderId/customer-acceptance"', start);
  assert.ok(start >= 0 && end > start, "delivery route must exist");
  const route = source.slice(start, end);
  assert.ok(route.includes("PRIVATE_DELIVERY_REFERENCE_REQUIRED"));
  assert.ok(route.includes("delivery_reference=$1"));
  assert.ok(route.includes("where id=$2 and status='paid'"));
  assert.ok(route.includes('customer_acceptance: "PENDING"'));
});

test("customer acceptance is a separate explicit post-delivery gate", () => {
  const source = read("../src/index.js");
  const start = source.indexOf('app.post("/api/owner/orders/:orderId/customer-acceptance"');
  const end = source.indexOf("// Public Yatharth Genesis registry check.", start);
  assert.ok(start >= 0 && end > start, "customer acceptance route must exist");
  const route = source.slice(start, end);
  assert.ok(route.includes("customer_confirmed !== true"));
  assert.ok(route.includes("where id=$2 and status='fulfilled'"));
  assert.ok(route.includes("status='completed'"));
  assert.ok(route.includes("owner_recorded_customer_confirmation_not_independent_audit"));
});

test("migration stores private evidence locators and separate timestamps", () => {
  const sql = fs.readFileSync(new URL("../sql/migrations/004_delivery_acceptance_evidence.sql", import.meta.url), "utf8");
  for (const contract of [
    "delivery_reference text",
    "delivered_at timestamptz",
    "customer_acceptance_reference text",
    "customer_accepted_at timestamptz",
    "orders_delivery_reference_private_check",
    "orders_acceptance_reference_private_check"
  ]) assert.ok(sql.includes(contract), "missing migration contract: " + contract);
});
