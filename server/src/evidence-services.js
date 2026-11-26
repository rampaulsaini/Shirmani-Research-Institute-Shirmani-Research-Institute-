import { randomUUID } from "node:crypto";

const MAX_BYTES = 10 * 1024 * 1024;
const ALLOWED_TYPES = new Set([
  "application/pdf",
  "image/jpeg",
  "image/png",
  "text/plain"
]);
const PURPOSES = new Set([
  "written_acceptance",
  "payment_proof",
  "payment_consent",
  "delivery",
  "customer_acceptance"
]);
const KEY_PREFIX = "sri-evidence/";

export class EvidenceServiceError extends Error {
  constructor(code, status = 400) {
    super(code);
    this.name = "EvidenceServiceError";
    this.code = code;
    this.status = status;
  }
}

const fail = (code, status) => { throw new EvidenceServiceError(code, status); };

export function createEvidenceServices({ storage = null, notifications = null } = {}) {
  const requireStorage = () => {
    if (!storage) fail("EVIDENCE_STORAGE_NOT_CONFIGURED", 503);
    for (const method of ["createUploadIntent", "headObject", "createSignedDownload", "deleteObject"]) {
      if (typeof storage[method] !== "function") fail("EVIDENCE_STORAGE_ADAPTER_INVALID", 503);
    }
    return storage;
  };

  return Object.freeze({
    async createUploadIntent({ orderId, purpose, contentType, byteSize, sha256 }) {
      const backend = requireStorage();
      if (typeof orderId !== "string" || !orderId.trim()) fail("ORDER_REQUIRED");
      if (!PURPOSES.has(purpose)) fail("EVIDENCE_PURPOSE_INVALID");
      if (!ALLOWED_TYPES.has(contentType)) fail("EVIDENCE_CONTENT_TYPE_NOT_ALLOWED", 415);
      if (!Number.isSafeInteger(byteSize) || byteSize < 1 || byteSize > MAX_BYTES) fail("EVIDENCE_SIZE_INVALID", 413);
      if (typeof sha256 !== "string" || !/^[a-f0-9]{64}$/i.test(sha256)) fail("EVIDENCE_SHA256_REQUIRED");

      const objectKey = KEY_PREFIX + randomUUID();
      const intent = await backend.createUploadIntent({
        objectKey,
        metadata: { orderId, purpose, contentType, byteSize, sha256: sha256.toLowerCase() },
        contentType,
        byteSize
      });
      if (!intent || typeof intent.uploadUrl !== "string" || !intent.uploadUrl.startsWith("https://")) {
        fail("EVIDENCE_UPLOAD_INTENT_INVALID", 502);
      }
      return Object.freeze({ objectKey, uploadUrl: intent.uploadUrl, expiresAt: intent.expiresAt ?? null });
    },

    async finalizeUpload({ objectKey, orderId, purpose, sha256 }) {
      const backend = requireStorage();
      if (typeof objectKey !== "string" || !objectKey.startsWith(KEY_PREFIX) ||
          !/^sri-evidence\/[0-9a-f-]{36}$/i.test(objectKey)) fail("EVIDENCE_OBJECT_KEY_INVALID");
      if (typeof orderId !== "string" || !orderId.trim() || !PURPOSES.has(purpose)) fail("EVIDENCE_BINDING_INVALID");
      if (typeof sha256 !== "string" || !/^[a-f0-9]{64}$/i.test(sha256)) fail("EVIDENCE_SHA256_REQUIRED");
      const object = await backend.headObject({ objectKey });
      if (!object) fail("EVIDENCE_OBJECT_NOT_FOUND", 404);
      const metadata = object.metadata || {};
      if (metadata.orderId !== orderId || metadata.purpose !== purpose) fail("EVIDENCE_BINDING_MISMATCH", 403);
      if (!ALLOWED_TYPES.has(object.contentType) || object.contentType !== metadata.contentType) fail("EVIDENCE_CONTENT_TYPE_MISMATCH", 415);
      if (!Number.isSafeInteger(object.byteSize) || object.byteSize < 1 || object.byteSize > MAX_BYTES ||
          object.byteSize !== metadata.byteSize) fail("EVIDENCE_SIZE_MISMATCH", 400);
      if (typeof object.sha256 !== "string" || object.sha256.toLowerCase() !== sha256.toLowerCase() ||
          metadata.sha256 !== sha256.toLowerCase()) fail("EVIDENCE_HASH_MISMATCH", 400);
      return Object.freeze({
        objectKey,
        orderId,
        purpose,
        contentType: object.contentType,
        byteSize: object.byteSize,
        sha256: object.sha256.toLowerCase(),
        verified: true
      });
    },

    async getAuthorizedDownload({ objectKey, authorize, expiresInSeconds = 60 }) {
      const backend = requireStorage();
      if (typeof authorize !== "function") fail("EVIDENCE_AUTHORIZATION_REQUIRED", 403);
      if (!Number.isInteger(expiresInSeconds) || expiresInSeconds < 1 || expiresInSeconds > 300) {
        fail("EVIDENCE_DOWNLOAD_TTL_INVALID");
      }
      const allowed = await authorize();
      if (allowed !== true) fail("EVIDENCE_ACCESS_DENIED", 403);
      if (typeof objectKey !== "string" || !/^sri-evidence\/[0-9a-f-]{36}$/i.test(objectKey)) {
        fail("EVIDENCE_OBJECT_KEY_INVALID");
      }
      const result = await backend.createSignedDownload({ objectKey, expiresInSeconds });
      if (!result || typeof result.url !== "string" || !result.url.startsWith("https://")) {
        fail("EVIDENCE_DOWNLOAD_URL_INVALID", 502);
      }
      return Object.freeze({ url: result.url, expiresAt: result.expiresAt ?? null });
    },

    async deleteEvidence({ objectKey, authorize }) {
      const backend = requireStorage();
      if (typeof authorize !== "function" || await authorize() !== true) fail("EVIDENCE_ACCESS_DENIED", 403);
      if (typeof objectKey !== "string" || !/^sri-evidence\/[0-9a-f-]{36}$/i.test(objectKey)) {
        fail("EVIDENCE_OBJECT_KEY_INVALID");
      }
      await backend.deleteObject({ objectKey });
      return Object.freeze({ deleted: true });
    },

    async sendAcceptanceLink({ orderId, verifiedContact, token }) {
      if (!notifications || typeof notifications.sendAcceptanceLink !== "function") {
        fail("CUSTOMER_NOTIFICATION_NOT_CONFIGURED", 503);
      }
      if (typeof orderId !== "string" || !orderId.trim() ||
          typeof verifiedContact !== "string" || !verifiedContact.trim() ||
          typeof token !== "string" || token.length < 32) fail("CUSTOMER_NOTIFICATION_INPUT_INVALID");
      // Adapter contract: the implementation must never log or persist the raw token.
      const result = await notifications.sendAcceptanceLink({ orderId, verifiedContact, token });
      if (!result || result.accepted !== true) fail("CUSTOMER_NOTIFICATION_NOT_ACCEPTED", 502);
      return Object.freeze({ accepted: true });
    }
  });
}
