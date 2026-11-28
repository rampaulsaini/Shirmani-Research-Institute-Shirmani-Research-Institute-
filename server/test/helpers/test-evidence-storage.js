import { assertEvidenceStorageAdapter } from "../../src/evidence-storage/contract.js";
import { createHash, randomUUID } from "node:crypto";
import { mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";

// Disposable CI/test fixture only. Production routes must never import this adapter.
const MAX_BYTES = 5 * 1024 * 1024;
const ALLOWED_TYPES = new Set([
  "application/pdf",
  "image/jpeg",
  "image/png",
  "text/plain"
]);

export async function createTestEvidenceStorage() {
  const root = await mkdtemp(join(tmpdir(), "sri-evidence-test-"));
  const records = new Map();
  let closed = false;

  const assertOpen = () => {
    if (closed) throw new Error("EVIDENCE_STORAGE_CLOSED");
  };
  const authorize = (record, ownerId, orderId) => {
    if (!record || record.ownerId !== ownerId || record.orderId !== orderId) {
      throw new Error("EVIDENCE_ACCESS_DENIED");
    }
  };

  return assertEvidenceStorageAdapter({
    async put({ bytes, contentType, ownerId, orderId }) {
      assertOpen();
      if (!ownerId || !orderId) throw new Error("EVIDENCE_OWNER_AND_ORDER_REQUIRED");
      if (!Buffer.isBuffer(bytes) && !(bytes instanceof Uint8Array)) {
        throw new Error("EVIDENCE_BYTES_REQUIRED");
      }
      const body = Buffer.from(bytes);
      if (!body.length || body.length > MAX_BYTES) throw new Error("EVIDENCE_SIZE_INVALID");
      if (!ALLOWED_TYPES.has(contentType)) throw new Error("EVIDENCE_CONTENT_TYPE_INVALID");

      const key = randomUUID();
      const sha256 = createHash("sha256").update(body).digest("hex");
      await writeFile(join(root, key), body, { flag: "wx", mode: 0o600 });
      records.set(key, { ownerId, orderId, contentType, byteLength: body.length, sha256 });
      return { key, sha256, byteLength: body.length, contentType };
    },

    async get({ key, ownerId, orderId }) {
      assertOpen();
      const record = records.get(key);
      authorize(record, ownerId, orderId);
      const bytes = await readFile(join(root, key));
      return { bytes, ...record };
    },

    async delete({ key, ownerId, orderId }) {
      assertOpen();
      const record = records.get(key);
      authorize(record, ownerId, orderId);
      await rm(join(root, key), { force: true });
      records.delete(key);
      return { deleted: true };
    },

    async close() {
      if (closed) return;
      closed = true;
      records.clear();
      await rm(root, { recursive: true, force: true });
    }
  });
}
