import { MysticSphere } from ".";

export const aeromancy: MysticSphere = {
  name: "Aeromancy",
  shortDescription: "Command air to protect allies and blast foes",

  cantrips: [
    {
      name: "Airborne Leap",

      effect: `
        You gain a +4 bonus to the Jump skill until the end of the next round.
      `,
      focus: false,
      narrative: `
        The air rises beneath you and pushes you up, propelling you farther when you leap.
      `,
      scaling: {
        2: "The bonus increases to +6.",
        4: "The bonus increases to +8.",
        6: "The bonus increases to +10.",
      },
      type: "Duration",
    },
    {
      name: "Manipulate Air",

      effect: `
        You change the wind speed within a \\medarea radius \\glossterm{emanation} from you by up to 10 miles per hour.
        If you decrease the wind's speed to 0, you can increase it again with the remainder of your speed change and choose any direction for it to travel.
        You choose the speed change and direction when you cast this spell, and that choice persists for the duration of this effect.
      `,
      focus: false,
      narrative: `
        The wind around you waxes and wanes at your command, softening the force of a tempest or creating one to harass your foes.
      `,
      scaling: {
        2: "The area increases to a \\largearea radius, and the maximum speed change increases to 20 miles per hour.",
        4: "The area increases to a \\hugearea radius, and the maximum speed change increases to 40 miles per hour.",
        6: "The area increases to a \\extarea radius, and the maximum speed change increases to 80 miles per hour.",
      },
      type: "Sustain (minor)",
    },
    {
      name: "Soften Landing",

      effect: `
        Choose yourself or an \\glossterm{ally} within \\longrange.
        Until the end of the round, that creature treats all falls as if they were 20 feet shorter for the purpose of determining \\glossterm{falling damage}.
      `,
      focus: false,
      narrative: `
        The air beneath you suddenly accelerates into a great wind, softening the force of your unexpected fall.
      `,
      scaling: {
        2: "The distance reduction increases to 50 feet.",
        4: "The distance reduction increases to 100 feet.",
        6: "The distance reduction increases to 200 feet.",
      },
      type: "Duration",
    },
  ],
  spells: [
    {
      name: "Curse of Arrow Attraction",

      attack: {
        crit: `
          The effect lasts until this curse is removed.
        `,
        hit: `
          The subject takes a -2 penalty to defenses against \\glossterm{mundane} ranged attacks from weapons or projectiles that are Small or smaller until it takes a \\glossterm{short rest}.
        `,
        target: "Make an attack vs. Mental against anything within \\longrange.",
      },
      narrative: `
        The air around your foe ripples with hidden air currents that seem to guide the flight of arrows, ensuring that they strike true.
      `,
      rank: 2,
      scaling: "accuracy",
      tags: ["Curse"],
      type: "Duration",
    },
    {
      name: "Greater Curse of Arrow Attraction",

      attack: {
        crit: `
          The effect lasts until this curse is removed.
        `,
        glance: "The effect lasts until the end of the next round.",
        hit: `
          The subject takes a -4 penalty to defenses against \\glossterm{mundane} ranged attacks from weapons or projectiles that are Medium or smaller until it takes a \\glossterm{short rest}.
        `,
        target: "Make an attack vs. Mental against anything within \\longrange.",
      },
      narrative: `
        The air around your foe ripples with hidden air currents that seem to guide the flight of arrows, ensuring that they strike true.
      `,
      rank: 5,
      scaling: "accuracy",
      tags: ["Curse"],
      type: "Duration",
    },
    {
      name: "Propulsion",

      effect: `
        Choose yourself or one Large or smaller \\glossterm{ally} within \\medrange.
        You \\glossterm{push} the subject up to 60 feet in any direction.
        You cannot change the direction of the movement partway through.
        Moving the subject upwards costs twice the normal movement cost.
      `,
      rank: 1,
      scaling: {
        3: "The distance increases to 120 feet.",
        5: "The distance increases to 240 feet.",
        7: "The distance increases to 480 feet.",
      },
      type: "Instant",
    },
    {
      name: "Mass Propulsion",

      effect: `
        Choose up to five creatures from among yourself and your Large or smaller \\glossterm{allies} within \\medrange.
        You \\glossterm{push} each subject up to 60 feet in any direction.
        Each subject must be pushed in the same direction.
        You cannot change the direction of the movement partway through.
        Moving a subject upwards costs twice the normal movement cost.
      `,
      rank: 3,
      scaling: {
        5: "The distance increases to 120 feet.",
        7: "The distance increases to 240 feet.",
      },
      type: "Instant",
    },
    {
      name: "Wind Screen",

      castingTime: "minor action",
      effect: `
        You gain a +1 \\glossterm{magic bonus} to Armor defense.
        In addition, you gain a +2 bonus to defenses against \\glossterm{mundane} ranged attacks from weapons or projectiles that are Small or smaller.
        Any effect which increases the size of creature this spell can affect also increases the size of ranged weapon it defends against by the same amount.
      `,
      // narrative: "",
      rank: 1,
      scaling: {
        3: "The bonus to Armor defense increases to +2.",
        5: "The bonus to Armor defense increases to +3.",
        7: "The bonus to Armor defense increases to +4.",
      },
      type: "Attune (self)",
    },
    {
      name: "Mass Wind Screen",

      castingTime: "minor action",
      functionsLike: {
        exceptThat:
          "it affects up to five creatures of your choice from among yourself and your \\glossterm{allies} within \\medrange.",
        spell: "wind screen",
      },
      // narrative: "",
      rank: 3,
      scaling: {
        5: "The bonus to Armor defense increases to +2.",
        7: "The bonus to Armor defense increases to +3.",
      },
      type: "Attune (target)",
    },
    {
      name: "Windstrike",

      attack: {
        // crit: '',
        hit: "The subject takes 1d10 \\add \\glossterm{power} bludgeoning damage.",
        target: "Make an attack vs. Armor against anything within \\medrange.",
      },
      // narrative: '',
      rank: 1,
      scaling: "damage",
      type: "Instant",
    },
    {
      name: "Windsnipe",

      attack: {
        // crit: '',
        glance: "Half damage.",
        hit: "The subject takes 2d8 \\add \\glossterm{power} bludgeoning damage.",
        target: "Make an attack vs. Armor against anything within \\distrange.",
      },
      // narrative: '',
      rank: 3,
      scaling: "damage",
      type: "Instant",
    },
    {
      name: "Buffet",

      attack: {
        crit: "Double damage, and you can knockback the subject 60 feet instead of 30 feet.",
        // This is +1d over the normal damage to help split the difference since the effect isn't
        // consistently t2 worthy. It deals an immediate 3d6 if you smash someone against a barrier.
        hit: `
          The subject takes 1d10 bludgeoning damage.
          If it loses \\glossterm{hit points} from this damage, you \\glossterm{knockback} it up to 30 feet in any direction (see \\pcref{Knockback Effects}).
          Moving the subject upwards costs twice the normal movement cost.
        `,
        target: "Make an attack vs. Fortitude against anything Large or smaller within \\medrange.",
      },
      // narrative: '',
      rank: 2,
      scaling: "damage",
      type: "Instant",
    },
    {
      name: "Greater Buffet",

      attack: {
        crit: "Double damage, and you can knockback the subject 120 feet instead of 60 feet.",
        glance: "Half damage.",
        // This deals an immediate 6d6 if you smash someone against a barrier, which is a lot of damage.
        hit: `
          The subject takes 2d10 bludgeoning damage.
          If it loses \\glossterm{hit points} from this damage, you \\glossterm{knockback} it up to 60 feet in any direction (see \\pcref{Knockback Effects}).
          Moving the subject upwards costs twice the normal movement cost.
        `,
        target: "Make an attack vs. Fortitude against anything Huge or smaller within \\medrange.",
      },
      // narrative: '',
      rank: 5,
      scaling: "damage",
      type: "Instant",
    },
    {
      name: "Gentle Descent",

      effect: "You gain a 30 foot \\glossterm{glide speed} (see \\pcref{Gliding}).",
      // narrative: '',
      rank: 2,
      scaling: {
        4: "You are immune to \\glossterm{falling damage} even if you do not glide.",
        6: "You can reduce your \\glossterm{glide speed} to 20 feet or increase it to 60 feet during each phase that you glide.",
      },
      type: "Attune (self)",
    },
    {
      name: "Mass Gentle Descent",

      functionsLike: {
        exceptThat:
          "it affects up to five creatures of your choice from among yourself and your \\glossterm{allies} within \\medrange.",
        spell: "gentle descent",
      },
      // narrative: '',
      rank: 4,
      scaling: {
        6: "The subject is immune to \\glossterm{falling damage} even if it does not glide.",
      },
      type: "Attune (target)",
    },
    {
      name: "Flight",

      effect: `
        You gain a 30 foot \\glossterm{fly speed} with a maximum height of 30 feet (see \\pcref{Flying}).
        If you are above that height, you gain a 30 foot \\glossterm{glide speed} instead.
      `,
      // narrative: '',
      rank: 4,
      scaling: {
        6: "The maximum height increases to 60 feet.",
      },
      type: "Attune (self)",
    },
    {
      name: "Agile Flight",

      effect: `
        You gain a 30 foot \\glossterm{fly speed} with a maximum height of 30 feet (see \\pcref{Flying}).
        Your \\glossterm{maneuverability} with this fly speed is perfect (see \\pcref{Flying Maneuverability}).
      `,
      // narrative: '',
      rank: 6,
      type: "Attune (self)",
    },
    {
      name: "Soaring Flight",

      effect: `
        You gain a 40 foot \\glossterm{fly speed} with a maximum height of 120 feet (see \\pcref{Flying}).
        Your \\glossterm{maneuverability} with this fly speed is poor (see \\pcref{Flying Maneuverability}).
        If you are above that height, you gain a 40 foot \\glossterm{glide speed} instead.
      `,
      // narrative: '',
      rank: 7,
      type: "Attune (self)",
    },
    {
      name: "Air Walk",

      effect: `
        You can walk on air as if it were solid ground.
        This only functions as long as you are no more than 60 feet above an object at least two size categories larger than you that is free-standing and capable of supporting your weight.
      `,
      // narrative: '',
      rank: 5,
      scaling: {
        7: "The maximum height increases to 120 feet.",
      },
      type: "Attune (self)",
    },
    {
      name: "Gust of Wind",

      attack: {
        // crit: '',
        // push instead of adding half power
        hit: `
          Each subject takes 1d10 bludgeoning damage.
          In addition, each subject is \\glossterm{pushed} 20 feet in the direction the line points away from you.
          Once a subject leaves the area, it stops being moved and blocks any other targets from being pushed.
        `,
        target: `
          Make an attack vs. Fortitude against everything in a \\largearea long, 5 ft. wide line from you.
        `,
      },
      // effect: '',
      // narrative: '',
      rank: 2,
      scaling: "damage",
      type: "Instant",
    },
    {
      name: "Greater Gust of Wind",

      attack: {
        // crit: '',
        glance: "Half damage.",
        // +1 level for farther push, +2 levels for area
        hit: `
          Each subject takes 2d10 bludgeoning damage.
          In addition, each subject is \\glossterm{pushed} 50 feet in the direction the line points away from you.
          Once a subject leaves the area, it stops being moved and blocks any other targets from being pushed.
        `,
        target: `
          Make an attack vs. Fortitude against everything in a \\hugearea long, 10 ft. wide line from you.
        `,
      },
      // narrative: '',
      rank: 5,
      scaling: "damage",
      type: "Instant",
    },
    {
      name: "Windblade",

      castingTime: "minor action",
      effect: `
        Melee weapons you wield gain a +5 foot \\glossterm{magic bonus} to \\glossterm{reach}.
        Attacks that hit because of this reach deal bludgeoning damage instead of any other damage types.
        This has no effect on ranged attacks the subject makes.
      `,
      // narrative: '',
      rank: 3,
      scaling: {
        5: "The bonus to reach increases to +10 feet.",
        7: "The bonus to reach increases to +15 feet.",
      },
      type: "Attune (self)",
    },
    {
      name: "Mass Windblade",

      castingTime: "minor action",
      functionsLike: {
        exceptThat:
          "it affects up to five creatures of your choice from among yourself and your \\glossterm{allies} within \\medrange.",
        spell: "windblade",
      },
      // narrative: '',
      rank: 5,
      scaling: {
        7: "The bonus to reach increases to +10 feet.",
      },
      type: "Attune (target)",
    },
    {
      name: "Retributive Winds",

      attack: {
        // crit: '',
        glance: "Half damage.",
        hit: `
          Each subject takes 2d6 \\add half \\glossterm{power} bludgeoning damage.
        `,
        target: `
          At the end of each phase, make an attack vs. Armor against each creature within \\shortrange that attacked you during that phase.
          Any effect which increases this spell's range increases the range of this retaliation by the same amount.
        `,
      },
      // effect: '',
      // narrative: '',
      rank: 3,
      scaling: "damage",
      type: "Attune (self)",
    },
    {
      name: "Control Weather",

      effect: `
        When you cast this spell, you choose a new weather pattern.
        You can only choose weather which would be reasonably probable in the climate and season of the area you are in.
        For example, you can normally create a thunderstorm, but not if you are in a desert.

        When you complete the spell, the weather begins to take effect in a two mile radius cylinder-shaped \\glossterm{zone} from your location.
        After five minutes, your chosen weather pattern fully takes effect.
        % TODO: define weather intensities
        You cannot change the intensity of the weather beyond what would be possible without magic during this time frame.
        For example, you can change a clear sky into a light thunderstorm, but you cannot create a hurricane or tornado from untroubled air.

        You can control the general tendencies of the weather, such as the direction and intensity of the wind.
        You cannot control specific applications of the weather, such as the location of lightning strikes.
        Contradictory weather conditions are not possible simultaneously.

        After the spell's effect ends, the weather continues on its natural course, which may cause your chosen weather pattern to end.
        % TODO: This should be redundant with generic spell mechanics
        If another ability would magically manipulate the weather in the same area, the most recently used ability takes precedence.
      `,
      // narrative: '',
      rank: 4,
      scaling: {
        6: "You can shape the weather for up to fifteen minutes before it takes effect, increasing the intensity of the changes you can make.",
      },
      type: "Attune (self)",
    },
    {
      name: "Cyclone",

      attack: {
        // crit: '',
        glance: "Half damage.",
        hit: `
          Each subject takes 2d6 \\add half \\glossterm{power} bludgeoning damage.
        `,
        target: `
          Make an attack vs. Fortitude against everything in a \\smallarea radius within \\medrange.
        `,
      },
      // narrative: '',
      rank: 3,
      scaling: "damage",
      type: "Instant",
    },
    {
      name: "Hurricane",

      attack: {
        // crit: '',
        glance: "Half damage.",
        hit: `
          Each subject takes 2d10 \\add half \\glossterm{power} bludgeoning damage.
          In addition, each subject is \\glossterm{pushed} 20 feet clockwise around you.
          Each subject's final position should be the same distance from you as its starting position.
        `,
        target: `
          Make an attack vs. Fortitude against \\glossterm{enemies} in a \\medarea radius from you.
        `,
      },
      // narrative: '',
      rank: 5,
      scaling: "damage",
      type: "Instant",
    },
    {
      name: "Windtheft",

      attack: {
        // crit: '',
        // glance: '',
        hit: `
          You \\glossterm{knockback} the object up to 60 feet towards you.
          You can use a \\glossterm{free hand} to catch the object if it reaches you.
        `,
        target: `
          Make an attack vs. Reflex against one Small or smaller object within \\medrange range.
          If the object is attended by a creature, the attack must also beat the attending creature's Reflex defense.
          If it is held in two hands or well secured, this attack automatically fails.
        `,
      },
      // narrative: '',
      rank: 2,
      scaling: "accuracy",
      type: "Instant",
    },
    {
      name: "Windseal",

      // +1.5 levels for avoidable damage, -0.5 for size limit. or something.
      attack: {
        crit: "Double damage from movement.",
        glance: "Half damage from movement.",
        hit: `
          As a \\glossterm{condition}, the subject is \\glossterm{slowed} by incredibly fast winds that inhibit movement.
          At the end of each phase, if it moved voluntarily during that phase, it takes 2d6 bludgeoning damage.
        `,
        target: `
          Make an attack vs. Fortitude against one Large or smaller creature within \\medrange.
        `,
      },
      // effect: '',
      // narrative: '',
      rank: 3,
      scaling: "damage",
      type: "Duration",
    },
    {
      name: "Dust Cloud",

      attack: {
        crit: `
          Each subject is \\glossterm{dazzled} as a \\glossterm{condition}.
        `,
        // glance: '',
        hit: `
          Each subject is \\glossterm{dazzled} until the end of the next round.
        `,
        target: `
          Make an attack vs. Reflex against all creatures in a \\smallarea radius within \\medrange from you.
        `,
      },
      // narrative: '',
      rank: 1,
      scaling: "accuracy",
      type: "Duration",
    },
    {
      name: "Massive Dust Cloud",

      attack: {
        crit: `
          Each subject is also \\glossterm{dazzled} as a \\glossterm{condition}.
        `,
        // glance: '',
        hit: `
          Each subject is \\glossterm{dazzled} until the end of the next round.
        `,
        target: `
          Make an attack vs. Reflex against all creatures in a \\largearea radius within \\longrange from you.
        `,
      },
      // narrative: '',
      rank: 4,
      scaling: "accuracy",
      type: "Duration",
    },
    {
      name: "Blinding Dust Cloud",

      attack: {
        crit: `
          Each subject is \\glossterm{blinded} as a \\glossterm{condition}.
        `,
        // glance: '',
        hit: `
          Each subject is \\glossterm{blinded} until the end of the next round.
        `,
        target: `
          Make an attack vs. Reflex against all creatures in a \\smallarea radius within \\medrange from you.
        `,
      },
      // narrative: '',
      rank: 7,
      scaling: "accuracy",
      type: "Duration",
    },
    {
      name: "Dustblind",

      attack: {
        crit: "The condition is must be removed twice before the effect ends.",
        glance: "The condition is removed at the end of the next round.",
        hit: `
          The subject is \\glossterm{blinded} as a \\glossterm{condition}.
        `,
        target: `
          Make an attack vs. Reflex against one creature within \\shortrange.
          If there is no dirt, dust, or collection of loose objects of similar size within 30 foot \\glossterm{range} of the subject's eyes, this attack automatically fails.
        `,
      },
      // narrative: '',
      rank: 6,
      scaling: "accuracy",
      type: "Duration",
    },
    {
      name: "Piercing Windstrike",

      attack: {
        // crit: '',
        hit: "The subject takes 2d8 \\add \\glossterm{power} piercing damage.",
        target: "Make an attack vs. Reflex against anything within \\medrange.",
      },
      narrative: `
        A rush of wind flows rapidly through the gaps in your foe's armor to pierce its heart.
      `,
      rank: 3,
      scaling: "damage",
      type: "Instant",
    },
    {
      name: "Downdraft",

      attack: {
        crit: `
          The effective force of gravity is increased by approximately four times instead.
          This increases the penalties to -4.
        `,
        glance: "The condition is removed at the end of the next round.",
        hit: `
          As a \\glossterm{condition}, air buffets the subject downward, pushing it towards the ground with great force.
          This approximately doubles the gravity it experiences, which imposes a -2 penalty to \\glossterm{accuracy}, physical \\glossterm{checks}, and \\glossterm{defenses}.
        `,
        target: `
          Make an attack vs. Fortitude against one creature within \\medrange.
        `,
      },
      // narrative: '',
      // +1 level since it's stronger than a typical rank 1 debuff
      rank: 3,
      scaling: "accuracy",
      type: "Duration",
    },
    {
      name: "Mistform",

      effect: `
        You can move through creatures freely.
        This does not allow you to move through inanimate objects.
        In addition, you gain a \\glossterm{glide speed} equal to your \\glossterm{base speed}.
      `,
      // narrative: '',
      rank: 4,
      scaling: {
        6: "You also ignore all sources of \\glossterm{difficult terrain}.",
      },
      type: "Attune (self)",
    },
  ],

  rituals: [
    {
      name: "Air Bubble",

      castingTime: "one minute",
      effect: `
        One ritual participant gains the ability to breathe clear, clean air regardless of its surroundings.
        This can allow it to breathe underwater and avoid air-based poisons.
      `,
      // narrative: '',
      rank: 3,
      type: "Attune (target)",
    },
    {
      name: "Detect Air",

      castingTime: "one minute",
      effect: `
        You learn the approximate distance and direction to any air within \\rnglong \\glossterm<range> of you.
        Since this is a \\glossterm<Detection> ability, its range can penetrate some solid objects (see \\pcref<Detection>).
        This ritual can detect air pockets with a minimum size of Fine.
      `,
      // narrative: '',
      rank: 1,
      tags: ["Detection"],
      type: "Instant",
    },
    {
      name: "Greater Detect Air",

      castingTime: "one minute",
      functionsLike: {
        exceptThat: "the range increases to \\extrange.",
        spell: "detect air",
      },
      // narrative: '',
      rank: 3,
      type: "Instant",
    },
    {
      name: "Supreme Detect Air",

      castingTime: "one minute",
      functionsLike: {
        exceptThat: "the range increases to 2,000 feet.",
        spell: "detect air",
      },
      // narrative: '',
      rank: 5,
      type: "Instant",
    },
  ],
};
