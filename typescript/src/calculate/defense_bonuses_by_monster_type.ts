import { DefenseType } from "@src/data";
import { MonsterType } from "@src/monsters/types";

export function defenseBonusesByMonsterType(monsterType: MonsterType): Record<DefenseType, number> {
  return {
    animal: {
      armor: 2,
      fortitude: 5,
      reflex: 4,
      mental: 3,
    },
    humanoid: {
      armor: 0,
      fortitude: 4,
      reflex: 4,
      mental: 4,
    },
  }[monsterType];
}
