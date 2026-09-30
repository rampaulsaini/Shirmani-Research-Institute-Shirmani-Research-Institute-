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


test("server source exposes privacy, media and bounded Automission routes", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  for (const route of [
    'app.get("/v1/ai-agents"',
    'app.get("/v1/ai-tasks/:id/events"',
    'app.post("/v1/privacy-requests"',
    'app.get("/v1/privacy-requests"',
    'app.post("/v1/media-assets"',
    'app.get("/v1/media-assets"'
  ]) assert.ok(source.includes(route), "missing hardening route: " + route);
  assert.ok(source.includes("Binary storage is external"), "missing media storage boundary");
});


test("server source exposes explicit deployment readiness gates", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  for (const required of [
    'app.get("/v1/platform/readiness"',
    "READY_FOR_DEPLOYMENT_CHECKS",
    "DATABASE_NOT_CONFIGURED",
    "JWT_SECRET_NOT_CONFIGURED",
    "production_live: false",
    "independent_verification: false"
  ]) assert.ok(source.includes(required), "missing readiness boundary: " + required);
});


test("server source exposes a deployment-gated payment webhook", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  for (const required of [
    'app.post("/v1/payments/webhook"',
    "PAYMENT_PROVIDER_NOT_CONFIGURED",
    "INVALID_PAYMENT_SIGNATURE",
    "payment_succeeded",
    "payment_refunded"
  ]) assert.ok(source.includes(required), "missing payment boundary: " + required);
});


test("server source exposes bounded Automission lifecycle controls", () => {
  const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
  for (const required of [
    'app.post("/v1/ai-tasks/:id/dispatch"',
    'app.post("/v1/ai-tasks/:id/retry"',
    'app.post("/v1/ai-tasks/:id/cancel"',
    "AI_TASK_NOT_DISPATCHABLE",
    "AI_TASK_NOT_RETRYABLE",
    "AI_TASK_NOT_CANCELLABLE",
    "requires_human_review"
  ]) assert.ok(source.includes(required), "missing Automission lifecycle control: " + required);
});


test("OpenAPI contract documents the platform gates", () => {
  const api = JSON.parse(fs.readFileSync(new URL("../../schemas/social-platform-api.openapi.json", import.meta.url), "utf8"));
  for (const path of [
    "/v1/platform/readiness",
    "/v1/capabilities/status",
    "/v1/ai-tasks/{id}/dispatch",
    "/v1/ai-tasks/{id}/retry",
    "/v1/ai-tasks/{id}/cancel",
    "/v1/payments/webhook"
  ]) assert.ok(api.paths[path], "missing OpenAPI path: " + path);
  assert.equal(api.info.version, "0.6.0");
});
