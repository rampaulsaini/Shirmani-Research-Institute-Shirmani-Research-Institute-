import assert from "node:assert/strict";
import test from "node:test";
import {
  DEFAULT_MAX_EVIDENCE_BYTES,
  EVIDENCE_CONTENT_TYPES,
  EVIDENCE_PURPOSES,
  EvidenceStore,
  validateEvidenceMetadata
} from "../src/evidence-store.js";

test("evidence metadata accepts only declared purposes and safe content types", () => {
  for (const purpose of EVIDENCE_PURPOSES) {
    for (const contentType of EVIDENCE_CONTENT_TYPES) {
      const result = validateEvidenceMetadata({
        purpose,
        contentType,
        uploaderId: "owner-account-1"
      });
      assert.equal(result.purpose, purpose);
      assert.equal(result.contentType, contentType);
      assert.equal(result.uploaderId, "owner-account-1");
      assert.equal(result.maxBytes, DEFAULT_MAX_EVIDENCE_BYTES);
      assert.equal(Object.isFrozen(result), true);
    }
  }
});

test("evidence metadata rejects unknown purposes and content types", () => {
  assert.throws(() => validateEvidenceMetadata({
    purpose: "arbitrary",
    contentType: "application/pdf",
    uploaderId: "owner"
  }), /EVIDENCE_PURPOSE_INVALID/);

  assert.throws(() => validateEvidenceMetadata({
    purpose: "payment_proof",
    contentType: "text/html",
    uploaderId: "owner"
  }), /EVIDENCE_CONTENT_TYPE_NOT_ALLOWED/);
});

test("evidence metadata rejects missing uploader and unsafe limits", () => {
  assert.throws(() => validateEvidenceMetadata({
    purpose: "payment_proof",
    contentType: "application/pdf",
    uploaderId: " "
  }), /EVIDENCE_UPLOADER_REQUIRED/);

  assert.throws(() => validateEvidenceMetadata({
    purpose: "payment_proof",
    contentType: "application/pdf",
    uploaderId: "owner"
  }, { maxBytes: 0 }), /EVIDENCE_MAX_BYTES_INVALID/);
});

test("base EvidenceStore fails closed until a reviewed adapter is supplied", async () => {
  const store = new EvidenceStore();
  await assert.rejects(store.put([], {}), /EVIDENCE_STORE_PUT_NOT_IMPLEMENTED/);
  await assert.rejects(store.head("opaque-key"), /EVIDENCE_STORE_HEAD_NOT_IMPLEMENTED/);
  await assert.rejects(store.get("opaque-key"), /EVIDENCE_STORE_GET_NOT_IMPLEMENTED/);
  await assert.rejects(store.delete("opaque-key"), /EVIDENCE_STORE_DELETE_NOT_IMPLEMENTED/);
});
