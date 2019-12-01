import { MonsterBase } from "@src/monsters";
import { calculateChallengeRatingBonus, monsterPowerBonusByLevel } from ".";

export function calculateMagicalPower({
  attributes,
  challengeRating,
  level,
}: Pick<MonsterBase, "attributes" | "challengeRating" | "level">) {
  const crBonus = calculateChallengeRatingBonus(challengeRating);
  const monsterBonus = monsterPowerBonusByLevel(level);
  return Math.max(attributes.wil ?? 0, level) + crBonus * monsterBonus;
}
