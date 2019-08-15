from cgi_simple import (
    div, fieldset, equation, flex_col, flex_row, flex_wrapper, labeled_text_input, minus, number_input,
    plus, span, text_input, underlabel
)
from sheet_data import ATTRIBUTE_SHORTHAND, ATTRIBUTE_SKILLS, ATTRIBUTES, ROLL20_CALC

equation_space = flex_col({'class': 'equation-glue'}, div({'class': 'equation-math'}, ' '))

def equation_misc(name, i=0):
    return flex_col([
        number_input({
            'class': 'equation-misc',
            'name': f"{name}_misc_{i}",
        }),
        text_input({
            'class': 'invisible-text-input',
            'name': f"{name}_misc_label_{i}",
        }),
    ])

def equation_misc_repeat(name, count=1):
    return plus().join([
        equation_misc(name, i)
        for i in range(count)
    ])

def create_page(destination):
    return flex_row({'class': 'second-page'}, [
        flex_col({'class': 'sidebar'}, [
            calc_skills(destination),
            level_chart(),
            flex_wrapper(div({'class': 'section-header abilities-known-header'}, 'Abilities Known')),
            calc_maneuvers(),
            calc_spells(),
            *[calc_blank_ability(i) for i in range(2)],
        ]),
        flex_col({'class': 'main-body'}, [
            flex_col({'class': 'statistics'}, [
                flex_wrapper(div({'class': 'section-header'}, 'Core Statistics')),
                calc_accuracy(),
                calc_base_speed(),
                calc_carrying_capacity(),
                calc_encumbrance(),
                calc_hit_points(),
                calc_initiative(),
                calc_insight_points(),
                calc_magical_power(),
                calc_mundane_power(),
                calc_skill_points(),
                flex_wrapper(div({'class': 'section-header'}, 'Defenses')),
                calc_defenses(),
                flex_wrapper(div({'class': 'section-header'}, 'Resistances')),
                calc_base_resistances(),
                calc_global_resistance(),
                calc_energy_resistance(),
                calc_physical_resistance(),
            ]),
            flex_wrapper(div({'class': 'section-header skill-modifiers'}, 'Skill Modifiers')),
            flex_row({'class': 'skill-modifier-reminder'}, [
                flex_col([
                    div({'class': 'skill-modifier-reminder-header'}, 'Training Level'),
                    div('Untrained'),
                    div('Trained'),
                    div('Mastered'),
                ]),
                flex_col([
                    div({'class': 'skill-modifier-reminder-header'}, 'Modifier'),
                    div('Half key attribute'),
                    div('Key attribute or 1 + half level'),
                    div('4 + key attribute or 4 + level'),
                ]),
            ])
        ]),
    ])

def calc_skills(destination):
    # Does not work
    blank_skill_info = [
        calc_skill('')
        for i in range(15)
    ] if destination == 'paper' else [
        div({'class': 'other-skills-header'}, 'Other Skills'),
        fieldset({'class': 'repeating_blankskills'}, [
            calc_blank_skill(),
        ]),
    ]

    return flex_col({'class': 'calc-skills'}, [
        div({'class': 'section-header'}, 'Skills'),
        skill_labels(),
        *blank_skill_info
    ])

def skill_labels():
    return flex_row({'class': 'skill-labels'}, [
        div({'class': 'skill-name'}),
        div({'class': 'skill-label'}, 'Points'),
        div({'class': 'skill-label'}, 'Mod'),
        div({'class': 'skill-label misc'}, 'Misc'),
    ])

def calc_skill(skill_name, attribute=None):
    skill_parsable = skill_name.lower().replace(' ', '_')
    return flex_row({'class': 'skill-row'}, [
        span({'class': 'skill-name'}, skill_name),
        number_input({'class': 'skill-points', 'name': skill_parsable + '_points'}),
        number_input({
            'class': 'skill-mod',
            'disabled': True,
            'name': skill_parsable + '_mod_display',
            'value': '@{' + skill_parsable + '_mod}',
        }),
        number_input({
            'class': 'equation-misc',
            'name': skill_parsable + '_misc_0',
        }),
        number_input({
            'class': 'equation-misc',
            'name': skill_parsable + '_misc_1',
        }),
    ])


def calc_blank_skill():
    return flex_row({'class': 'skill-row'}, [
        text_input({'class': 'skill-name', 'name': 'blank_skill_name'}),
        number_input({'class': 'skill-points', 'name': 'blank_skill_points'}),
        number_input({'class': 'skill-ranks', 'name': 'blank_skill_ranks'}),
        number_input({'class': 'skill-attr', 'name': 'blank_skill_attribute'}),
        equation_misc('blank_skill'),
    ])


