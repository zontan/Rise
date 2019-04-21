from sheet_data import ATTRIBUTES, ATTRIBUTE_SKILLS

def generate_script():
    return "\n".join([
        '<script type="text/worker">',
        *[attribute_change(a.lower()) for a in ATTRIBUTES],
        *[attribute_skills(a.lower()) for a in ATTRIBUTE_SKILLS],
        accuracy(),
        armor_defense(),
        fortitude(),
        reflex(),
        mental(),
        threat(),
        encumbrance(),
        initiative(),
        base_speed(),
        legend_points(),
        wound_threshold(),
        skill_points(),
        '</script>',
        ""
    ])


def attribute_change(a):
    return f"""
        on("change:level change:{a}_starting change:{a}_misc", function(eventInfo) {{
            getAttrs(["{a}_starting", "{a}_misc", "level"], function(v) {{
                var starting = Number(v.{a}_starting);
                var scaling = 0;
                if (starting === 1) {{
                    scaling = Math.floor(v.level / 2);
                }} else if (starting > 1) {{
                    scaling = Number(v.level) - 1;
                }}
                setAttrs({{
                    {a}: starting + scaling + Number(v.{a}_misc),
                    {a}_scaling: scaling,
                }});
            }});
        }});
    """


def attribute_skills(attribute):
    return '\n'.join([
        set_skill(attribute, skill.lower().replace(' ', '_'))
        for skill in ATTRIBUTE_SKILLS[attribute]
    ])


def set_skill(a, s):
    if a == 'other':
        return f"""
            on("change:level change:{s}_points change:{s}_misc", function(eventInfo) {{
                getAttrs(["level", "{s}_points", "{s}_misc"], function(v) {{
                    var level = Number(v.level);
                    var pointsModifier = 0;
                    var ranks = 0;

                    if (Number(v.{s}_points) === 1) {{
                        ranks = Math.floor(level / 2);
                        pointsModifier = 1;
                    }} else if (Number(v.{s}_points) >= 2) {{
                        ranks = level
                        pointsModifier = 4;
                    }}

                    setAttrs({{
                        {s}_attribute: 0,
                        {s}_ranks: ranks + pointsModifier,
                        {s}_total: ranks + pointsModifier + Number(v.{s}_misc),
                    }});
                }});
            }});
        """
    else:
        include_encumbrance = a in ['strength', 'dexterity']
        encumbrance_changed = ' change:encumbrance' if include_encumbrance else ""
        get_encumbrance = ', "encumbrance"' if include_encumbrance else ""
        subtract_encumbrance = ' - Number(v.encumbrance)' if include_encumbrance else ""
        return f"""
            on("sheet:opened change:level change:{a} change:{s}_points change:{s}_misc{encumbrance_changed}", function(eventInfo) {{
                getAttrs(["level", "{a}", "{a}_starting", "{s}_points", "{s}_misc"{get_encumbrance}], function(v) {{
                    var level = Number(v.level);
                    var attributeModifier = 0;
                    var pointsModifier = 0;
                    var ranks = 0;

                    if (Number(v.{s}_points) === 1) {{
                        attributeModifier = Number(v.{a});
                        ranks = Math.floor(level / 2);
                        pointsModifier = 1;
                    }} else if (Number(v.{s}_points) >= 2) {{
                        attributeModifier = Number(v.{a});
                        ranks = level
                        pointsModifier = 4;
                    }}

                    var scaling = Math.max(ranks, attributeModifier);

                    var negativeModifier = Number(v.{a}) < 0 ? Number(v.{a}) : 0;

                    setAttrs({{
                        {s}_attribute: attributeModifier,
                        {s}_ranks: ranks,
                        {s}_total: scaling + pointsModifier + negativeModifier + Number(v.{s}_misc || 0){subtract_encumbrance},
                    }});
                }});
            }});
        """


def accuracy():
    return f"""
        on("change:level change:perception", function(eventInfo) {{
            getAttrs(["level", "perception"], function(v) {{
                var cr_mod = Math.max(0, Number(v.challenge_rating || 1) - 1);
                setAttrs({{
                    base_accuracy: Math.max(Number(v.level), Number(v.perception)) + cr_mod,
                }});
            }});
        }});
    """


def armor_defense():
    return f"""
        on("change:level change:dexterity change:body_armor_defense_value change:shield_defense_value change:armor_defense_misc change:challenge_rating", function(eventInfo) {{
            getAttrs(["level", "dexterity", "body_armor_defense_value", "shield_defense_value", "armor_defense_misc", "challenge_rating"], function(v) {{
                var scaling = Math.max(Number(v.level), Number(v.dexterity));
                var cr_mod = Math.max(0, Number(v.challenge_rating || 1) - 1);
                var total = scaling + Number(v.body_armor_defense_value) + Number(v.shield_defense_value) + Number(v.armor_defense_misc) + cr_mod;
                setAttrs({{
                    armor_defense: total,
                    armor_defense_scaling: scaling,
                }});
            }});
        }});
    """

