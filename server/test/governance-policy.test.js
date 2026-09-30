import test from "node:test";
import assert from "node:assert/strict";
import { governancePolicy, AI_PROHIBITED_ACTIONS, HUMAN_REVIEW_REQUIRED } from "../src/governance-policy.js";

test("governance policy keeps AI inside bounded advisory authority", () => {
  const policy = governancePolicy();
  assert.equal(policy.status, "ARCHITECTURE");
  assert.equal(policy.supreme_control.personal_absolute_power, false);
  assert.equal(policy.supreme_control.ai_absolute_power, false);
  assert.ok(policy.ai.prohibited.includes("court_override"));
  assert.ok(policy.ai.prohibited.includes("self_verification"));
  assert.ok(policy.ai.human_review_required.includes("election_or_civic_process_action"));
  assert.ok(AI_PROHIBITED_ACTIONS.length >= 7);
  assert.ok(HUMAN_REVIEW_REQUIRED.length >= 8);
});

test("essential-service and environmental objectives remain bounded policy objectives", () => {
  const policy = governancePolicy();
  assert.ok(policy.essential_services.objective.includes("food"));
  assert.ok(policy.essential_services.objective.includes("education"));
  assert.ok(policy.environment.protected_domains.includes("forests"));
  assert.ok(policy.environment.protected_domains.includes("oceans"));
  assert.equal(policy.essential_services.implementation_status, "POLICY_OBJECTIVE_REQUIRES_CAPACITY_AND_FINANCING_EVIDENCE");
  assert.equal(policy.truth_boundary.architecture_is_not_deployed_government, true);
});
