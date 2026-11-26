import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import test from "node:test";
import { createPrivateEvidenceStorage } from "../src/private-evidence-storage.js";

function fakePrivateAdapter({ corruptHead = false } = {}) {
  const objects = new Map();
  return {
    objects,
    async putPrivateObject({ key, body, contentType, metadata }) {
      objects.set(key, {
        body: Buffer.from(body),
        contentType,
        byteSize: body.byteLength,
        sha256: corruptHead ? "0".repeat(64) : metadata.sha256,
        private: true
      });
    },
    async headPrivateObject({ key }) {
      const item = objects.get(key);
      if (!item) return null;
      return {
        contentType: item.contentType,
        byteSize: item.byteSize,
        sha256: item.sha256
      };
    },
    async createSignedGetUrl({ key, expiresInSeconds }) {
      assert.ok(objects.has(key));
      assert.ok(objects.get(key).private);
      return {
        url: "https://private-test.invalid/object/short-lived",
        expiresInSeconds
      };
    }
  };
}

test("stores evidence under a server-generated key and verifies size, MIME and SHA-256", async () => {
  const adapter = fakePrivateAdapter();
  const storage = createPrivateEvidenceStorage({ adapter });
  const bytes = Buffer.from("%PDF-1.7 test evidence");
  const evidence = await storage.store({
    ownerId: "owner-1",
    orderId: "order-1",
    purpose: "payment-proof",
    contentType: "application/pdf",
    bytes
  });

  assert.match(evidence.key, /^evidence\/[0-9a-f-]{36}$/);
  assert.equal(evidence.byteSize, bytes.byteLength);
  assert.equal(evidence.sha256, createHash("sha256").update(bytes).digest("hex"));
  assert.equal(evidence.status, "verified");
  assert.equal(adapter.objects.get(evidence.key).private, true);
});

test("rejects unapproved MIME types and invalid or oversized payloads before storage", async () => {
  const adapter = fakePrivateAdapter();
  const storage = createPrivateEvidenceStorage({ adapter, maxBytes: 8 });
  await assert.rejects(storage.store({
    ownerId: "owner-1", orderId: "order-1", purpose: "payment-proof",
    contentType: "text/html", bytes: Buffer.from("x")
  }), /not allowed/);
  await assert.rejects(storage.store({
    ownerId: "owner-1", orderId: "order-1", purpose: "payment-proof",
    contentType: "text/plain", bytes: Buffer.from("123456789")
  }), /size/);
  assert.equal(adapter.objects.size, 0);
});

test("fails closed when stored object metadata does not match the upload", async () => {
  const storage = createPrivateEvidenceStorage({ adapter: fakePrivateAdapter({ corruptHead: true }) });
  await assert.rejects(storage.store({
    ownerId: "owner-1", orderId: "order-1", purpose: "delivery-proof",
    contentType: "text/plain", bytes: Buffer.from("delivery")
  }), /integrity verification/);
});

test("requires owner authorization before issuing a short-lived HTTPS download URL", async () => {
  const adapter = fakePrivateAdapter();
  const storage = createPrivateEvidenceStorage({ adapter });
  const evidence = await storage.store({
    ownerId: "owner-1", orderId: "order-1", purpose: "delivery-proof",
    contentType: "text/plain", bytes: Buffer.from("delivered")
  });

  await assert.rejects(storage.createOwnerDownload({
    evidence,
    requesterId: "other-user",
    authorizeOwner: async () => false
  }), error => error.code === "EVIDENCE_ACCESS_DENIED");

  const grant = await storage.createOwnerDownload({
    evidence,
    requesterId: "owner-1",
    authorizeOwner: async context =>
      context.requesterId === "owner-1" &&
      context.ownerId === "owner-1" &&
      context.orderId === "order-1" &&
      context.evidenceKey === evidence.key &&
      context.purpose === "delivery-proof" &&
      context.sha256 === evidence.sha256
  });
  assert.equal(grant.url.startsWith("https://"), true);
  assert.equal(grant.expiresInSeconds, 60);
});

test("rejects malformed adapter configuration and excessive signed URL lifetime", async () => {
  assert.throws(() => createPrivateEvidenceStorage({ adapter: {} }), /adapter is required/);
  const storage = createPrivateEvidenceStorage({ adapter: fakePrivateAdapter() });
  const evidence = await storage.store({
    ownerId: "owner-1",
    orderId: "order-1",
    purpose: "payment-proof",
    contentType: "text/plain",
    bytes: Buffer.from("proof")
  });
  await assert.rejects(storage.createOwnerDownload({
    evidence: { ...evidence, key: "evidence/arbitrary-object" },
    requesterId: "owner-1",
    authorizeOwner: async () => true
  }), /verified evidence/);
  await assert.rejects(storage.createOwnerDownload({
    evidence,
    requesterId: "owner-1",
    authorizeOwner: async () => true,
    expiresInSeconds: 301
  }), /short expiry/);
});