def calc_attributes():
    return flex_col({'class': 'calc-attributes'}, [
        flex_wrapper(div({'class': 'section-header attributes-header'}, 'Attributes')),
        ''.join([calc_attribute(attribute.lower()) for attribute in ATTRIBUTES]),
    ])

def calc_attribute(attribute_name):
    return ''.join([
        equation(
            [
                underlabel('(Start)', number_input({
                    'name': attribute_name + '_starting',
                })),
                plus(),
                underlabel('Lvl mod', number_input({
                    'disabled': True,
                    'name': attribute_name + '_scaling_display',
                    'value': '@{' + attribute_name + '_scaling}',
                })),
                plus(),
                equation_misc(attribute_name),
            ],
            result_attributes={
                'disabled': 'true',
                'name': attribute_name + '_display',
                'value': '@{' + attribute_name + '}',
            },
            result_label=ATTRIBUTE_SHORTHAND[attribute_name],
            underlabel_attributes={'class': 'attribute-name'},
        )
    ])

def level_chart():
    return flex_row([
        calc_attributes(),
        adventuring(),
    ])

def abilities(name_prefix):
    return flex_col({'class': 'abilities'}, [
        flex_wrapper(div({'class': 'ability-header chart-header'}, 'Feats and Abilities')),
        ''.join([text_input({
            'class': 'level' + str(level),
            'name': 'ability-name-' + name_prefix + '-' + str(level)
        }) for level in range(1, 14)]),
    ])

def calc_carrying_capacity():
    return flex_row([
        div({'class': 'calc-header'}, 'Carrying Capacity'),
        underlabel(
            'Light',
            number_input({
                'disabled': False,
                'name': 'carrying_capacity_light_display',
            }),
        ),
        equation_space,
        underlabel(
            'Max',
            number_input({
                'disabled': False,
                'name': 'carrying_capacity_max_display',
            }),
        ),
        equation_space,
        underlabel(
            'Over',
            number_input({
                'disabled': False,
                'name': 'carrying_capacity_over_display',
            }),
        ),
        equation_space,
        underlabel(
            'Push',
            number_input({
                'disabled': False,
                'name': 'carrying_capacity_push_display',
            }),
        ),
    ])

def calc_accuracy():
    return flex_row([
        div({'class': 'calc-header'}, 'Accuracy'),
        equation(
            [
                underlabel('Lvl/Per', number_input({
                    'disabled': True,
                    'name': 'accuracy_scaling_display',
                    'value': '@{accuracy_scaling}',
                })),
                plus(),
                equation_misc_repeat('accuracy', 3),
            ],
            result_attributes={
                'disabled': True,
                'name': 'accuracy_display',
                'value': '@{accuracy}',
            },
        ),
    ])

def calc_base_resistances():
    return flex_row([
        div({'class': 'calc-header'}, 'Base Resistances'),
        underlabel(
            'Damage',
            number_input({
                'disabled': True,
                'name': 'damage_resistance_base_display',
                'value': '(@{damage_resistance_base})',
            }),
        ),
        equation_space,
        underlabel(
            'Wound',
            number_input({
                'disabled': False,
                'name': 'wound_resistance_base_display',
                'value': '(@{wound_resistance_base})',
            }),
        ),
    ])

def calc_damage_resistance():
    return flex_row([
        div({'class': 'calc-header'}, 'Damage Resist'),
        equation(
            [
                underlabel(
                    'Base',
                    number_input({
                        'disabled': True,
                        'name': 'damage_resistance_base_display',
                        'value': '@{damage_resistance_base}',
                    }),
                ),
                plus(),
                equation_misc_repeat('damage_resistance', 3)
            ],
            result_attributes={
                'disabled': 'true',
                'name': 'damage_resistance_display',
                'value': '(@{damage_resistance})',
            },
        ),
    ])

def calc_wound_resistance():
    return flex_row([
        div({'class': 'calc-header'}, 'Wound Resist'),
        equation(
            [
                underlabel(
                    'Base',
                    number_input({
                        'disabled': True,
                        'name': 'wound_resistance_base_display',
                        'value': '@{wound_resistance_base}',
                    }),
                ),
                plus(),
                equation_misc_repeat('wound_resistance', 3),
            ],
            result_attributes={
                'disabled': 'true',
                'name': 'wound_resistance_display',
                'value': '(@{wound_resistance})',
            },
        ),
    ])

