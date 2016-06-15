from cgi_simple import *

from sheet_data import ATTRIBUTES, DEFENSES, ATTRIBUTE_SKILLS, ROLL20_CALC, roll20_max_text

def create_page():
    return flex_col({'class': 'second-page'}, [
        flex_row({'class': 'core-calculations'}, [
            flex_col({'class': 'attributes'}, [
                rise_title(),
                calc_attributes(),
            ]),
            flex_col({'class': 'statistics'}, [
                flex_wrapper(div({'class': 'section-header'}, 'Accuracy')),
                calc_combat_prowess(),
                calc_attacks(),
                flex_wrapper(div({'class': 'section-header'}, 'Core Statistics')),
                calc_hit_points(),
                flex_wrapper(div({'class': 'section-header'}, 'Defenses')),
                calc_defenses(),
            ]),
        ]),
        level_chart(),
    ])

def calc_attributes():
    return flex_col({'class': 'calc-attributes'}, [
        flex_wrapper(div({'class': 'section-header'}, 'Attributes')),
        ''.join([calc_attribute(attribute) for attribute in ATTRIBUTES]),
    ])

def calc_attribute(attribute_name):
    calc_name = attribute_name.lower()
    return ''.join([
        div({'class': 'calc-attribute-header'}, attribute_name),
        #labeled_number_input(
        #    attribute_name,
        #    'calc-attribute-' + attribute_name.lower(),
        #    {'class': 'calc-attribute-header'}
        #),
        #flex_row({'class': 'equation'}, [
        equation(
            [
                underlabeled_number_input(
                    'Base',
                    calc_name+'-base',
                    attributes = {'class': 'eq-base'},
                    input_attributes = {'value': '0'},
                ),
                plus(),
                underlabeled_number_input(
                    'Level',
                    calc_name+'-level',
                    attributes = {'class': 'eq-level'},
                    input_attributes = {'value': '0'},
                ),
                misc_spacer(),
                plus(),
                underlabeled_number_input('Misc', calc_name+'-misc', {'class': 'eq-misc'}, input_attributes = {'value': '0'}),
            ],
            result_attributes = {
                'disabled': 'true',
                'name': calc_name.lower(),
                'value': ROLL20_CALC['attribute'](calc_name),
            },
        )
    ])

def level_numbers(name_prefix):
    return flex_col({'class': 'level-numbers'}, [
        flex_wrapper(div({'class': 'level-number-header', 'class': 'chart-header'}, 'Lvl')),
        ''.join([
            text_input({'name': 'ability-level-' + name_prefix + '-' + str(level)})
            #flex_row({'class': 'level-number-wrapper level'+str(level)}, div({'class': 'level-number'}, str(level)))
            for level in range(1,14)
        ]),
    ])

def level_chart():
    return flex_col({'class': 'level-chart'}, [
        flex_row({'class': 'level-chart-headers'}, [
            flex_wrapper({'class': 'level-wrapper'}, [
                div({'class': 'chart-header'}, 'Lvl'),
            ]),
            flex_wrapper({'class': 'name-wrapper'}, [
                div({'class': 'chart-header'}, 'Feats and Abilities'),
            ]),
            flex_wrapper({'class': 'level-wrapper'}, [
                div({'class': 'chart-header'}, 'Lvl'),
            ]),
            flex_wrapper({'class': 'name-wrapper'}, [
                div({'class': 'chart-header'}, 'Feats and Abilities'),
            ]),
        ]),
        "".join([level_row(level) for level in range(1,14)]),
    ])

def level_row(level):
    return flex_row({'class': 'level-chart-row'}, [
        flex_wrapper({'class': 'ability-level-row'}, [
            text_input({'name': 'ability-level-l-' + str(level)})
        ]),
        flex_wrapper({'class': 'ability-name-row'}, [
            text_input({'name': 'ability-name-l-' + str(level)})
        ]),
        flex_wrapper({'class': 'ability-level-row'}, [
            text_input({'name': 'ability-level-r-' + str(level)})
        ]),
        flex_wrapper({'class': 'ability-name-row'}, [
            text_input({'name': 'ability-name-r-' + str(level)})
        ]),
    ])

