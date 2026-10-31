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