def calc_global_resistance():
    return flex_row([
        div({'class': 'calc-header'}, 'All Damage'),
        equation(
            [
                equation_misc_repeat('global_resistance', 4)
            ],
            result_attributes={
                'disabled': 'true',
                'name': 'global_resistance_display',
                'value': '(@{global_resistance})',
            },
            result_label='Bonus'
        ),
    ])

def calc_physical_resistance():
    return flex_row([
        div({'class': 'calc-header'}, 'Physical Damage'),
        equation(
            [
                underlabel(
                    'Armor',
                    number_input({
                        'disabled': True,
                        'name': 'physical_resistance_base_display',
                        'value': '@{physical_resistance_base}',
                    }),
                ),
                plus(),
                equation_misc_repeat('physical_resistance', 3)
            ],
            result_attributes={
                'disabled': 'true',
                'name': 'physical_resistance_display',
                'value': '(@{physical_resistance})',
            },
            result_label='Bonus'
        ),
    ])

def calc_energy_resistance():
    return flex_row([
        div({'class': 'calc-header'}, 'Energy Damage'),
        equation(
            [
                equation_misc_repeat('energy_resistance', 4)
            ],
            result_attributes={
                'disabled': 'true',
                'name': 'energy_resistance_display',
                'value': '(@{energy_resistance})',
            },
            result_label='Bonus'
        ),
    ])

def calc_hit_points():
    return flex_row([
        div({'class': 'calc-header'}, 'Hit Points'),
        equation(
            [
                underlabel('Base', number_input({
                    'disabled': True,
                    'name': 'hit_points_base',
                    'value': '6',
                })),
                plus(),
                underlabel('(Con)', number_input({
                    'disabled': True,
                    'name': 'hit_points_constitution',
                    'value': '(@{constitution_starting})',
                })),
                plus(),
                equation_misc_repeat('hit_points', 2),
            ],
            result_attributes={
                'disabled': True,
                'name': 'initiative_display',
                'value': '@{initiative}',
            },
        ),
    ])

def calc_initiative():
    return flex_row([
        div({'class': 'calc-header'}, 'Initiative'),
        equation(
            [
                underlabel('Dex/Per', number_input({
                    'disabled': True,
                    'name': 'initiative_scaling_display',
                    'value': '@{initiative_scaling}',
                })),
                plus(),
                equation_misc_repeat('initiative', 3),
            ],
            result_attributes={
                'disabled': True,
                'name': 'initiative_display',
                'value': '@{initiative}',
            },
        ),
    ])

def calc_magical_power():
    return flex_row([
        div({'class': 'calc-header'}, 'Magical Power'),
        equation(
            [
                underlabel('Lvl/Wil', number_input({
                    'disabled': True,
                    'name': 'magical_power_scaling_display',
                    'value': '@{magical_power_scaling}',
                })),
                plus(),
                equation_misc_repeat('magical_power', 3),
            ],
            result_attributes={
                'disabled': True,
                'name': 'magical_power_display',
                'value': '@{magical_power}',
            },
        ),
    ])

def calc_mundane_power():
    return flex_row([
        div({'class': 'calc-header'}, 'Mundane Power'),
        equation(
            [
                underlabel('Lvl/Str', number_input({
                    'disabled': True,
                    'name': 'mundane_power_scaling_display',
                    'value': '@{mundane_power_scaling}',
                })),
                plus(),
                equation_misc_repeat('mundane_power', 3),
            ],
            result_attributes={
                'disabled': True,
                'name': 'mundane_power_display',
                'value': '@{mundane_power}',
            },
        ),
    ])

def calc_base_speed():
    return flex_row([
        div({'class': 'calc-header'}, 'Base Speed'),
        equation(
            [
                underlabel('Size', number_input({'name': 'speed_size'})),
                minus(),
                underlabel('Armor', number_input({'name': 'speed_armor'})),
                plus(),
                equation_misc_repeat('speed', 2)
            ],
            result_attributes={
                'disabled': True,
                'name': 'base_speed_display',
                'value': '@{base_speed}',
            },
        )
    ])

# def calc_strike_damage():
#     return flex_row([
#         div({'class': 'calc-header'}, 'Strike Dmg'),
#         equation(
#             [
#                 underlabel('Lvl/Str', text_input({
#                     'name': 'strike_damage_scaling_display',
#                 })),
#                 plus(),
#                 text_input({
#                     'class': 'equation-misc',
#                     'name': 'strike_damage_misc',
#                 }),
#             ],
#             result_attributes={
#                 'name': 'strike_damage_display',
#             },
#             input_type=text_input,
#         ),
#     ])

