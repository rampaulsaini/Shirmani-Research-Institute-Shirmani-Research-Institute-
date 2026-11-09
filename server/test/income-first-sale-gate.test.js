import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";

const read = path => fs.readFileSync(new URL(path, import.meta.url), "utf8");

test("public sale enquiry endpoint requires consent, validates contact, deduplicates and audits", () => {
  const source = read("../src/index.js");
  const start = source.indexOf('app.post("/api/enquiry"');
  const end = source.indexOf("// Liveness:", start);
  assert.ok(start >= 0 && end > start, "public /api/enquiry route must exist");
  const route = source.slice(start, end);
  for (const contract of [
    "body.consent !== true",
    "VALID_CONTACT_REQUIRED",
    "pg_advisory_xact_lock",
    "from client_enquiries",
    "interval '24 hours'",
    "insert into client_enquiries",
    "insert into audit_events",
    "No order or payment was created."
  ]) assert.ok(route.includes(contract), "missing enquiry contract: " + contract);
  assert.doesNotMatch(route, /payment\s*=\s*["']VERIFIED/);
});

test("public showroom exposes one featured SRI-SVC-001 pilot and posts only to the service API", () => {
  const html = read("../../showroom-public-interface.html");
  for (const contract of [
    "Shirmani Research Institute — Supreme Showroom",
    "SRI-SVC-001",
    "Hindi / English Writing",
    "₹999",
    "Scope",
    "Deadline",
    "Revisions",
    "9622254967@ptyes",
    "sainirampaul60@gmail.com",
    "https://shirmani-social-api-node.onrender.com/api/enquiry",
    "name=\"consent\"",
    "Open service desk"
  ]) assert.ok(html.includes(contract), "missing showroom sale-gate contract: " + contract);
  assert.ok(html.includes("result.duplicate"), "duplicate response must be visible to the customer");
});

test("payment proof instructions require human account matching and keep evidence private", () => {
  const doc = fs.readFileSync(new URL("../../docs/payment-proof-format.md", import.meta.url), "utf8");
  for (const contract of [
    "UPI or PayPal transaction screenshot",
    "Transaction ID / UTR",
    "bank SMS",
    "actual credited transaction",
    "authorized human reviewer",
    "Do not upload unredacted bank evidence",
    "customer acceptance"
  ]) assert.ok(doc.includes(contract), "missing payment-proof contract: " + contract);
});


test("sale-gate database schema supports private payment verification, delivery and acceptance", () => {
  const schema = read("../sql/schema.sql");
  assert.match(schema, /create table if not exists paid_orders/);
  assert.match(schema, /verification_status text not null default 'pending'/);
  assert.match(schema, /verification_method text/);
  assert.match(schema, /verified_by uuid references accounts\(id\)/);
  assert.match(schema, /screenshot_url text not null check \(screenshot_url ~ '\^private:/);
  assert.match(schema, /add column if not exists delivery_reference text/);
  assert.match(schema, /add column if not exists delivered_at timestamptz/);
  assert.match(schema, /add column if not exists customer_acceptance_reference text/);
  assert.match(schema, /add column if not exists customer_accepted_at timestamptz/);
});

test("sale-gate API enforces owner bank match before paid, delivery before acceptance", () => {
  const source = read("../src/index.js");
  assert.ok(source.includes('app.post("/api/owner/orders/:orderId/payment-proof"'));
  assert.ok(source.includes('app.post("/api/owner/payment-proofs/:proofId/verify"'));
  assert.ok(source.includes('confirm_bank_match !== true'));
  assert.ok(source.includes("verification_status='verified'"));
  assert.ok(source.includes("verification_method='owner_bank_statement'"));
  assert.ok(source.includes("where id=$2 and status='paid'"));
  assert.ok(source.includes("where id=$2 and status='fulfilled'"));
  assert.ok(source.includes("ORDER_MUST_BE_PAID_BEFORE_DELIVERY"));
  assert.ok(source.includes("ORDER_MUST_BE_DELIVERED_BEFORE_ACCEPTANCE"));
});
