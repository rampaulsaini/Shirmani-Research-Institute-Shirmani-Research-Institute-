import assert from "node:assert/strict";
import test from "node:test";
import {
  createMemoryObjectAdapter,
  createPrivateObjectStore,
  PrivateObjectStoreError
} from "../src/storage/private-object-store.js";

const errorCode = code => error => error instanceof PrivateObjectStoreError && error.code === code;

test("stores private bytes with generated locator, MIME, size and SHA-256 metadata", async () => {
  const store = createPrivateObjectStore({ adapter: createMemoryObjectAdapter() });
  const body = Buffer.from("private evidence fixture");
  const saved = await store.put({ body, contentType: "text/plain" });

  assert.match(saved.locator, /^private:\/\/evidence\/[0-9a-f-]{36}$/i);
  assert.equal(saved.size, body.length);
  assert.match(saved.sha256, /^[a-f0-9]{64}$/);
  assert.equal((await store.head(saved.locator.slice("private://".length))).sha256, saved.sha256);
});

test("rejects unsupported MIME types, empty bodies, oversized bodies and non-byte input", async () => {
  const store = createPrivateObjectStore({
    adapter: createMemoryObjectAdapter(),
    maxBytes: 4,
    allowedMimeTypes: ["text/plain"]
  });
  await assert.rejects(store.put({ body: Buffer.from("x"), contentType: "text/html" }), errorCode("UNSUPPORTED_CONTENT_TYPE"));
  await assert.rejects(store.put({ body: Buffer.alloc(0), contentType: "text/plain" }), errorCode("OBJECT_SIZE_OUT_OF_RANGE"));
  await assert.rejects(store.put({ body: Buffer.from("12345"), contentType: "text/plain" }), errorCode("OBJECT_SIZE_OUT_OF_RANGE"));
  await assert.rejects(store.put({ body: "not bytes", contentType: "text/plain" }), errorCode("INVALID_OBJECT_BODY"));
});

test("private reads fail closed without an authorizer or with a denied authorizer", async () => {
  const store = createPrivateObjectStore({ adapter: createMemoryObjectAdapter() });
  const saved = await store.put({ body: Buffer.from("secret"), contentType: "text/plain" });
  const key = saved.locator.slice("private://".length);

  await assert.rejects(store.get({ key }), errorCode("AUTHORIZATION_REQUIRED"));
  await assert.rejects(store.get({ key, authorize: async () => false }), errorCode("FORBIDDEN"));
  const result = await store.get({ key, authorize: async ({ action, metadata }) =>
    action === "read" && metadata.key === key
  });
  assert.equal(result.body.toString(), "secret");
});

test("deletion requires authorization and is idempotently reported when absent", async () => {
  const store = createPrivateObjectStore({ adapter: createMemoryObjectAdapter() });
  const saved = await store.put({ body: Buffer.from("delete me"), contentType: "text/plain" });
  const key = saved.locator.slice("private://".length);

  await assert.rejects(store.delete({ key, authorize: async () => false }), errorCode("FORBIDDEN"));
  assert.equal(await store.delete({ key, authorize: async () => true }), true);
  assert.equal(await store.head(key), null);
  assert.equal(await store.delete({ key, authorize: async () => true }), false);
});

test("rejects malformed keys and detects tampering on retrieval", async () => {
  const adapter = createMemoryObjectAdapter();
  const store = createPrivateObjectStore({ adapter });
  await assert.rejects(store.head("../public/file"), errorCode("INVALID_STORAGE_KEY"));

  const saved = await store.put({ body: Buffer.from("original"), contentType: "text/plain" });
  const key = saved.locator.slice("private://".length);
  // Simulate storage corruption without changing the recorded digest.
  await adapter.put({
    key: "evidence/00000000-0000-4000-8000-000000000001",
    body: Buffer.from("tampered"),
    contentType: "text/plain",
    size: 8,
    sha256: saved.sha256
  });
  // The adapter is append-only; a direct test adapter cannot overwrite an existing key.
  const corruptedAdapter = {
    ...adapter,
    async head(requestedKey) {
      if (requestedKey === key) return { contentType: "text/plain", size: saved.size, sha256: saved.sha256 };
      return adapter.head(requestedKey);
    },
    async get(requestedKey) {
      if (requestedKey === key) return Buffer.from("tampered");
      return adapter.get(requestedKey);
    }
  };
  const integrityStore = createPrivateObjectStore({ adapter: corruptedAdapter });
  await assert.rejects(
    integrityStore.get({ key, authorize: async () => true }),
    errorCode("OBJECT_INTEGRITY_FAILURE")
  );
});
