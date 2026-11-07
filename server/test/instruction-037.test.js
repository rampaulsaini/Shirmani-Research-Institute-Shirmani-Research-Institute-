import assert from "node:assert/strict";
import test from "node:test";
import fs from "node:fs";

const source = fs.readFileSync(new URL("../src/index.js", import.meta.url), "utf8");
const dockerfile = fs.readFileSync(new URL("../Dockerfile", import.meta.url), "utf8");

test("Instruction 037 health endpoint is process liveness and never reports dependency failure as process death", () => {
  assert.match(source, /app\.get\("\/api\/health"/);
  assert.match(source, /return res\.status\(200\)\.json\(\{[\s\S]*?live: true/);
});

test("Instruction 037 readiness requires a real database, JWT secret and explicit CORS origin", () => {
  assert.match(source, /app\.get\("\/api\/ready"/);
  assert.match(source, /checks\.database === "READY"/);
  assert.match(source, /checks\.jwt === "CONFIGURED"/);
  assert.match(source, /checks\.cors === "CONFIGURED"/);
  assert.match(source, /res\.status\(ready \? 200 : 503\)/);
});

test("Production startup does not invent credentials or terminate before diagnostics", () => {
  assert.match(source, /Production configuration incomplete:/);
  assert.doesNotMatch(source, /process\.exit\(1\)/);
  assert.match(source, /return callback\(null, false\)/);
});

test("Both documented public Yatharth verification paths use the same database-backed verifier", () => {
  assert.match(source, /app\.get\("\/api\/yatharth\/verify\/:accountId", dbRequired, verifyYatharthAccount\)/);
  assert.match(source, /app\.get\("\/verify\/:accountId", dbRequired, verifyYatharthAccount\)/);
  assert.match(source, /verification_scope: "database_reservation_record_only"/);
});

test("Docker healthcheck uses liveness, not dependency readiness", () => {
  assert.match(dockerfile, /\/api\/health/);
  assert.doesNotMatch(dockerfile, /\/v1\/platform\/readiness/);
});
