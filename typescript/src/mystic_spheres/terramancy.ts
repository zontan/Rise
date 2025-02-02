import { MysticSphere } from ".";

export const terramancy: MysticSphere = {
  name: "Terramancy",
  shortDescription: "Manipulate earth to crush foes.",
  sources: ["arcane", "domain", "nature"],

  cantrips: [
    {
      name: "Shape Earth",

      effect: `
        Choose one unattended, nonmagical body of earth or unworked stone you touch.
        You make a Craft check to alter the subject (see \\pcref{Craft}), except that you do not need any special tools to make the check, such as a shovel or hammer and chisel.
        The maximum \\glossterm{damage resistance} of a material you can affect with this ability is equal to your \\glossterm{power}.

        % should be longer than polymorph's alter object ability
        Each time you cast this spell, you can accomplish work that would take up to five rounds with a normal Craft check.
      `,
      focus: false,
      scaling: {
        2: `The amount of work you accomplish with the spell increases to one minute.`,
        4: `The amount of work you accomplish with the spell increases to two minutes.`,
        6: `The amount of work you accomplish with the spell increases to five minutes.`,
      },
      type: "Instant",
    },
  ],
  spells: [
    {
      name: "Rock Throw",

      attack: {
        hit: `The subject takes 1d10 + \\glossterm{power} bludgeoning damage.`,
        targeting: `
          Make an attack vs. Armor against anything within \\medrange.
          This attack gains a +2 \\glossterm{accuracy} bonus if you are on a Medium or larger body of stone.
        `,
      },
      rank: 1,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },

    {
      name: "Greater Rock Throw",

      attack: {
        hit: `The subject takes 4d6 + \\glossterm{power} bludgeoning damage.`,
        targeting: `
          Make an attack vs. Armor against anything within \\longrange.
          This attack gains a +2 \\glossterm{accuracy} bonus if you are on a Medium or larger body of stone.
        `,
      },
      rank: 4,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },

    {
      name: "Supreme Rock Throw",

      attack: {
        hit: `The subject takes 6d10 + \\glossterm{power} bludgeoning damage.`,
        targeting: `
          Make an attack vs. Armor against anything within \\distrange.
          This attack gains a +2 \\glossterm{accuracy} bonus if you are on a Medium or larger body of stone.
        `,
      },
      rank: 7,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },

    {
      name: "Shrapnel Blast",

      attack: {
        hit: `Each subject takes 1d8 + half \\glossterm{power} bludgeoning and piercing damage.`,
        targeting: `
          Make an attack vs. Reflex against everything in a \\smallarea cone from you.
          This attack gains a +2 \\glossterm{accuracy} bonus if you are on a Medium or larger body of stone.
        `,
      },
      rank: 1,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },

    {
      name: "Earthcraft",

      effect: `
        You create up to three weapons, suits of body armor, or shields from a body of earth or stone within 5 feet of you.
        You can create any weapon, shield, or body armor that you are proficient with, and which could normally be made entirely from metal, except for heavy armor.
        The body targeted must be at least as large as the largest item you create.

        An item created with this spell functions like a normal item of its type, except that any \\glossterm{strikes} that you make with a weapon created with this ability are \\glossterm{magical} abilities, so you use your magical \\glossterm{power} to determine their damage instead of your \\glossterm{mundane} power.
      `,
      rank: 1,
      scaling: {
        3: `
          You can also create heavy armor.
          In addition, the items is magically enhanced.
          A weapon grants a +1 \\glossterm{magic bonus} to \\glossterm{accuracy} with strikes using the weapon,
            and both shields and body armor grant a +1 \\glossterm{magic bonus} to Armor defense.
        `,
        5: `The magic bonus increases to +2.`,
        7: `The magic bonus increases to +3.`,
      },
      type: "Attune (self)",
    },

    {
      name: "Earthspike",

      attack: {
        glance: `Half damage.`,
        hit: `The subject takes 2d8 piercing damage.
        If it loses \\glossterm{hit points} from this damage, it is \\immobilized as a \\glossterm{condition}.`,
        targeting: `
          Make an attack vs. Armor against anything within \\shortrange that is on a stable surface.
          This attack gains a +2 \\glossterm{accuracy} bonus if the target is on a Medium or larger body of stone.
        `,
      },
      rank: 5,
      scaling: "accuracy",
      tags: ["Manifestation"],
      type: "Duration",
    },

    {
      name: "Earthcage",

      attack: {
        crit: `The condition must be removed twice before the effect ends.`,
        glance: "The effect lasts \\glossterm{briefly}.",
        hit: `
          The subject is is \\decelerated as a \\glossterm{condition}.
          While it has no remaining \\glossterm{damage resistance}, it is \\immobilized instead of decelerated.
        `,
        targeting: `
          Make an attack vs. Reflex against one Large or smaller creature within \\medrange.
          This attack gains a +2 \\glossterm{accuracy} bonus if the target is on a Medium or larger body of stone.
        `,
      },
      rank: 7,
      scaling: "accuracy",
      type: "Duration",
    },

    {
      name: "Meld into Stone",

      effect: `
        You and up to 100 pounds of nonliving equipment meld into one stone object you touch that is at least as large as your body.
        If you try to bring excess equipment into the stone, the spell fails without effect.

        As long as the spell lasts, you can move within the stone as if it was thick water.
        However, at least part of you must remain within one foot of the place you originally melded with the stone.
        You gain no special ability to breathe or see while embedded the stone, and you cannot speak if your mouth is within the stone.
        The stone muffles sound, but very loud noises may reach your ears within it.
        If you fully exit the stone, this spell ends.

        If this spell ends before you exit the stone, or if the stone stops being a valid target for the spell (such as if it is broken into pieces), you are forcibly expelled from the stone.
        When you are forcibly expelled from the stone, you take 4d10 bludgeoning damage and become \\nauseated as a \\glossterm{condition}.
      `,
      rank: 3,
      scaling: {
        5: `Exiting the stone does not cause this spell to end.
            You can repeatedly exit and re-enter the stone as long as you maintain attunement to the spell.`,
        7: `You can leave tiny tunnels carrying air through the stone as you move through it, allowing you to effectively breathe within the stone.
            These trails disappear when this spell ends.`,
      },
      type: "Attune (self)",
    },

    {
      name: "Tremor",

      attack: {
        crit: `Each subject is also unable to stand up as a \\glossterm{condition}.`,
        hit: `Each subject is knocked \\prone.`,
        targeting: `
          Make an attack vs. Reflex against all Large or smaller creatures in a \\smallarea within \\medrange that are on a stable surface.
          This attack gains a +2 \\glossterm{accuracy} bonus against each target that is on a Medium or larger body of stone.
        `,
      },
      narrative: `
        You create an highly localized tremor that rips through the ground.
      `,
      rank: 1,
      scaling: "accuracy",
      type: "Duration",
    },

    {
      name: "Fissure",

      attack: {
        glance: `Half damage.`,
        hit: `Each subject takes 2d8 + half \\glossterm{power} bludgeoning damage.
        Each Large or smaller target that loses \\glossterm{hit points} from this damage is also knocked \\prone.`,
        targeting: `
          Make an attack vs. Reflex against everything in a \\smallarea within \\medrange that is on a stable surface.
          This attack gains a +2 \\glossterm{accuracy} bonus against each target that is on a Medium or larger body of stone.
        `,
      },
      narrative: `
        You create an intense but highly localized tremor that rips through the ground.
      `,
      rank: 4,
      scaling: "damage",
      type: "Instant",
    },

    {
      name: "Earthquake",

      attack: {
        glance: `Half damage.`,
        hit: `Each subject takes 4d8 + half \\glossterm{power} bludgeoning damage.
        Each Huge or smaller subject that takes damage this way is also knocked \\prone.`,
        targeting: `
          Make an attack vs. Reflex against everything in a \\largearea radius within \\longrange that is on a stable surface.
          This attack gains a +2 \\glossterm{accuracy} bonus against each target that is on a Medium or larger body of stone.
        `,
      },
      narrative: `
        You create an intense tremor that rips through the ground.
      `,
      rank: 7,
      type: "Instant",
    },

    {
      name: "Swallowed by Earth",

      // losing line of effect compensates for recurring extra damage
      attack: {
        glance: `Half damage.`,
        hit: `The subject takes 4d6 bludgeoning damage.
        If it is Large or smaller and it loses \\glossterm{hit points} from this damage, it is swallowed by the earth as a \\glossterm{condition}.
        While it is swallowed by the earth, it is \\paralyzed and does not have \\glossterm{line of sight} or \\glossterm{line of effect} to any creature other than itself.
        At the end of each subsequent round, it takes 4d6 bludgeoning damage as the earth grinds it into paste.
        If the earth or stone it is swallowed by is destroyed or otherwise rendered unable to contain the creature, this effect ends.
        Special movement abilities such as teleportation can also remove the subject from the fissure.`,
        targeting: `
          Make an attack vs. Reflex against one creature within \\medrange that is on a stable surface.
          This attack gains a +2 \\glossterm{accuracy} bonus if the target is on a Medium or larger body of stone.
        `,
      },
      narrative: `
        You open up a rift in the ground that swallows and traps a foe.
      `,
      rank: 7,
      type: "Duration",
    },

    {
      name: "Earthbind",

      attack: {
        crit: `The condition must be removed twice before the effect ends.`,
        hit: `
          As a \\glossterm{condition}, the subject is pulled towards the ground with great force, approximately doubling the gravity it experiences.
          It is \\slowed and unable to use any fly speed or glide speed.
        `,
        targeting: `
          Make an attack vs. Fortitude against one creature within \\medrange that is no more than 120 feet above a stable surface that could support its weight.
          This attack gains a +2 \\glossterm{accuracy} bonus if that surface is a Medium or larger body of stone.
        `,
      },
      rank: 2,
      scaling: "accuracy",
      type: "Duration",
    },

    {
      name: "Greater Earthbind",

      functionsLike: {
        name: 'earthbind',
        exceptThat: 'the subject is \\decelerated instead of slowed.',
      },
      rank: 6,
      scaling: "accuracy",
      type: "Duration",
    },

    {
      name: "Quagmire",

      effect: `
        % TODO: wording to allow it to affect smaller parts of larger objects
        % TODO: define maximum resistance
        Choose one \\smallarea radius \\glossterm{zone} within \\longrange.
        All earth and stone in the area is softened into a thick sludge, creating a quagmire that is difficult to move through.
        The movement cost required to move out of each affected square within the area is quadrupled.
        This does not affect objects under structural stress, such as walls and support columns.
      `,
      rank: 4,
      scaling: { 6: `The area increases to a \\medarea radius.` },
      type: "Sustain (minor)",
    },

    {
      name: "Earthen Fortification",

      effect: `
        You construct a fortification made of packed earth within \\medrange.
        This takes the form of up to ten contiguous 5-foot squares, each of which is four inches thick.
        The squares can be placed at any angle and used to form any structure as long as that structure is stable.
        Since the fortifications are made of packed earth, their maximum weight is limited, and structures taller than ten feet high are usually impossible.
        % TODO: define hit points and resistances of earth

        The fortifications form slowly, rather than instantly.
        The structure becomes complete at the end of the action phase in the next round after this spell is cast.
        This makes it difficult to trap creatures within structures formed.
      `,
      rank: 4,
      // TODO: define hit points and resistances of stone
      scaling: {
        6: `You can also construct fortifications from stone.
            This makes them more resistant to attack and allows the construction of more complex structures.`,
      },
      tags: ["Manifestation"],
      type: "Attune (self)",
    },

    {
      name: "Earthglide",

      effect: `
        You can move through earth and unworked stone at a rate of 5 feet per round.
        This does not allow you to breathe while inside the earth or stone, so your ability to traverse long distances may be limited.
      `,
      rank: 5,
      scaling: { 7: `Your speed increases to be equal to half the \\glossterm{base speed} for your size.` },
      type: "Attune (self)",
    },

    {
      name: "Rocky Shell",

      effect: `
        You cover your body with two overlapping layers of rock that crumple when they take damage.
        The rock does not cover your joints, allowing you to move, though the shell increases your \\glossterm{encumbrance} by 2.
        Whenever you would take damage, you take only half of that damage, and one layer of rock is destroyed.
        When the last layer is destroyed, this ability provides no further benefit.

        If you take simultaneous damage from more sources than you have remaining layers, the remaining layers apply to the largest damage sources, and you take full damage from any lower damage values.
      `,
      rank: 2,
      scaling: {
        4: `The spell creates three layers of rock.`,
        6: `The spell creates four layers of rock.`,
      },
      tags: ["Manifestation"],
      type: "Attune (self)",
    },

    {
      name: "Earthen Anchor",

      effect: `
        You are immune to \\glossterm{knockback} or \\glossterm{push} effects from attacks, unless the effects come from an attack that scores a \\glossterm{critical hit}.
        This does not make it immune to \\glossterm{teleportation}, and does not affect movement effects used by its \\glossterm{allies}.
      `,
      rank: 2,
      scaling: {
        4: `You are also immune to \\glossterm{teleport} effects from attacks that are not critical hits.`,
        6: `You are immune to knockback, push, and teleport effects from all attacks, including critical hits.`,
      },
      type: "Attune (self)",
    },

    {
      name: "Mass Earthen Anchor",

      castingTime: "minor action",
      functionsLike: {
        mass: true,
        name: "Earthen Anchor",
      },
      // narrative: '',
      rank: 4,
      scaling: {
        6: "Each subject is also immune to \\glossterm{teleport} effects from attacks that are not critical hits.",
      },
      type: "Attune (target)",
    },

    {
      name: "Volcano",

      attack: {
        hit: `Each subject takes 2d6 + half \\glossterm{power} bludgeoning and fire damage.`,
        targeting: `
          Make an attack vs. Reflex against everything in a \\areasmall radius from a point on a stable surface within \\shortrange.
          This attack gains a +2 \\glossterm{accuracy} bonus if that point is on a Medium or larger body of stone.
        `,
      },
      narrative: `
        You create a small volcano that bursts forth, showering nearby creatures in burning shrapnel.
      `,
      rank: 2,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },

    {
      name: "Greater Volcano",

      attack: {
        hit: `Each subject takes 4d8 + half \\glossterm{power} bludgeoning and fire damage.`,
        targeting: `
          Make an attack vs. Reflex against everything in a \\arealarge radius from a point on a stable surface within \\longrange.
          This attack gains a +2 \\glossterm{accuracy} bonus if that point is on a Medium or larger body of stone.
        `,
      },
      narrative: `
        You create a large volcano that bursts forth, showering nearby creatures in burning shrapnel.
      `,
      rank: 6,
      scaling: "damage",
      tags: ["Manifestation"],
      type: "Instant",
    },
  ],
  rituals: [],
};
