import { MysticSphere } from ".";

export const channelDivinity: MysticSphere = {
  name: "Channel Divinity",
  shortDescription: "Invoke divine power to smite foes and gain power.",
  sources: ["divine"],

  cantrips: [
    {
      effect: `
        The magical essence of your deity or alignment is overlayed on your body as an aura.
        This represents your deity if you are a cleric, or your alignment if you are a paladin.
        In either case, you gain the ability to see the auras of other creatures using this spell if they are within \\rngshort range.
        If you see another creature with the same aura as you, this spell grants you the unerring knowledge of that similarity.
        This can allow you to identify other followers of your deity or alignment with certainty.

        This spell lasts until you use it again or until you \\glossterm{dismiss} it as a \\glossterm{free action}.
      `,
      focus: false,
      name: "Testament",
      scaling: {
        2: "The range increases to \\rngmed.",
        4: `
          If you are a cleric, you can also unerringly see an aura around creatures who worship your deity.
          If you are a paladin, you can also unerringly see an aura around creatures who share your devoted alignment.
        `,
        6: "The range increases to \\rnglong.",
      },
      type: "Duration",
    },
    {
      effect: `
        You emit \\glossterm{bright illumination} in a radius of your choice, up to a maximum of 15 feet, and \\glossterm{shadowy illumination} in twice that radius.
        The color of the light depends on the nature of your deity or alignment.
        Each deity has their own color or color combination.
        Typically, good is yellow, evil is purple, law is white, and chaos is a myriad of ever-changing colors.
      `,
      focus: false,
      name: "Divine Radiance",
      narrative: `
        You call on the majesty of your deity or alignment to radiate into the world.
      `,
      scaling: {
        2: "The maximum radius of bright illumination increases to 30 feet.",
        4: "The maximum radius of bright illumination increases to 60 feet.",
        6: "The maximum radius of bright illumination increases to 120 feet.",
      },
      type: "Sustain (minor)",
    },
  ],
  spells: [
    {
      name: "Faith Rewarded",

      effect: `
        At the end of the next round, you become infused with divine power.
        You remove one \\glossterm{brief} effect or \\glossterm{condition} affecting you and heal 2d6 \\glossterm{hit points}.
        This cannot remove an effect applied during that round.
        In addition, you gain a +4 bonus to \\glossterm{accuracy} during the round after you become infused with divine power.
        After you use this ability, you \\glossterm{briefly} cannot use it or any other \\abilitytag{Healing} ability.
      `,
      rank: 4,
      scaling: { special: "The healing increases by +1d for each rank beyond 4." },
      tags: ['Healing'],
      type: "Duration",
    },

    {
      name: "Divine Authority",

      effect: `
        You gain a +3 \\glossterm{magic bonus} to the Persuasion skill.
        In addition, you are treated as being \\glossterm{trained} in that skill if you would otherwise be untrained.
        `,
      rank: 1,
      scaling: {
        3: `The bonus increases to +4.`,
        5: `The bonus increases to +5.`,
        7: `The bonus increases to +6.`,
      },
      type: "Attune (self)",
    },

    {
      name: "Agent of the Divine",

      effect: `
        You gain a +2 \\glossterm{magic bonus} to \\glossterm{accuracy}.
        In addition, you gain a +4 \\glossterm{magic bonus} to \\glossterm{power}.
        `,
      rank: 5,
      scaling: { 7: `The accuracy bonus increases to +3, and the power bonus increases to +8.` },
      type: "Attune (self)",
    },

    {
      name: "Endurance of the Faithful",

      effect: `
        This spell does not have the \\abilitytag{Focus} tag.

        You are \\glossterm{impervious} to all damage this round.
        Because this is a \\abilitytag{Swift} ability, it affects damage you take during the current phase.
      `,
      focus: false,
      rank: 2,
      scaling: {
        4: `You also gain a +2 bonus to \\glossterm{vital rolls} this round.`,
        6: `The bonus to vital rolls increases to +4.`,
      },
      tags: ["Swift"],
      type: "Instant",
    },

    {
      name: "Divine Judgment",

      attack: {
        hit: `
          The subject takes 1d10 + \\glossterm{power} energy damage.
        `,
        targeting: `
          Make an attack vs. Mental against anything within \\medrange.
        `,
      },
      rank: 1,
      scaling: "damage",
      type: "Instant",
    },

    {
      name: "Greater Divine Judgment",

      attack: {
        hit: `
          The subject takes 4d6 + \\glossterm{power} energy damage.
        `,
        targeting: `
          Make an attack vs. Mental against anything within \\longrange.
        `,
      },
      rank: 4,
      scaling: "damage",
      type: "Instant",
    },

    {
      name: "Supreme Divine Judgment",

      attack: {
        hit: `
          The subject takes 6d10 + \\glossterm{power} energy damage.
        `,
        targeting: `
          Make an attack vs. Mental against anything within \\distrange.
        `,
      },
      rank: 7,
      scaling: "damage",
      type: "Instant",
    },

    {
      name: "Retributive Judgment",

      // +1 level for situational +2 accuracy
      attack: {
        hit: `
          The subject takes 1d10 + half \\glossterm{power} energy damage.
          If it loses \\glossterm{hit points} from this damage, it is \\glossterm{briefly} \\stunned.
          After it stops being stunned, it becomes immune to being stunned in this way until it takes a \\glossterm{short rest}.
        `,
        targeting: `
          Make an attack vs. Mental against anything within \\medrange.
          You gain a +2 bonus to accuracy with this attack if the target attacked you or one of your \\glossterm{allies} during the previous round.
        `,
      },
      rank: 2,
      scaling: "damage",
      type: "Duration",
    },

    {
      name: "Greater Retributive Judgment",

      functionsLike: {
        name: 'retributive judgment',
        exceptThat: 'the damage increases to 4d8 + \\glossterm{power}.',
      },
      rank: 6,
      scaling: "damage",
      type: "Duration",
    },

    {
      name: "Glimpse of Divinity",

      attack: {
        crit: "The condition must be removed twice before the effect ends.",
        glance: "The effect lasts \\glossterm{briefly}.",
        hit: `
          The subject is \\dazzled as a \\glossterm{condition}.
        `,
        targeting: `
          Make an attack vs. Mental against one creature within \\distrange.
        `,
      },
      rank: 3,
      scaling: "accuracy",
      type: "Duration",
    },

    {
      name: "Greater Glimpse of Divinity",

      functionsLike: {
        name: 'glimpse of divinity',
        exceptThat: 'the subject is also \\glossterm{dazed} as part of the same condition.',
      },
      rank: 7,
      scaling: "accuracy",
      type: "Duration",
    },

    {
      name: "Fear of the Divine",

      attack: {
        crit: "The subject is \\panicked instead of \\frightened.",
        glance: "The effect lasts \\glossterm{briefly}.",
        hit: `
          The subject is \\frightened by you as a \\glossterm{condition}.
        `,
        targeting: `
          Make an attack vs. Mental against one creature within \\medrange.
        `,
      },
      rank: 5,
      tags: ['Emotion'],
      scaling: "accuracy",
      type: "Duration",
    },

    {
      name: "Judge Unworthy",

      attack: {
        crit: "The penalty increases to -5.",
        // glance: '',
        hit: `
          As a \\glossterm{condition}, the subject takes a -2 penalty to Mental defense.
        `,
        targeting: `
          Make an attack vs. Mental with a +2 \\glossterm{accuracy} bonus against one creature within \\medrange.
        `,
      },
      rank: 1,
      scaling: "accuracy",
      type: "Duration",
    },

    {
      name: "Word of Faith",

      attack: {
        hit: `
          Each subject takes 1d10 + half \\glossterm{power} energy damage.
        `,
        targeting: `
          Make an attack vs. Mental against all \\glossterm{enemies} in a \\smallarea radius from you.
        `,
      },
      rank: 2,
      scaling: "damage",
      type: "Instant",
    },

    {
      name: "Greater Word of Faith",

      attack: {
        glance: "Half damage.",
        hit: `
          Each subject takes 2d8 + half \\glossterm{power} energy damage.
        `,
        targeting: `
          Make an attack vs. Mental against all \\glossterm{enemies} in a \\largearea radius from you.
        `,
      },
      rank: 4,
      scaling: "damage",
      type: "Instant",
    },

    {
      name: "Supreme Word of Faith",

      attack: {
        glance: "Half damage.",
        hit: `
          Each subject takes 4d6 + half \\glossterm{power} energy damage.
        `,
        targeting: `
          Make an attack vs. Mental against all \\glossterm{enemies} in a \\hugearea radius from you.
        `,
      },
      rank: 6,
      type: "Instant",
    },

    {
      name: "Mantle of Faith",

      castingTime: "minor action",
      effect: `
        You gain a +4 \\glossterm{magic bonus} to your \\glossterm{damage resistance}.
      `,
      rank: 1,
      scaling: {
        3: `The bonus increases to +8.`,
        5: `The bonus increases to +16.`,
        7: `The bonus increases to +32.`,
      },
      type: "Attune (self)",
    },

    {
      name: "Divine Might",

      castingTime: "minor action",
      effect: `
        Your size increases by one \\glossterm{size category}.
        This increases the \\glossterm{base speed} for your size and reduces your Stealth skill.
        It may also increase your \\glossterm{reach} (see \\pcref{Size in Combat}).
        However, your physical form is not altered fully to match your new size, and your Strength and Dexterity are unchanged.
      `,
      rank: 3,
      scaling: {
        5: `You also gain a +2 bonus to Strength-based checks, and you gain a +2 bonus to Strength for the purpose of determining your weight limits (see \\pcref{Weight Limits}).`,
        7: "You can increase your size by up to two size categories",
      },
      type: "Attune (self)",
    },

    {
      name: "Divine Presence",

      attack: {
        crit: "The effect becomes a \\glossterm{condition} on each subject.",
        // glance: '',
        hit: `
          Each subject is \\glossterm{briefly} \\shaken by you.
        `,
        targeting: `
          At the end of each round, make an attack vs. Mental against all \\glossterm{enemies} in a \\smallarea radius \\glossterm{emanation} from you.
          After you attack a creature this way, it becomes immune to this attack from you until it takes a \\glossterm{short rest}.
        `,
      },
      rank: 3,
      scaling: "accuracy",
      tags: ["Emotion"],
      type: "Attune (self)",
    },

    {
      name: "Greater Divine Presence",

      functionsLike: {
        name: "divine presence",
        exceptThat: `
          each subject is \\frightened by you instead of shaken.
        `,
      },
      rank: 7,
      tags: ["Emotion"],
      type: "Attune (self)",
    },

    {
      name: "Faithful Endurance",

      castingTime: "minor action",
      effect: `
        You gain a +1 \\glossterm{magic bonus} to \\glossterm{vital rolls} (see \\pcref{Vital Rolls}).
      `,
      rank: 3,
      scaling: { 5: `The bonus increases to +2.`, 7: `The bonus increases to +3.` },
      type: "Attune (self)",
    },

    {
      name: "Divine Conduit",

      castingTime: "minor action",
      effect: `
        You reduce your \\glossterm{focus penalty} with divine spells by 2.
      `,
      rank: 2,
      scaling: {
        4: `You gain a +1 \\glossterm{magic bonus} to \\glossterm{accuracy}.`,
        6: `You gain a +4 \\glossterm{magic bonus} to \\glossterm{power}.`,
      },
      type: "Attune (self)",
    },

    {
      name: "Divine Favor",

      castingTime: "minor action",
      effect: `
        You gain a +1 \\glossterm{magic bonus} to \\glossterm{accuracy} with all attacks.
      `,
      rank: 1,
      scaling: {
        3: `The bonus increases to +2.`,
        5: `The bonus increases to +3.`,
        7: `The bonus increases to +4.`,
      },
      type: "Attune (self)",
    },

    {
      name: "Divine Power",

      castingTime: "minor action",
      effect: `
        You gain a +2 \\glossterm{magic bonus} to \\glossterm{power}.
      `,
      rank: 1,
      scaling: {
        3: `The bonus increases to +4.`,
        5: `The bonus increases to +8.`,
        7: `The bonus increases to +16.`,
      },
      type: "Attune (self)",
    },

    {
      name: "Divine Offering",

      castingTime: "minor action",
      effect: `
        When you cast this spell, you gain a \\glossterm{vital wound} that has no vital wound effect.
        In exchange, you gain a +4 \\glossterm{magic bonus} to \\glossterm{vital rolls} and become immune to \\glossterm{conditions}.
      `,
      rank: 6,
      type: "Sustain (free)",
    },

    {
      name: "Divine Seal",

      effect: `
        Choose a \\medarea radius \\glossterm{zone} within \\longrange.
        Whenever a creature casts a divine spell in the area, if that creature does not share your deity (for clerics) or devoted alignment (for paladins), the spell has a 50\\% chance to fail with no effect.
      `,
      rank: 4,
      scaling: {
        6: `The area increases to a \\largearea radius.`,
      },
      type: "Sustain (minor)",
    },

    {
      name: "Banish Anathema",

      attack: {
        glance: "Half damage.",
        hit: `
          The subject takes 2d6 + half \\glossterm{power} energy damage.
          If it loses \\glossterm{hit points} from this damage, it immediately teleports into a random unoccupied location in the Astral Plane.
          At the end of the next round, it teleports back to its original location, or into the closest open space if that location is occupied.
          After it returns, it becomes immune to being teleported in this way until it takes a \\glossterm{short rest}.
        `,
        targeting: `
          Make an attack vs. Mental against one creature within \\medrange.
        `,
      },
      rank: 3,
      scaling: "damage",
      type: "Duration",
    },

    {
      name: "Certain Banish Anathema",

      functionsLike: {
        name: "banish anathema",
        exceptThat: "you gain a +3 accuracy bonus with the attack, and the damage increases to 4d6 + half \\glossterm{power}.",
      },
      rank: 6,
      scaling: "damage",
      type: "Duration",
    },

  ],
  rituals: [
    {
      name: "Consecration",

      castingTime: "24 hours",
      effect: `
        The area within an \\medarea radius \\glossterm{zone} from your location becomes sacred to your deity.
        % TODO: what cares about consecration?
        This has no tangible effects by itself, but some special abilities and monsters behave differently in consecrated areas.
      `,
      rank: 3,
      type: "Attune (self)",
    },
    {
      name: "Permanent Consecration",

      castingTime: "24 hours",
      effect: `
        The area within an \\medarea radius \\glossterm{zone} from your location becomes permanently sacred to your deity.
      `,
      rank: 5,
      type: "Duration",
    },

    {
      name: "Divine Transit",

      castingTime: "24 hours",
      effect: `
        Choose a destination up to 100 miles away from you on your current plane.
        Up to five Medium or smaller ritual participants are teleported to the temple or equivalent holy site to your deity that is closest to the chosen destination.

        You must specify the destination with a precise mental image of its appearance.
        The image does not have to be perfect, but it must unambiguously identify the destination.
        If you specify its appearance incorrectly, or if the area has changed its appearance, the destination may be a different area than you intended.
        The new destination will be one that more closely resembles your mental image.
        If no such area exists, the ritual simply fails.
        % TODO: does this need more clarity about what teleportation works?
        `,
      rank: 5,
      type: "Instant",
    },

    {
      name: "Commune",

      castingTime: "24 hours",
      effect: `
        You ask your source of divine power a single yes or no question.
        You receive a correct answer to that question to the limit of that source's knowledge, which is usually quite extensive.
        The answer is typically given as "yes" or "no", but it may answer "unclear" if the source does not know the answer.
        In cases where a one-word answer would be misleading or contrary to the source's interests, a short phrase may be given as an answer instead.

        This ritual only yields accurate results once for any given situation.
        If you perform the ritual again in a situation that has not meaningfully changed, you receive no answer regardless of your question.
        For example, if you are presented with seven doorways, with one doorway leading to a magnificent treasure and all other doorways leading to certain death, you cannot simply perform this ritual six times to determine the correct doorway.
      `,
      rank: 5,
      type: "Instant",
    },
  ],
};
