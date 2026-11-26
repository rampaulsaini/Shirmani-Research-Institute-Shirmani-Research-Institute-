import assert from "node:assert/strict";
import test from "node:test";
import {
  createPrivateEvidenceService,
  EvidenceError,
  sha256Hex
} from "../src/private-evidence-contract.js";

const bytes = Buffer.from("synthetic evidence fixture");
const digest = sha256Hex(bytes);
const actorId = "test-owner";
const orderId = "test-order-1";
const purpose = "delivery";
const keyPattern = /^private-evidence\/[0-9a-f-]{36}$/i;

function fakeStorage(overrides = {}) {
  const objects = new Map();
  const calls = [];
  return {
    objects,
    calls,
    async createUploadIntent(input) {
      calls.push(["createUploadIntent", input]);
      objects.set(input.objectKey, {
        contentType: input.contentType,
        byteLength: input.byteLength,
        sha256: input.metadata.sha256,
        metadata: input.metadata
      });
      return { uploadUrl: "https://storage.invalid/upload/one" };
    },
    async headObject(objectKey) {
      calls.push(["headObject", objectKey]);
      return objects.get(objectKey) || null;
    },
    async createSignedDownload(input) {
      calls.push(["createSignedDownload", input]);
      return { url: "https://storage.invalid/private/download" };
    },
    async deleteObject(input) {
      calls.push(["deleteObject", input]);
      objects.delete(input.objectKey);
    },
    ...overrides
  };
}

const createIntent = storage => createPrivateEvidenceService({ storage }).createUploadIntent({
  actorId,
  orderId,
  purpose,
  contentType: "application/pdf",
  byteLength: bytes.length,
  sha256: digest
});

test("provider-free contract fails closed when no storage adapter exists", async () => {
  const service = createPrivateEvidenceService();
  await assert.rejects(
    service.createUploadIntent({ actorId, orderId, purpose, contentType: "application/pdf", byteLength: bytes.length, sha256: digest }),
    error => error instanceof EvidenceError && error.code === "EVIDENCE_STORAGE_NOT_CONFIGURED" && error.status === 503
  );
});

test("upload intent uses server-generated opaque key and enforces content, size and digest", async () => {
  const storage = fakeStorage();
  const intent = await createIntent(storage);
  assert.match(intent.objectKey, keyPattern);
  assert.equal(intent.uploadUrl, "https://storage.invalid/upload/one");
  assert.equal(storage.calls[0][1].metadata.orderId, orderId);
  assert.equal(storage.calls[0][1].metadata.purpose, purpose);
  await assert.rejects(
    createPrivateEvidenceService({ storage }).createUploadIntent({
      actorId, orderId, purpose, contentType: "application/x-executable", byteLength: bytes.length, sha256: digest
    }),
    error => error.code === "EVIDENCE_CONTENT_TYPE_NOT_ALLOWED"
  );
  await assert.rejects(
    createPrivateEvidenceService({ storage, maxBytes: 8 }).createUploadIntent({
      actorId, orderId, purpose, contentType: "application/pdf", byteLength: bytes.length, sha256: digest
    }),
    error => error.code === "EVIDENCE_SIZE_NOT_ALLOWED"
  );
  await assert.rejects(
    createPrivateEvidenceService({ storage }).createUploadIntent({
      actorId, orderId, purpose, contentType: "application/pdf", byteLength: bytes.length, sha256: "not-a-hash"
    }),
    error => error.code === "EVIDENCE_SHA256_REQUIRED"
  );
});

test("finalization verifies object existence, order binding, purpose, hash, size and MIME", async () => {
  const storage = fakeStorage();
  const service = createPrivateEvidenceService({ storage });
  const intent = await createIntent(storage);
  const valid = await service.finalizeUpload({
    actorId, orderId, purpose, objectKey: intent.objectKey, expectedSha256: digest
  });
  assert.equal(valid.verified, true);
  assert.equal(valid.sha256, digest);

  await assert.rejects(
    service.finalizeUpload({ actorId, orderId: "another-order", purpose, objectKey: intent.objectKey, expectedSha256: digest }),
    error => error.code === "EVIDENCE_METADATA_MISMATCH" && error.status === 403
  );
  await assert.rejects(
    service.finalizeUpload({ actorId, orderId, purpose, objectKey: intent.objectKey, expectedSha256: "a".repeat(64) }),
    error => error.code === "EVIDENCE_HASH_MISMATCH" && error.status === 422
  );
  await assert.rejects(
    service.finalizeUpload({ actorId, orderId, purpose, objectKey: "private-evidence/not-a-uuid", expectedSha256: digest }),
    error => error.code === "EVIDENCE_OBJECT_KEY_INVALID"
  );
  await assert.rejects(
    service.finalizeUpload({ actorId, orderId, purpose, objectKey: "private-evidence/00000000-0000-4000-8000-000000000000", expectedSha256: digest }),
    error => error.code === "EVIDENCE_OBJECT_NOT_FOUND" && error.status === 404
  );
});

test("download authorization is checked before a signed URL is created", async () => {
  const storage = fakeStorage();
  const service = createPrivateEvidenceService({ storage });
  const intent = await createIntent(storage);
  await assert.rejects(
    service.getAuthorizedDownload({ actorId, objectKey: intent.objectKey, authorize: async () => false }),
    error => error.code === "EVIDENCE_ACCESS_DENIED" && error.status === 403
  );
  assert.equal(storage.calls.some(([name]) => name === "createSignedDownload"), false);
  const result = await service.getAuthorizedDownload({
    actorId, objectKey: intent.objectKey, authorize: async () => true
  });
  assert.equal(result.expiresInSeconds, 60);
  assert.equal(storage.calls.at(-1)[1].expiresInSeconds, 60);
});

test("deletion requires authorization and delegates only the opaque object key", async () => {
  const storage = fakeStorage();
  const service = createPrivateEvidenceService({ storage });
  const intent = await createIntent(storage);
  await assert.rejects(
    service.deleteEvidence({ actorId, objectKey: intent.objectKey, authorize: async () => false }),
    error => error.code === "EVIDENCE_ACCESS_DENIED"
  );
  assert.equal(storage.objects.has(intent.objectKey), true);
  assert.deepEqual(
    await service.deleteEvidence({ actorId, objectKey: intent.objectKey, authorize: async () => true }),
    { deleted: true }
  );
  assert.equal(storage.objects.has(intent.objectKey), false);
});

test("sha256 helper accepts buffers only and computes the expected digest", () => {
  assert.equal(sha256Hex(bytes), digest);
  assert.throws(() => sha256Hex("not a buffer"), /BUFFER_REQUIRED/);
});
