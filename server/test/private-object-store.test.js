import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import test from "node:test";
import { createPrivateObjectStore } from "../src/storage/private-object-store.js";

function memoryPrivateAdapter() {
  const objects = new Map();
  return {
    async putPrivate({ key, body, contentType, sha256 }) {
      objects.set(key, { body: Buffer.from(body), contentType, sha256 });
    },
    async headPrivate(key) {
      const item = objects.get(key);
      return item ? {
        key,
        contentType: item.contentType,
        byteSize: item.body.length,
        sha256: item.sha256
      } : null;
    },
    async getPrivate(key) {
      const item = objects.get(key);
      return item ? { ...item, body: Buffer.from(item.body) } : null;
    },
    async deletePrivate(key) {
      return objects.delete(key);
    }
  };
}

const secret = "test-only-signing-secret-at-least-32-bytes";
const pdf = Buffer.from("%PDF-1.7 test fixture");

function makeStore(options = {}) {
  return createPrivateObjectStore({
    adapter: memoryPrivateAdapter(),
    signingSecret: secret,
    ...options
  });
}

test("stores only bounded, allowlisted objects and returns a SHA-256 digest", async () => {
  const store = makeStore();
  const result = await store.put({ key: "orders/order-1/delivery.pdf", body: pdf, contentType: "application/pdf" });
  assert.equal(result.visibility, "private");
  assert.equal(result.byteSize, pdf.length);
  assert.equal(result.sha256, createHash("sha256").update(pdf).digest("hex"));
  assert.equal((await store.head({ key: result.key })).sha256, result.sha256);
});

test("rejects traversal, malformed keys, non-byte bodies, disallowed MIME and oversized objects", async () => {
  const store = makeStore({ maxBytes: 8 });
  await assert.rejects(store.put({ key: "../secret", body: pdf, contentType: "application/pdf" }), { code: "INVALID_OBJECT_KEY" });
  await assert.rejects(store.put({ key: "orders//file", body: pdf, contentType: "application/pdf" }), { code: "INVALID_OBJECT_KEY" });
  await assert.rejects(store.put({ key: "orders/file", body: "not bytes", contentType: "application/pdf" }), { code: "INVALID_OBJECT_BODY" });
  await assert.rejects(store.put({ key: "orders/file", body: pdf, contentType: "text/html" }), { code: "MIME_TYPE_NOT_ALLOWED" });
  await assert.rejects(store.put({ key: "orders/file", body: pdf, contentType: "application/pdf" }), { code: "OBJECT_TOO_LARGE" });
});

test("does not issue a read grant for a missing object", async () => {
  const store = makeStore();
  await assert.rejects(store.issueReadGrant({ key: "orders/missing", subject: "owner-1" }), { code: "OBJECT_NOT_FOUND" });
});

test("read grants are bound to the subject and expire", async () => {
  let now = 1_800_000_000_000;
  const store = makeStore({ clock: () => now });
  await store.put({ key: "orders/order-2/consent.pdf", body: pdf, contentType: "application/pdf" });
  const grant = await store.issueReadGrant({ key: "orders/order-2/consent.pdf", subject: "owner-1", ttlSeconds: 30 });
  await assert.rejects(store.readWithGrant({ token: grant.token, subject: "owner-2" }), { code: "GRANT_SUBJECT_MISMATCH" });
  now += 30_000;
  await assert.rejects(store.readWithGrant({ token: grant.token, subject: "owner-1" }), { code: "READ_GRANT_EXPIRED" });
});

test("read grants are single-use, integrity checked and never expose a public URL", async () => {
  const store = makeStore();
  await store.put({ key: "orders/order-3/payment.pdf", body: pdf, contentType: "application/pdf" });
  const grant = await store.issueReadGrant({ key: "orders/order-3/payment.pdf", subject: "owner-1" });
  assert.equal(Object.hasOwn(grant, "url"), false);
  const read = await store.readWithGrant({ token: grant.token, subject: "owner-1" });
  assert.deepEqual(read.body, pdf);
  assert.equal(read.visibility, "private");
  await assert.rejects(store.readWithGrant({ token: grant.token, subject: "owner-1" }), { code: "READ_GRANT_ALREADY_USED" });
});

test("rejects tampered grants and invalid grant lifetimes", async () => {
  const store = makeStore();
  await store.put({ key: "orders/order-4/proof.pdf", body: pdf, contentType: "application/pdf" });
  const grant = await store.issueReadGrant({ key: "orders/order-4/proof.pdf", subject: "owner-1" });
  await assert.rejects(store.readWithGrant({ token: grant.token + "x", subject: "owner-1" }), { code: "INVALID_READ_GRANT" });
  await assert.rejects(store.issueReadGrant({ key: "orders/order-4/proof.pdf", subject: "owner-1", ttlSeconds: 301 }), { code: "INVALID_GRANT_TTL" });
});

test("supports explicit deletion and returns false for a missing object", async () => {
  const store = makeStore();
  await store.put({ key: "orders/order-5/archive.pdf", body: pdf, contentType: "application/pdf" });
  assert.equal(await store.delete({ key: "orders/order-5/archive.pdf" }), true);
  assert.equal(await store.delete({ key: "orders/order-5/archive.pdf" }), false);
  assert.equal(await store.head({ key: "orders/order-5/archive.pdf" }), null);
});

test("requires a production-strength signing secret and a complete private adapter", () => {
  assert.throws(() => makeStore({ signingSecret: "short" }), { code: "STORAGE_SIGNING_SECRET_TOO_SHORT" });
  assert.throws(() => createPrivateObjectStore({ adapter: {}, signingSecret: secret }), { code: "INVALID_STORAGE_ADAPTER" });
});
