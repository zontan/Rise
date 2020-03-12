const baseValues: Record<number, number> = {
  1: 14,
  2: 16,
  3: 18,
  4: 21,
  5: 24,
  6: 27,
  7: 30,
  8: 34,
  9: 38,
  10: 43,
  11: 48,
  12: 54,
  13: 61,
  14: 69,
  15: 77,
  16: 86,
  17: 96,
  18: 108,
  19: 122,
  20: 138,
  21: 154,
  22: 172,
  23: 192,
  24: 216,
  25: 244,
};

export function woundResistanceByLevel(level: number, constitution: number | null) {
  return baseValues[Math.max(level, constitution || 0)];
}
