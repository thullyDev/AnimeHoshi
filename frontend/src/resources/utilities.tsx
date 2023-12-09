export function slugify(text: string) {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9 -]/g, "") // Remove special characters
    .replace(/\s+/g, "-") // Replace spaces with hyphens
    .replace(/-+/g, "-"); // Replace consecutive hyphens with a single hyphen
}

export function replaceAll(input: string, search: string, replacement: string) {
  const parts = input.split(search);
  const result = parts.join(replacement);
  return result;
}
