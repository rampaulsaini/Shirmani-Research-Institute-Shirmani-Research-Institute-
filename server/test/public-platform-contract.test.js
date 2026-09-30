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

test("order schema is present and payment remains provider-gated", () => {
  const schema = fs.readFileSync(new URL("../sql/schema.sql", import.meta.url), "utf8");
  assert.match(schema, /create table if not exists orders/);
  assert.match(schema, /status text not null default 'intent'/);
  assert.match(schema, /provider_reference/);
});
