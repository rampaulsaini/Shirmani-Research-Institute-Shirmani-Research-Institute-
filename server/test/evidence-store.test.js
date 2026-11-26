import assert from "node:assert/strict";
import { createHash, randomUUID } from "node:crypto";
import { Readable } from "node:stream";
import test from "node:test";
import { createEvidenceStore } from "../src/evidence-store.js";

// Disposable in-memory adapter for contract tests only. It is not a production
// storage implementation and intentionally has no filesystem/network access.
function createMemoryAdapter() {
  const objects = new Map();

  return {
    async put(readable, metadata) {
      const chunks = [];
      for await (const chunk of readable) chunks.push(Buffer.from(chunk));
      const body = Buffer.concat(chunks);
      const key = `test-only/${randomUUID()}`;
      const record = {
        body,
        metadata: {
          key,
          sha256: createHash("sha256").update(body).digest("hex"),
          sizeBytes: body.length,
          contentType: metadata.contentType
        }
      };
      objects.set(key, record);
      return { ...record.metadata };
    },

    async head(key) {
      const record = objects.get(key);
      return record ? { ...record.metadata } : null;
    },

    async get(key) {
      const record = objects.get(key);
      return record ? Readable.from([Buffer.from(record.body)]) : null;
    },

    async delete(key) {
      return objects.delete(key);
    }
  };
}

test("evidence store requires all adapter methods", () => {
  assert.throws(() => createEvidenceStore(null), /EVIDENCE_STORE_ADAPTER_REQUIRED/);
  assert.throws(() => createEvidenceStore({ put() {}, head() {}, get() {} }),
    /EVIDENCE_STORE_METHOD_REQUIRED:delete/);
});

test("evidence store validates inputs and freezes copied metadata", async () => {
  const adapter = createMemoryAdapter();
  const store = createEvidenceStore(adapter);

  assert.throws(
    () => store.put(null, { contentType: "text/plain" }),
    /EVIDENCE_STREAM_REQUIRED/
  );
  assert.throws(
    () => store.put(Readable.from("evidence"), null),
    /EVIDENCE_METADATA_REQUIRED/
  );
  assert.throws(() => store.head(" "), /EVIDENCE_KEY_REQUIRED/);
  assert.throws(() => store.get(""), /EVIDENCE_KEY_REQUIRED/);
  assert.throws(() => store.delete(""), /EVIDENCE_KEY_REQUIRED/);

  let receivedMetadata;
  const observingAdapter = {
    ...adapter,
    async put(stream, metadata) {
      receivedMetadata = metadata;
      return adapter.put(stream, metadata);
    }
  };
  const observedStore = createEvidenceStore(observingAdapter);
  const inputMetadata = { contentType: "text/plain", purpose: "test" };
  const result = await observedStore.put(Readable.from("sample"), inputMetadata);

  assert.notEqual(receivedMetadata, inputMetadata);
  assert.equal(Object.isFrozen(receivedMetadata), true);
  assert.deepEqual(inputMetadata, { contentType: "text/plain", purpose: "test" });
  assert.match(result.key, /^test-only\//);
});

test("memory adapter round-trips bytes, reports integrity metadata, and deletes", async () => {
  const store = createEvidenceStore(createMemoryAdapter());
  const original = Buffer.from("private evidence test payload");
  const expectedHash = createHash("sha256").update(original).digest("hex");

  const saved = await store.put(Readable.from([original]), {
    contentType: "text/plain",
    purpose: "contract-test"
  });

  assert.equal(saved.sizeBytes, original.length);
  assert.equal(saved.sha256, expectedHash);
  assert.equal(saved.contentType, "text/plain");
  assert.deepEqual(await store.head(saved.key), saved);

  const readable = await store.get(saved.key);
  assert.ok(readable);
  const chunks = [];
  for await (const chunk of readable) chunks.push(Buffer.from(chunk));
  assert.deepEqual(Buffer.concat(chunks), original);

  assert.equal(await store.delete(saved.key), true);
  assert.equal(await store.head(saved.key), null);
  assert.equal(await store.get(saved.key), null);
  assert.equal(await store.delete(saved.key), false);
});
