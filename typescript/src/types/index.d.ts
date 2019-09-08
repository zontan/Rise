declare namespace Creature {
  type Attribute = "str" | "dex" | "con" | "int" | "per" | "wil";

  type Attributes = Record<Attribute, number>;

  type Skill =
    // Strength
    | "climb"
    | "jump"
    | "swim"

    // Dexterity
    | "acrobatics"
    | "escape artist"
    | "ride"
    | "sleight of hand"
    | "stealth"

    // Constitution has no skills

    // Intelligence
    | "craft"
    | "deduction"
    | "devices"
    | "disguise"
    | "heal"
    | "knowledge"
    | "linguistics"

    // Perception
    | "awareness"
    | "creature handling"
    | "sense motive"
    | "spellcraft"
    | "survival"

    // Willpower has no skills

    // Other skills
    | "bluff"
    | "intimidate"
    | "perform"
    | "persuasion";

  type Skills = Record<Skill, number>;

  type Size =
    | "fine"
    | "diminuitive"
    | "tiny"
    | "small"
    | "medium"
    | "large"
    | "huge"
    | "gargantuan"
    | "colossal";
}

type DamageType =
  | "physical"
  | "acid"
  | "bludgeoning"
  | "piercing"
  | "slashing"
  | "energy"
  | "cold"
  | "electricity"
  | "fire";

type ResistanceType = DamageType | "global";
