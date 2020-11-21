from rise.latex.mystic_sphere import MysticSphere
from rise.latex.spell import Spell
from rise.latex.effects import Effects


# Primary: damage
# Secondary: debuff
# Tertiary: buff
# None: utility
cryomancy=MysticSphere(
    name='Cryomancy',
    short_description='Drain heat to injure and freeze foes',
    cantrips=[
        Effects('Chill', 'One creature or object within \\rngclose range', """
            Make an attack vs. Fortitude against the target.
            \\hit The target takes 2 cold damage.
        """, scaling="""
            \\rank<3> The damage increases to 5.
            \\rank<5> The damage increases to 10.
            \\rank<7> The damage increases to 20.
        """, tags=[]),
    ],
    lists=['Arcane', 'Nature', 'Pact'],
    spells=[
        Spell('Freezing Grasp', 1, 'One creature or object within your \\glossterm<reach>', """
            This spell does not have the \\glossterm<Focus> tag.
            You must have a \\glossterm<free hand> to cast this spell.

            Make a melee attack vs. Reflex against the target.
            \\hit The target takes cold damage equal to 1d10 plus your \\glossterm<power>.
        """, scaling="damage", tags=[], focus=False),
        Spell('Cone of Cold', 1, 'Everything in a \\areamed cone from you', """
            Make an attack vs. Fortitude against each target.
            \\hit Each target takes cold damage equal to 1d8 plus half your \\glossterm<power>.
        """, scaling="damage", tags=[]),
        Spell('Frozen Legs', 4, 'One creature within \\rngmed range', """
            Make an attack vs. Fortitude against the target.
            \\hit The target takes 2d6 cold damage.
            If it loses \\glossterm<hit points> from this damage, it is \\glossterm<immobilized> as a \\glossterm<condition>.
            \\glance As above, except that that the target takes half damage.
        """, scaling="damage", tags=[]),
        Spell('Mass Frozen Legs', 6, '\\glossterm<Enemies> in a \\areasmall radius within \\rngmed range', """
            Make an attack vs. Fortitude against each target.
            \\hit Each target that has no remaining \\glossterm<resistance> to cold damage is \\glossterm<immobilized> as a \\glossterm<condition>.
            \\glance As above, except that the condition is removed at the end of the next round.
        """, scaling="accuracy", tags=[]),
        # +2 levels for cold + bludgeoning, which breaks resistances
        Spell('Ice Lance', 4, 'Everything in a \\arealarge, 5 ft.\\ wide line from you', """
            Make an attack vs. Armor against each target.
            \\hit Each target takes piercing and cold damage equal to 2d8 plus half your \\glossterm<power>.
            \\glance As above, except that that each target takes half damage.
        """, scaling="damage", tags=['Manifestation']),
        # +2 levels for cold + bludgeoning, which breaks resistances
        Spell('Ice Spike', 3, 'One creature or object within \\rngmed range', """
            Make an attack vs. Armor against the target.
            \\hit The target takes piercing and cold damage equal to 2d8 plus your \\glossterm<power>.
            \\glance As above, except that that the target takes half damage.
        """, scaling="damage", tags=['Manifestation']),
        Spell('Freeze Poison', 2, 'Yourself or one \\glossterm<ally> within \\rngmed range', """
            The target takes 1d6 cold damage.
            In addition, it gains an additional success to resist a poison currently affecting it (see \\pcref<Poison>).
        """, scaling="""
            \\rank<4> The number of additional successes increases to two.
            \\rank<6> The number of additional successes increases to three, which is enough to remove most poisons immediately.
        """, tags=[]),
        Spell('Brittle Chill', 3, 'One creature or object within \\rngmed range', """
            Make an attack vs. Fortitude against the target.
            \\hit The target takes 2d6 cold damage.
            If it loses \\glossterm<hit points> from this damage, it is \\glossterm<vulnerable> to bludgeoning damage as a \\glossterm<condition>.
            \\glance As above, except that that the target takes half damage.
        """, scaling="damage", tags=[]),
        Spell('Chilled Mind', 1, 'One creature within \\rngmed range', """
            Make an attack vs. Fortitude against the target.
            \\hit The target takes 1d6 cold damage.
            If it loses \\glossterm<hit points> from this damage, it is \\glossterm<stunned> as a \\glossterm<condition>.
        """, scaling="damage", tags=[]),
        Spell('Mass Chilled Mind', 5, '\\glossterm<Enemies> in a \\arealarge radius from you', """
            Make an attack vs. Fortitude against each target.
            \\hit Each target that has no remaining \\glossterm<resistance> to cold damage is \\glossterm<stunned> as a \\glossterm<condition>.
            \\glance As above, except that the condition is removed at the end of the next round.
        """, scaling="accuracy", tags=[]),
        Spell('Skate', 1, 'Yourself', """
            The target can move on top of calm water as if it were land.
            It treats the water as \\glossterm<difficult terrain>.

            You can cast this spell as a \\glossterm<minor action>.
        """, scaling="""
            \\rank<3> This spell can target an \\glossterm<ally> within \\rngmed range instead of you.
            \\rank<5> The target can also move on top of rough or stormy water.
            \\rank<7> The target no longer treats the water as difficult terrain.
        """, tags=['Attune (target)']),
        Spell('Skyskate', 3, 'Yourself', """
            Whenever you move, you can leave a trail of ice behind you.
            The ice lasts until the end of the round before disappearing.

            While you are leaving a trail of ice behind you, you can move into thin air by walking on your own ice trail, just as if it was solid ground.
            If you are still standing on your own ice trail when it disappears at the end of the round, you fall.

            Creatures following closely behind you while you move may also be able to use your ice trail.
            However, most Large or larger creatures will break the ice trail if they step onto it, which may cause both of you to fall.
        """, scaling="""
            \\rank<5> Your ice trail collapses more gradually.  If you are still standing on your own ice trail when it disappears, you can fall up to 50 feet before you start taking \\glossterm<falling damage>.
            \\rank<7> Your ice trail lasts until the end of the next round after your movement.
        """, tags=['Attune (self)', 'Manifestation']),
        Spell('Icy Shell', 2, 'Yourself', """
            You cover your body with four overlapping layers of ice that crumple when they take damage.
            The ice does not cover your joints, allowing you to move freely.
            You are \\glossterm<resistant> to \\glossterm<physical damage> and \\glossterm<fire damage>.
            Whenever you take physical damage or fire damage, one layer of ice is destroyed.
            When the last layer of ice is destroyed, this ability provides no further benefit.
        """, scaling="""
            \\rank<4> The spell creates six layers of ice.
            \\rank<6> The spell creates eight layers of ice.
        """, tags=['Attune (self)', 'Manifestation']),
        Spell('Winterwave', 3, 'Everything in a \\arealarge cone from you', """
            Make an attack vs. Fortitude against each target.
            \\hit Each target takes cold damage equal to 2d6 plus half your \\glossterm<power>.
            \\glance As above, except that that each target takes half damage.
        """, scaling="damage", tags=[]),
        Spell('Frostbite', 3, 'One creature or object within \\rngclose range', """
            Make an attack vs. Fortitude against the target.
            \\hit The target takes cold damage equal to 2d8 plus your \\glossterm<power>.
            If it loses \\glossterm<hit points> from this damage, it is \\glossterm<slowed> as a \\glossterm<condition>.
            \\glance As above, except that that the target takes half damage.
        """, scaling="damage", tags=[]),
        # +2 levels for cold + bludgeoning, which breaks resistances
        Spell('Hailstorm', 5, 'Everything in a \\areasmall radius within \\rngmed range', """
            Make an attack vs. Armor against each target.
            \\hit Each target takes cold and bludgeoning damage equal to 2d10 plus half your \\glossterm<power>.
            \\glance As above, except that that each target takes half damage.
        """, scaling="damage", tags=[]),
        Spell('Blizzard', 3, '\\glossterm<Enemies> and objects in a \\areamed radius from you', """
            Make an attack vs. Fortitude against each target.
            \\hit Each target takes cold damage equal to 2d6 plus half your \\glossterm<power>.
            \\glance As above, except that that each target takes half damage.
        """, scaling="damage", tags=[]),
        Spell('Icecraft', 1, 'One pool of unattended, nonmagical water within \\rngclose range.', """
            This spell creates an icy weapon or a suit of icy armor from the target pool of water.
            You can create any weapon, shield, or body armor that you are proficient with, and which would normally be made entirely from metal, except for heavy armor.
            The pool of water targeted must be at least as large as the item you create.

            The item functions like a normal item of its type, except that it is more fragile.
            Its \\glossterm<vital resistance> is equal to twice your \\glossterm<power>, and it is \\glossterm<vulnerable> to fire damage.

            When a creature wearing armor created in this way takes physical damage, cold damage, or fire damage, that damage is also dealt to the armor.
            Likewise, when a creature wielding a weapon created in this way deals damage with the weapon, that damage is also dealt to the weapon.
            If the item becomes \\glossterm<broken>, this effect is \\glossterm<dismissed>.

            This spell lasts until you use it again or until you \\glossterm<dismiss> it as a \\glossterm<free action>.
        """, scaling="""
            \\rank<3> The \\glossterm<vital resistance> of the item increases to three times your power.
                In addition, you can also create heavy armor.
            \\rank<5> The item created is magically enhanced.
                A weapon grants a +2 \\glossterm<magic bonus> to \\glossterm<power> with \\glossterm<mundane> abilities,
                    and armor grants a +1 \\glossterm<magic bonus> to Armor defense.
            \\rank<7> The \\glossterm<vital resistance> of the item increases to four times your power.
        """, tags=[]),
        Spell('Frost Breath', 4, 'Yourself', """
            As a standard action, you can breathe cold like a dragon.
            When you do, make an attack vs. Fortitude against everything in a \\arealarge cone.
            \\hit Each target takes cold damage equal to 2d8 plus half your \\glossterm<power>.
            \\glance As above, except that that each target takes half damage.

            You can cast this spell as a \\glossterm<minor action>.
        """, scaling="damage", tags=['Attune (self)']),
        Spell('Frostburn', 7, 'One creature within \\rngclose range', """
            Make an attack vs. Fortitude against the target.
            \\hit As a \\glossterm<condition>, the target is seared by painful cold.
            % TODO: standardize "ignite" damage
            At the end of each round, it takes 4d10 cold damage.
            \\glance As above, except that the condition is removed at the end of the next round after its damage is dealt.
            \\crit As above, except that the damage from the condition is doubled.
        """, tags=[]),
    ],
    rituals=[
        Spell('Frostfall', 4, None, """
            The temperature in a two mile radius cylinder-shaped \\glossterm<zone> from your location decreases rapidly.
            Over the next minute after you finish this ritual, the temperature decreases by 40 degrees Fahrenheit, to a minimum of \\minus30 degrees.
            Unlike normal, this effect does not require \\glossterm<line of effect> to you.
            Instead, it affects all outdoor locations within the area.
            Even a thin barrier, such as a tent, is enough to protect locations from the effect of this ritual.
        """, tags=['Attune (self)'], ritual_time='one hour'),
        Spell('Froststorm', 8, None, """
            This ritual functions like the \\spell<frostfall> ritual, except that the temperature in the area decreases by 60 degrees, to a minimum of \\minus70 degrees.
        """, tags=['Attune (self)'], ritual_time='one hour'),
    ],
    category='damage',
)
