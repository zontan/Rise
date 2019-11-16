export function attribute(value: number | null) {
  if (value === null) {
    return "N/A";
  } else {
    return value.toString();
  }
}
