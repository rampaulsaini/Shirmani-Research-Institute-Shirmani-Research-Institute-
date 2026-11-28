export function isValidContactEmail(value) {
  return typeof value === "string" && /^\S+@\S+\.\S+$/.test(value);
}
