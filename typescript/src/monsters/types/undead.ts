import { passiveAbilities } from "@src/passive_abilities";
import { addType, TypelessMonsterInput } from "./add_type";

export const undeadInput: TypelessMonsterInput[] = [
  {
    attackInputs: [
      {
        crit: "The target loses two \\glossterm{hit points}.",
        defense: "reflex",
        hit: "The target loses a \\glossterm{hit point}.",
        source: "magical",
        name: "Draining Touch",
        target: "One creature the allip \\glossterm{threatens}",
      },
    ],
    challengeRating: 4,
    level: 3,
    name: "allip",
    passiveAbilities: [
      passiveAbilities.incorporeal,
      {
        description: `
          At the end of each round, the allip makes an attack vs. Mental against each creature
          within an \\arealarge radius \\glossterm{emanation} from it.
          It cannot make this attack more than once against any individual target between \\glossterm{short rests}.
          \\hit Each target is \\glossterm{confused} as a \\glossterm{condition}.
        `,
        name: "Babble",
      },
    ],
    skillPoints: { awareness: 2, intimidate: 2, stealth: 2 },
    // TODO: add fly speed
    speed: 30,
    startingAttributes: { str: null, dex: 3, con: null, int: 1, per: 1, wil: 2 },
  },
];

export const undead = addType("undead", undeadInput);
