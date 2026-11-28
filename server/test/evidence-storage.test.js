import { assertEvidenceStorageAdapter } from "../src/evidence-storage/contract.js";
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import test from "node:test";
import { createTestEvidenceStorage } from "./helpers/test-evidence-storage.js";

test("test evidence storage writes opaque keys and returns checksum metadata", async t => {
  const storage = await createTestEvidenceStorage();
  t.after(() => storage.close());

  const bytes = Buffer.from("synthetic test evidence only");
  const saved = await storage.put({
    bytes,
    contentType: "text/plain",
    ownerId: "owner-test-1",
    orderId: "order-test-1"
  });

  assert.match(saved.key, /^[0-9a-f-]{36}$/);
  assert.equal(saved.byteLength, bytes.length);
  assert.equal(saved.sha256, createHash("sha256").update(bytes).digest("hex"));

  const loaded = await storage.get({
    key: saved.key,
    ownerId: "owner-test-1",
    orderId: "order-test-1"
  });
  assert.deepEqual(loaded.bytes, bytes);
  assert.equal(loaded.sha256, saved.sha256);
});

test("test evidence storage denies cross-owner and cross-order reads and deletes", async t => {
  const storage = await createTestEvidenceStorage();
  t.after(() => storage.close());

  const saved = await storage.put({
    bytes: Buffer.from("private fixture"),
    contentType: "text/plain",
    ownerId: "owner-test-1",
    orderId: "order-test-1"
  });

  await assert.rejects(
    storage.get({ key: saved.key, ownerId: "owner-test-2", orderId: "order-test-1" }),
    /EVIDENCE_ACCESS_DENIED/
  );
  await assert.rejects(
    storage.get({ key: saved.key, ownerId: "owner-test-1", orderId: "order-test-2" }),
    /EVIDENCE_ACCESS_DENIED/
  );
  await assert.rejects(
    storage.delete({ key: saved.key, ownerId: "owner-test-2", orderId: "order-test-1" }),
    /EVIDENCE_ACCESS_DENIED/
  );

  assert.deepEqual(
    (await storage.get({ key: saved.key, ownerId: "owner-test-1", orderId: "order-test-1" })).bytes,
    Buffer.from("private fixture")
  );
});

test("test evidence storage rejects unsafe size, missing identity and unapproved MIME types", async t => {
  const storage = await createTestEvidenceStorage();
  t.after(() => storage.close());

  await assert.rejects(
    storage.put({ bytes: Buffer.from("x"), contentType: "text/html", ownerId: "o", orderId: "a" }),
    /EVIDENCE_CONTENT_TYPE_INVALID/
  );
  await assert.rejects(
    storage.put({ bytes: Buffer.alloc(5 * 1024 * 1024 + 1), contentType: "application/pdf", ownerId: "o", orderId: "a" }),
    /EVIDENCE_SIZE_INVALID/
  );
  await assert.rejects(
    storage.put({ bytes: Buffer.from("x"), contentType: "text/plain", ownerId: "", orderId: "a" }),
    /EVIDENCE_OWNER_AND_ORDER_REQUIRED/
  );
});

test("test evidence storage deletes objects and cleans up its disposable root", async t => {
  const storage = await createTestEvidenceStorage();
  t.after(() => storage.close());

  const saved = await storage.put({
    bytes: Buffer.from("temporary"),
    contentType: "text/plain",
    ownerId: "owner-test",
    orderId: "order-test"
  });
  assert.deepEqual(
    await storage.delete({ key: saved.key, ownerId: "owner-test", orderId: "order-test" }),
    { deleted: true }
  );
  await assert.rejects(
    storage.get({ key: saved.key, ownerId: "owner-test", orderId: "order-test" }),
    /EVIDENCE_ACCESS_DENIED/
  );
  await storage.close();
  await assert.rejects(
    storage.get({ key: saved.key, ownerId: "owner-test", orderId: "order-test" }),
    /EVIDENCE_STORAGE_CLOSED/
  );
});

test("evidence adapter contract rejects incomplete implementations", async () => {
  assert.throws(
    () => assertEvidenceStorageAdapter({ put() {}, get() {}, delete() {} }),
    /EVIDENCE_STORAGE_ADAPTER_INVALID/
  );
});

test("disposable evidence fixture conforms to the shared adapter contract", async t => {
  const adapter = createTestEvidenceStorage();
  const storage = await adapter;
  t.after(() => storage.close());
  assert.equal(typeof storage.put, "function");
  assert.equal(typeof storage.get, "function");
  assert.equal(typeof storage.delete, "function");
  assert.equal(typeof storage.close, "function");
});
