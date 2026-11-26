import assert from "node:assert/strict";
import { Readable } from "node:stream";
import test from "node:test";
import { createEvidenceStore } from "../src/evidence-store.js";

test("evidence store rejects missing or incomplete adapters", () => {
  assert.throws(() => createEvidenceStore(), {
    name: "TypeError",
    message: "EVIDENCE_STORE_ADAPTER_REQUIRED"
  });

  for (const missing of ["put", "head", "get", "delete"]) {
    const adapter = {
      put() {}, head() {}, get() {}, delete() {}
    };
    delete adapter[missing];
    assert.throws(() => createEvidenceStore(adapter), {
      name: "TypeError",
      message: `EVIDENCE_STORE_METHOD_REQUIRED:${missing}`
    });
  }
});

test("evidence store validates upload stream and metadata before delegation", async () => {
  const calls = [];
  const adapter = {
    async put(stream, metadata) {
      calls.push({ stream, metadata });
      return { key: "opaque/test-key", sha256: "a".repeat(64), sizeBytes: 3, contentType: "text/plain" };
    },
    async head() { return null; },
    async get() { return null; },
    async delete() { return false; }
  };
  const store = createEvidenceStore(adapter);

  assert.throws(() => store.put(null, { purpose: "payment" }), {
    name: "TypeError",
    message: "EVIDENCE_STREAM_REQUIRED"
  });
  assert.throws(() => store.put(Readable.from("abc"), null), {
    name: "TypeError",
    message: "EVIDENCE_METADATA_REQUIRED"
  });

  const stream = Readable.from("abc");
  const metadata = { purpose: "payment", contentType: "text/plain" };
  const result = await store.put(stream, metadata);
  assert.deepEqual(result, {
    key: "opaque/test-key",
    sha256: "a".repeat(64),
    sizeBytes: 3,
    contentType: "text/plain"
  });
  assert.equal(calls.length, 1);
  assert.equal(calls[0].stream, stream);
  assert.deepEqual(calls[0].metadata, metadata);
  assert.notEqual(calls[0].metadata, metadata);
  assert.equal(Object.isFrozen(calls[0].metadata), true);
  assert.equal(Object.isFrozen(store), true);
});

test("evidence store validates keys and delegates object operations", async () => {
  const seen = [];
  const adapter = {
    async put() { return null; },
    async head(key) { seen.push(["head", key]); return { sizeBytes: 7 }; },
    async get(key) { seen.push(["get", key]); return Readable.from("evidence"); },
    async delete(key) { seen.push(["delete", key]); return true; }
  };
  const store = createEvidenceStore(adapter);

  for (const operation of ["head", "get", "delete"]) {
    assert.throws(() => store[operation]("  "), {
      name: "TypeError",
      message: "EVIDENCE_KEY_REQUIRED"
    });
  }

  assert.deepEqual(await store.head("opaque/key"), { sizeBytes: 7 });
  assert.equal((await store.get("opaque/key")).readable, true);
  assert.equal(await store.delete("opaque/key"), true);
  assert.deepEqual(seen, [
    ["head", "opaque/key"],
    ["get", "opaque/key"],
    ["delete", "opaque/key"]
  ]);
});

test("contract does not claim that an opaque key proves object existence", async () => {
  const store = createEvidenceStore({
    async put() { return { key: "opaque/missing", sha256: "b".repeat(64), sizeBytes: 1, contentType: "text/plain" }; },
    async head() { return null; },
    async get() { return null; },
    async delete() { return false; }
  });

  const saved = await store.put(Readable.from("x"), { purpose: "test" });
  assert.equal(saved.key, "opaque/missing");
  assert.equal(await store.head(saved.key), null);
  assert.equal(await store.get(saved.key), null);
});
