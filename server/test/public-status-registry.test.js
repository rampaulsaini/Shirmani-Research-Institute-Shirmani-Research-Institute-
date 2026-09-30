import test from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const registryPath = new URL("../../docs/yatharth-system/feature-status-registry.json", import.meta.url);

test("public feature registry is fail-closed and exposes required status vocabulary", async () => {
  const registry = JSON.parse(await readFile(registryPath, "utf8"));
  assert.equal(registry.truth_rule, "architecture_is_not_deployment");
  assert.equal(registry.verification.independent_verified_claims, 0);
  assert.equal(registry.public_dashboard.path, "yatharth-status.html");
  assert.equal(registry.public_dashboard.fail_safe, true);
  for (const required of ["LIVE", "BETA", "ARCHITECTURE", "RESEARCH", "REVIEW_REQUIRED", "DISABLED", "INCONCLUSIVE", "NOT_VERIFIED"]) {
    assert.ok(registry.status_vocabulary.includes(required), `missing status: ${required}`);
  }
});

test("public registry completion contract includes operational safety requirements", async () => {
  const registry = JSON.parse(await readFile(registryPath, "utf8"));
  const required = registry.completion_contract.required;
  for (const item of ["implementation", "tests", "security_privacy", "monitoring", "user_facing_status", "rollback_or_appeal"]) {
    assert.ok(required.includes(item), `missing completion requirement: ${item}`);
  }
});
