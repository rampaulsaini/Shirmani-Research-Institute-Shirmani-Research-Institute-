import assert from "node:assert/strict";
import test from "node:test";
import { createEvidenceStore } from "../src/evidence-store.js";

function fakeDriver() {
  const objects = new Map();
  return {
    objects,
    async put(key, bytes, metadata) {
      objects.set(key, { bytes: Buffer.from(bytes), metadata: { ...metadata } });
    },
    async head(key) {
      const item = objects.get(key);
      return item ? { ...item.metadata } : null;
    },
    async get(key) {
      const item = objects.get(key);
      return item ? Buffer.from(item.bytes) : null;
    },
    async delete(key) {
      return objects.delete(key);
    }
  };
}

test("evidence store creates server-generated opaque keys and verifies stored bytes", async () => {
  const driver = fakeDriver();
  const store = createEvidenceStore(driver);
  const input = Buffer.from("private evidence");
  const saved = await store.put(input, { contentType: "text/plain", purpose: "payment_proof" });

  assert.match(saved.key, /^evidence\/[0-9a-f-]{36}$/);
  assert.equal(saved.byteSize, input.length);
  assert.match(saved.sha256, /^[a-f0-9]{64}$/);
  assert.equal((await store.head(saved.key)).sha256, saved.sha256);
  assert.deepEqual(await store.get(saved.key), input);
  assert.equal(await store.delete(saved.key), true);
  assert.equal(await store.head(saved.key), null);
  assert.equal(await store.get(saved.key), null);
});

test("evidence store rejects caller-selected keys, unsupported content and purposes", async () => {
  const store = createEvidenceStore(fakeDriver());
  await assert.rejects(store.put(Buffer.from("x"), {
    contentType: "text/html", purpose: "payment_proof"
  }), /content type/);
  await assert.rejects(store.put(Buffer.from("x"), {
    contentType: "text/plain", purpose: "arbitrary"
  }), /purpose/);
  await assert.rejects(store.head("private://user-selected-path"), /Invalid evidence key/);
  await assert.rejects(store.get("../outside"), /Invalid evidence key/);
  await assert.rejects(store.delete("evidence/not-a-uuid"), /Invalid evidence key/);
});

test("evidence store rejects empty, oversized and non-Buffer payloads", async () => {
  const store = createEvidenceStore(fakeDriver(), { maxBytes: 4 });
  await assert.rejects(store.put(Buffer.alloc(0), {
    contentType: "text/plain", purpose: "delivery"
  }), /size/);
  await assert.rejects(store.put(Buffer.alloc(5), {
    contentType: "text/plain", purpose: "delivery"
  }), /size/);
  await assert.rejects(store.put("not bytes", {
    contentType: "text/plain", purpose: "delivery"
  }), /Buffer/);
});

test("evidence store detects missing objects and tampered object bytes", async () => {
  const driver = fakeDriver();
  const store = createEvidenceStore(driver);
  const saved = await store.put(Buffer.from("original"), {
    contentType: "text/plain", purpose: "written_acceptance"
  });
  assert.equal(await store.get("evidence/00000000-0000-4000-8000-000000000000"), null);
  driver.objects.get(saved.key).bytes = Buffer.from("tampered");
  await assert.rejects(store.get(saved.key), /checksum or size/);
});

test("evidence store requires a complete provider driver", () => {
  assert.throws(() => createEvidenceStore({ put() {} }), /head\(\)/);
});
