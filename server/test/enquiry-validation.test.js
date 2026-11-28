import test from "node:test";
import assert from "node:assert/strict";
import { isValidContactEmail } from "../src/validation.js";

test("accepts ordinary and plus-addressed contact emails", () => {
  assert.equal(isValidContactEmail("buyer@example.com"), true);
  assert.equal(isValidContactEmail("buyer+pilot@research.example.co.in"), true);
});

test("rejects malformed, whitespace-containing, and non-string contacts", () => {
  for (const value of [
    "",
    "buyer",
    "buyer@example",
    "buyer @example.com",
    "buyer@example .com",
    "@example.com",
    "buyer@example.com ",
    null,
    undefined,
    42
  ]) {
    assert.equal(isValidContactEmail(value), false, String(value));
  }
});
