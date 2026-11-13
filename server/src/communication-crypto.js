import { createCipheriv, createDecipheriv, createHash, randomBytes } from "node:crypto";

const ALGORITHM = "aes-256-gcm";
const FORMAT_VERSION = 1;

function parseKey(value) {
  if (typeof value !== "string" || !/^[A-Za-z0-9+/]{43}=$/.test(value)) {
    throw new Error("EMAIL_CONTENT_KEY must be a base64-encoded 32-byte key");
  }
  const key = Buffer.from(value, "base64");
  if (key.length !== 32 || key.toString("base64") !== value) {
    throw new Error("EMAIL_CONTENT_KEY must be a canonical base64-encoded 32-byte key");
  }
  return key;
}

/**
 * Encrypt message content before it is written to PostgreSQL.
 * Store the returned ciphertext, key version and SHA-256 separately.
 * The key must come from a secret manager/environment, never from the database.
 */
export function encryptMessageContent(plaintext, options = {}) {
  if (typeof plaintext !== "string") throw new TypeError("Message content must be a string");
  const key = Buffer.isBuffer(options.key) ? options.key : parseKey(options.key ?? process.env.EMAIL_CONTENT_KEY);
  if (key.length !== 32) throw new Error("Email content encryption key must be 32 bytes");
  const keyVersion = options.keyVersion ?? process.env.EMAIL_CONTENT_KEY_VERSION;
  if (typeof keyVersion !== "string" || !/^[A-Za-z0-9._-]{1,64}$/.test(keyVersion)) {
    throw new Error("EMAIL_CONTENT_KEY_VERSION must be configured");
  }

  const nonce = randomBytes(12);
  const cipher = createCipheriv(ALGORITHM, key, nonce);
  const ciphertext = Buffer.concat([cipher.update(plaintext, "utf8"), cipher.final()]);
  const tag = cipher.getAuthTag();
  const envelope = Buffer.from(JSON.stringify({
    v: FORMAT_VERSION,
    alg: ALGORITHM,
    nonce: nonce.toString("base64"),
    tag: tag.toString("base64"),
    data: ciphertext.toString("base64")
  }), "utf8");

  return {
    encryptedContent: envelope,
    contentKeyVersion: keyVersion,
    contentSha256: createHash("sha256").update(plaintext, "utf8").digest("hex")
  };
}

/** Decrypt only with the matching externally supplied key version. */
export function decryptMessageContent(encryptedContent, options = {}) {
  const key = Buffer.isBuffer(options.key) ? options.key : parseKey(options.key ?? process.env.EMAIL_CONTENT_KEY);
  if (key.length !== 32) throw new Error("Email content encryption key must be 32 bytes");
  const expectedVersion = options.keyVersion ?? process.env.EMAIL_CONTENT_KEY_VERSION;
  if (typeof expectedVersion !== "string" || !/^[A-Za-z0-9._-]{1,64}$/.test(expectedVersion)) {
    throw new Error("EMAIL_CONTENT_KEY_VERSION must be configured");
  }
  if (!Buffer.isBuffer(encryptedContent)) throw new TypeError("Encrypted content must be a Buffer");

  let envelope;
  try { envelope = JSON.parse(encryptedContent.toString("utf8")); }
  catch { throw new Error("Invalid encrypted content envelope"); }
  if (envelope?.v !== FORMAT_VERSION || envelope?.alg !== ALGORITHM) {
    throw new Error("Unsupported encrypted content format");
  }
  const decode = (value, expectedLength, label) => {
    if (typeof value !== "string" || !/^[A-Za-z0-9+/]+={0,2}$/.test(value)) throw new Error("Invalid " + label);
    const result = Buffer.from(value, "base64");
    if (result.toString("base64") !== value || (expectedLength && result.length !== expectedLength)) throw new Error("Invalid " + label);
    return result;
  };
  const nonce = decode(envelope.nonce, 12, "nonce");
  const tag = decode(envelope.tag, 16, "authentication tag");
  const ciphertext = decode(envelope.data, null, "ciphertext");
  const decipher = createDecipheriv(ALGORITHM, key, nonce);
  decipher.setAuthTag(tag);
  const plaintext = Buffer.concat([decipher.update(ciphertext), decipher.final()]).toString("utf8");
  return { plaintext, contentKeyVersion: expectedVersion, contentSha256: createHash("sha256").update(plaintext, "utf8").digest("hex") };
}
