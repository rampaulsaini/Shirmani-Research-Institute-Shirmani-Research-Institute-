import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const schema = JSON.parse(readFileSync(new URL("../schemas/impartial-understanding-parameter.schema.json", import.meta.url), "utf8"));

test("schema requires an auditable evidence and review record", () => {
  assert.equal(schema.type, "object");
  for (const field of [
    "perspective_label", "evidence_state", "evidence_refs", "counterview_checked",
    "uncertainty_note", "harm_and_stakeholder_check", "self_review_result",
    "audit_timestamp", "model_version"
  ]) assert.ok(schema.required.includes(field), `missing required field: ${field}`);
});

test("evidence state cannot silently expand beyond defined labels", () => {
  assert.deepEqual(schema.properties.evidence_state.enum, [
    "VERIFIED", "SOURCE_BASED", "PHILOSOPHICAL_IDENTITY", "INSUFFICIENT_EVIDENCE"
  ]);
});

test("VERIFIED requires at least one evidence reference and a stated uncertainty note", () => {
  const rule = schema.allOf.find(x => x.if?.properties?.evidence_state?.const === "VERIFIED");
  assert.equal(rule.then.properties.evidence_refs.minItems, 1);
  assert.equal(rule.then.properties.uncertainty_note.minLength, 1);
});

test("the 99.9999/0.0001 ratio is explicitly optional and non-measured", () => {
  const aspiration = schema.properties.user_defined_philosophical_aspiration;
  assert.ok(aspiration);
  assert.equal(aspiration.properties.heart_view_percent.const, 99.9999);
  assert.equal(aspiration.properties.mind_intellect_view_percent.const, 0.0001);
  assert.equal(aspiration.properties.status.const, "PHILOSOPHICAL_ASPIRATION_NOT_MEASURED");
});

test("insufficient evidence cannot receive a passing self-review", () => {
  const rule = schema.allOf.find(x => x.if?.properties?.evidence_state?.const === "INSUFFICIENT_EVIDENCE");
  assert.deepEqual(rule.then.properties.self_review_result.enum, ["revise", "insufficient-evidence"]);
});
