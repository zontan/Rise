from rise.latex.mystic_sphere import MysticSphere
from rise.latex.spell import Spell
from rise.latex.effects import Effects


# This seems weird?
# Secondary: buff, damage, debuff, utility
summon=MysticSphere(
    name="Summoning",
    short_description="Summon creatures to fight with you",
    cantrips=[
    ],
    lists=['Arcane', 'Divine', 'Nature'],
    spells=[
        # TODO: this needs more spell
        Spell('Summon Monster', 1, 'One unoccupied square on stable ground within \\rngmed range', """
            You summon a creature in the target location.
            It visually appears to be a common Small or Medium animal of your choice, though in reality it is a manifestation of magical energy.
            Regardless of the appearance and size chosen, the creature's statistics use the values below.
            If a summoned creature gains a \\glossterm<vital wound> or has no hit points remaining at the end of a phase, it disappears.

            \\begin<itemize>
                \\item Its \\glossterm<hit points> are equal to half the base value for your level (see \\tref<Hit Points>).
                \\item Each of its \\glossterm<defenses> is equal to 4 \\add your level.
                \\item Its \\glossterm<accuracy> is equal to your \\glossterm<accuracy> \\sub 2.
                \\item Its \\glossterm<land speed> is 30 feet.
                \\item It has no \\glossterm<attunement points>.
            \\end<itemize>

            Each round, you can choose the creature's actions by mentally commanding it as a \\glossterm<minor action>.
            There are only two actions it can take.
            As a \\glossterm<move action>, it can move as you direct.
            As a standard action, it can make a melee \\glossterm<strike> against a creature it threatens.
            If it hits, it deals physical damage equal to 1d6 plus half your \\glossterm<power>.
            The subtypes of damage dealt by this attack depend on the creature's appearance, but are limited to bludgeoning, piercing, and slashing damage.
            Most animals bite or claw their foes, which deals bludgeoning and slashing damage.

            If you do not command the creature's actions, it will continue to obey its last instructions if possible or do nothing otherwise.
            Summoned creatures have no mind or independent agency, and will not act on their own even if attacked.
        """, scaling="damage", tags=['Attune (self)', 'Manifestation']),
        Spell('Summon Unicorn', 6, 'One unoccupied square within \\rngmed range', """
            This spell functions like the \\textit<summon monster> spell, except that the summoned creature appears to be a unicorn.
            Its attacks deal piercing damage equal to 2d10 plus half your \\glossterm<power>, and you can command it to heal instead of attack.
            If you do, during the \\glossterm<action phase> it cause one of your \\glossterm<allies> within \\rngshort range of it to regain 2d10 \\glossterm<hit points>.
            You can tell it which creature to heal.
            If you do not instruct it to heal a specific creature, it will automatically heal the ally closest to it that has lost at least one hit point.
        """, scaling="""
            The damage and healing both increase by +1d for each rank beyond 6.
        """, tags=['Attune (self)', 'Manifestation']),
        Spell('Summon Weapon', 3, 'One unoccupied square within \\rngmed range', """
            This spell functions like the \\textit<summon monster> spell, with the following exceptions.
            The summoned creature takes the form of a melee weapon of your choice that you are proficient with.
            It is sized appropriately to be wielded by a creature of your size.
            It floats three feet off the ground, and has a 30 foot \\glossterm<fly speed> instead of a \\glossterm<land speed>, with good \\glossterm<maneuverability> (see \\pcref<Flying>).
            The weapon's maximum height above the ground is limited to 10 feet.
            The creature's accuracy and damage are based on your chosen weapon, and it gains the effect of the weapon's normal tags (see \\pcref<Weapon Tags>).
            It gains a +2d bonus to damage, and it adds half your \\glossterm<power> to damage.
            The weapon is considered to be held in two hands if possible, which can increase the damage dealt by medium weapons (see \\pcref<Weapon Usage Classes>).

            You cannot control the summoned weapon's actions.
            Each round, the weapon automatically moves towards the creature closest to it during the \\glossterm<movement phase>, following that creature to the best of its abilities.
            During the \\glossterm<action phase>, it makes a melee \\glossterm<strike> against a creature within its \\glossterm<reach>.
            The weapon prefers to avoid accuracy and damage penalties that would be imposed by cover or special weapon grips.
            It choses randomly if all possible targets are equally easy to attack.
        """, scaling="damage", tags=['Manifestation', 'Sustain (minor)']),
        Spell('Aerial Weapon', 4, 'One unoccupied square within \\rngmed range', """
            This spell functions like the \\spell<summon weapon> spell, except that the weapon's maximum height above the ground is increased to 100 feet.
            This allows the weapon to fly up to fight airborne foes.
            In addition, the weapon's damage bonus is increased to +3d.
        """, scaling="damage", tags=['Manifestation', 'Sustain (minor)']),
        Spell('Summon Ballista', 3, 'One unoccupied square within \\rngmed range', """
            This spell functions like the \\spell<summon weapon> spell, except that it creates a fully functional Large ballista instead of a weapon.
            The ballista functions like any other weapon, with the following exceptions.

            It cannot move, and makes ranged \\glossterm<strikes> instead of melee strikes.
            Its attacks have a maximum range of 100 feet and deal piercing damage.
            In addition, the ballista attacks the creature farthest from it, instead of the creature closest to it.
        """, scaling="damage", tags=['Manifestation', 'Sustain (minor)']),
        Spell('Summon Earth Elemental', 5, 'One unoccupied square on stable ground within \\rngmed range', """
            This spell functions like the \\spell<summon monster> spell, except that the summoned creature appears to be an earth elemental.
            Its attacks deal bludgeoning damage equal to 2d8 plus half your \\glossterm<power>.
            It has a \\glossterm<resistance> to \\glossterm<physical damage> equal to half its maximum \\glossterm<hit points>.
        """, scaling="damage", tags=['Attune (self)', 'Manifestation']),
        Spell('Summon Water Elemental', 2, 'One unoccupied square on stable ground within \\rngmed range', """
            This spell functions like the \\spell<summon monster> spell, except that the summoned creature appears to be an water elemental.
            Its attacks deal bludgeoning damage equal to 1d8 plus half your \\glossterm<power>.
            It has a 30 foot \\glossterm<swim speed>, and it suffers no penalties for fighting underwater (see \\pcref<Underwater Combat>).
            However, it is \\glossterm<vulnerable> to electricity damage.
        """, scaling="damage", tags=['Attune (self)', 'Manifestation']),
        Spell('Summon Air Elemental', 4, 'One unoccupied square on stable ground within \\rngmed range', """
            This spell functions like the \\spell<summon monster> spell, except that the summoned creature appears to be an air elemental.
            Its attacks deal bludgeoning damage equal to 2d6 plus half your \\glossterm<power>.
            It has a 30 foot \\glossterm<fly speed> with good \\glossterm<maneuverability>.
        """, scaling="damage", tags=['Attune (self)', 'Manifestation']),
        # only elemental that deals non-physical damage
        Spell('Summon Fire Elemental', 3, 'One unoccupied square on stable ground within \\rngmed range', """
            This spell functions like the \\spell<summon monster> spell, except that the summoned creature appears to be a fire elemental.
            Its attacks deal fire damage equal to 1d10 plus half your \\glossterm<power>.
            In addition, it is immune to fire damage.
        """, scaling="damage", tags=['Attune (self)', 'Manifestation']),
        Spell('Summon Bear', 3, 'One unoccupied square on stable ground within \\rngmed range', """
            This spell functions like the \\spell<summon monster> spell, except that the creature appears to be a Medium bear.
            Its attacks deal bludgeoning and slashing damage equal to 1d10 plus half your \\glossterm<power>.
            In addition, it suffers no penalty for attacking in a grapple.
            As a standard action, it can make a \\glossterm<grapple> attack against a creature it threatens.
            While grappling, the manifested creature can either make a strike or attempt to escape the grapple.
        """, scaling="damage", tags=['Attune (self)', 'Manifestation']),
        Spell('Summon Mount', 3, 'One unoccupied square on stable ground within \\rngmed range', """
            This spell functions like the \\spell<summon monster> spell, except that you must also choose an \\glossterm<ally> within \\rngmed range to ride the summoned creature.
            The summoned creature appears to be either a Large horse or a Medium pony.
            It comes with a bit and bridle and a riding saddle, and will only accept the target as a rider.
            The creature follows its rider's directions to the extent that a well-trained horse would and it cannot attack.
        """, scaling="""
            \\rank<5> The creature gains a +1 bonus to its defenses.
            \\rank<7> The defense bonus increases to +2.
        """, tags=['Attune (target)', 'Manifestation']),
        Spell('Summon Wolfpack', 7, 'One unoccupied square on stable ground within \\rngmed range', """
            This spell functions like the \\spell<summon monster> spell, except that it summons a pack of four Small wolf-shaped creatures instead of a single creature.
            Their attacks deal 2d10 bludgeoning and piercing damage.
            Each creature has a -2 penalty to \\glossterm<accuracy> and \\glossterm<defenses> compared to a normal summoned creature.
            In addition, each creature has half the hit points of a normal summoned creature.
            % TODO: wording?
            You must command the creatures as a group, rather than as individuals.
            Each creature obeys your command to the extent it can.
        """, tags=['Attune (self)', 'Manifestation']),
        Spell('Summon Pegasus', 5, 'One unoccupied location on stable ground within \\rngmed range', """
            This spell functions like the \\spell<summon mount> spell, except that the summoned creature appears to be either a Large or Medium pegasus.
            % TODO: wording of "trained as a mount"?
            It has a 30 foot \\glossterm<fly speed> and is trained as a mount.
        """, scaling="""
            \\rank<7> The creature gains a +1 bonus to its defenses.
        """, tags=['Attune (target)', 'Manifestation']),
        Spell('Summon Asp', 4, 'target', """
            This spell functions like the \\spell<summon creature> spell, except that the summoned creature appears to be a snake.
            Its attacks deal bludgeoning and piercing damage equal to 2d6 plus half your \\glossterm<power>.
            Whenever its strike causes a living creature to lose \\glossterm<hit points>, the damaged creature becomes \\glossterm<poisoned> with asp venom (see \\tref{Typical Poisons}).
            It immediately is \\glossterm<sickened> while it is poisoned.
            The poison's third stage causes the target to become \\glossterm<nauseated> as long as it is poisoned.
        """, scaling="damage", tags=['Attune (self)', 'Manifestation']),
    ],
    rituals=[
        # weird to have a spell and a ritual but both are useful
        Spell('Ritual Mount', 3, 'Yourself or an \\glossterm<ally> within \\rngmed range', """
            This ritual summons your choice of a Large light horse or a Medium pony to serve as a mount.
            The creature appears in an unoccupied location within \\rngmed range.
            It comes with a bit and bridle and a riding saddle, and will only accept the target as a rider.
            It has the same statistics as a creature from the \\spell<summon monster> spell, except that it follows its rider's directions to the extent that a well-trained horse would and it cannot attack.
        """, tags=['Attune (ritual)', 'Manifestation'], ritual_time='one minute'),
    ],
    # What category does this belong to?
    category='buff, offense',
)
