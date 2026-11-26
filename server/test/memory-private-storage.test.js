import assert from "node:assert/strict";
import test from "node:test";
import { createMemoryPrivateStorageAdapter } from "../src/storage/memory-private-storage.js";

const bytes = Buffer.from("private test evidence");
const digest = "5b3e6f4c8a5d";

test("stores bytes with SHA-256 metadata and returns defensive copies", () => {
  const storage = createMemoryPrivateStorageAdapter();
  const metadata = storage.put({
    ownerId: "owner-1",
    objectKey: "evidence/order-1.pdf",
    body: bytes,
    mimeType: "application/pdf"
  });
  assert.equal(metadata.byte_size, bytes.length);
  assert.equal(metadata.status, "ready");
  assert.match(metadata.sha256, /^[a-f0-9]{64}$/);
  const retrieved = storage.get({ ownerId: "owner-1", objectKey: metadata.object_key });
  assert.deepEqual(retrieved, bytes);
  retrieved.fill(0);
  assert.deepEqual(storage.get({ ownerId: "owner-1", objectKey: metadata.object_key }), bytes);
});

test("rejects invalid bytes, disallowed MIME, oversize objects, duplicate keys and hash mismatch", () => {
  const storage = createMemoryPrivateStorageAdapter({ maxBytes: 8 });
  const put = overrides => storage.put({
    ownerId: "owner-1",
    objectKey: "evidence/item",
    body: Buffer.from("12345678"),
    mimeType: "text/plain",
    ...overrides
  });
  assert.throws(() => put({ body: "not bytes" }), /body must be bytes/);
  assert.throws(() => put({ body: Buffer.alloc(9) }), /OBJECT_SIZE_NOT_ALLOWED/);
  assert.throws(() => put({ mimeType: "text/html" }), /MIME_TYPE_NOT_ALLOWED/);
  assert.throws(() => put({ expectedSha256: "wrong" }), /SHA256_MISMATCH/);
  put({});
  assert.throws(() => put({}), /OBJECT_ALREADY_EXISTS/);
});

test("owner scoping prevents another account from reading or deleting private objects", () => {
  const storage = createMemoryPrivateStorageAdapter();
  storage.put({ ownerId: "owner-1", objectKey: "private/a", body: bytes, mimeType: "text/plain" });
  assert.equal(storage.head({ ownerId: "owner-2", objectKey: "private/a" }), null);
  assert.equal(storage.get({ ownerId: "owner-2", objectKey: "private/a" }), null);
  assert.equal(storage.remove({ ownerId: "owner-2", objectKey: "private/a" }), false);
  assert.deepEqual(storage.get({ ownerId: "owner-1", objectKey: "private/a" }), bytes);
});

test("read grants are signed, short-lived, scoped, and single-use", () => {
  let now = 1_800_000_000_000;
  const storage = createMemoryPrivateStorageAdapter({
    clock: () => now,
    grantTtlMs: 30_000,
    grantSecret: Buffer.alloc(32, 7)
  });
  storage.put({ ownerId: "owner-1", objectKey: "private/a", body: bytes, mimeType: "text/plain" });
  const grant = storage.issueReadGrant({ ownerId: "owner-1", objectKey: "private/a" });
  const redeemed = storage.redeemReadGrant({ grant });
  assert.deepEqual(redeemed.body, bytes);
  assert.equal(redeemed.metadata.owner_id, "owner-1");
  assert.throws(() => storage.redeemReadGrant({ grant }), /GRANT_ALREADY_USED/);

  const expired = storage.issueReadGrant({ ownerId: "owner-1", objectKey: "private/a", ttlMs: 10_000 });
  now += 10_000;
  assert.throws(() => storage.redeemReadGrant({ grant: expired }), /GRANT_EXPIRED/);
  assert.throws(() => storage.redeemReadGrant({ grant: grant + "tampered" }), /INVALID_GRANT/);
  assert.throws(() => storage.issueReadGrant({ ownerId: "owner-2", objectKey: "private/a" }), /OBJECT_NOT_FOUND/);
  assert.throws(() => storage.issueReadGrant({ ownerId: "owner-1", objectKey: "private/a", ttlMs: 30_001 }), /GRANT_TTL_NOT_ALLOWED/);
});

test("delete removes retrievability and writes an audit event without storing content", () => {
  const storage = createMemoryPrivateStorageAdapter();
  storage.put({ ownerId: "owner-1", objectKey: "private/a", body: bytes, mimeType: "text/plain" });
  assert.equal(storage.remove({ ownerId: "owner-1", objectKey: "private/a" }), true);
  assert.equal(storage.get({ ownerId: "owner-1", objectKey: "private/a" }), null);
  assert.equal(storage.remove({ ownerId: "owner-1", objectKey: "private/a" }), false);
  const audit = storage.listAudit();
  assert.deepEqual(audit.map(entry => entry.action), [
    "object.created",
    "object.deleted"
  ]);
  assert.equal(JSON.stringify(audit).includes(bytes.toString()), false);
  assert.equal(audit[1].sha256.length, 64);
});

test("does not claim durable or production storage capability", () => {
  const storage = createMemoryPrivateStorageAdapter();
  assert.equal("uploadUrl" in storage, false);
  assert.equal("downloadUrl" in storage, false);
  assert.equal("provider" in storage, false);
});
