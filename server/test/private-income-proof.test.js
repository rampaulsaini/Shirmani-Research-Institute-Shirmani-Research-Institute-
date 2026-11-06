import assert from "node:assert/strict";
import test from "node:test";
import fs from "node:fs";

test("private exports require authentication and owner identity", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  for (const route of [
    'app.get("/api/export-enquiries", dbRequired, auth, ownerOnly',
    'app.get("/api/export-income", dbRequired, auth, ownerOnly',
    'app.post("/api/owner/orders/:orderId/payment-proof", dbRequired, auth, ownerOnly',
    'app.post("/api/owner/payment-proofs/:proofId/verify", dbRequired, auth, ownerOnly'
  ]) assert.ok(source.includes(route), "missing protected route: " + route);
  assert.ok(source.includes('Cache-Control", "private, no-store, max-age=0"'));
  assert.ok(source.includes('text/csv; charset=utf-8'));
});

test("only verified and consented proof records contribute to income", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  assert.ok(source.includes("verification_status='verified' and customer_consent=true"));
  assert.ok(source.includes("UNAVAILABLE_PENDING_VERIFICATION"));
  assert.ok(source.includes("owner_attested_bank_match_not_independent_audit"));
  assert.ok(source.includes("private://"), "public screenshot URLs must not be accepted");
});

test("payment proof schema requires all evidence fields and verification trail", () => {
  const migration = fs.readFileSync(new URL("../sql/migrations/003_private_income_proof.sql", import.meta.url), "utf8");
  for (const field of ["payment_id", "upi_ref", "screenshot_url", "customer_consent", "verification_status", "verified_by", "verified_at"]) {
    assert.ok(migration.includes(field), "missing proof field: " + field);
  }
  assert.match(migration, /customer_consent boolean not null check \(customer_consent = true\)/);
  assert.match(migration, /verification_status = 'verified'.*verification_method is not null/s);
});

test("CSV serialization protects against spreadsheet formula injection", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  assert.ok(source.includes('/^[\\s]*[=+\\-@]/'));
  assert.ok(source.includes('text.replace(/"/g, \'""\')'));
});
