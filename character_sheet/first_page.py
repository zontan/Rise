from cgi_simple import *

from sheet_data import ATTRIBUTES, DEFENSES, ATTRIBUTE_SKILLS, ROLL20_CALC, roll20_max_text

def create_page():
    return flex_row([
        flex_col({'class': 'sidebar'}, [
            rise_title(),
            attributes_and_skills(),
        ]),
        flex_col({'class': 'main-body'}, [
            boring_stuff(),
            core_statistics(),
            passive_abilities(),
            active_abilities(),
            attacks(),
        ]),
    ])

def boring_stuff():
    return div({'class': 'boring-stuff'}, [
        flex_row([
            labeled_text_input('Character name', 'character-name'),
            labeled_text_input('Player name', 'player-name'),
            labeled_text_input('Concept', 'concept'),
        ]),
        flex_row([
            labeled_text_input('Class and level', 'class-and-level'),
            labeled_text_input('Race and background', 'race-and-background'),
            labeled_text_input('Alignment and deity', 'alignment-and-deity'),
            labeled_text_input('Appearance', 'appearance'),
        ]),
    ])

def attributes_and_skills():
    return flex_col({'class': 'attributes-and-skills'}, [
        flex_wrapper(div({'class': 'section-header'}, 'Attributes<br>and Skills')),
        ''.join([attribute_section(attribute) for attribute in ATTRIBUTES]),
        flex_col({'class': 'other-skills', 'class': 'attribute-section'}, [
            div({'class': 'attribute'}, 'Other Skills'),
            ''.join([skill_box(skill) for skill in 'Bluff Intimidate Perform Persuasion'.split()]),
        ]),
    ])

def attribute_section(attribute):
    return flex_col({'class': attribute.lower(), 'class': 'attribute-section'}, [
        labeled_number_input(
            attribute,
            attributes = {'class': 'attribute'},
            input_attributes = {
                'disabled': 'true',
                'name': attribute.lower()+'-display',
                'value': ROLL20_CALC['attribute'](attribute.lower()),
            },
        ),
        ''.join([skill_box(skill) for skill in ATTRIBUTE_SKILLS[attribute.lower()]])
    ])

def skill_box(name):
    return flex_row({'class': 'skill-box'}, [
        button(
            {
                'class': 'number-label',
                'name': 'roll_skill-'+name,
                'type': 'roll',
                'value': name+': [[1d20+ @{'+name+'}]]'
            },
            name
        ),
        number_input({
            'name': name.lower(),
        }),
    ])

def resources():
    return flex_col({'class': 'resources'}, [
        flex_wrapper(div({'class': 'section-header'}, 'Resources')),
        ''.join([
            #flex_row({'class': 'resource-row'}, [
            unlabeled_number_input(
                text_input_attributes = {'name': 'resource-name-'+str(i)},
                number_input_attributes = {'name': 'resource-number-'+str(i)},
            )
            #] * 3),
        for i in range(5)]),
    ])

def core_statistics():
    return ''.join([
        flex_row({'class': 'core-statistics'}, [
            defenses(),
            movement(),
            # resources(),
            hit_points(),
            #labeled_number_input('Hit Points', 'hit-points')
        ])
    ])

def defenses():
    return flex_col({'class': 'defenses'}, [
        flex_wrapper(div({'class': 'section-header'}, 'Defenses')),
        "".join([
            labeled_number_input(
                defense,
                input_attributes = {
                    'disabled': 'true',
                    'name': defense + '-display',
                    'value': ROLL20_CALC[defense.lower()],
                },
            )
            for defense in DEFENSES
        ]),
    ])

def hit_points():
    return flex_col({'class': 'hit-points'}, [
        flex_wrapper(div({'class': 'section-header'}, 'Hit Points')),
        "".join([
            labeled_number_input(hp_type, input_name = 'hit-points-'+hp_type)
            for hp_type in 'Max Bloodied Temp Nonlethal Critical'.split()
        ]),
    ])

def movement():
    return flex_col({'class': 'movement'}, [
        flex_wrapper(div({'class': 'section-header'}, 'Movement')),
        "".join([
            labeled_number_input(movement_type)
            for movement_type in 'Speed Climb Fly Swim'.split()
        ]),
        unlabeled_number_input(),
    ])

def passive_abilities():
    return flex_col({'class': 'passive-abilities'}, [
        flex_wrapper(div({'class': 'section-header'}, 'Passive Abilities')),
        "".join([
            flex_row({'class': 'passive-ability-row'}, [
                passive_ability(prefix='l', ability_number = i),
                passive_ability(prefix='r', ability_number = i),
            ])
            for i in range(4)
        ]),
    ])

def passive_ability(prefix, ability_number):
    return div(
        text_input({
            'class': 'passive-ability',
            'name': 'passive{0}-{1}-name'.format(ability_number, prefix)
        })
    )

    return flex_row({'class': 'passive-ability'}, [
        labeled_text_input('Name', 'passive{0}-{1}-name'.format(ability_number, prefix), {'class': 'passive-name'}),
        labeled_text_input('Effect', 'passive{0}-{1}-effect'.format(ability_number, prefix), {'class': 'passive-effect'}),
    ])

def conditional_effects():
    return ''

def abilities():
    return ''

def active_abilities():
    return flex_col({'class': 'active-abilities'}, [
        flex_wrapper(div({'class': 'section-header'}, 'Abilities')),
        "".join([active_ability(i) for i in range(5)]),
    ])

def active_ability(ability_number = None):
    return flex_row({'class': 'active-ability'}, [
        labeled_text_input(
            'Ability',
            'active-ability{0}-name'.format(ability_number),
            {'class': 'active-ability-name'}
        ),
        underlabeled_number_input(
            'Bonus',
            'active-ability{0}-bonus'.format(ability_number),
            {'class': 'active-ability-bonus'}
        ),
        labeled_text_input(
            'Effect',
            'active-ability{0}-effect'.format(ability_number),
            {'class': 'active-ability-effect'}
        ),
    ])

def attacks():
    return flex_col({'class': 'attacks'}, [
        flex_wrapper(div({'class': 'section-header'}, 'Attacks')),
        "".join([attack(i) for i in range(5)]),
    ])

def attack(attack_number = None):
    return flex_row({'class': 'attack'}, [
        labeled_text_input(
            'Name',
            'attack{0}-name'.format(attack_number),
            {'class': 'attack-name'}
        ),
        underlabeled_number_input(
            'Bonus',
            'attack{0}-bonus'.format(attack_number),
            {'class': 'attack-bonus'}
        ),
        labeled_text_input(
            'Damage/Effect',
            'attack{0}-effect'.format(attack_number),
            {'class': 'attack-effect'}
        ),
    ])

def rise_title():
    return div(
        {'class': 'rise-title'},
        'Rise'
    )
