from rise.latex.mystic_sphere import MysticSphere
from rise.latex.spell import Spell
from rise.latex.effects import Effects

biomancy=MysticSphere(
    name="Biomancy",
    short_description="Manipulate the biological nature of creatures",
    cantrips=[
    ],
    lists=['Arcane', 'Nature', 'Pact'],
    spells=[
        Spell('Poison -- Asp Venom', 2, 'One living creature within \\rngmed range', """
            Make an attack vs. Fortitude against the target.
            \\hit The target becomes \\glossterm<poisoned> by the first \\glossterm<poison stage> of asp venom.
            At the end of each subsequent round, you repeat this attack, as normal for poisons (see \\pcref<Poison>).
            A creature poisoned by asp venom becomes \\glossterm<sickened> as long as it is poisoned.
            Reaching the third \\glossterm<poison stage> causes the target to become \\glossterm<nauseated> as long as it is poisoned.
            A third failed attack ends the poison.
            \\crit As above, except that target immediately reaches the second \\glossterm<poison stage>, as normal for poisons.
        """, scaling="accuracy", tags=['Manifestation']),
        Spell('Poison -- Dragon Bile', 3, 'One living creature within \\rngmed range', """
            Make an attack vs. Fortitude against the target.
            \\hit The target becomes \\glossterm<poisoned> with dragon bile.
            At the end of each subsequent round, you repeat this attack, as normal for poisons.
            For each \\glossterm<poison stage>, including the initial stage, the target loses 1d10 \\glossterm<hit points>.
            A third failed attack ends the poison.
            % No \\glance effect
            \\crit As above, except that target immediately reaches the second \\glossterm<poison stage>, as normal for poisons.
        """, scaling="""
            The hit point loss from the poison increases by +1d for each rank beyond 3.
        """, tags=['Manifestation']),
        Spell('Neutralize Poison', 1, 'Yourself or one target within \\rngmed range', """
            The target gains an additional success to resist a poison currently affecting it (see \\pcref<Poison>).
        """, scaling="""
            \\rank<3> The number of additional successes increases to two.
            \\rank<5> The number of additional successes increases to three, which is enough to remove most poisons immediately.
            \\rank<7> The target can also gain the same number of successes to remove an additional poison affecting it.
        """, tags=[]),
        Spell('Poison Transferance', 3, ['Yourself or an \\glossterm<ally> within \\rngmed range', 'One other living creature within that range'], """
            The primary target must be currently affected by a poison.
            Make an attack vs. Fortitude against the secondary target.
            \\hit The primary target gains an additional success to resist a poison currently affecting it.
            In addition, the secondary target becomes \\glossterm<poisoned> by that same poison, and immediately suffers the effect of the poison's first \\glossterm<poison stage>.
            % No \\glance effect; weird shenanigans if you autoremove the poison
            \\crit As above, except that the primary target gains two successes to resist its poison.
            In addition, the secondary target immediately reaches the poison's second poison stage.
        """, scaling="accuracy", tags=[]),
        Spell('Poison Immunity', 4, 'Yourself', """
            You become immune to all \\glossterm<poisons>.
            You stop being poisoned by any poisons currently affecting you, and new poisons cannot be applied to you.
        """, scaling="""
            \\rank<6> You can cast this spell as a \\glossterm<minor action>.
        """, tags=['Attune (self)']),
        Spell('Intensify Poison', 1, 'One living creature within \\rngmed range', """
            Make an attack vs. Fortitude with a +4 bonus to \\glossterm<accuracy> against the target.
            If the target is not currently poisoned, this ability has no effect.
            \\hit Choose a poison affecting the target.
            The poison progresses by two stages against the target, which can have varying effects depending on the poison (see \\pcref<Poison>).
            \\crit As above, except that the poison progresses by four stages instead of two.
        """, scaling="accuracy", tags=[]),
        Spell('Brief Regeneration', 2, 'Yourself or one living \\glossterm<ally> within \\rngshort range', """
            The target regains \\glossterm<hit points> equal to 1d6 plus half your \\glossterm<power>.
        """, scaling="""
            The healing increases by +1d for each rank beyond 2.
        """, tags=[]),
        Spell('Vital Regeneration', 5, 'Yourself or an \\glossterm<ally> within \\rngmed range', """
            You can cast this spell as a \\glossterm<minor action>.

            A the end of each round, the target can remove one of its \\glossterm<vital wounds>.
            If it does, it gains two \\glossterm<fatigue points>.
        """, scaling="""
            \\rank<7> The target can remove two \\glossterm<vital wounds> instead of one.
            It gains two \\glossterm<fatigue points> per vital wound removed this way.
        """, tags=['Attune (target)']),
        Spell('Regeneration', 4, 'Yourself', """
            You can cast this spell as a \\glossterm<minor action>.

            At the end of each round, if you did not lose any \\glossterm<hit points> that round, you regain 1d10 \\glossterm<hit points>.
        """, scaling="""
            The healing increases by +1d for each rank beyond 4.
        """, tags=['Attune (self)']),
        Spell('Swimmer', 2, 'Yourself', """
            You can cast this spell as a \\glossterm<minor action>.

            The target gains a \\glossterm<swim speed> equal to its \\glossterm<base speed>.
            In addition, it gains a +2 \\glossterm<magic bonus> to Swim checks.
        """, scaling="""
            \\rank<4> This spell can target an \\glossterm<ally> within \\rngmed range instead of you.
            \\rank<6> The bonus increases to +4.
        """, tags=['Attune (target)']),
        Spell('Climber', 2, 'Yourself', """
            You can cast this spell as a \\glossterm<minor action>.

            The target gains a \\glossterm<climb speed> equal to its \\glossterm<base speed>.
            In addition, it gains a +2 \\glossterm<magic bonus> to Climb checks.
        """, scaling="""
            \\rank<4> This spell can target an \\glossterm<ally> within \\rngmed range instead of you.
            \\rank<6> The bonus increases to +4.
        """, tags=['Attune (target)']),
        Spell('Runner', 2, 'Yourself', """
            You can cast this spell as a \\glossterm<minor action>.

            The target gains a +10 foot \\glossterm<magic bonus> to its \\glossterm<land speed>.
        """, scaling="""
            \\rank<4> This spell can target an \\glossterm<ally> within \\rngmed range instead of you.
            \\rank<6> The bonus increases to +20 feet.
        """, tags=['Attune (target)']),
        Spell('Enhanced Muscles', 2, 'Yourself', """
            You gain a +2 \\glossterm<magic bonus> to Strength-based checks.
            In addition, you gain a +2 \\glossterm<magic bonus> to Strength for the purpose of determining your \\glossterm<carrying capacity>.
        """, scaling="""
            \\rank<4> The bonus increases to +3.
            \\rank<6> The bonus increases to +4.
        """, tags=['Attune (self)']),
        Spell('Longshot', 1, 'Yourself', """
            The target reduces its penalties for \\glossterm<range increments> by 1.
        """, scaling="""
            \\rank<3> This spell can target an \\glossterm<ally> within \\rngmed range instead of you.
            \\rank<5> The penalty reduction increases to 2.
            \\rank<7> The penalty reduction increases to 3.
        """, tags=['Attune (target)']),
        Spell('Enhanced Senses', 1, 'Yourself', """
            The target gains a +3 \\glossterm<magic bonus> to the Awareness skill.
        """, scaling="""
            \\rank<3> This spell can target an \\glossterm<ally> within \\rngmed range instead of you.
            \\rank<5> The bonus increases to +5.
            \\rank<7> The bonus increases to +7.
        """, tags=['Attune (target)']),
        Spell('Scent', 3, 'Yourself', """
            You can cast this spell as a \\glossterm<minor action>.

            You gain the \\glossterm<scent> ability, giving you a +10 bonus to scent-based Awareness checks (see \\pcref<Senses>).
        """, scaling="""
            \\rank<5> The bonus increases to +15.
            \\rank<7> The bonus increases to +20.
        """, tags=['Attune (self)']),
        Spell('Acidic Blood', 3, ['Yourself', 'Everything adjacent to you'], """
            Your blood becomes acidic.
            This does not harm you, but your blood can be dangerous to anything nearby when you bleed.
            At the end of each round, if you lost \\glossterm<hit points> during that round, make an attack vs. Fortitude against everything adjacent to you.
            \\hit Each secondary target takes acid damage equal to 2d6 plus half your \\glossterm<power>.
            \\glance As above, except that that each target takes half damage.
        """, scaling="damage", tags=['Attune (target)']),
        # +1 level for damage -> attuned std action
        # +1 level over other dragon breaths for damage choice, including both
        # physical and energy
        Spell('Dragon Breath', 4, 'Yourself (see text)', """
            You can cast this spell as a \\glossterm<minor action>.

            You gain the ability to breath energy like a dragon.
            When you cast this spell, choose a type of damage: acid, cold, electricity, or fire.
            As a standard action, you can breath a cone of that type of energy.
            When you do, make an attack vs. Reflex against everything within a \\areamed cone from you.
            \\hit Each target takes damage of the chosen type equal to 2d8 plus half your \\glossterm<power>.
            \\glance As above, except that that each target takes half damage.
        """, scaling="damage", tags=['Attune (self)']),
        Spell('Withering', 2, 'One living creature within \\rngmed range', """
            Make an attack vs. Fortitude with a +2 bonus to \\glossterm<accuracy> against the target.
            \\hit As a \\glossterm<condition>, the target's body withers.
            It takes a -2 penalty to Fortitude defense.
            Whenever it loses one or more \\glossterm<hit points> from a single attack, this penalty increases by 1.
            This penalty increase stacks, and persists even if the target regains the lost hit points.
            \\crit As above, except that the penalty starts at -5.
        """, scaling="accuracy", tags=[]),
        Spell('Withering Curse', 3, 'One living creature within \\rngmed range', """
            Make an attack vs. Mental with a +2 bonus to \\glossterm<accuracy> against the target.
            \\hit The target becomes more vulnerable to injury until it takes a short rest.
            It takes a -2 penalty to Fortitude defense.
            Whenever it loses one or more \\glossterm<hit points> from a single attack, this penalty increases by 1.
            This penalty increase stacks, and persists even if the target regains the lost hit points.
            \\glance As above, except that the condition is removed at the end of the next round.
            \\crit As above, except that the effect lasts until this curse is removed.
        """, scaling="accuracy", tags=['Curse']),
        Spell('Sickness', 1, 'One living creature within \\rngshort range', """
            Make an attack vs. Fortitude against the target.
            \\hit The target is \\glossterm<sickened> as a \\glossterm<condition>.
            \\crit The target is \\glossterm<nauseated> as a \\glossterm<condition>.
        """, scaling="accuracy", tags=[]),
        Spell('Sickening Curse', 3, 'One living creature within \\rngmed range', """
            Make an attack vs. Mental against the target.
            \\hit The target is \\glossterm<sickened> until it takes a \\glossterm<short rest>.
            \\crit As above, except that the effect lasts until this curse is removed.
            \\glance As above, except that the condition is removed at the end of the next round.
        """, scaling="accuracy", tags=['Curse']),
        Spell('Eyebite', 4, 'One living creature within \\rngmed range', """
            Make an attack vs. Fortitude against the target.
            \\hit The target takes 2d6 physical damage.
            If it loses \\glossterm<hit points> from this damage, it is \\glossterm<blinded> as a \\glossterm<condition>.
            \\glance As above, except that that the target takes half damage.
        """, scaling="damage", tags=[]),
        Spell('Organ Failure', 1, 'One living creature within \\rngmed range', """
            Make an attack vs. Fortitude against the target.
            \\hit The target takes 1d6 physical damage.
            If it loses \\glossterm<hit points> from this damage, it is \\glossterm<nauseated> as a \\glossterm<condition>.
        """, scaling="damage", tags=[]),
        Spell('Cripple', 7, 'One living creature within \\rngshort range', """
            Make an attack vs. Fortitude against the target.
            \\hit The target is \\glossterm<immobilized> as a \\glossterm<condition>.
            \\glance As above, except that the condition is removed at the end of the next round.
            \\crit The target is \\glossterm<paralyzed> as a \\glossterm<condition>.
        """, tags=[]),
        Spell('Bleed', 2, 'One living creature within \\rngmed range', """
            Make an attack vs. Fortitude against the target.
            \\hit The target begins bleeding as a \\glossterm<condition>.
            At the end of each round, it takes 1d8 physical damage.
            If the the target gains a \\glossterm<vital wound> from this damage, the condition ends.

            This condition can be removed with the \\textit<treat condition> ability from the Medicine skill (see \\pcref<Medicine>).
            The \\glossterm<difficulty rating> of the check is equal to 10.
            \\crit As above, except that the damage from the condition is doubled.
        """, scaling="damage", tags=[]),
        Spell('Blood Fountain', 5, 'One living creature within \\rngmed range', """
            Make an attack vs. Fortitude against the target.
            \\hit The target begins bleeding as a \\glossterm<condition>.
            At the end of each round, it takes 2d8 physical damage.
            If the the target gains a \\glossterm<vital wound> from this damage, the condition ends.

            This condition can be removed with the \\textit<treat condition> ability from the Medicine skill (see \\pcref<Medicine>).
            The \\glossterm<difficulty rating> of the check is equal to 20.
            \\glance As above, except that the condition is removed at the end of the next round after its damage is dealt.
            \\crit As above, except that the damage from the condition is doubled.
        """, scaling="damage", tags=[]),
    ],
    rituals=[
        Spell('Awaken', 6, 'One Large or smaller \\glossterm<ally> within \\rngmed range', """
            The target becomes sentient.
            Its Intelligence becomes 1d6 - 5.
            Its type changes from animal to magical beast.
            It gains the ability to speak and understand one language that you know of your choice.
            Its maximum age increases to that of a human (rolled secretly).
            This effect is permanent.

            You can only learn this ritual if you have access to this mystic sphere through the nature \\glossterm<magic source>.
        """, tags=[], ritual_time='24 hours'),
        Spell('Air Breathing', 3, 'One Medium or smaller ritual participant', """
            The target can breathe air as easily as a human breathes air, preventing it from suffocating above water if it can normally only breathe water or some other substance.
        """, tags=['Attune (ritual)'], ritual_time='one minute'),
        Spell('Water Breathing', 3, 'One Medium or smaller ritual participant', """
            The target can breathe water as easily as a human breathes air, preventing it from drowning or suffocating underwater.
        """, tags=['Attune (ritual)'], ritual_time='one minute'),
    ],
    category='damage',
)
