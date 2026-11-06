import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";

test("public platform API exposes order and dashboard primitives", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  for (const route of [
    "/v1/marketplace/orders",
    "/v1/marketplace/orders/:id/cancel",
    "/v1/dashboard",
    "/v1/work-orders",
    "/v1/disputes",
    "/v1/verification-reviews/:claimId"
  ]) assert.ok(source.includes(route), `Missing route: ${route}`);
});

test("public client enquiry endpoint validates consent and persists leads separately from orders", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  assert.ok(source.includes('app.post("/v1/enquiries", dbRequired, enquiryLimiter'));
  assert.ok(source.includes('body.consent !== true'));
  assert.ok(source.includes('"VALID_CONTACT_REQUIRED"'));
  assert.ok(source.includes('"Enquiry received for human review. No order or payment has been created."'));
  const schema = fs.readFileSync(new URL("../sql/schema.sql", import.meta.url), "utf8");
  assert.match(schema, /create table if not exists client_enquiries/);
  assert.match(schema, /status text not null default 'new'/);
  assert.match(schema, /consent_at timestamptz not null/);
});

test("order schema is present and payment remains provider-gated", () => {
  const schema = fs.readFileSync(new URL("../sql/schema.sql", import.meta.url), "utf8");
  assert.match(schema, /create table if not exists orders/);
  assert.match(schema, /status text not null default 'intent'/);
  assert.match(schema, /provider_reference/);
});


test("account page matches the server auth contract without persisting bearer tokens", () => {
  const page = fs.readFileSync(new URL("../../account-access.html", import.meta.url), "utf8");
  assert.ok(page.includes("'/v1/auth/register'"));
  assert.ok(page.includes("'/v1/auth/login'"));
  assert.ok(page.includes("{display_name:name,email,password:password.value}"));
  assert.ok(page.includes("payload.error"));
  assert.ok(page.includes("returned session token सहेजा नहीं गया"));
  assert.doesNotMatch(page, /localStorage\\.setItem|sessionStorage\\.setItem/);
});


test("private enquiry inbox is owner-only with account-id and configured-email authorization", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  assert.ok(source.includes('const ownerOnly = async (req, res, next) =>'));
  assert.ok(source.includes('const ownerAccountId = process.env.OWNER_ACCOUNT_ID'));
  assert.ok(source.includes('if (ownerAccountId && req.user?.sub === ownerAccountId) return next()'));
  assert.ok(source.includes('if (!ownerEmail)'));
  assert.ok(source.includes('select lower(email) as email from accounts where id=$1'));
  assert.ok(source.includes('if (rows[0]?.email !== ownerEmail)'));
  assert.ok(source.includes('app.get("/v1/owner/enquiries", dbRequired, auth, ownerOnly'));
  assert.ok(source.includes('limit $1'));
  assert.ok(source.includes('access: "owner_only"'));
});

test("legacy public enquiry adapter is consent-gated and never creates a payment", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  assert.ok(source.includes('app.get("/api/init-db", dbRequired'));
  assert.ok(source.includes("to_regclass('public.client_enquiries')"));
  assert.ok(source.includes('app.post("/api/enquiry", dbRequired, enquiryLimiter'));
  assert.ok(source.includes('body.consent !== true'));
  assert.ok(source.includes('"CONSENT_REQUIRED"'));
  assert.ok(source.includes('payment: "PENDING"'));
  assert.ok(source.includes('income: "₹0"'));
  assert.ok(source.includes('app.get("/api/health"'));
  assert.ok(source.includes("orders where status='paid' and currency='INR'"));
});


test("private CSV exports require owner authentication and verified income evidence", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  assert.ok(source.includes('app.get("/api/export-enquiries", dbRequired, auth, ownerOnly'));
  assert.ok(source.includes('app.get("/api/export-income", dbRequired, auth, ownerOnly'));
  assert.ok(source.includes('pe.verification_status=\'verified\''));
  assert.ok(source.includes('pe.customer_consent_at is not null'));
  assert.ok(source.includes('req.query.format === "csv"'));
  assert.ok(source.includes('status: rows.length ? "VERIFIED" : "UNAVAILABLE"'));
  assert.ok(source.includes('const csvCell = (value) =>'));
  const migration = fs.readFileSync(new URL("../sql/20261106_payment_evidence.sql", import.meta.url), "utf8");
  assert.match(migration, /customer_consent_at timestamptz not null/);
  assert.match(migration, /verification_status text not null default 'pending'/);
  assert.match(migration, /screenshot_storage_key text/);
  assert.match(migration, /verification_status <> 'verified'/);
});