def fortitude():
    return f"""
        on("change:level change:strength change:constitution change:fortitude_class change:fortitude_misc change:challenge_rating", function(eventInfo) {{
            getAttrs(["level", "strength", "constitution", "constitution_starting", "fortitude_class", "fortitude_misc", "challenge_rating"], function(v) {{
                var scaling = Math.max(Number(v.level), Number(v.constitution));
                var cr_mod = Math.max(0, Number(v.challenge_rating || 1) - 1);
                var total = scaling + Number(v.constitution_starting) + Number(v.fortitude_class) + Number(v.fortitude_misc) + cr_mod;
                setAttrs({{
                    fortitude: total,
                    fortitude_scaling: scaling,
                }});
            }});
        }});
    """

def reflex():
    return f"""
        on("change:level change:dexterity change:perception change:shield_defense_value change:reflex_class change:reflex_misc change:challenge_rating", function(eventInfo) {{
            getAttrs(["level", "dexterity", "perception", "dexterity_starting", "reflex_class", "reflex_misc", "challenge_rating"], function(v) {{
                var scaling = Math.max(Number(v.level), Number(v.dexterity));
                var cr_mod = Math.max(0, Number(v.challenge_rating || 1) - 1);
                var total = scaling + Number(v.dexterity_starting) + Number(v.reflex_class) + Number(v.reflex_misc) + cr_mod;
                setAttrs({{
                    reflex: total,
                    reflex_scaling: scaling,
                }});
            }});
        }});
    """

def mental():
    return f"""
        on("change:level change:intelligence change:willpower change:mental_class change:mental_misc change:challenge_rating", function(eventInfo) {{
            getAttrs(["level", "intelligence", "willpower", "willpower_starting", "mental_class", "mental_misc", "challenge_rating"], function(v) {{
                var scaling = Math.max(Number(v.level), Number(v.willpower));
                var cr_mod = Math.max(0, Number(v.challenge_rating || 1) - 1);
                var total = scaling + Number(v.willpower_starting) + Number(v.mental_class) + Number(v.mental_misc) + cr_mod;
                setAttrs({{
                    mental: total,
                    mental_scaling: scaling,
                }});
            }});
        }});
    """

def threat():
    return f"""
        on("change:level change:strength change:body_armor_defense_value change:threat_misc", function(eventInfo) {{
            getAttrs(["level", "strength", "body_armor_defense_value", "threat_misc"], function(v) {{
                var scaling = Math.max(Number(v.level), Number(v.strength));
                var armor_modifier = Math.floor(Number(v.body_armor_defense_value) / 2);
                setAttrs({{
                    threat: scaling + armor_modifier + Number(v.threat_misc),
                    threat_armor: armor_modifier,
                    threat_scaling: scaling,
                }});
            }});
        }});
    """

def encumbrance():
    return f"""
        on("change:body_armor_encumbrance change:encumbrance_misc change:strength_starting", function(eventInfo) {{
            getAttrs(["body_armor_encumbrance", "encumbrance_misc", "strength_starting"], function(v) {{
                setAttrs({{
                    encumbrance: Math.max(
                        Number(v.body_armor_encumbrance || 0)
                        - Number(v.encumbrance_misc || 0)
                        - Number(v.strength_starting)
                    , 0),
                }});
            }});
        }});
    """

def initiative():
    return f"""
        on("change:dexterity change:perception change:initiative_misc", function(eventInfo) {{
            getAttrs(["dexterity", "perception", "initiative_misc"], function(v) {{
                var scaling = Math.max(Number(v.dexterity), Number(v.perception));
                setAttrs({{
                    initiative: scaling + Number(v.initiative_misc),
                    initiative_scaling: scaling,
                }});
            }});
        }});
    """

def base_speed():
    return f"""
        on("change:speed_size change:speed_armor change:speed_misc", function(eventInfo) {{
            getAttrs(["speed_size", "speed_armor", "speed_misc"], function(v) {{
                setAttrs({{
                    base_speed: Number(v.speed_size || 0) - Number(v.speed_armor || 0) + Number(v.speed_misc || 0),
                }});
            }});
        }});
    """

def legend_points():
    return f"""
        on("change:level", function(eventInfo) {{
            getAttrs(["level"], function(v) {{
                setAttrs({{
                    legend_points: Number(v.level) >= 3 ? 1 : 0,
                }});
            }});
        }});
    """

def wound_threshold():
    return f"""
        on("change:wound_threshold_misc change:level change:constitution_starting change:challenge_rating", function(eventInfo) {{
            getAttrs(["wound_threshold_misc", "level", "constitution_starting", "challenge_rating"], function(v) {{
                var from_level = (1 + Number(v.level || 0)) * (5 + Number(v.constitution_starting || 0))
                var wound_threshold = Number(v.wound_threshold_misc || 0) + from_level;
                setAttrs({{
                    wound_threshold_max: wound_threshold,
                    wound_threshold_total: wound_threshold,
                }});
            }});
        }});
    """

def skill_points():
    return f"""
        on("change:intelligence_starting change:skill_points_misc", function(eventInfo) {{
            getAttrs(["intelligence_starting", "skill_points_misc"], function(v) {{
                setAttrs({{
                    skill_points: 8 + Number(v.intelligence_starting || 0) * 2 + Number(v.skill_points_misc || 0),
                }});
            }});
        }});
    """
