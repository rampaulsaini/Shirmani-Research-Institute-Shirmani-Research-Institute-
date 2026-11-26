import { createHash, randomUUID } from "node:crypto";

export const EVIDENCE_MIME_TYPES = Object.freeze([
  "image/jpeg",
  "image/png",
  "application/pdf",
  "text/plain"
]);

export const DEFAULT_MAX_EVIDENCE_BYTES = 10 * 1024 * 1024;

/**
 * Provider-neutral private evidence service.
 *
 * The adapter is deliberately injected: this module does not provision a
 * bucket, choose a region, or contact Cloudflare. A future R2 adapter must
 * implement these methods with a private bucket and server-side credentials.
 */
export function createPrivateEvidenceStorage({
  adapter,
  maxBytes = DEFAULT_MAX_EVIDENCE_BYTES,
  clock = () => new Date()
} = {}) {
  if (!adapter ||
      typeof adapter.putPrivateObject !== "function" ||
      typeof adapter.headPrivateObject !== "function" ||
      typeof adapter.createSignedGetUrl !== "function") {
    throw new TypeError("A private-object storage adapter is required");
  }
  if (!Number.isSafeInteger(maxBytes) || maxBytes < 1) {
    throw new TypeError("maxBytes must be a positive safe integer");
  }

  return Object.freeze({
    async store({ ownerId, orderId, purpose, contentType, bytes }) {
      if (typeof ownerId !== "string" || !ownerId.trim() ||
          typeof orderId !== "string" || !orderId.trim() ||
          typeof purpose !== "string" || !/^[a-z][a-z0-9_-]{1,39}$/.test(purpose)) {
        throw new TypeError("Valid owner, order and evidence purpose are required");
      }
      if (!EVIDENCE_MIME_TYPES.includes(contentType)) {
        throw new TypeError("Evidence content type is not allowed");
      }
      if (!(bytes instanceof Uint8Array) || bytes.byteLength < 1 || bytes.byteLength > maxBytes) {
        throw new RangeError("Evidence size is outside the allowed range");
      }

      const body = Buffer.from(bytes);
      const sha256 = createHash("sha256").update(body).digest("hex");
      const key = `evidence/${randomUUID()}`;
      const createdAt = clock().toISOString();

      await adapter.putPrivateObject({
        key,
        body,
        contentType,
        metadata: { ownerId, orderId, purpose, sha256 }
      });

      const stored = await adapter.headPrivateObject({ key });
      if (!stored ||
          stored.contentType !== contentType ||
          stored.byteSize !== body.byteLength ||
          stored.sha256 !== sha256) {
        throw new Error("Stored evidence failed server-side integrity verification");
      }

      return Object.freeze({
        key,
        ownerId,
        orderId,
        purpose,
        contentType,
        byteSize: body.byteLength,
        sha256,
        status: "verified",
        createdAt
      });
    },

    async createOwnerDownload({ evidence, requesterId, authorizeOwner, expiresInSeconds = 60 }) {
      if (!evidence || typeof evidence.key !== "string" ||
          typeof requesterId !== "string" ||
          typeof authorizeOwner !== "function" ||
          !Number.isInteger(expiresInSeconds) ||
          expiresInSeconds < 1 || expiresInSeconds > 300) {
        throw new TypeError("Valid evidence, requester, authorization and short expiry are required");
      }
      const allowed = await authorizeOwner({
        requesterId,
        ownerId: evidence.ownerId,
        orderId: evidence.orderId
      });
      if (allowed !== true) {
        const error = new Error("Evidence access denied");
        error.code = "EVIDENCE_ACCESS_DENIED";
        throw error;
      }
      const result = await adapter.createSignedGetUrl({
        key: evidence.key,
        expiresInSeconds
      });
      if (!result || typeof result.url !== "string" || !result.url.startsWith("https://")) {
        throw new Error("Storage adapter did not return a secure HTTPS URL");
      }
      return Object.freeze({
        url: result.url,
        expiresInSeconds
      });
    }
  });
}