def level_chart_column(title, html_name, contents):
    return flex_col({'class': html_name}, [
        flex_wrapper(div({'class': html_name+'-header', 'class': 'chart-header'}, title)),
        contents
    ])

def attribute_bonuses():
    return flex_col({'class': 'attribute-bonuses'}, [
        flex_wrapper(div({'class': 'attribute-bonus-header', 'class': 'chart-header'}, 'Attributes')),
        ''.join([text_input({'class': 'level'+str(level)}) for level in range(1,21)]),
    ])

def abilities(name_prefix):
    return flex_col({'class': 'abilities'}, [
        flex_wrapper(div({'class': 'ability-header', 'class': 'chart-header'}, 'Feats and Abilities')),
        ''.join([text_input({'class': 'level'+str(level), 'name': 'ability-name-'+name_prefix+'-'+str(level)}) for level in range(1, 14)]),
    ])

def calc_combat_prowess():
    return flex_row([
        div({'class': 'calc-header'}, 'Prowess'),
        equation(
            [
                underlabeled_number_input('Good', 'bab-good'),
                plus(),
                underlabeled_number_input('Avg', 'bab-avg'),
                plus(),
                underlabeled_number_input('Poor', 'bab-poor'),
            ],
            result_attributes = {
                'disabled': 'true',
                'name': 'base-attack-bonus',
                'value': ROLL20_CALC['base_attack_bonus'],
            },
        ),
    ])

def calc_hit_points():
    return flex_row([
        div({'class': 'calc-header'}, 'Hit Points'),
        equation(
            [
                this_or_that([
                    underlabeled_number_input(
                        half('Fort'),
                        input_attributes = {
                            'disabled': 'true',
                            'name': 'hp-fort',
                            'value': 'floor(('+ROLL20_CALC['fortitude']+')/2)',
                        },
                    ),
                    underlabeled_number_input(
                        half('Ment'),
                        input_attributes = {
                            'disabled': 'true',
                            'name': 'hp-ment',
                            'value': 'floor(('+ROLL20_CALC['mental']+')/2)',
                        },
                    ),
                ]),
                times(),
                underlabeled_number_input('Level', 'hp-level', {'class': 'eq-level'}),
                misc_spacer(),
                plus(),
                underlabeled_number_input('Misc', 'hp-misc', {'class': 'eq-misc'}),
            ],
            result_attributes = {
                'disabled': 'true',
                'name': 'hit-points',
                'value': ROLL20_CALC['hit_points'],
            },
        ),
    ])

def calc_attacks():
    return ''.join([
        calc_melee(),
        calc_ranged(),
    ])

def calc_defenses():
    return ''.join([
        calc_armor(),
        calc_maneuver(),
        calc_fort(),
        calc_ref(),
        calc_mental(),
    ])

def calc_melee():
    return flex_row([
        div({'class': 'calc-header'}, 'Melee'),
        equation(
            [
                this_or_that([
                    underlabeled_number_input(
                        'Prow',
                        input_attributes = {
                            'disabled': 'true',
                            'name': 'melee-calc-bab',
                            'value': ROLL20_CALC['base_attack_bonus'],
                        },
                    ),
                    underlabeled_number_input(
                        'Str',
                        input_attributes = {
                            'disabled': 'true',
                            'name': 'melee-calc-strength',
                            'value': ROLL20_CALC['attribute']('strength')
                        },
                    ),
                    underlabeled_number_input(
                        'Dex',
                        input_attributes = {
                            'disabled': 'true',
                            'name': 'melee-calc-dexterity',
                            'value': ROLL20_CALC['attribute']('dexterity')
                        },
                    ),
                ]),
                plus(),
                underlabeled_number_input(
                    'Prof',
                    input_attributes = {
                        'disabled': 'true',
                        'name': 'proficiency',
                        'value': '4',
                    },
                ),
                misc_spacer(),
                plus(),
                underlabeled_number_input('Misc', 'melee-misc', {'class': 'eq-misc'}),
            ],
            result_attributes = {
                'disabled': 'true',
                'name': 'melee',
                'value': '+'.join([
                    roll20_max_text(
                        ROLL20_CALC['base_attack_bonus'],
                        roll20_max_text(
                            ROLL20_CALC['attribute']('strength'),
                            ROLL20_CALC['attribute']('dexterity'),
                        ),
                    ),
                    '@{proficiency}',
                ]),
            },
        ),
    ])

