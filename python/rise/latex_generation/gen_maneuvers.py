#!/usr/bin/env python3

import click
from rise.latex_generation.book_path import book_path
from rise.latex.maneuver import Maneuver
from rise.latex.util import latexify
from rise.statistics.rise_data import maneuver_sources

def generate_maneuvers():
    maneuvers = []

    maneuvers.append(Maneuver(
        name='Battle Cry',
        short_description='Inspire allies',
        target="All \\glossterm<allies> that can hear you",
        effect_text="""
            Each target gains a +1 bonus to \\glossterm<accuracy> until the end of the next round.
            This does not affect attacks during the current phase.
        """,
        rank_upgrades={
            '3': 'Each target also gains a +1 bonus to Mental defense.',
            '5': 'The accuracy bonus increases to +2.',
            '7': 'The Mental defense bonus increases to +2.',
        },
        tags=[],
        lists=['Primal'],
    ))

    maneuvers.append(Maneuver(
        name='Brace for Impact',
        short_description='Take half physical damage',
        target="Yourself",
        effect_text="""
            You take half damage from \\glossterm<physical> damage this round.
            This halving is applied before \\glossterm<resistances> and similar abilities.
        """,
        rank_upgrades={
            # Alternate idea: bonuses against attackers or ignore conditions
            '3': 'You also gain a +1 bonus to all defenses.',
            '5': 'You also take half damage from \\glossterm<energy> damage this round.',
            '7': 'The defense bonus increases to +2.',
        },
        tags=['Swift'],
        lists=['Martial', 'Primal', 'Wild', 'Esoteric'],
    ))

    maneuvers.append(Maneuver(
        name='Certain Strike',
        short_description='Make a strike that trades damage for accuracy',
        target="As chosen \\glossterm<strike>",
        effect_text="""
            Make a \\glossterm<strike> with a +2 bonus to accuracy and a -2d penalty to damage.
        """,
        rank_upgrades={
            '3': 'The accuracy bonus increases to +3.',
            '5': 'The accuracy bonus increases to +4.',
            '7': 'The accuracy bonus increases to +5.',
        },
        tags=[],
        lists=['Martial', 'Primal', 'Trick', 'Wild', 'Esoteric'],
    ))

    maneuvers.append(Maneuver(
        name='Unerring Strike',
        short_description='Make a strike that mitigates miss chances',
        target="As chosen \\glossterm<strike>",
        effect_text="""
            Make a \\glossterm<strike>.
            You can reroll any \\glossterm<miss chances>, such as when attacking \\glossterm<invisible> creatures, and take the better result.
        """,
        rank=3,
        rank_upgrades={
            '5': 'You ignore any 20\% miss chance effects with the strike.',
            '7': 'You ignore all miss chance effects with the strike.',
        },
        tags=[],
        lists=['Martial', 'Esoteric'],
    ))

    maneuvers.append(Maneuver(
        name='Counterattack',
        short_description='Make a strike with bonuses if attacked',
        target="As chosen \\glossterm<strike>",
        effect_text="""
            Make a \\glossterm<strike>.
            If the target attacked you earlier in the current round, you gain a +1 bonus to \\glossterm<accuracy> and a +1d bonus to damage with the strike.
        """,
        rank_upgrades={
            '3': 'The damage bonus increases to +2d.',
            '5': 'The accuracy bonus increases to +2.',
            '7': 'The damage bonus increases to +3d.',
        },
        tags=[],
        lists=['Primal', 'Martial', 'Trick'],
    ))

    maneuvers.append(Maneuver(
        name='Fearsome Blow',
        short_description='Make a strike that inflicts fear',
        target="As chosen \\glossterm<strike>",
        effect_text="""
            Make a \\glossterm<strike> with a -2d penalty to damage.
            If the attack result hits the target's Mental defense,
                it is \\glossterm<shaken> by you as a \\glossterm<condition>.
        """,
        rank=3,
        rank_upgrades={
            '5': 'On a \\glossterm<critical hit>, the target is \\glossterm<panicked> instead of shaken.',
            '7': 'On a hit, the target is \\glossterm<frightened> instead of shaken.',
        },
        tags=['Emotion'],
        lists=['Primal', 'Martial', 'Trick', 'Esoteric'],
    ))

    maneuvers.append(Maneuver(
        name='Demoralizing Shout',
        short_description='Inflict fear on nearby enemies',
        target="\\glossterm<Enemies> in a \\areasmall radius from you.",
        effect_text="""
            Make an attack vs. Mental against each target.
            \\hit Each target is \\glossterm<shaken> by you as a \\glossterm<condition>.
        """,
        rank_upgrades={
            '3': 'The area increases to a \\areamed radius.',
            '5': 'The area increases to a \\arealarge radius.',
            '7': 'The area increases to a \\areahuge radius.',
        },
        tags=['Emotion'],
        lists=['Primal'],
    ))

    maneuvers.append(Maneuver(
        name='Ground Stomp',
        short_description='Knock foes prone and make a strike',
        target='All Large or smaller creatures in a \\areasmall radius from you that are standing on earth or unworked stone',
        effect_text="""
            Make an attack vs. Reflex against each target.
            If you use this ability during the \\glossterm<action phase>, you can also make a \\glossterm<strike> during the \\glossterm<delayed action phase>.
            \\hit Each target is knocked \\prone.
        """,
        rank=3,
        rank_upgrades={
            '5': 'The maximum size increases to Huge.',
            '7': 'The maximum size increases to Gargantuan.',
        },
        tags=[],
        lists=['Primal'],
    ))

    maneuvers.append(Maneuver(
        name='Leaping Strike',
        short_description='Jump and make a strike',
        target="One creature or object you \\glossterm<threaten> during movement (see text)",
        effect_text="""
            You make a Jump check to leap and move as normal for the leap, up to a maximum distance equal to your \\glossterm<base speed> (see \\pcref<Leap>).
            You can make a melee \\glossterm<strike> with a -1 penalty to \\glossterm<accuracy> from any location you occupy during the leap.
        """,
        rank_upgrades={
            '3': "You gain a +1d bonus to damage with the strike if you attack while above the target's space.",
            '5': 'The damage bonus increases to +2d.',
            '7': 'The damage bonus increases to +3d.',
        },
        tags=[],
        lists=['Primal', 'Wild', 'Esoteric'],
    ))

    maneuvers.append(Maneuver(
        name='Liver Shot',
        short_description='Make a strike that sickens',
        target="As chosen \\glossterm<strike>",
        effect_text="""
            Make a \\glossterm<strike> with a -2d penalty to damage.
            If the attack result hits the target's Fortitude defense,
                it is \\glossterm<sickened> as a \\glossterm<condition>.
        """,
        rank=3,
        rank_upgrades={
            '5': 'On a \\glossterm<critical hit>, the target is is \\glossterm<paralyzed> instead of sickened.',
            '7': 'On a hit, the target is \\glossterm<nauseated> instead of sickened.',
        },
        tags=[],
        lists=['Primal', 'Martial', 'Wild', 'Trick', 'Esoteric'],
    ))

    maneuvers.append(Maneuver(
        name='Power Attack',
        short_description='Make a strike that trades accuracy for damage',
        target="As chosen \\glossterm<strike>",
        effect_text="""
            Make a \\glossterm<strike> with a -2 penalty to \\glossterm<accuracy> and a +2d bonus to damage.
        """,
        rank_upgrades={
            '3': 'The damage bonus increases to +3d.',
            '5': 'The damage bonus increases to +4d.',
            '7': 'The damage bonus increases to +5d.',
        },
        tags=[],
        lists=['Primal', 'Martial', 'Wild'],
    ))

    maneuvers.append(Maneuver(
        name='Pulverizing Smash',
        short_description='Make a strike against Fortitude defense',
        target="As chosen \\glossterm<strike>",
        effect_text="""
            Make a \\glossterm<strike>.
            The attack is made against the target's Fortitude defense instead of its Armor defense.
        """,
        rank_upgrades={
            '3': 'You gain a +1d bonus to damage with the strike.',
            '5': 'The damage bonus increases to +2d.',
            '7': 'The damage bonus increases to +3d.',
        },
        tags=[],
        lists=['Primal', 'Martial', 'Wild'],
    ))

    maneuvers.append(Maneuver(
        name='Rapid Assault',
        short_description='Make two strikes',
        target="One or two creatures or objects you \\glossterm<threaten>",
        effect_text="""
            Make two melee \\glossterm<strikes> divided as you choose among the targets.
            You take a -2 penalty to accuracy and a -2d penalty to damage on both strikes.
        """,
        rank_upgrades={
            '3': 'The accuracy penalty is reduced to -1.',
            '5': 'The damage penalty is reduced to -1d.',
            '7': 'The accuracy and damage penalties are removed.',
        },
        tags=[],
        lists=['Primal', 'Martial', 'Wild', 'Trick', 'Esoteric'],
    ))

    maneuvers.append(Maneuver(
        name='Reaping Charge',
        short_description='Make strikes while moving in a line',
        target="See text",
        effect_text="""
            Move up to half your movement speed in a straight line.
            You can make a melee \\glossterm<strike> with a slashing or bludgeoning weapon.
            The strike targets any number of creatures and objects that you \\glossterm<threaten> at any point during your movement, except for the space you start in and the space you end in.
            You take a -2 penalty to \\glossterm<accuracy> with the strike.
        """,
        rank_upgrades={
            '3': 'The accuracy penalty is reduced to -1.',
            '5': 'You can move up to your full movement speed instead of at half speed.',
            '7': 'The accuracy penalty is removed.',
        },
        tags=[],
        lists=['Primal', 'Martial', 'Wild', 'Esoteric'],
    ))

    maneuvers.append(Maneuver(
        name='Strip the Flesh',
        short_description='Make a weak strike that is extremely painful',
        target="As chosen \\glossterm<strike>",
        effect_text="""
            Make a \\glossterm<strike> using a slashing weapon with a -2d penalty to damage.
            If the strike deals damage, the target loses an additional \\glossterm<hit point>.
        """,
        rank_upgrades={
            '3': 'You gain a +1 bonus to \\glossterm<accuracy> with the strike.',
            '5': 'The accuracy bonus increases to +2.',
            '7': 'The accuracy bonus increases to +3.',
        },
        tags=[],
        lists=['Primal', 'Martial', 'Wild', 'Trick'],
    ))

    maneuvers.append(Maneuver(
        name='Sweeping Strike',
        short_description='Make strikes against nearby foes',
        target="Up to two creatures or objects you \\glossterm<threaten>",
        effect_text="""
            Make a melee \\glossterm<strike> with a slashing or bludgeoning weapon against each target.
        """,
        rank_upgrades={
            '3': 'You can target up to four creature you \\glossterm<threaten>.',
            '5': 'You gain a +1d bonus to damage with the strike.',
            '7': 'The damage bonus increases to +2d.',
        },
        tags=[],
        lists=['Primal', 'Martial', 'Wild', 'Esoteric'],
    ))

    maneuvers.append(Maneuver(
        name='Thunderous Shout',
        short_description='Deal damage in a cone',
        target="Everything in a \\areasmall cone-shaped burst from you",
        effect_text="""
            Make an attack vs. Fortitude against each target.
            \\hit Each target takes energy \\glossterm<standard damage>.
        """,
        rank_upgrades={
            '3': 'The area increases to a \\areamed radius.',
            '5': 'The area increases to a \\arealarge radius.',
            '7': 'The area increases to a \\areahuge radius.',
        },
        tags=[],
        lists=['Primal'],
    ))

    maneuvers.append(Maneuver(
        name='Whirlwind',
        short_description='Make strikes against all threatened foes',
        target="All creatures you \\glossterm<threaten>",
        effect_text="""
            Make a melee \\glossterm<strike> with a slashing weapon against each target.
            You take a -1 penalty to \\glossterm<accuracy> with the strike.
        """,
        rank_upgrades={
            '3': """
                You can move up to 5 feet when you use this ability.
                The strike targets all creatures you threaten at any point in your movement.
            """,
            '5': 'The distance you can move increases to be equal to half your movement speed.',
            '7': 'The distance you can move increases to be equal to your movement speed.',
        },
        tags=[],
        lists=['Primal', 'Martial', 'Wild', 'Esoteric'],
    ))

    maneuvers.append(Maneuver(
        name='Challenging Strike',
        short_description='Make a strike and draw attention',
        effect_text="""
            Make a melee \\glossterm<strike> with a -2d penalty to damage.
            If the strike beats the target's Mental defense, it takes a -2 penalty to \\glossterm<accuracy> against creatures other than you as a \\glossterm<condition>.
            This condition is removed if another creature applies this condition to the same target.
        """,
        rank_upgrades={
            '3': 'The penalty increases to -3.',
            '5': 'The penalty increases to -4.',
            '7': 'The penalty increases to -5.',
        },
        tags=[],
        lists=['Martial'],
    ))

    maneuvers.append(Maneuver(
        name='Penetrating Strike',
        short_description='Make a strike against Reflex defense',
        effect_text="""
            Make a \\glossterm<strike> with a piercing weapon.
            The attack is made against the target's Reflex defense instead of its Armor defense.
        """,
        rank_upgrades={
            '3': 'You gain a +1 bonus to \\glossterm<accuracy> with the strike.',
            '5': 'The accuracy bonus increases to +2.',
            '7': 'The accuracy bonus increases to +3.',
        },
        tags=[],
        lists=['Martial', 'Wild', 'Trick', 'Esoteric'],
    ))

    maneuvers.append(Maneuver(
        name='Rally the Troops',
        short_description='Suppress conditions on allies',
        effect_text="""
            You and your \\glossterm<allies> within a \\areamed radius from you are immune to \\glossterm<conditions> this round.
            In addition, each target can ignore any effects from one \\glossterm<condition> it is already affected by this round.
        """,
        rank_upgrades={
            '3': 'The area increases to a \\arealarge radius from you.',
            '5': 'Each target can ignore any number of conditions instead of only one.',
            '7': 'The area increases to a \\areahuge radius from you.',
        },
        tags=['Swift'],
        lists=['Martial'],
    ))

    maneuvers.append(Maneuver(
        name='Hamstring',
        short_description='Make a strike that slows',
        effect_text="""
            Make a \\glossterm<strike> with a -2d penalty to damage.
            If the attack result hits the target's Fortitude defense,
                it is \\glossterm<slowed> as a \\glossterm<condition>.
        """,
        rank=3,
        rank_upgrades={
            '5': 'On a \\glossterm<critical hit>, the target is \\glossterm<decelerated> instead of slowed.',
            '7': 'This condition cannot be removed until the target takes a \\glossterm<short rest>.',
        },
        tags=[],
        lists=['Wild', 'Trick', 'Esoteric'],
    ))

    maneuvers.append(Maneuver(
        name='Hunting Strike',
        short_description='Make a strike and gain an accuracy bonus against the target',
        effect_text="""
            Make a \\glossterm<strike> against a creature.
            After making the strike, you gain a +1 bonus to \\glossterm<accuracy> against the target with all attacks.
            This effect stacks with itself, up to a maximum of a +4 bonus.
            It lasts until you take a \\glossterm<short rest> or use this ability on a different creature.
        """,
        rank_upgrades={
            '3': 'The first time you hit a target with this ability, it provides a +2 bonus instead of a +1 bonus.',
            '5': 'The maximum accuracy bonus increases to +6.',
            '7': 'The first time you hit a target with this ability, it provides a +3 bonus instead of a +2 bonus.',
        },
        tags=[],
        lists=['Wild'],
    ))

    maneuvers.append(Maneuver(
        name='Head Shot',
        short_description='Make a strike that dazes',
        effect_text="""
            Make a \\glossterm<strike> with a -2d penalty to damage.
            If the attack result hits the target's Mental defense,
                it is \\glossterm<dazed> as a \\glossterm<condition>.
        """,
        rank=3,
        rank_upgrades={
            '5': 'On a \\glossterm<critical hit>, the target is also \\glossterm<confused> as part of the same condition.',
            '7': 'On a hit, the target is \\glossterm<stunned> instead of dazed.',
        },
        tags=['Emotion'],
        lists=['Trick', 'Esoteric'],
    ))

    maneuvers.append(Maneuver(
        name='Second Wind',
        short_description='Recover hit points',
        effect_text="""
            You regain a \\glossterm<hit point>.
            You can only use this ability once between \\glossterm<short rests>.
        """,
        rank_upgrades={
            '3': 'If you have a \\glossterm<vital wound>, you regain two \\glossterm<hit points> instead of one.',
            '5': 'You can use the ability twice between \\glossterm<short rests>.',
            '7': 'You remove two \\glossterm<hit points> regardless of whether you have a \\glossterm<vital wound>.',
        },
        tags=[],
        lists=['Esoteric', 'Primal', 'Wild'],
    ))

    maneuvers.append(Maneuver(
        name='Distant Shot',
        short_description='Make a long-ranged strike',
        effect_text="""
            Make a ranged \\glossterm<strike>.
            You reduce your penalties for \\glossterm<range increments> with the strike by 2.
        """,
        rank_upgrades={
            '3': 'You gain a +1 bonus to \\glossterm<accuracy> with the strike.',
            '5': 'The accuracy bonus increases to +2.',
            '7': 'The accuracy bonus increases to +3.',
        },
        tags=[],
        lists=['Martial', 'Wild'],
    ))

    maneuvers.append(Maneuver(
        name='Agonizing Strike',
        short_description='Make a strike that sickens with pain',
        effect_text="""
            Make a \\glossterm<strike> with a -2d penalty to damage.
            If the attack result hits the target's Mental defense,
                it is \\glossterm<sickened> as a \\glossterm<condition>.
        """,
        rank=3,
        rank_upgrades={
            '5': 'On a \\glossterm<critical hit>, the target is is \\glossterm<paralyzed> instead of sickened.',
            '7': 'On a hit, the target is \\glossterm<nauseated> instead of sickened.',
        },
        tags=['Emotion'],
        lists=['Martial', 'Primal', 'Wild', 'Trick', 'Esoteric'],
    ))

    maneuvers.append(Maneuver(
        name='Deattunement Strike',
        short_description="Make a strike to break a target's \\glossterm<attunement>",
        effect_text="""
            Make a \\glossterm<strike> with a -2d penalty to damage.
            If the attack result hits the target's Mental defense,
                it stops being \\glossterm<attuned> to one effect of its choice.
            This functions as if the target had used the \\textit<release attunement> ability,
                including allowing the target to regain its \\glossterm<action point> when it takes a \\glossterm<short rest>.
        """,
        rank_upgrades={
            '3': 'You gain a +1 bonus to \\glossterm<accuracy> with the strike.',
            '5': 'The accuracy bonus increases to +2.',
            '7': 'The accuracy bonus increases to +3.',
        },
        tags=[],
        lists=['Esoteric', 'Trick'],
    ))

    maneuvers.append(Maneuver(
        name='Spring Attack',
        short_description='Make a strike and continue moving',
        effect_text="""
            Move up to half your movement speed and make a melee \\glossterm<strike> with a -2d penalty to damage.
            If you use this ability during the \\glossterm<action phase>, you may use the other half of your movement during the \\glossterm<delayed action phase>.',
        """,
        rank_upgrades={
            '3': 'You also gain a +1 bonus to Armor defense and Reflex defense until the end of the round. This is a \\glossterm<Swift> effect.',
            '5': """
                You can move up to your full speed when you use this ability.
                % TODO: wording
                Your movement during the \\glossterm<delayed action phase>, if any, becomes equal to the remaining distance you could have moved during the \\glossterm<action phase>.
            """,
            '7': 'The defense bonuses increase to +2.',
        },
        tags=[],
        lists=['Esoteric', 'Trick', 'Wild'],
    ))

    maneuvers.append(Maneuver(
        name="Wanderer's Strike",
        short_description='Make a strike and move',
        effect_text="""
            You can either move up to half your speed or make a \\glossterm<strike>.
            %TODO: wording
            During the \\glossterm<delayed action phase>, you can take the action you did not take during the \\glossterm<action phase>.
        """,
        rank=3,
        rank_upgrades={
            '5': 'You gain a +1d bonus to damage with the strike.',
            '7': 'The damage bonus increases to +2d.',
        },
        tags=[],
        lists=['Primal', 'Wild', 'Esoteric'],
    ))

    maneuvers.append(Maneuver(
        name='Shield Slam',
        short_description='Make a dazing strike with a shield',
        effect_text="""
            Make a strike using a shield.
            If the attack result hits the target's Fortitude defense,
                it is \\glossterm<dazed> as a \\glossterm<condition>.
        """,
        rank=3,
        rank_upgrades={
            '5': 'On a \\glossterm<critical hit>, the target is also \\glossterm<confused> as part of the same \\glossterm<condition>.',
            '7': 'On a hit, the target is \\glossterm<stunned> instead of dazed.',
        },
        tags=[],
        lists=['Martial'],
    ))

    maneuvers.append(Maneuver(
        name='Quivering Palm',
        short_description='Make a nauseating strike with an unarmed attack',
        effect_text="""
            Make a strike using an \\glossterm<unarmed attack>.
            If the attack result hits the target's Fortitude defense,
                it is \\glossterm<sickened> as a \\glossterm<condition>.
        """,
        rank=3,
        rank_upgrades={
            '5': 'On a \\glossterm<critical hit>, the target is is \\glossterm<paralyzed> instead of sickened.',
            '7': 'On a hit, the target is \\glossterm<nauseated> instead of sickened.',
        },
        tags=[],
        lists=['Esoteric'],
    ))

    maneuvers.append(Maneuver(
        name='Feint',
        short_description='Make a weak attack to take an opponent off guard',
        effect_text="""
            Make a melee \\glossterm<strike> with a -2d penalty to damage.
            If you hit, the target takes a -2 penalty to Armor defense until the end of the next round.
        """,
        rank_upgrades={
            '3': 'The penalty increases to -3.',
            '5': 'The penalty increases to -4.',
            '7': 'The penalty increases to -5.',
        },
        tags=[],
        lists=['Esoteric', 'Martial', 'Trick'],
    ))

    maneuvers.append(Maneuver(
        name='Reckless Strike',
        short_description='Lower defenses to make a powerful strike',
        effect_text="""
            Make a melee \\glossterm<strike> with a +1 bonus to \\glossterm<accuracy> and a +1d bonus to damage.
            Until the end of the next round, you take a -2 penalty to all defenses.
        """,
        rank_upgrades={
            '3': 'The damage bonus increases to +2d.',
            '5': 'The accuracy bonus increases to +2.',
            '7': 'The damage bonus increases to +4d.',
        },
        tags=[],
        lists=['Primal'],
    ))

    maneuvers.append(Maneuver(
        name='Knockdown',
        short_description='Knock a foe prone with brute force',
        effect_text="""
            Make a melee \\glossterm<strike> using a bludgeoning weapon with a -2d penalty to damage.
            If the attack result hits the target's Fortitude defense,
                it falls \\glossterm<prone>.
        """,
        rank_upgrades={
            '3': """
                On a \\glossterm<critical hit>, the target is unable to stand up on its own until the end of the next round.
                If it is somehow brought into a standing position, it will immediately fall and become prone again.
            """,
            '5': 'The damage penalty is reduced to -1d.',
            '7': 'On a hit, the target is unable to stand on its own.',
        },
        tags=[],
        lists=['Esoteric', 'Martial', 'Primal'],
    ))

    maneuvers.append(Maneuver(
        name='Defensive Strike',
        short_description='Make a careful strike without lowering your defenses',
        effect_text="""
            Make a melee \\glossterm<strike> with a -2d penalty to damage.
            In addition, you gain a +2 bonus to Armor defense until the end of the round.
            The defense bonus is a \\glossterm<Swift> effect, so it protects you from attacks in the current phase.
        """,
        rank_upgrades={
            '3': 'The defense bonus increases to +3.',
            '5': 'The defense bonus increases to +4.',
            '7': 'The defense bonus increases to +5.',
        },
        tags=['Swift (see text)'],
        lists=['Esoteric', 'Martial', 'Trick', 'Wild'],
    ))

    maneuvers.append(Maneuver(
        name='Quickdraw',
        short_description='Rapidly draw a new weapon and attack with it',
        effect_text="""
            You draw a weapon into a single free hand and make a \\glossterm<strike> with the weapon.
        """,
        rank_upgrades={
            # TODO: wording
            '3': 'You gain a +1 bonus to \\glossterm<accuracy> with the strike.',
            '5': 'You may sheathe a different weapon held only in the same hand before drawing the new weapon.',
            '7': 'The accuracy bonus increases to +2.',
        },
        tags=[],
        lists=['Esoteric', 'Martial', 'Trick', 'Primal', 'Wild'],
    ))

    maneuvers.append(Maneuver(
        name='Spellbane Strike',
        short_description='Attack vulnerabilities in focusing foes',
        effect_text="""
            Make a melee \\glossterm<strike> with a -1d penalty to damage.
            If the target is using a \\glossterm<Focus> ability during the current phase, the strike deals double damage.
        """,
        rank_upgrades={
            '3': 'You gain a +1 bonus to \\glossterm<accuracy> with the strike.',
            '5': 'The damage penalty is removed.',
            '7': 'The accuracy bonus increases to +2.',
        },
        tags=[],
        lists=['Esoteric', 'Martial', 'Trick', 'Primal', 'Wild'],
    ))

    maneuvers.append(Maneuver(
        name='Focused Strike',
        short_description='You concentrate to strike a critical blow.',
        effect_text="""
            Make a melee \\glossterm<strike> with a \\minus1d penalty to damage.
            The attack roll \\glossterm<explodes> regardless of what you roll.
        """,
        rank_upgrades={
            '3': 'You also gain a \\plus1 bonus to \\glossterm<accuracy> with the strike.',
            '5': 'You reduce your \\glossterm<focus penalties> with this ability by 1.',
            '7': 'The accuracy bonus increases to \\plus2.',
        },
        tags=['Focus'],
        lists=['Esoteric', 'Martial'],
    ))

    return maneuvers

