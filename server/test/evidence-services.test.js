import assert from "node:assert/strict";
import test from "node:test";
import { createEvidenceServices, EvidenceServiceError } from "../src/evidence-services.js";

const hash = "a".repeat(64);
const orderId = "test-order-001";

function errorCode(promise, code) {
  return assert.rejects(promise, error => error instanceof EvidenceServiceError && error.code === code);
}

function fakeStorage(overrides = {}) {
  const calls = [];
  const object = {
    contentType: "application/pdf",
    byteSize: 128,
    sha256: hash,
    metadata: { orderId, purpose: "payment_proof", contentType: "application/pdf", byteSize: 128, sha256: hash }
  };
  return {
    calls,
    object,
    async createUploadIntent(input) {
      calls.push(["createUploadIntent", input]);
      return { uploadUrl: "https://storage.invalid/upload", expiresAt: "2030-01-01T00:00:00Z" };
    },
    async headObject(input) { calls.push(["headObject", input]); return object; },
    async createSignedDownload(input) {
      calls.push(["createSignedDownload", input]);
      return { url: "https://storage.invalid/private-download" };
    },
    async deleteObject(input) { calls.push(["deleteObject", input]); },
    ...overrides
  };
}

test("missing storage fails closed for upload, finalize, download and delete", async () => {
  const service = createEvidenceServices();
  await errorCode(service.createUploadIntent({ orderId, purpose: "payment_proof", contentType: "application/pdf", byteSize: 128, sha256: hash }), "EVIDENCE_STORAGE_NOT_CONFIGURED");
  await errorCode(service.finalizeUpload({ objectKey: "sri-evidence/00000000-0000-0000-0000-000000000000", orderId, purpose: "payment_proof", sha256: hash }), "EVIDENCE_STORAGE_NOT_CONFIGURED");
  await errorCode(service.getAuthorizedDownload({ objectKey: "sri-evidence/00000000-0000-0000-0000-000000000000", authorize: async () => true }), "EVIDENCE_STORAGE_NOT_CONFIGURED");
  await errorCode(service.deleteEvidence({ objectKey: "sri-evidence/00000000-0000-0000-0000-000000000000", authorize: async () => true }), "EVIDENCE_STORAGE_NOT_CONFIGURED");
});

test("upload keys are server-generated and metadata is bound to order and purpose", async () => {
  const storage = fakeStorage();
  const service = createEvidenceServices({ storage });
  const intent = await service.createUploadIntent({ orderId, purpose: "payment_proof", contentType: "application/pdf", byteSize: 128, sha256: hash });
  assert.match(intent.objectKey, /^sri-evidence\/[0-9a-f-]{36}$/i);
  assert.equal(storage.calls[0][1].metadata.orderId, orderId);
  assert.equal(storage.calls[0][1].metadata.purpose, "payment_proof");
  assert.equal(storage.calls[0][1].metadata.sha256, hash);
});

test("rejects disallowed content, oversize files and malformed hashes before adapter call", async () => {
  const storage = fakeStorage();
  const service = createEvidenceServices({ storage });
  await errorCode(service.createUploadIntent({ orderId, purpose: "payment_proof", contentType: "application/x-msdownload", byteSize: 128, sha256: hash }), "EVIDENCE_CONTENT_TYPE_NOT_ALLOWED");
  await errorCode(service.createUploadIntent({ orderId, purpose: "payment_proof", contentType: "application/pdf", byteSize: 10 * 1024 * 1024 + 1, sha256: hash }), "EVIDENCE_SIZE_INVALID");
  await errorCode(service.createUploadIntent({ orderId, purpose: "payment_proof", contentType: "application/pdf", byteSize: 128, sha256: "bad" }), "EVIDENCE_SHA256_REQUIRED");
  assert.equal(storage.calls.length, 0);
});

test("finalization rejects nonexistent object, wrong order and tampered hash", async () => {
  const missing = fakeStorage({ async headObject() { return null; } });
  await errorCode(createEvidenceServices({ storage: missing }).finalizeUpload({
    objectKey: "sri-evidence/00000000-0000-0000-0000-000000000000", orderId, purpose: "payment_proof", sha256: hash
  }), "EVIDENCE_OBJECT_NOT_FOUND");

  const wrongOrder = fakeStorage();
  wrongOrder.object.metadata.orderId = "another-order";
  await errorCode(createEvidenceServices({ storage: wrongOrder }).finalizeUpload({
    objectKey: "sri-evidence/00000000-0000-0000-0000-000000000000", orderId, purpose: "payment_proof", sha256: hash
  }), "EVIDENCE_BINDING_MISMATCH");

  const tampered = fakeStorage();
  tampered.object.sha256 = "b".repeat(64);
  await errorCode(createEvidenceServices({ storage: tampered }).finalizeUpload({
    objectKey: "sri-evidence/00000000-0000-0000-0000-000000000000", orderId, purpose: "payment_proof", sha256: hash
  }), "EVIDENCE_HASH_MISMATCH");
});

test("authorization is checked before any signed download is requested", async () => {
  const storage = fakeStorage();
  const service = createEvidenceServices({ storage });
  const key = "sri-evidence/00000000-0000-0000-0000-000000000000";
  await errorCode(service.getAuthorizedDownload({ objectKey: key, authorize: async () => false }), "EVIDENCE_ACCESS_DENIED");
  assert.equal(storage.calls.some(call => call[0] === "createSignedDownload"), false);
  const result = await service.getAuthorizedDownload({ objectKey: key, authorize: async () => true, expiresInSeconds: 30 });
  assert.equal(result.url, "https://storage.invalid/private-download");
  assert.equal(storage.calls.at(-1)[1].expiresInSeconds, 30);
  await errorCode(service.getAuthorizedDownload({ objectKey: key, authorize: async () => true, expiresInSeconds: 301 }), "EVIDENCE_DOWNLOAD_TTL_INVALID");
});

test("delete requires authorization and only accepts server-shaped keys", async () => {
  const storage = fakeStorage();
  const service = createEvidenceServices({ storage });
  await errorCode(service.deleteEvidence({ objectKey: "sri-evidence/00000000-0000-0000-0000-000000000000", authorize: async () => false }), "EVIDENCE_ACCESS_DENIED");
  assert.equal(storage.calls.some(call => call[0] === "deleteObject"), false);
  await assert.rejects(service.deleteEvidence({ objectKey: "private://caller/path", authorize: async () => true }), /EVIDENCE_OBJECT_KEY_INVALID/);
});

test("missing notification adapter fails closed; configured fake adapter receives acceptance request", async () => {
  const service = createEvidenceServices();
  await errorCode(service.sendAcceptanceLink({ orderId, verifiedContact: "test@example.invalid", token: "x".repeat(40) }), "CUSTOMER_NOTIFICATION_NOT_CONFIGURED");
  let captured;
  const configured = createEvidenceServices({ notifications: {
    async sendAcceptanceLink(input) { captured = input; return { accepted: true }; }
  } });
  assert.deepEqual(await configured.sendAcceptanceLink({ orderId, verifiedContact: "test@example.invalid", token: "x".repeat(40) }), { accepted: true });
  assert.equal(captured.token, "x".repeat(40));
});
