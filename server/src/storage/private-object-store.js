import { createHash, createHmac, randomBytes, timingSafeEqual } from "node:crypto";

const DEFAULT_ALLOWED_MIME_TYPES = [
  "application/pdf",
  "text/plain",
  "image/jpeg",
  "image/png",
  "image/webp"
];

const fail = code => Object.assign(new Error(code), { code });

function validateKey(key) {
  if (typeof key !== "string" || key.length > 240 || !key) throw fail("INVALID_OBJECT_KEY");
  const segments = key.split("/");
  if (segments.some(segment => !/^[A-Za-z0-9][A-Za-z0-9_-]{0,99}$/.test(segment))) {
    throw fail("INVALID_OBJECT_KEY");
  }
  return key;
}

function validateSubject(subject) {
  if (typeof subject !== "string" || !subject.trim() || subject.length > 200) {
    throw fail("INVALID_GRANT_SUBJECT");
  }
  return subject;
}

/**
 * Provider-neutral private-object storage boundary.
 *
 * The adapter must implement private put/head/get/delete operations. This module
 * does not make an adapter private by itself: production adapters must enforce
 * private ACLs, transport security, encryption, and their own authorization.
 * Read grants are short-lived, subject-bound, single-use bearer capabilities.
 * The in-memory replay guard is process-local and is not a distributed replay
 * defense; production deployments must replace it with a shared atomic store.
 */
export function createPrivateObjectStore({
  adapter,
  signingSecret,
  clock = () => Date.now(),
  maxBytes = 10 * 1024 * 1024,
  allowedMimeTypes = DEFAULT_ALLOWED_MIME_TYPES
} = {}) {
  for (const method of ["putPrivate", "headPrivate", "getPrivate", "deletePrivate"]) {
    if (typeof adapter?.[method] !== "function") throw fail("INVALID_STORAGE_ADAPTER");
  }
  if (typeof signingSecret !== "string" || Buffer.byteLength(signingSecret) < 32) {
    throw fail("STORAGE_SIGNING_SECRET_TOO_SHORT");
  }
  if (!Number.isSafeInteger(maxBytes) || maxBytes < 1) throw fail("INVALID_STORAGE_SIZE_LIMIT");

  const allowed = new Set(allowedMimeTypes);
  const usedGrantIds = new Set();

  const sign = payload => createHmac("sha256", signingSecret).update(payload).digest("base64url");
  const encode = value => Buffer.from(JSON.stringify(value)).toString("base64url");

  function decodeAndVerify(token) {
    if (typeof token !== "string" || token.length > 2048) throw fail("INVALID_READ_GRANT");
    const parts = token.split(".");
    if (parts.length !== 2 || !parts[0] || !parts[1]) throw fail("INVALID_READ_GRANT");
    const expected = Buffer.from(sign(parts[0]));
    const actual = Buffer.from(parts[1]);
    if (expected.length !== actual.length || !timingSafeEqual(expected, actual)) {
      throw fail("INVALID_READ_GRANT");
    }
    let payload;
    try { payload = JSON.parse(Buffer.from(parts[0], "base64url").toString("utf8")); }
    catch { throw fail("INVALID_READ_GRANT"); }
    if (!payload || payload.v !== 1 || typeof payload.k !== "string" ||
        typeof payload.s !== "string" || typeof payload.n !== "string" ||
        !Number.isSafeInteger(payload.e)) throw fail("INVALID_READ_GRANT");
    return payload;
  }

  return Object.freeze({
    async put({ key, body, contentType }) {
      validateKey(key);
      if (!Buffer.isBuffer(body) && !(body instanceof Uint8Array)) throw fail("INVALID_OBJECT_BODY");
      const bytes = Buffer.from(body);
      if (bytes.length > maxBytes) throw fail("OBJECT_TOO_LARGE");
      if (typeof contentType !== "string" || !allowed.has(contentType.toLowerCase())) {
        throw fail("MIME_TYPE_NOT_ALLOWED");
      }
      const mime = contentType.toLowerCase();
      const sha256 = createHash("sha256").update(bytes).digest("hex");
      await adapter.putPrivate({ key, body: bytes, contentType: mime, sha256 });
      return Object.freeze({ key, contentType: mime, byteSize: bytes.length, sha256, visibility: "private" });
    },

    async head({ key }) {
      validateKey(key);
      const metadata = await adapter.headPrivate(key);
      return metadata ? Object.freeze({ ...metadata, visibility: "private" }) : null;
    },

    async issueReadGrant({ key, subject, ttlSeconds = 60 }) {
      validateKey(key);
      validateSubject(subject);
      if (!Number.isInteger(ttlSeconds) || ttlSeconds < 1 || ttlSeconds > 300) {
        throw fail("INVALID_GRANT_TTL");
      }
      const metadata = await adapter.headPrivate(key);
      if (!metadata) throw fail("OBJECT_NOT_FOUND");
      const payload = encode({
        v: 1,
        k: key,
        s: subject,
        e: Math.floor(clock() / 1000) + ttlSeconds,
        n: randomBytes(16).toString("base64url")
      });
      return Object.freeze({ token: payload + "." + sign(payload), expiresInSeconds: ttlSeconds });
    },

    async readWithGrant({ token, subject }) {
      validateSubject(subject);
      const grant = decodeAndVerify(token);
      if (grant.s !== subject) throw fail("GRANT_SUBJECT_MISMATCH");
      if (Math.floor(clock() / 1000) >= grant.e) throw fail("READ_GRANT_EXPIRED");
      if (usedGrantIds.has(grant.n)) throw fail("READ_GRANT_ALREADY_USED");
      // Reserve before awaiting I/O so concurrent requests cannot both consume it.
      usedGrantIds.add(grant.n);
      const stored = await adapter.getPrivate(grant.k);
      if (!stored || !Buffer.isBuffer(stored.body)) throw fail("OBJECT_NOT_FOUND");
      const body = Buffer.from(stored.body);
      const sha256 = createHash("sha256").update(body).digest("hex");
      if (stored.sha256 && stored.sha256 !== sha256) throw fail("OBJECT_INTEGRITY_MISMATCH");
      return Object.freeze({
        key: grant.k,
        body,
        contentType: stored.contentType,
        byteSize: body.length,
        sha256,
        visibility: "private"
      });
    },

    async delete({ key }) {
      validateKey(key);
      return Boolean(await adapter.deletePrivate(key));
    }
  });
}

export { DEFAULT_ALLOWED_MIME_TYPES };
