import assert from "node:assert/strict";
import test from "node:test";
import { EvidenceStore } from "../src/evidence-store.js";

class MemoryEvidenceAdapter {
  objects = new Map();

  async put({ body, metadata }) {
    const key = `test-object-${this.objects.size + 1}`;
    this.objects.set(key, { body: Buffer.from(body), metadata: { ...metadata } });
    return key;
  }

  async head(key) {
    const value = this.objects.get(key);
    return value ? { ...value.metadata } : null;
  }

  async get(key) {
    const value = this.objects.get(key);
    return value ? Buffer.from(value.body) : null;
  }

  async delete(key) {
    return this.objects.delete(key);
  }
}

const validEvidence = overrides => ({
  body: Buffer.from("test evidence"),
  contentType: "text/plain",
  purpose: "payment_proof",
  uploaderId: "test-owner",
  ...overrides
});

test("evidence store records opaque key, size and SHA-256 metadata", async () => {
  const adapter = new MemoryEvidenceAdapter();
  const store = new EvidenceStore(adapter);
  const saved = await store.put(validEvidence());

  assert.equal(saved.key, "test-object-1");
  assert.equal(saved.sizeBytes, Buffer.byteLength("test evidence"));
  assert.match(saved.checksumSha256, /^[a-f0-9]{64}$/);
  assert.equal(saved.purpose, "payment_proof");
  assert.equal((await store.head(saved.key)).checksumSha256, saved.checksumSha256);

  const loaded = await store.get(saved.key);
  assert.equal(loaded.body.toString(), "test evidence");
  assert.equal(loaded.metadata.uploaderId, "test-owner");
});

test("evidence store rejects unsupported content types and purposes", async () => {
  const store = new EvidenceStore(new MemoryEvidenceAdapter());
  await assert.rejects(store.put(validEvidence({ contentType: "text/html" })), /content type/);
  await assert.rejects(store.put(validEvidence({ purpose: "miscellaneous" })), /purpose/);
});

test("evidence store rejects empty, oversized and non-byte payloads", async () => {
  const store = new EvidenceStore(new MemoryEvidenceAdapter(), { maxBytes: 4 });
  await assert.rejects(store.put(validEvidence({ body: Buffer.alloc(0) })), /size/);
  await assert.rejects(store.put(validEvidence({ body: Buffer.alloc(5) })), /size/);
  await assert.rejects(store.put(validEvidence({ body: "not bytes" })), /Buffer or Uint8Array/);
});

test("evidence store verifies downloaded bytes against stored checksum and size", async () => {
  const adapter = new MemoryEvidenceAdapter();
  const store = new EvidenceStore(adapter);
  const saved = await store.put(validEvidence());
  adapter.objects.get(saved.key).body = Buffer.from("tampered");
  await assert.rejects(store.get(saved.key), /integrity check failed/);
});

test("evidence store returns null for missing objects and deletes by opaque key", async () => {
  const adapter = new MemoryEvidenceAdapter();
  const store = new EvidenceStore(adapter);
  assert.equal(await store.head("missing-object"), null);
  assert.equal(await store.get("missing-object"), null);
  const saved = await store.put(validEvidence());
  assert.equal(await store.delete(saved.key), true);
  assert.equal(await store.head(saved.key), null);
});

test("evidence store requires a complete adapter and valid key", async () => {
  assert.throws(() => new EvidenceStore({ put() {} }), /head\(\)/);
  const store = new EvidenceStore(new MemoryEvidenceAdapter());
  await assert.rejects(store.head(""), /opaque storage key/);
});
