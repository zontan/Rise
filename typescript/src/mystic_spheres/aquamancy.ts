import { MysticSphere } from ".";

export const aquamancy: MysticSphere = {
  name: "Aquamancy",
  shortDescription: "Command water to crush and drown foes.",
  sources: ["domain", "nature"],

  cantrips: [
    {
      name: "Create Water",

      effect: `
        You create up to two gallons of wholesome, drinkable water divided among any number of locations within \\shortrange, allowing you to fill multiple small water containers.
        You must create a minimum of one ounce of water in each location.
      `,
      focus: false,
      narrative: `
        The desert air ripples with heat, scorching the group of adventurers.
        When they finally stop to rest, you conjure water from thin air, giving them all the strength to press on.
      `,
      scaling: {
        2: "The volume created increases to five gallons.",
        4: "The volume created increases to ten gallons.",
        6: "The volume created increases to twenty gallons.",
      },
      tags: ["Creation"],
      type: "Instant",
    },
    {
      name: "Manipulate Water",

      effect: `
        You change the speed of water within a \\medarea radius \\glossterm{emanation} from you by up to 5 miles per hour.
        If you decrease the water's speed to 0, you can increase it again with the remainder of your speed change and choose any direction for it to travel.
        You choose the speed change and direction when you cast this spell, and that choice persists for the duration of this effect.

        In addition to allowing you to change the direction of currents within large bodies of water, you can also use this to propel water across surfaces.
        Generally, moving water uphill costs at least 5 miles per hour of speed for every foot of elevation that you are trying to climb, which can limit your ability to move water up large distances.
      `,
      focus: false,
      scaling: {
        2: "The area increases to a \\largearea radius, and the maximum speed change increases to 10 miles per hour.",
        4: "The area increases to a \\hugearea radius, and the maximum speed change increases to 20 miles per hour.",
        6: "The area increases to a \\gargarea radius, and the maximum speed change increases to 40 miles per hour.",
      },
      type: "Sustain (minor)",
    },
    {
      name: "Purify Water",

      effect: `
        You can separate out dirt, sand, salt, and similar minor pollutants from up to five gallons of water within \\shortrange.
        The waste material moves to the edge of the water so it falls out or can be easily removed.
        This does not remove poisons, magical effects, or contaminants heavier than half a pound.
        Using this on a very large body of water is difficult, since the waste material can easily mix with the water unaffected by a single casting of this spell.
      `,
      focus: false,
      // narrative: '',
      scaling: {
        2: "The volume affected increases to ten gallons.",
        4: "The volume affected increases to twenty gallons.",
        6: "The volume affected increases to fifty gallons.",
      },
      type: "Instant",
    },
    {
      name: "Slippery Escape",

      effect: `
        You \\glossterm{briefly} gain a +3 bonus to the Flexibility skill.
      `,
      focus: false,
      narrative: `
        A thin layer of water covers you, allowing you to slip through the grasp of your foes more easily.
      `,
      scaling: {
        2: "The bonus increases to +4.",
        4: "The bonus increases to +5.",
        6: "The bonus increases to +6.",
      },
      tags: ["Manifestation"],
      type: "Duration",
    },
  ],
  spells: [
    {
      name: "Desiccating Curse",

      attack: {
        crit: "The effect lasts until this curse is removed.",
        glance: "The effect lasts \\glossterm{briefly}.",
        hit: `
          The subject is \\sickened.
          If it immerses itself in or drinks a body of water of minimum size equal to two size categories smaller than itself,
            the subject stops being sickened for 10 minutes.
          This effect lasts until the subject takes a \\glossterm{short rest}.
        `,
        targeting: `
          Make an attack vs. Mental against one creature within \\rngmed range.
        `,
      },
      rank: 3,
      scaling: "accuracy",
      tags: ["Curse"],
      type: "Duration",
    },
    {
      name: "Greater Desiccating Curse",

      functionsLike: {
        name: "desiccating curse",
        exceptThat: "the subject is \\nauseated instead of sickened.",
      },
      rank: 7,
      scaling: "accuracy",
      tags: ["Curse"],
      type: "Duration",
    },
    {
      name: "Sphere of Constraint",

      attack: {
        crit: `
          The effect becomes a \\glossterm{condition}.
        `,
        // glance: '',
        hit: `
          The majority of each subject's body is \\glossterm{briefly} surrounded by a layer of water.
          This does not impede its ability to breathe, but it takes penalties as if it was fighting underwater (see \\pcref{Underwater Combat}).
        `,
        targeting: `
          Make an attack vs. Reflex against all creatures completely within a \\smallarea radius within \\rngmed range.
          This attack automatically fails against creatures whose entire space is not within the area.
        `,
      },
      narrative: `
          A sphere of water appears in midair that adheres to your foes.
      `,
      rank: 5,
      scaling: "accuracy",
      tags: ["Manifestation"],
      type: "Duration",
    },
    // fighting underwater is +2 ranks better than a normal rank 2 condition
    {
      name: "Constraining Bubble",

      attack: {
        crit: `
          The water also the covers the subject's face.
          This does not meaningfully impede its sight, but it cannot breathe anything other than the water.
        `,
        glance: "The effect lasts \\glossterm{briefly}.",
        hit: `
          As a \\glossterm{condition}, the majority of the subject's body is surrounded by a layer of water.
          This does not impede its ability to breathe, but it takes penalties as if it was fighting underwater (see \\pcref{Underwater Combat}).
        `,
        targeting: `
          Make an attack vs. Reflex against a Huge or smaller creature within \\medrange.
        `,
      },
      rank: 6,
      scaling: "accuracy",
      tags: ["Manifestation"],
      type: "Duration",
    },

    {
      name: "Crushing Wave",

      attack: {
        // crit: '',
        // glance: '',
        hit: `
          Each subject takes 1d8 + half \\glossterm{power} bludgeoning damage.
        `,
        targeting: `
          Make an attack vs. Reflex against everything in a \\smallarealong, 10 ft. wide line from you.
        `,
      },
      rank: 1,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },
    {
      name: "Greater Crushing Wave",

      attack: {
        // crit: '',
        glance: "Half damage.",
        hit: `
          Each subject takes 2d6 + half \\glossterm{power} bludgeoning damage.
        `,
        targeting: `
          Make an attack vs. Reflex against everything in a \\largearealong, 10 ft. wide line from you.
        `,
      },
      rank: 3,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },
    {
      name: "Aquajet Propulsion",

      attack: {
        // crit: '',
        // glance: '',
        hit: `
          The subject takes 1d8 + \\glossterm{power} bludgeoning damage.
        `,
        targeting: `
          Make an attack vs. Armor against anything within \\medrange.
          Whether you hit or miss, you may \\glossterm{push} yourself up to 15 feet away from the target as the water propels you backwards.
          Moving yourself upwards costs twice the normal movement cost.
          This movement is doubled underwater instead of being dramatically slowed like normal for forced movement.
        `,
      },
      rank: 1,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },
    {
      name: "Greater Aquajet Propulsion",

      functionsLike: {
        name: 'aquajet propulsion',
        exceptThat: "the damage increases to 2d6 + \\glossterm{power}, and the push distance increases to 30 feet.",
      },
      rank: 3,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },
    {
      name: "Supreme Aquajet Propulsion",

      functionsLike: {
        name: 'aquajet propulsion',
        exceptThat: "the damage increases to 2d10 + \\glossterm{power}, and the push distance increases to 60 feet.",
      },
      rank: 5,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },
    {
      name: "Fountain",

      attack: {
        // crit: '',
        // glance: '',
        hit: `
          Each subject takes 1d8 + half \\glossterm{power} bludgeoning damage.
        `,
        targeting: `
          Make an attack vs. Armor against everything within a \\smallarea radius from you.
        `,
      },
      rank: 1,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },
    {
      name: "Greater Fountain",

      attack: {
        // crit: '',
        glance: "Half damage.",
        hit: `
          Each subject takes 2d6 + half \\glossterm{power} bludgeoning damage.
        `,
        targeting: `
          Make an attack vs. Armor against all \\glossterm{enemies} within a \\medarea radius from you.
        `,
      },
      rank: 3,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },
    {
      name: "Supreme Fountain",

      attack: {
        // crit: '',
        glance: "Half damage.",
        hit: `
          Each subject takes 4d8 + half \\glossterm{power} bludgeoning damage.
        `,
        targeting: `
          Make an attack vs. Armor against all \\glossterm{enemies} within a \\largearea radius from you.
        `,
      },
      rank: 6,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },
    {
      name: "Wall of Water",

      // targeting: None,
      effect: `
          You create a wall of water in a 15 ft.\\ high, \\medarealong line within \\medrange.
          The wall is four inches thick, and blocks \\glossterm{line of effect} for abilities.
          Sight through the wall is possible, though distorted.
          The wall provides both \\glossterm{cover} and \\glossterm{concealment} to targets on the opposite side of the wall, for a total of a +4 bonus to Armor defense.
          Creatures can pass through the wall unharmed, though it costs five extra feet of movement to move through the wall.

          Each five-foot square of wall has \\glossterm{hit points} equal to three times your \\glossterm{power} and all of its defenses are 0.
      `,
      rank: 3,
      scaling: {
        5: "The area of the wall increases to a \\largearealong line.",
        7: "The area of the wall increases to a \\hugearealong line.",
      },
      tags: ["Manifestation"],
      type: "Sustain (minor)",
    },
    {
      name: "Underwater Freedom",

      castingTime: "minor action",
      effect: `
        You suffer no penalties for acting underwater, except for those relating to using ranged weapons.
      `,
      rank: 2,
      scaling: {
        4: "You also gain a swim speed equal to half the \\glossterm{base speed} for your size.",
        6: "The swim speed increases to be equal to the \\glossterm{base speed} for your size.",
      },
      type: "Attune (self)",
    },
    {
      name: "Mass Underwater Freedom",

      castingTime: "minor action",
      functionsLike: {
        mass: true,
        name: "underwater freedom",
      },
      rank: 4,
      scaling: {
        6: "Each subject also gains a swim speed equal to half the \\glossterm{base speed} for its size.",
      },
      type: "Attune (target)",
    },
    // +2 levels for push, -1 level for no power
    {
      name: "Raging River",

      attack: {
        // crit: '',
        // glance: '',
        hit: `
          Each subject takes 1d10 bludgeoning damage.
          In addition, each subject is \\glossterm{pushed} 15 feet in the direction the line points away from you.
          Once a subject leaves the area, it stops being moved and blocks any other targets from being pushed.
        `,
        targeting: `
          Make an attack vs. Fortitude against everything in a \\medarealong, 10 ft. wide line from you.
        `,
      },
      rank: 2,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },
    // +3 levels for push, -1 level for no power
    {
      name: "Greater Raging River",

      attack: {
        // crit: '',
        // glance: '',
        hit: `
          Each subject takes 2d10 bludgeoning damage.
          In addition, each subject is \\glossterm{pushed} 30 feet in the direction the line points away from you.
          Once a subject leaves the area, it stops being moved and blocks any other targets from being pushed.
        `,
        targeting: `
          Make an attack vs. Fortitude against everything in a \\largearealong, 15 ft. wide line from you.
        `,
      },
      rank: 5,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },
    {
      name: "Geyser",

      attack: {
        // crit: '',
        glance: "Half damage.",
        // +1d from normal AOE due to weird area that probably just hits one person
        hit: `
          Each subject takes 2d8 + half \\glossterm{power} bludgeoning damage.
        `,
        targeting: `
          Make an attack vs. Reflex against everything in a \\medarealong, 5 ft.\\ wide vertical line within \\longrange.
          If this spell has its area increased, only the length of the line increases.
        `,
      },
      rank: 3,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },
    {
      name: "Greater Geyser",

      attack: {
        // crit: '',
        glance: "Half damage.",
        // +1d from normal AOE due to weird area that probably just hits one person
        hit: `
          Each subject takes 4d10 + half \\glossterm{power} bludgeoning damage.
        `,
        targeting: `
          Make an attack vs. Reflex against everything in a \\largearealong, 5 ft.\\ wide vertical line within \\distrange.
          If this spell has its area increased, only the length of the line increases.
        `,
      },
      rank: 6,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },
    {
      name: "Rainstorm",

      effect: `
        Torrential rain begins falling out of thin air within a \\medarea radius \\glossterm{zone} within \\longrange.
        The rain extinguishes minor fires such as campfires and torches on contact.
        Everything in the area gains a +4 bonus to \\glossterm{defenses} against attacks that deal fire damage.
      `,
      rank: 1,
      scaling: {
        3: "The area increases to a \\largearea radius \\glossterm{zone}.",
        5: "The range increases to a \\distrange.",
        7: "The area increases to a \\hugearea radius \\glossterm{zone}.",
      },
      tags: ["Manifestation"],
      type: "Sustain (minor)",
    },
    {
      name: "Obscuring Mist",

      effect: `
        Fog fills the air within a \\smallarea radius \\glossterm{zone} from your location.
        The fog partially obstructs sight, granting \\glossterm{concealment} to anything seen through the fog (see \\pcref{Concealment}).
      `,
      rank: 2,
      scaling: {
        4: "The area increases to a \\medarea radius \\glossterm{zone}.",
        6: "The area increases to a \\largearea radius \\glossterm{zone}.",
      },
      type: "Sustain (minor)",
    },
    {
      name: "Ring of Mist",

      effect: `
        Fog fills the air within a \\medarea radius \\glossterm{zone} from your location.
        The fog partially obstructs sight, granting \\glossterm{concealment} to anything seen through the fog (see \\pcref{Concealment}).
        You can exclude an inner radius of any size from the area, allowing you to create fog that surrounds your location without blocking sight to things near to you.
      `,
      rank: 6,
      type: "Sustain (minor)",
    },
    {
      name: "Misty Shroud",

      effect: `
        Fog fills the air within a \\smallarea radius \\glossterm{emanation} from your location.
        The fog partially obstructs sight, granting \\glossterm{concealment} to anything seen through the fog (see \\pcref{Concealment}).
      `,
      rank: 4,
      scaling: {
        6: "The area increases to a \\medarea radius \\glossterm{emanation}.",
      },
      type: "Attune (self)",
    },
    {
      name: "Octopus Tentacles",

      functionsLike: {
        exceptThat: `
          you create eight tentacles that extend from your body.
          Whenever you make a \\glossterm{strike} with the tentacles, you can attack with all of the tentacles at once, with each tentacle attacking a different target.
          This functions as if your attacks had the \\glossterm{Sweeping} (7) tag, with no limit on how far each secondary target must be from the primary target (see \\pcref{Sweeping}).
        `,
        name: "aqueous tentacle",
      },
      rank: 4,
      scaling: {
        6: "You gain a +5 bonus to \\glossterm{reach} with attacks using the tentacles.",
      },
      type: "Attune (self)",
    },
    {
      name: "Aqueous Tentacle",

      effect: `
        You grow a massive watery tentacle that extends from your body.
        The tentacle grants you a slam \\glossterm{natural weapon} (see \\tref{Natural Weapons}).
        The natural weapon deals 1d10 damage, as normal for a slam natural weapon, and it has the Sweeping (1) tag.
        In addition, it has the Long \\glossterm{weapon tag} (see \\pcref{Weapon Tags}).
        Strikes using the tentacle are considered \\glossterm{magical} abilities, which means you use your \\glossterm{magical} \\glossterm{power} to determine their damage.
      `,
      rank: 2,
      scaling: {
        4: "You gain a +5 foot bonus to \\glossterm{reach} with attacks using the tentacle.",
        6: "The bonus to reach increases to 10 feet.",
      },
      tags: ["Manifestation"],
      type: "Attune (self)",
    },
    {
      name: "Desiccation",

      attack: {
        crit: 'The condition must be removed twice before the effect ends.',
        // glance: '',
        hit: `
          The subject is \\sickened as a \\glossterm{condition}.
        `,
        targeting: `
          Make an attack vs. Fortitude against one living creature within \\rngmed range.
        `,
      },
      rank: 1,
      scaling: "damage",
      type: "Duration",
    },
    {
      name: "Greater Desiccation",

      attack: {
        crit: 'The condition must be removed twice before the effect ends.',
        glance: 'The effect lasts \\glossterm{briefly}.',
        hit: `
          The subject is \\nauseated as a \\glossterm{condition}.
        `,
        targeting: `
          Make an attack vs. Fortitude against one living creature within \\rngmed range.
        `,
      },
      rank: 5,
      scaling: "damage",
      type: "Duration",
    },
    {
      name: "Wave of Desiccation",

      attack: {
        crit: 'The effect becomes a \\glossterm{condition}.',
        hit: `
          Each subject that has no remaining \\glossterm{damage resistance} is \\glossterm{briefly} \\nauseated.
        `,
        targeting: `
          Make an attack vs. Fortitude against all living creatures in a \\largearealong, 15 ft. wide line from you.
        `,
      },
      rank: 2,
      scaling: "accuracy",
      type: "Duration",
    },
    {
      name: "Greater Wave of Desiccation",

      attack: {
        crit: 'The effect becomes a \\glossterm{condition}.',
        hit: `
          Each subject is \\glossterm{briefly} \\nauseated.
        `,
        targeting: `
          Make an attack vs. Fortitude against all living creatures in a \\largearealong, 15 ft. wide line from you.
        `,
      },
      rank: 5,
      scaling: "accuracy",
      type: "Duration",
    },
    {
      name: "Aqueous Form",

      effect: `
        You transform your body and equipment into water, allowing you to compress your body or contort yourself into odd shapes.
        This has the following effects:
        \\begin{itemize}
          \\item You gain a \\glossterm{swim speed} equal to the \\glossterm{base speed} for your size.
          \\item You gain a +8 \\glossterm{magic bonus} to the Flexibility skill. In addition, the minimum size you can squeeze down to is reduced to one inch, which can dramatically improve your ability to squeeze through tight spaces.
          \\item You are immune to \\glossterm{critical hits} from \\glossterm{strikes}.
          \\item Your \\glossterm{damage resistance} is halved.
        \\end{itemize}
      `,
      rank: 4,
      scaling: {
        6: "The bonus to Flexibility increases to +12.",
      },
      type: "Attune (self)",
    },
    {
      name: "Fog Cloud",

      effect: `
        A cloud of fog appears in a \\medarea radius within \\longrange.
        All sight through the area is partially obscured, granting \\glossterm{concealment} to anything in the area and anything viewed through the area (see \\pcref{Concealment}).
      `,
      rank: 3,
      scaling: {
        5: "The area increases to a \\largearea radius.",
        7: "The area increases to a \\hugearea radius.",
      },
      tags: ["Manifestation"],
      type: "Sustain (minor)",
    },
    {
      name: "Fog Wall",

      effect: `
        You create a wall of fog in a 15 ft.\\ high, \\medarealong \\glossterm{wall} within \\rngmed range.
        The fog makes it difficult to see through the wall, granting \\glossterm{concealment} to anything viewed through the wall (see \\pcref{Concealment}).
      `,
      rank: 1,
      scaling: {
        3: "The area increases to a 30 foot high, \\largearealong line.",
        5: "The area increases to a 60 foot high, \\hugearealong line.",
        7: "The area increases to a 120 foot high, 240 foot long line.",
      },
      tags: ["Manifestation"],
      type: "Sustain (minor)",
    },
    {
      name: "Fluid Motion",

      effect: `
        When you move using one of your movement speeds, you can transform yourself into a rushing flow of water with a volume roughly equal to your normal volume until your movement is complete.
        You can only transform into water in this way once during your movement, and you regain your normal form at the end of the movement.
        In this form, you may move wherever water could go, you cannot take other actions, such as jumping, attacking, or casting spells.
        You may move through squares occupied by enemies without penalty.
        Being \\grappled or otherwise physically constrained does not prevent you from transforming into water in this way.

        Your speed is halved when moving uphill and doubled when moving downhill.
        Unusually steep inclines may cause greater movement differences while in this form.

        If the water is split, you may reform from anywhere the water has reached, to as little as a single ounce of water.
        If not even an ounce of water exists contiguously, your body reforms from all of the largest available sections of water, cut into pieces of appropriate size.
        This usually causes you to die.
      `,
      rank: 5,
      scaling: {
        7: `
          You can transform to and from water any number of times during a single movement.
          You must still regain your normal form at the end of the movement.
        `,
      },
      type: "Attune (self)",
    },
    {
      name: "Forceful Aquajet",

      attack: {
        crit: "Double damage, and you can knockback the subject 60 feet instead of 30 feet.",
        hit: `
          The subject takes 1d6 bludgeoning damage.
          If it loses \\glossterm{hit points} from this damage, you \\glossterm{knockback} it up to 30 feet in any direction (see \\pcref{Knockback Effects}).
          Moving the subject upwards costs twice the normal movement cost.
        `,
        targeting:
          "Make an attack vs. Armor against anything Large or smaller within \\medrange.",
      },
      // narrative: '',
      rank: 1,
      scaling: "accuracy",
      type: "Instant",
    },
    {
      name: "Greater Forceful Aquajet",

      functionsLike: {
        name: 'forceful aquajet',
        // This deals an immediate 6d6 if you smash someone against a barrier, which is a lot of damage.
        exceptThat: "the damage increases to 2d6. In addition, the knockback distance increases to 60 feet, or 120 feet on a critical hit.",
      },
      // narrative: '',
      rank: 4,
      scaling: "damage",
      type: "Instant",
    },
    {
      name: "Supreme Forceful Aquajet",

      functionsLike: {
        name: 'forceful aquajet',
        // This deals an immediate 12d6 if you smash someone against a barrier, which is a lot of damage.
        exceptThat: "the damage increases to 4d6. In addition, the knockback distance increases to 120 feet, or 240 feet on a critical hit.",
      },
      // narrative: '',
      rank: 7,
      scaling: "damage",
      type: "Instant",
    },
  ],
  rituals: [
    {
      name: "Dampen",

      effect: `
          Up to five ritual participants each gain a +2 bonus to defenses against attacks that deal fire damage.
      `,
      rank: 1,
      type: "Attune (ritual)",
      castingTime: "one minute",
    },
    {
      name: "Water Breathing",

      effect: `
        One ritual participant gains the ability to breathe water as easily as a human breathes air, preventing it from drowning or suffocating underwater.
      `,
      rank: 3,
      type: "Attune (ritual)",
      castingTime: "one minute",
    },
    {
      name: "Detect Water",

      effect: `
        You learn the approximate distance and direction to any bodies of water within \\rnglong \\glossterm{range} of you.
        Since this is a \\abilitytag{Detection} ability, its range can penetrate some solid objects (see \\pcref{Detection}).
        This spell can detect bodies of water with a minimum size of Fine.
      `,
      rank: 1,
      tags: ["Detection"],
      type: "Instant",
      castingTime: "one minute",
    },
    {
      name: "Greater Detect Water",

      functionsLike: {
        exceptThat: "the range increases to \\extrange.",
        name: "detect water",
      },
      rank: 3,
      tags: ["Detection"],
      type: "Instant",
      castingTime: "one minute",
    },
    {
      name: "Supreme Detect Water",

      functionsLike: {
        exceptThat: "the range increases to 2,000 foot range.",
        name: "detect air",
      },
      rank: 5,
      tags: ["Detection"],
      type: "Instant",
      castingTime: "one minute",
    },
  ],
};