# def calc_threat():
#     return flex_row([
#         div({'class': 'calc-header'}, 'Threat'),
#         equation(
#             [
#                 underlabel('Lvl/Str', number_input({
#                     'disabled': True,
#                     'name': 'threat_scaling_display',
#                     'value': '@{threat_scaling}',
#                 })),
#                 plus(),
#                 underlabel('1/2 Armor', number_input({
#                     'disabled': True,
#                     'name': 'threat_armor_display',
#                     'value': '@{threat_armor}',
#                 })),
#                 equation_misc('threat')
#             ],
#             result_attributes={
#                 'disabled': True,
#                 'name': 'threat_display',
#                 'value': '@{threat}',
#             },
#         ),
#     ])

def calc_encumbrance():
    return flex_row([
        div({'class': 'calc-header'}, 'Encumbrance'),
        equation(
            [
                underlabel('Armor', number_input({'name': 'body_armor_encumbrance'})),
                minus(),
                underlabel('(Str)', number_input({
                    'disabled': True,
                    'name': 'encumbrance_strength',
                    'value': '(@{strength_starting})',
                })),
                minus(),
                equation_misc('encumbrance', 0),
                minus(),
                equation_misc('encumbrance', 1)
            ],
            result_attributes={
                'disabled': True,
                'name': 'encumbrance_display',
                'value': '@{encumbrance}',
            },
        ),
    ])

def calc_defenses():
    return ''.join([
        calc_armor(),
        calc_fort(),
        calc_ref(),
        calc_mental(),
    ])

def calc_skill_points():
    return flex_row([
        div({'class': 'calc-header'}, 'Skill Points'),
        equation(
            [
                underlabel('Base', number_input({
                    'disabled': True, 'name': 'skill_points_base', 'value': 8,
                })),
                plus(),
                underlabel('2 * (Int)', number_input({
                    'disabled': True,
                    'name': 'skill_points_intelligence',
                    'value': '(@{intelligence_starting} * 2)',
                })),
                plus(),
                equation_misc_repeat('skill_points', 2)
            ],
            result_attributes={
                'disabled': 'true',
                'name': 'skill_points_display',
                'value': '(@{skill_points})',
            },
        ),
    ])

def calc_maneuvers():
    return flex_row([
        div({'class': 'calc-header'}, 'Maneuvers'),
        equation(
            [
                underlabel('Base', number_input({
                    'disabled': False,
                    'name': 'maneuvers_class',
                })),
                plus(),
                underlabel('Insight', number_input({
                    'disabled': False,
                    'name': 'maneuvers_insight',
                })),
                plus(),
                equation_misc_repeat('maneuvers', 2)
            ],
            result_attributes={
                'disabled': True,
                'name': 'maneuvers',
                'value': '@{maneuvers}',
            },
        )
    ])

def calc_spells():
    return flex_row([
        div({'class': 'calc-header'}, 'Spells'),
        equation(
            [
                underlabel('Base', number_input({
                    'disabled': False,
                    'name': 'spells_class',
                })),
                plus(),
                underlabel('Insight', number_input({
                    'disabled': False,
                    'name': 'spells_insight',
                })),
                plus(),
                equation_misc_repeat('spells', 2)
            ],
            result_attributes={
                'disabled': True,
                'name': 'spells',
                'value': '@{spells}',
            },
        )
    ])

def calc_blank_ability(i):
    return flex_row([
        div({'class': 'calc-header'}, text_input({'name': f'active_ability_name_{i}'})),
        equation(
            [
                underlabel('Base', number_input({
                    'disabled': False,
                    'name': f'active_ability_base_{i}',
                })),
                plus(),
                underlabel('Insight', number_input({
                    'disabled': False,
                    'name': f'active_ability_insight_{i}',
                })),
                plus(),
                equation_misc_repeat(f'active_ability_{i}', 2)
            ],
            result_attributes={
                'disabled': True,
                'name': 'active_ability_known_display',
                'value': f'@{{active_ability_known_{i}}}',
            },
        )
    ])

def calc_insight_points():
    return flex_row([
        div({'class': 'calc-header'}, 'Insight Points'),
        equation(
            [
                underlabel('Base', number_input({
                    'disabled': True,
                    'name': 'insight_points_base',
                    'value': 2,
                })),
                plus(),
                underlabel('(Int)', number_input({
                    'disabled': True,
                    'name': 'insight_points_intelligence',
                    'value': '(@{intelligence_starting})',
                })),
                plus(),
                equation_misc_repeat('insight_points', 2)
            ],
            result_attributes={
                'disabled': 'true',
                'name': 'insight_points',
                'value': ROLL20_CALC['insight_points'],
            },
        ),
    ])