def calc_ranged():
    return flex_row([
        div({'class': 'calc-header'}, 'Ranged'),
        equation(
            [
                this_or_that([
                    underlabeled_number_input(
                        'Prow',
                        input_attributes = {
                            'disabled': 'true',
                            'name': 'melee-calc-bab',
                            'value': ROLL20_CALC['base_attack_bonus']
                        },
                    ),
                    underlabeled_number_input(
                        'Per',
                        input_attributes = {
                            'disabled': 'true',
                            'name': 'melee-calc-perception',
                            'value': ROLL20_CALC['attribute']('perception')
                        },
                    ),
                ]),
                plus(),
                underlabeled_number_input(
                    'Prof',
                    input_attributes = {
                        'disabled': 'true',
                        'name': 'proficiency',
                        'value': '4',
                    },
                ),
                misc_spacer(),
                plus(),
                underlabeled_number_input('Misc', 'ranged-misc', {'class': 'eq-misc'}),
            ],
            result_attributes = {
                'disabled': 'true',
                'name': 'ranged',
                'value': '+'.join([
                    roll20_max_text(
                        ROLL20_CALC['base_attack_bonus'],
                        ROLL20_CALC['attribute']('perception'),
                    ),
                    '@{proficiency}',
                ]),
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
                base_10(),
                plus(),
                this_or_that([
                    underlabeled_number_input(
                        'Prow',
                        input_attributes = {
                            'disabled': 'true',
                            'name': 'armor-calc-bab',
                            'value': ROLL20_CALC['base_attack_bonus']
                        },
                    ),
                    underlabeled_number_input(
                        'Dex',
                        input_attributes = {
                            'disabled': 'true',
                            'name': 'armor-calc-dexterity',
                            'value': ROLL20_CALC['attribute']('dexterity')
                        },
                    ),
                    underlabeled_number_input(
                        'Con',
                        input_attributes = {
                            'disabled': 'true',
                            'name': 'armor-calc-constitution',
                            'value': ROLL20_CALC['attribute']('constitution')
                        },
                    ),
                ]),
                plus(),
                underlabeled_number_input('Armor', 'armor-body'),
                plus(),
                underlabeled_number_input('Shield', 'shield'),
                plus(),
                underlabeled_number_input('Misc', 'armor-misc', {'class': 'eq-misc'}),
            ],
            result_attributes = {
                'disabled': 'true',
                'name': 'armor',
                'value': ROLL20_CALC['armor'],
            },
        ),
    ])

def misc_spacer():
    return div({'class': 'misc-spacer'}, '')

def calc_maneuver():
    return flex_row([
        div({'class': 'calc-header'}, 'Maneuver'),
        equation(
            [
                base_10(),
                plus(),
                this_or_that([
                    underlabeled_number_input(
                        'Prow',
                        input_attributes = {
                            'disabled': 'true',
                            'name': 'maneuver-calc-bab',
                            'value': ROLL20_CALC['base_attack_bonus']
                        },
                    ),
                    underlabeled_number_input(
                        'Str',
                        input_attributes = {
                            'disabled': 'true',
                            'name': 'maneuver-calc-strength',
                            'value': ROLL20_CALC['attribute']('strength')
                        },
                    ),
                    underlabeled_number_input(
                        'Dex',
                        input_attributes = {
                            'disabled': 'true',
                            'name': 'maneuver-calc-dexterity',
                            'value': ROLL20_CALC['attribute']('dexterity')
                        },
                    ),
                ]),
                plus(),
                underlabeled_number_input('Shield', 'shield'),
                misc_spacer(),
                plus(),
                #misc_spacer(),
                underlabeled_number_input('Misc', 'maneuver-misc', {'class': 'eq-misc'}),
            ],
            result_attributes = {
                'disabled': 'true',
                'name': 'maneuver',
                'value': ROLL20_CALC['maneuver'],
            },
        ),
    ])