def generate_maneuver_latex():
    maneuvers = sorted(generate_maneuvers(), key=lambda m: m.name)
    maneuver_texts = []
    for maneuver in maneuvers:
        try:
            maneuver_texts.append(maneuver.to_latex())
        except Exception as e:
            raise Exception(f"Error converting maneuver '{maneuver.name}' to LaTeX") from e
    return latexify('\n'.join(maneuver_texts))


def generate_maneuver_list_latex():
    maneuvers_by_source = group_by_source(generate_maneuvers())
    return latexify(
        "\n\n".join([
            latex_for_source(source, maneuvers_by_source[source])
            for source in maneuver_sources
        ])
    )

def group_by_source(maneuvers):
    by_source = {source: [] for source in maneuver_sources}
    for maneuver in maneuvers:
        for source in maneuver_sources:
            if source in maneuver.lists:
                by_source[source].append(maneuver)
    return by_source

def latex_for_source(source, maneuvers):
    maneuver_headers = []
    for maneuver in sorted(maneuvers, key=lambda m: m.name):
        maneuver_headers.append(f"\\maneuverhead<{maneuver.name}> {maneuver.short_description}.")

    maneuver_list = "\n".join(maneuver_headers)
    return f"""
        \\small
        \\subsection<{source} Maneuvers>\\label<{source} Maneuvers>
            \\begin<spelllist>
                {maneuver_list}
            \\end<spelllist>
    """

def write_to_file():
    maneuver_latex = generate_maneuver_latex()
    maneuver_list_latex = generate_maneuver_list_latex()

    with open(book_path('maneuver_descriptions.tex'), 'w') as maneuver_descriptions_file:
        maneuver_descriptions_file.write(maneuver_latex)
    with open(book_path('maneuver_lists.tex'), 'w') as maneuver_lists_file:
        maneuver_lists_file.write(maneuver_list_latex)

@click.command()
@click.option('-o', '--output/--no-output', default=False)
def main(output):
    if output:
        write_to_file()
    else:
        print(generate_maneuver_latex())

if __name__ == "__main__":
    main()