def base_10():
    return number_input({
        'disabled': 'true',
        'value': '10'
    })

def calc_armor():
    return flex_row([
        div({'class': 'calc-header'}, 'Armor'),
        equation(
            [
                underlabel('Lvl', number_input({
                    'disabled': True,
                    'name': 'armor_defense_scaling_display',
                    'value': '@{level}',
                })),
                plus(),
                underlabel('(Dex)', number_input({
                    'disabled': True,
                    'name': 'body_armor_dexterity_display',
                    'value': '@{dexterity_starting}',
                })),
                plus(),
                underlabel('Body', number_input({'name': 'body_armor_defense_value'})),
                plus(),
                underlabel('Shield', number_input({'name': 'shield_defense_value'})),
                plus(),
                number_input({
                    'class': 'equation-misc',
                    'name': 'armor_defense',
                })
            ],
            result_attributes={
                'disabled': 'true',
                'name': 'armor_defense_display',
                'value': '@{armor_defense}',
            },
        ),
    ])

def calc_fort():
    return flex_row([
        div({'class': 'calc-header'}, 'Fortitude'),
        equation(
            [
                underlabel('Lvl', number_input({
                    'disabled': True,
                    'name': 'fortitude_scaling_display',
                    'value': '@{level}',
                })),
                plus(),
                underlabel('(Con)', number_input({
                    'disabled': True,
                    'name': 'fortitude_starting_attribute',
                    'value': '(@{constitution_starting})',
                })),
                plus(),
                underlabel('Class', number_input({'name': 'fortitude_class', 'value': '4'})),
                plus(),
                equation_misc_repeat('fortitude', 2)
            ],
            result_attributes={
                'disabled': 'true',
                'name': 'fortitude_defense_display',
                'value': '@{fortitude}',
            },
        ),
    ])

def calc_ref():
    return flex_row([
        div({'class': 'calc-header'}, 'Reflex'),
        equation(
            [
                underlabel('Lvl', number_input({
                    'disabled': True,
                    'name': 'reflex_scaling_display',
                    'value': '@{level}',
                })),
                plus(),
                underlabel('(Dex)', number_input({
                    'disabled': True,
                    'name': 'reflex_starting_attribute',
                    'value': '(@{dexterity_starting})',
                })),
                plus(),
                underlabel('Class', number_input({'name': 'reflex_class', 'value': '4'})),
                plus(),
                equation_misc_repeat('reflex', 2)
            ],
            result_attributes={
                'disabled': 'true',
                'name': 'reflex_display',
                'value': '@{reflex}',
            },
        ),
    ])

def calc_mental():
    return flex_row([
        div({'class': 'calc-header'}, 'Mental'),
        equation(
            [
                underlabel('Lvl', number_input({
                    'disabled': True,
                    'name': 'mental_scaling_display',
                    'value': '@{level}',
                })),
                plus(),
                underlabel('(Wil)', number_input({
                    'disabled': True,
                    'name': 'mental_starting_attribute',
                    'value': '(@{willpower_starting})',
                })),
                plus(),
                underlabel('Class', number_input({'name': 'mental_class', 'value': '4'})),
                plus(),
                equation_misc_repeat('mental', 2)
            ],
            result_attributes={
                'disabled': 'true',
                'name': 'mental_display',
                'value': '@{mental}',
            },
        ),
    ])

def adventuring():
    return flex_col({'class': 'adventuring'}, [
        standard_damage(),
    ])

def standard_damage():
    return flex_col({'class': 'standard-damage'}, [
        div({'class': 'section-header'}, 'Standard Damage'),
        flex_row({'class': 'damage-chart'}, [
            flex_col([
                div({'class': 'header'}, 'Power'),
                "".join([div(f"{i}-{i+1}") for i in range(0, 25, 2)])
            ]),
            flex_col([
                div({'class': 'header'}, 'Damage'),
                "".join([
                    div(standard_damage_at_power(i))
                    for i in range(0, 25, 2)
                ]),
            ])
        ])
    ])

def standard_damage_at_power(power):
    return {
        0: '1d8',
        2: '1d10',
        4: '2d6',
        6: '2d8',
        8: '2d10',
        10: '4d6',
        12: '4d8',
        14: '4d10',
        16: '5d10',
        18: '6d10',
        20: '7d10',
        22: '8d10',
        24: '9d10',
    }[power]
