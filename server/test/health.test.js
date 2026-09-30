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