def calc_fort():
    return flex_row([
        div({'class': 'calc-header'}, 'Fort'),
        equation(
            [
                base_10(),
                plus(),
                this_or_that([
                    underlabeled_number_input('Base', 'fort-base'),
                    underlabeled_number_input(
                        label_name = 'Str',
                        input_attributes = {
                            'disabled': 'true',
                            'name': 'fort-calc-strength',
                            'value': ROLL20_CALC['attribute']('strength'),
                        },
                    ),
                    underlabeled_number_input(
                        label_name = 'Con',
                        input_attributes = {
                            'disabled': 'true',
                            'name': 'fort-calc-constitution',
                            'value': ROLL20_CALC['attribute']('constitution'),
                        },
                    ),
                ]),
                plus(),
                underlabeled_number_input('Class'),
                misc_spacer(),
                plus(),
                underlabeled_number_input('Misc', 'fort-misc', {'class': 'eq-misc'}),
            ],
            result_attributes = {
                'disabled': 'true',
                'name': 'fortitude',
                'value': ROLL20_CALC['fortitude'],
            },
        ),
    ])

def calc_ref():
    return flex_row([
        div({'class': 'calc-header'}, 'Ref'),
        equation(
            [
                base_10(),
                plus(),
                this_or_that([
                    underlabeled_number_input('Base', 'ref-base'),
                    flex_row([
                        underlabeled_number_input(
                            'Dex',
                            input_attributes = {
                                'disabled': 'true',
                                'name': 'ref-calc-dexterity',
                                'value': ROLL20_CALC['attribute']('dexterity'),
                            },
                        ),
                        plus(),
                        underlabeled_number_input(
                            'Per',
                            input_attributes = {
                                'disabled': 'true',
                                'name': 'ref-calc-perception',
                                'value': ROLL20_CALC['attribute']('perception'),
                            },
                        ),
                    ]),
                ]),
                plus(),
                underlabeled_number_input('Class'),
                plus(),
                underlabeled_number_input('Shield', 'shield'),
                misc_spacer(),
                plus(),
                underlabeled_number_input('Misc', 'ref-misc', {'class': 'eq-misc'}),
            ],
            result_attributes = {
                'disabled': 'true',
                'name': 'reflex',
                'value': ROLL20_CALC['reflex'],
            },
        ),
    ])

def calc_mental():
    return flex_row([
        div({'class': 'calc-header'}, 'Ment'),
        equation(
            [
                base_10(),
                plus(),
                this_or_that([
                    underlabeled_number_input('Base', 'ment-base'),
                    flex_row([
                        underlabeled_number_input(
                            'Wil',
                            input_attributes = {
                                'disabled': 'true',
                                'name': 'ment-calc-willpower',
                                'value': ROLL20_CALC['attribute']('willpower')
                            },
                        ),
                        plus(),
                        underlabeled_number_input(
                            'Int',
                            input_attributes = {
                                'disabled': 'true',
                                'name': 'ment-calc-intelligence',
                                'value': ROLL20_CALC['attribute']('intelligence'),
                            },
                        ),
                    ]),
                ]),
                plus(),
                underlabeled_number_input('Class'),
                misc_spacer(),
                plus(),
                underlabeled_number_input('Misc', 'ment-misc', {'class': 'eq-misc'}),
            ],
            result_attributes = {
                'disabled': 'true',
                'name': 'mental',
                'value': ROLL20_CALC['mental'],
            },
        ),
    ])
