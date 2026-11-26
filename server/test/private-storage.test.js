import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import test from "node:test";
import { createPrivateStorage } from "../src/private-storage.js";

function checksum(body) {
  return createHash("sha256").update(body).digest("hex");
}

function memoryAdapter() {
  const objects = new Map();
  return {
    objects,
    async putObject({ key, body, contentType, sha256 }) {
      objects.set(key, {
        key,
        body: Buffer.from(body),
        contentType,
        byteSize: body.length,
        sha256
      });
    },
    async headObject(key) {
      const object = objects.get(key);
      if (!object) return null;
      return {
        key: object.key,
        contentType: object.contentType,
        byteSize: object.byteSize,
        sha256: object.sha256
      };
    },
    async getObject(key) {
      const object = objects.get(key);
      return object ? { body: Buffer.from(object.body), contentType: object.contentType } : null;
    },
    async deleteObject(key) {
      objects.delete(key);
    }
  };
}

test("private storage writes, reads and deletes bytes with verified metadata", async () => {
  const adapter = memoryAdapter();
  const storage = createPrivateStorage({ adapter });
  const body = Buffer.from("private evidence fixture");
  const expected = checksum(body);

  const stored = await storage.put({
    key: "service-orders/order-123/acceptance.pdf",
    body,
    contentType: "application/pdf",
    expectedSha256: expected
  });
  assert.equal(stored.byteSize, body.length);
  assert.equal(stored.sha256, expected);
  assert.equal(stored.contentType, "application/pdf");

  const read = await storage.get("service-orders/order-123/acceptance.pdf");
  assert.deepEqual(read.body, body);
  assert.equal(read.sha256, expected);
  assert.equal(await storage.delete("service-orders/order-123/acceptance.pdf"), true);
  assert.equal(await storage.head("service-orders/order-123/acceptance.pdf"), null);
  assert.equal(await storage.get("service-orders/order-123/acceptance.pdf"), null);
  assert.equal(await storage.delete("service-orders/order-123/acceptance.pdf"), false);
});

test("private storage rejects traversal, malformed keys and empty bodies", async () => {
  const storage = createPrivateStorage({ adapter: memoryAdapter() });
  await assert.rejects(
    storage.put({ key: "../public/leak.pdf", body: Buffer.from("x"), contentType: "application/pdf" }),
    { code: "INVALID_PRIVATE_STORAGE_KEY" }
  );
  await assert.rejects(
    storage.put({ key: "orders//file.pdf", body: Buffer.from("x"), contentType: "application/pdf" }),
    { code: "INVALID_PRIVATE_STORAGE_KEY" }
  );
  await assert.rejects(
    storage.put({ key: "orders/file.pdf", body: Buffer.alloc(0), contentType: "application/pdf" }),
    { code: "PRIVATE_STORAGE_SIZE_OUT_OF_RANGE" }
  );
});

test("private storage enforces content type, size and caller checksum", async () => {
  const storage = createPrivateStorage({ adapter: memoryAdapter(), maxBytes: 8 });
  const body = Buffer.from("123456789");

  await assert.rejects(
    storage.put({ key: "orders/file.exe", body: Buffer.from("x"), contentType: "application/x-msdownload" }),
    { code: "PRIVATE_STORAGE_CONTENT_TYPE_NOT_ALLOWED" }
  );
  await assert.rejects(
    storage.put({ key: "orders/file.txt", body, contentType: "text/plain" }),
    { code: "PRIVATE_STORAGE_SIZE_OUT_OF_RANGE" }
  );
  await assert.rejects(
    storage.put({
      key: "orders/file.txt",
      body: Buffer.from("evidence"),
      contentType: "text/plain",
      expectedSha256: "0".repeat(64)
    }),
    { code: "PRIVATE_STORAGE_CHECKSUM_MISMATCH" }
  );
});

test("private storage detects altered bytes returned by an adapter", async () => {
  const adapter = memoryAdapter();
  const storage = createPrivateStorage({ adapter });
  await storage.put({
    key: "orders/evidence.txt",
    body: Buffer.from("original"),
    contentType: "text/plain"
  });
  adapter.objects.get("orders/evidence.txt").body = Buffer.from("tampered");

  await assert.rejects(
    storage.get("orders/evidence.txt"),
    { code: "PRIVATE_STORAGE_READ_CHECKSUM_MISMATCH" }
  );
});

test("private storage rejects incomplete adapters and invalid limits", () => {
  assert.throws(
    () => createPrivateStorage({ adapter: {} }),
    { code: "PRIVATE_STORAGE_ADAPTER_INCOMPLETE" }
  );
  assert.throws(
    () => createPrivateStorage({ adapter: memoryAdapter(), maxBytes: 0 }),
    { code: "INVALID_PRIVATE_STORAGE_MAX_BYTES" }
  );
});
