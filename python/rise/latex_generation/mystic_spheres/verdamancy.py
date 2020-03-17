from rise.latex.mystic_sphere import MysticSphere
from rise.latex.spell import Spell
from rise.latex.effects import Effects


# Primary: debuff
# Secondary: utility
# Tertiary: damage
# None: buff
verdamancy=MysticSphere(
    name="Verdamancy",
    short_description="Animate and manipulate plants",
    cantrips=[
        Effects('Rapid Growth', 'Small or smaller inanimate plant within \\rngclose range', """
            The target grows as if a month of time had passed.
            When this spell ends, the plant returns to its original state.
        """, tags=['Sustain (minor)']),
    ],
    lists=['Nature'],
    spells=[
        Spell('Entangle', 1, 'One Large or smaller creature within \\rngclose range', """
            You cause plants to grow and trap a foe.
            Make an attack vs. Reflex against the target.
            The target must be within 5 feet of earth or plants.
            You gain a +2 bonus to \\glossterm<accuracy> with this attack if the target is in standing in \\glossterm<undergrowth>.
            \\hit The target is \\glossterm<immobilized> as a \\glossterm<condition>.
            This condition can be removed if the target or a creature that can reach the target makes a \\glossterm<difficulty rating> 5 Strength check break the target free of the plants.
            The target can make this check as a \\glossterm<move action>, while other creatures can make the check as a standard action.

            \\rankline
            \\rank<3> The \\glossterm<difficulty rating> of the Strength check increases to 10.
            \\rank<5> The condition cannot be removed with a check.
            \\rank<7> You gain a +1 bonus to \\glossterm<accuracy> with the attack.
        """, tags=[]),
        Spell('Embedded Growth', 1, 'One creature within \\rngclose range', """
            You throw a seed that embeds itself in a foe and grows painfully.
            Make an attack vs. Fortitude against the target.
            \\hit As a \\glossterm<condition>, the target takes physical \\glossterm<standard damage> during each \\glossterm<action phase> in subsequent rounds.
            This condition can be removed if the target or a creature that can reach the target makes a \\glossterm<difficulty rating> 5 Heal check as a standard action to remove the seed.

            \\rankline
            \\rank<3> You gain a +1 bonus to \\glossterm<accuracy> with the attack.
            \\rank<5> The accuracy bonus increases to +2.
            \\rank<7> The accuracy bonus increases to +3.
        """, tags=[]),
        Spell('Fire Seeds', 3, 'One unattended acorn or similar seed structure you touch', """
            % Does "seed structure" make sense?
            You transform up to three unattended acorns or similar seed structures into small bombs.
            As a standard action, you or another creature can throw the acorn anywhere within \\rngclose range.
            % More accurate version: the acorn has a range increment of 10 feet to hit its target, but that accuracy roll is completely independent of the explosion.
            % Doesn't seem worth the complexity, and implicitly gives the fire seed surprisingly long range since objects are easy to hit.
            On impact, the acorn detonates, and you make an attack vs. Armor against everything within a \\areasmall radius of the struck creature or object.
            \\hit Each target takes fire \\glossterm<standard damage>.

            \\rankline
            \\rank<5> The damage increases to \\glossterm<standard damage> +1d.
            \\rank<7> The damage increases to \\glossterm<standard damage> +2d.
        """, tags=['Sustain (free)']),
        Spell('Wall of Thorns', 3, 'Each creature that moves through the area (see text)', """
            You create a wall of thorns in 20 ft.\\ high, \\areamed \\glossterm<wall> within \\rngmed range.
            The base of at least half of the wall must be in arable earth.
            The wall is four inches thick, but permeable.
            It provides \\glossterm<cover> to attacks made through the wall.
            Creatures can pass through the wall, though it costs five extra feet of movement to move through the wall.
            When a creature moves through the wall, make an attack vs. Armor against it.
            You can only make an attack in this way against a given creature once per \\glossterm<phase>.
            \\hit The target takes piercing \\glossterm<standard damage> -1d.

            Each five-foot square of wall has hit points equal to three times your \\glossterm<power>, and all of its defenses are 0.
            It is \\glossterm<vulnerable> to fire damage.

            \\rankline
            \\rank<5> The area increases to a \\arealarge shapeable line.
            \\rank<7> The damage increases to \\glossterm<standard damage>.
        """, tags=['Attune (self)']),
        Spell('Plant Growth', 1, 'All plants and arable earth in a \\areamed radius within \\rngmed range', """
            Choose whether you want plants within the area to grow or diminish.

            If you choose for plants to grow, all arable earth within the area becomes \\glossterm<light undergrowth>.
            Light undergrowth within the area is increased in density to \\glossterm<heavy undergrowth>.
            If you choose for plants to diminish, all \\glossterm<heavy undergrowth> in the area is reduced to \\glossterm<light undergrowth>, and all \\glossterm<light undergrowth> is removed.

            When this spell's duration ends, the plants return to their natural size.

            \\rankline
            \\rank<3> The area increases to a \\arealarge radius.
            \\rank<5> The range increases to \\rnglong.
            \\rank<7> The area increases to a \\areahuge radius.
        """, tags=['Sustain (minor)']),
        Spell('Blight', 1, 'One living creature or plant within \\rngmed range', """
            Make an attack vs. Fortitude against the target.
            % TODO: is this the right damage type?
            \\hit The target takes acid \\glossterm<standard damage>.
            This damage is doubled if the target is a plant, including plant creatures.

            \\rankline
            \\rank<3> The damage increases to \\glossterm<standard damage> +1d.
            \\rank<5> The damage increases to \\glossterm<standard damage> +2d.
            \\rank<7> The damage increases to \\glossterm<standard damage> +3d.
        """, tags=[]),
        Spell('Shillelagh', 1, 'One nonmagical stick of wood', """
            You transform the target into a club, greatclub, or quarterstaff, as you choose (see \\pcref<Weapons>).
            You cannot change the target's size by more than one size category.
            You gain a +2 \\glossterm<magic bonus> to \\glossterm<power> on attacks with it.

            \\rankline
            \\rank<3> You also gain +1 \\glossterm<magic bonus> to \\glossterm<accuracy> with the weapon.
            \\rank<5> The power bonus increases to +4.
            \\rank<7> The accuracy bonus increases to +2.
        """, tags=['Attune (self)']),
        Spell('Natural Camouflage', 1, 'Yourself', """
            You gain a +4 \\glossterm<magic bonus> to the Stealth skill while you have \\glossterm<cover> or \\glossterm<concealment> from plants.

            \\rankline
            \\rank<3> The bonus increases to +6.
            \\rank<5> The bonus increases to +8.
            \\rank<7> The bonus increases to +10.
        """, tags=['Sustain (minor)']),
        Spell('Flourishing Vines', 4, 'Yourself', """
            Long, thin vines continuously grow and writhe on your body.
            At the end of each round, you may choose to cause the vines to extend out onto the ground in a \\areamed radius around you.
            When you do, that area becomes covered in \\glossterm<light undergrowth>.
            Whenever you move, the vines retreat back to your body.
            That prevents the vines from impeding your movement, though they do impede the movement of any other creatures that move simultaneously.

            \\rankline
            \\rank<6> The area increases to a \\arealarge radius.
            \\rank<8> The area increases to a \\areahuge radius.
        """, tags=['Attune (self)']),
        Spell('Thornblade', 3, 'Yourself or an \\glossterm<ally> within \\rngclose range', """
            All damage the target deals with \\glossterm<strikes> becomes piercing damage in addition to the attack's normal damage types.
            Whenever the target deals damage to a creature with a \\glossterm<strike>, thorns from the striking weapon enter the target's body.
            As a \\glossterm<condition>, the damaged creature takes piercing \\glossterm<standard damage> -2d at the end of each round.

            This condition can be removed by the \\textit<treat condition> ability (see \\pcref<Treat Condition>).
            The \\glossterm<difficulty rating> of the check is equal to 5 \\add your \\glossterm<power>.

            \\rankline
            \\rank<5> The damage increases to \\glossterm<standard damage> -1d.
            \\rank<7> The damage increases to \\glossterm<standard damage>.
        """, tags=['Attune (target)']),
    ],
    rituals=[
        Spell('Fertility', 3, None, """
            This ritual creates an area of bountiful growth in a one mile radius \\glossterm<zone> from your location.
            Normal plants within the area become twice as productive as normal for the next year.
            This ritual does not stack with itself.
            If the \\ritual<infertility> ritual is also applied to the same area, the most recently performed ritual takes precedence.

            This ritual takes 24 hours to perform, and requires 8 action points from its participants.
        """, tags=['AP']),
        Spell('Infertility', 3, None, """
            This ritual creates an area of death and decay in a one mile radius \\glossterm<zone> from your location.
            Normal plants within the area become half as productive as normal for the next year.
            This ritual does not stack with itself.
            If the \\ritual<fertility> ritual is also applied to the same area, the most recently performed ritual takes precedence.

            This ritual takes 24 hours to perform, and requires 8 action points from its participants.
        """, tags=['AP']),
        Spell('Lifeweb Transit', 5, 'Up to five Medium or smaller ritual participants', """
            Choose up a living plant that all ritual participants touch during the ritual.
            The plant must be at least one size category larger than the largest target.
            In addition, choose a destination up to 100 miles away from you on your current plane.
            By walking through the chosen plant, each target is teleported to the closest plant to the destination that is at least one size category larger than the largest target.

            You must specify the destination with a precise mental image of its appearance.
            The image does not have to be perfect, but it must unambiguously identify the destination.
            If you specify its appearance incorrectly, or if the area has changed its appearance, the destination may be a different area than you intended.
            The new destination will be one that more closely resembles your mental image.
            If no such area exists, the ritual simply fails.
            % TODO: does this need more clarity about what teleportation works?

            This ritual takes 24 hours to perform and requires 32 action points from its ritual participants.
        """, tags=['AP']),
    ],
)
