import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";

test("production deployment contract exists without real secrets", () => {
  const env = fs.readFileSync(new URL("../.env.example", import.meta.url), "utf8");
  for (const key of ["DATABASE_URL", "CORS_ORIGIN", "JWT_SECRET", "PAYMENT_WEBHOOK_SECRET"]) {
    assert.match(env, new RegExp("^" + key + "=", "m"));
  }
  assert.doesNotMatch(env, /ghp_[A-Za-z0-9_]+|github_pat_[A-Za-z0-9_]+/);
});

test("container and deployment runbook exist", () => {
  assert.ok(fs.existsSync(new URL("../Dockerfile", import.meta.url)));
  const runbook = fs.readFileSync(new URL("../../docs/public-platform/deployment-runbook.md", import.meta.url), "utf8");
  assert.match(runbook, /Production LIVE/i);
  assert.match(runbook, /Independent verification/i);
});
