import assert from "node:assert/strict";
import test from "node:test";
import fs from "node:fs";

test("server source exposes the hardened health contract", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  for (const required of [
    'app.get("/health"',
    'status === "READY" ? 200 : 503',
    'database',
    'auth'
  ]) assert.ok(source.includes(required), "missing health contract: " + required);
});

test("server source exposes every currently documented implemented route", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  for (const route of [
    "/v1/auth/register",
    "/v1/auth/login",
    "/v1/profile/:id",
    "/v1/feed",
    "/v1/posts",
    "/v1/self-interviews",
    "/v1/marketplace/listings",
    "/v1/ai-tasks/:id",
    "/v1/marketplace/transactions"
  ]) assert.ok(source.includes(route), "missing route: " + route);
});


test("server source exposes account, trust and AI control routes", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  for (const route of [
    'app.patch("/v1/profile/:id"',
    'app.get("/v1/self-interviews"',
    'app.post("/v1/reports"',
    'app.post("/v1/ai-tasks"',
    'app.get("/v1/account/export"',
    'app.delete("/v1/account"'
  ]) assert.ok(source.includes(route), "missing control route: " + route);
});


test("server source exposes public platform module routes", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  for (const route of [
    'app.get("/v1/users/:id/followers"',
    'app.post("/v1/posts/:id/comments"',
    'app.get("/v1/notifications"',
    'app.post("/v1/courses/:listingId/enroll"',
    'app.post("/v1/work-orders"',
    'app.post("/v1/disputes"',
    'app.get("/v1/verification-reviews/:claimId"',
    'app.post("/v1/marketplace/orders"',
    'app.get("/v1/dashboard"'
  ]) assert.ok(source.includes(route), "missing module route: " + route);
});

test("server source preserves production truth boundaries", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  for (const boundary of [
    "DATABASE_NOT_CONFIGURED",
    "JWT_SECRET_NOT_CONFIGURED",
    "NOT_PAID",
    "Recorded order/payment fields are not proof"
  ]) assert.ok(source.includes(boundary), "missing boundary: " + boundary);
});


test("server source exposes explicit capability status without overstating readiness", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  for (const required of [
    'app.get("/v1/capabilities/status"',
    '"DEPLOYMENT_GATED"',
    '"INDEPENDENTLY_VERIFIED"',
    "workflow_completion_is_not_truth_verification",
    "conceptual_currency_design_is_not_legal_currency"
  ]) assert.ok(source.includes(required), "missing capability status boundary: " + required);
});
