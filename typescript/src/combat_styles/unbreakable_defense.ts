import { CombatStyle } from ".";

export const unbreakableDefense: CombatStyle = {
  name: "Unbreakable Defense",
  shortDescription: "Guard yourself and your allies with careful attacks and recovery abilities.",

  maneuvers: [
    {
      name: "Parry",

      functionsLike: {
        abilityType: "ability",
        exceptThat: `
          you gain an additional +2 bonus to Armor defense.
          In addition, whenever a creature misses you with a melee \\glossterm{strike} this round, that creature takes a -2 penalty to Armor defense during the next round.
          As normal, this bonus does not stack with itself, even if the same creature misses you with multiple melee attacks.
          This ability is \\abilitytag{Swift}, so it protects you from attacks in the current phase.
        `,
        name: "total defense",
      },
      rank: 1,
      scaling: {
        3: "The penalty increases to -3.",
        5: "The penalty increases to -4.",
        7: "The penalty increases to -5.",
      },
      tags: ["Swift"],
      type: "Duration",
    },

    {
      name: "Redirecting Parry",

      functionsLike: {
        abilityType: "ability",
        exceptThat: `
          you gain an additional +2 bonus to Armor defense.
          In addition, whenever a creature misses you with a melee \\glossterm{strike} this round, that creature treats itself as a target of that strike in addition to any other targets.
          It cannot choose to reduce its accuracy or damage against itself.
          This ability is \\abilitytag{Swift}, so it protects you from attacks in the current phase.
        `,
        name: "total defense",
      },
      rank: 3,
      scaling: {
        5: "A creature that makes a strike against itself in this way takes a -2 penalty to defenses against that strike.",
        7: "The penalty increases to -4.",
      },
      tags: ["Swift"],
      type: "Duration",
    },

    {
      name: "Flamboyant Parry",

      functionsLike: {
        abilityType: "ability",
        exceptThat: `
          you gain an additional +2 bonus to Armor defense.
          In addition, whenever a creature misses you with a melee \\glossterm{strike} this round, that creature becomes \\glossterm{dazed} as a \\glossterm{condition}.
          This ability is \\abilitytag{Swift}, so it protects you from attacks in the current phase.
        `,
        name: "total defense",
      },
      rank: 5,
      scaling: {
        7: "The Armor defense bonus increases to +3.",
      },
      tags: ["Swift"],
      type: "Duration",
    },

    {
      name: "Reflective Parry",

      functionsLike: {
        abilityType: "ability",
        exceptThat: `
          you gain an additional +2 bonus to Armor defense.
          In addition, whenever a creature misses you with a \\glossterm{targeted} attack this round, that creature treats itself as a target of that attack in addition to any other targets.
          This ability is \\abilitytag{Swift}, so it protects you from attacks in the current phase.
        `,
        name: "total defense",
      },
      rank: 7,
      tags: ["Swift"],
      type: "Duration",
    },

    {
      name: "Brace for Impact",

      effect: `
        You are \\glossterm{impervious} to \\glossterm{physical damage} this round.
        This halving is applied before \\glossterm{resistances} and similar abilities.
        Because this is a \\abilitytag{Swift} ability, it affects damage you take during the current phase.
      `,
      rank: 2,
      scaling: {
        4: "You are impervious to all damage, not just physical damage.",
        6: "You also negate any \\glossterm{conditions} that you would gain this round.",
      },
      tags: ["Swift"],
      type: "Duration",
    },

    {
      name: "Bracing Strike",

      effect: `
        Make a \\glossterm{strike} with a -2d damage penalty.
        Your \\glossterm{power} with the strike is halved.

        In addition, you are \\glossterm{impervious} to \\glossterm{physical damage} this round.
        This halving is applied before \\glossterm{resistances} and similar abilities.
        Becoming impervious in this way is a \\abilitytag{Swift} ability, so it affects damage you take during the current phase.
      `,
      rank: 5,
      scaling: {
        7: "You are impervious to all damage, not just physical damage.",
      },
      type: "Duration",
    },

    {
      name: "Second Wind",

      effect: `
        When you use this ability, you increase your \\glossterm{fatigue level} by two.

        You regain hit points equal to your maximum \\glossterm{hit points}.
        If you take damage in the same phase that you use this ability, the healing and damage offset, which can prevent you from gaining vital wounds from dropping below 0 hit points (see \\pcref{Regaining Hit Points and Resistances}).

        After you use this ability, you cannot use it again until you take a \\glossterm{short rest}.
      `,
      rank: 4,
      tags: [],
      scaling: {
        6: `
          You can also remove a single condition.
          This cannot remove a condition applied during the current round.
        `,
      },
      type: "Duration",
    },

    {
      name: "Shield Slam",

      effect: `
        Make a \\glossterm{strike} using a shield.
        Your \\glossterm{power} with the strike is halved.
        Each creature that loses \\glossterm{hit points} from the strike is \\sickened as a \\glossterm{condition}.
      `,
      rank: 1,
      scaling: {
        3: "You gain a +1 accuracy bonus with the strike.",
        5: "The accuracy bonus increases to +2.",
        7: "The accuracy bonus increases to +3.",
      },
      type: "Duration",
    },

    {
      name: "Nauseating Shield Slam",

      effect: `
        Make a \\glossterm{strike} with -1d damage penalty using a shield.
        Your \\glossterm{power} with the strike is halved.
        Each creature that loses \\glossterm{hit points} from the strike is \\nauseated as a \\glossterm{condition}.
      `,
      scaling: {
        5: "You gain a +1 accuracy bonus with the strike.",
        7: "The accuracy bonus increases to +2.",
      },
      rank: 3,
      type: "Duration",
    },

    {
      name: "Defensive Strike",

      effect: `
        Make a melee \\glossterm{strike}.
        You take a -1d penalty to damage with the strike.
        In exchange, you gain a +2 bonus to Armor and Reflex defenses until the end of the round.
        The defense bonus is a \\abilitytag{Swift} effect, so it protects you from attacks in the current phase.
      `,
      rank: 2,
      scaling: {
        4: "The defense bonuses increase to +3.",
        6: "The defense bonuses increase to +4.",
      },
      tags: ["Swift (see text)"],
      type: "Duration",
    },

    // TODO: change to rank 5 once campaigns progress far enough
    {
      name: "Cleansing Strike",

      effect: `
        Make a strike.
        You take a -2d penalty to damage with the strike.
        In addition, you may remove a \\glossterm{condition} affecting you.
        This cannot remove a condition applied during the current round.
        The penalties from the condition still affect you when you make the strike.
      `,
      rank: 4,
      scaling: {
        6: "The damage penalty is reduced to -1d.",
      },
      type: "Duration",
    },

    {
      name: "Revitalizing Strike",

      effect: `
        Make a strike.
        In addition, you regain 1d10 hit points.
        After you use this ability, you cannot use it or any other \\abilitytag{Healing} ability until after the end of the next round.
      `,
      scaling: {
        special: "The healing increases by +1d for each rank beyond 3.",
      },
      rank: 3,
      tags: ['Healing'],
      type: "Instant",
    },

    {
      name: "Bracing Strike",

      effect: `
        Make a strike.
        In addition, you gain a +1 bonus to \\glossterm{vital rolls} until the end of the round.
        This bonus is a \\abilitytag{Swift} effect, so it affects any vital wounds you gain during the current phase.
      `,
      rank: 2,
      scaling: {
        4: "The bonus increases to +2.",
        6: "The bonus increases to +3.",
      },
      tags: ["\\abilitytag{Swift} (see text)"],
      type: "Duration",
    },

    {
      name: "Guard the Pass",

      effect: `
        Make a melee \\glossterm{strike}.
        Until the end of the next round, your \\glossterm{enemies} treat all squares within a \\tinyarea radius from you as \\glossterm{difficult terrain}.
      `,
      rank: 1,
      scaling: {
        3: "The area increases to a \\smallarea radius \\glossterm{emanation} from you.",
        5: "The area increases to a \\medarea radius \\glossterm{emanation} from you.",
        7: "The area increases to a \\largearea radius \\glossterm{emanation} from you.",
      },
      type: "Duration",
    },

    {
      name: "Prepared Defense",

      effect: `
        Make a \\glossterm{strike} with a -1d damage penalty.
        After you make the strike, choose any one defense: Armor, Fortitude, Reflex, or Mental.
        You gain a +2 bonus to that defense during the next round.
      `,
      rank: 1,
      scaling: {
        3: "The bonus increases to +3.",
        5: "The bonus increases to +4.",
        7: "The bonus increases to +5.",
      },
      type: "Duration",
    },
  ],
};
