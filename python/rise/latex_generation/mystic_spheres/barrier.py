from rise.latex.mystic_sphere import MysticSphere
from rise.latex.spell import Spell
from rise.latex.effects import Effects



# Primary: buff
# Secondary: utility
# None: damage, debuff
barrier=MysticSphere(
    name='Barrier',
    short_description="Construct barriers to shield allies and areas from hostile forces",
    cantrips=[
        Effects('Minor Barrier', None, """
            This cantrip functions like the \\spell<mystic barrier> spell, except that its \\glossterm<range> is \\rngclose and the maximum dimensions of the barrier are a 5 ft.\\ by 5 ft.\\ square.

            \\rankline
            \\rank<3> The range increases to \\rngmed.
            \\rank<5> The maximum dimensions of the wall increase to a 5 ft.\\ by 10 ft.\\ rectangle.
            \\rank<7> The maximum dimensions of the wall increase to a 10 ft.\\ by 10 ft.\\ square.
        """, tags=[]),
    ],
    lists=['Arcane', 'Divine', 'Nature'],
    spells=[
        Spell('Mirror Barrier', 4, None, """
            This spell functions like the \\spell<mystic barrier> spell, except that it reflects \\glossterm<mundane> attacks against it.
            The barrier's defenses become equal to 5 + your level.
            Whenever a creature misses the barrier with a \\glossterm<mundane> attack, it makes the same attack against itself, rolling a new attack roll against its own defenses.
            In addition, the \\glossterm<vital resistance> of each 5-ft.\\ square increases to be equal to three times your \\glossterm<power>.

            \\rankline
            \\rank<6> The area increases to a \\arealarge line.
            \\rank<8> The \\glossterm<vital resistance> of each 5-ft.\\ square increases to be equal to four times your \\glossterm<power>.
        """, tags=['Manifestation', 'Sustain (minor)']),
        Spell('Visual Barrier', 2, None, """
            This spell functions like the \\spell<mystic barrier> spell, except that you can choose the visibility of the barrier.
            There are three possibilities: fully invisible, barely visible like a normal \\spell<mystic barrier>, and visible as a deep black tht completely blocks sight.
            You can change the opacity of the barrier as a \\glossterm<minor action>.

            \\rankline
            \\rank<4> The \\glossterm<vital resistance> of each 5-ft.\\ square increases to be equal to three times your \\glossterm<power>.
            \\rank<6> The area increases to a \\arealarge line.
            \\rank<8> The \\glossterm<vital resistance> of each 5-ft.\\ square increases to be equal to four times your \\glossterm<power>.
        """, tags=['Manifestation', 'Sustain (minor)']),
        Spell('Audible Barrier', 2, None, """
            This spell functions like the \\spell<mystic barrier> spell, except that you can choose how much the barrier blocks sound.
            There are two possibilities: fully sound-permeable, and fully sound-blocking like a normal \\spell<mystic barrier>.
            You can change how much the barrier blocks sound as a \\glossterm<minor action>.
            Exceptionally strong sounds, such as sonic attacks that deal energy damage, are blocked by the barrier like other damaging effects.
            In addition, the \\glossterm<vital resistance> of each 5-ft.\\ square increases to be equal to three times your \\glossterm<power>.

            \\rankline
            \\rank<4> The \\glossterm<vital resistance> of each 5-ft.\\ square increases to be equal to three times your \\glossterm<power>.
            \\rank<6> The area increases to a \\arealarge line.
            \\rank<8> The \\glossterm<vital resistance> of each 5-ft.\\ square increases to be equal to four times your \\glossterm<power>.
        """, tags=['Manifestation', 'Sustain (minor)']),
        Spell('Forceful Barrier', 3, None, """
            This spell functions like the \\spell<mystic barrier> spell, except that it breaks objects in its area that obstruct its path.
            Each object in the path of the wall takes energy \\glossterm<standard damage>.
            Any object destroyed in this way does not block the barrier's area of effect.
            This does no damage to creatures, who block the path of the barrier like normal.
            In addition, the \\glossterm<vital resistance> of each 5-ft.\\ square increases to be equal to three times your \\glossterm<power>.

            \\rankline
            \\rank<5> The area increases to a \\arealarge line.
            \\rank<7> The \\glossterm<vital resistance> of each 5-ft.\\ square increases to be equal to four times your \\glossterm<power>.
        """, tags=['Manifestation', 'Sustain (minor)']),
        Spell('Mystic Barrier', 1, None, """
            You create a wall of magical energy within \\rngmed range.
            You can choose the dimensions of the wall, up to a maximum of a 20 ft.\\ high, \\areamed length line.
            If you create the wall within a space too small to hold it, it fills as much of the space as possible, starting from the middle of the chosen space.
            This can allow you to completely block off small tunnels.
            The wall is visible as a shimmering magical membrane that does not block sight.
            Nothing can pass through the wall until it is destroyed.
            Each 5-ft.\\ square of wall has a \\glossterm<vital resistance> equal to twice your \\glossterm<power>.

            When you cast this spell, you can \\glossterm<attune> to it.
            If you do, it gains the \\glossterm<Attune> (self) tag and loses the \\glossterm<Sustain> (minor) tag.

            \\rankline
            \\rank<3> The \\glossterm<vital resistance> of each 5-ft.\\ square increases to be equal to three times your \\glossterm<power>.
            \\rank<5> The area increases to a \\arealarge line.
            \\rank<7> The \\glossterm<vital resistance> of each 5-ft.\\ square increases to be equal to four times your \\glossterm<power>.
        """, tags=['Manifestation', 'Sustain (minor)']),
        Spell('Mystic Bridge', 3, None, """
            You create a horizontal field of magical energy within \\rngmed range.
            You can choose the dimensions of the field, up to a maximum of a \\areamed length, 10 ft.\\ width line.
            If you create the field within a space too small to hold it, it fills as much of the space as possible, allowing you to completely block off small vertical tunnels.
            The field is visible as a shimmering magical membrane that does not block sight.
            Nothing can pass through the field until it is destroyed.
            Each 5-ft.\\ square of the field has a \\glossterm<vital resistance> equal to twice your \\glossterm<power>.

            \\rankline
            \\rank<5> The area increases to a \\arealarge line.
            \\rank<7> The area increases to be a \\areahuge, 20 ft.\\ wide line.
        """, tags=['Manifestation', 'Sustain (minor)']),
        Spell('Protective Sphere', 1, 'Yourself or one Large or smaller \\glossterm<ally> within \\rngmed range', """
            You create a sphere of magical energy around the target in its space.
            The sphere is visible as a shimmering magical membrane that does not block sight.
            Nothing can pass through the field until it is destroyed.
            This prevents the target from having \\glossterm<line of effect> to anything outside of the area.
            Each 5-ft.\\ square of the field has a \\glossterm<vital resistance> equal to twice your \\glossterm<power>.

            If another creature is in the target's space when this spell is cast, this spell fails without effect.

            \\rankline
            \\rank<3> The \\glossterm<vital resistance> of each 5-ft.\\ square increases to be equal to three times your \\glossterm<power>.
            \\rank<5> The maximum size of the target increases to Huge.
            \\rank<7> The \\glossterm<vital resistance> of each 5-ft.\\ square increases to be equal to four times your \\glossterm<power>.
        """, tags=['Manifestation', 'Sustain (minor)']),
        Spell('Quickseal', 2, 'One openable object within \\rngmed range (see text)', """
            You create a curved field of magical energy that blocks access to the target's opening mechanism.
            The opening mechanism must be Small or smaller in size.
            Nothing can pass through the field until it is destroyed.
            The field has a \\glossterm<vital resistance> equal to twice your \\glossterm<power>.

            \\rankline
            \\rank<4> The \\glossterm<vital resistance> of the field increases to three times your \\glossterm<power>.
            \\rank<6> The \\glossterm<vital resistance> of the field increases to four times your \\glossterm<power>.
            \\rank<8> The \\glossterm<vital resistance> of the field increases to five times your \\glossterm<power>.
        """, tags=['Manifestation', 'Sustain (minor)']),
        Spell('Personal Sphere', 5, 'Yourself', """
            You create a sphere of magical energy around yourself.
            The sphere is visible as a shimmering magical membrane that does not block sight.
            Nothing can pass through the field until it is destroyed.
            This prevents the target from having \\glossterm<line of effect> to anything outside of the area.
            When you move, the sphere moves with you, though you cannot force it against another creature or object.
            Each 5-ft.\\ square of the field has a \\glossterm<vital resistance> equal to three times your \\glossterm<power>.

            \\rankline
            \\rank<7> The \\glossterm<vital resistance> of each 5-ft.\\ square increases to be equal to four times your \\glossterm<power>.
        """, tags=['Manifestation', 'Sustain (minor)']),
        Spell('Entrapping Sphere', 4, 'One Large or smaller creature or object within \\rngmed range', """
            Make an attack vs. Reflex against the target.
            \\hit You create a sphere of magical energy around the target in its space.
            The sphere is visible as a shimmering magical membrane that does not block sight.
            Nothing can pass through the field until it is destroyed.
            This prevents the target from having \\glossterm<line of effect> to anything outside of the area.
            Each 5-ft.\\ square of the field has a \\glossterm<vital resistance> equal to twice your \\glossterm<power>.

            If another creature is in the target's space when this spell is cast, this spell fails without effect.

            \\rankline
            \\rank<6> The \\glossterm<vital resistance> of each 5-ft.\\ square increases to be equal to three times your \\glossterm<power>.
            \\rank<8> The maximum size of the target increases to Huge.
        """, tags=['Manifestation', 'Sustain (standard)']),
        Spell('Invulnerable Barrier', 6, None, """
            This spell functions like the \\spell<mystic barrier> spell, except that each 5-ft.\\ square of wall has a \\glossterm<vital resistance> equal to four times your \\glossterm<power>.
            In addition, the wall is \\glossterm<resistant> to physical damage.

            \\rankline
            \\rank<8> The area increases to a \\arealarge line.
        """, tags=['Manifestation', 'Sustain (minor)']),
        Spell('Wall of Energy Impedance', 3, None, """
            You create a wall of magical energy in a 20 ft.\\ high, \\areamed line within \\rngmed range.
            The wall is visible as a shimmering magical membrane that does not block sight.
            It does not impede passage for objects or creatures, but any ability that deals \\glossterm<energy damage> treats the wall as an impassable barrier.
            Each 5-ft.\\ square of wall has a \\glossterm<vital resistance> equal to twice your \\glossterm<power>.

            \\rankline
            \\rank<5> The area increases to a \\arealarge line.
            \\rank<7> The \\glossterm<vital resistance> of each 5-ft.\\ square increases to be equal to three times your \\glossterm<power>.
        """, tags=['Manifestation', 'Sustain (minor)']),
        Spell('Wall of Magic Impedance', 5, None, """
            You create a wall of magical energy in a 20 ft.\\ high, \\areamed line within \\rngmed range.
            The wall is visible as a shimmering magical membrane that does not block sight.
            It does not impede passage for objects or creatures, but any \\glossterm<magical> ability treats the wall as an impassable barrier.
            Each 5-ft.\\ square of wall has a \\glossterm<vital resistance> equal to three times your \\glossterm<power>.

            \\rankline
            \\rank<7> The area increases to a \\arealarge line.
        """, tags=['Manifestation', 'Sustain (minor)']),
        Spell('One-Way Barrier', 7, None, """
            This spell functions like the \\spell<mystic barrier> spell, except that you choose one side of the barrier when you cast the spell.
            Whenever an object, creature, or ability passes through the barrier from the chosen side, the barrier parts to allow it through.
            If it stops halfway, it can return to its side, but once it passes through fully it treats the barrier as impassable from the other side.
        """, tags=['Manifestation', 'Sustain (standard)']),
        Spell('Kinetic Shield', 1, 'Yourself or an \\glossterm<ally> in \\rngmed range', """
            The target gains a +2 \\glossterm<magic bonus> to \\glossterm<resistances> against \\glossterm<physical> damage.

            You can cast this spell as a \\glossterm<minor action>.

            \\rankline
            \\rank<3> The bonus increases to +4.
            \\rank<5> The bonus increases to be equal to half your \\glossterm<power>.
            \\rank<7> The bonus increases to be equal to your \\glossterm<power>.
        """, tags=['Attune (target)']),
        Spell('Resist Energy', 1, 'Yourself or an \\glossterm<ally> in \\rngmed range', """
            The target gains a +2 \\glossterm<magic bonus> to \\glossterm<resistances> against \\glossterm<energy> damage.

            You can cast this spell as a \\glossterm<minor action>.

            \\rankline
            \\rank<3> The bonus increases to +4.
            \\rank<5> The bonus increases to be equal to half your \\glossterm<power>.
            \\rank<7> The bonus increases to be equal to your \\glossterm<power>.
        """, tags=['Attune (target)']),
        Spell('Universal Shield', 2, 'Yourself or an \\glossterm<ally> in \\rngmed range', """
            The target gains a +2 \\glossterm<magic bonus> to \\glossterm<resistances> against all damage.

            \\rankline
            \\rank<4> The bonus increases to +4.
            \\rank<6> The bonus increases to be equal to half your \\glossterm<power>.
            \\rank<8> The bonus increases to be equal to your \\glossterm<power>.
        """, tags=['Attune (target)']),
        Spell('Repulsion Field', 3, '\\glossterm<Enemies> that enter the area (see text)', """
            This spell creates a repulsive field in a \\areamed radius \\glossterm<zone> from your location.
            When an enemy makes physical contact with the spell's area for the first time, you make an attack vs. Mental against it.
            \\hit The target is unable to enter the spell's area with any part of its body.
            The rest of its movement in the current phase is cancelled.

            Creatures in the area at the time that the spell is cast are unaffected by the spell.

            \\rankline
            \\rank<5> The area increases to a \\arealarge radius.
            \\rank<7> The area increases to a \\areahuge radius.
        """, tags=['Sustain (minor)']),
        Spell('Energy Immunity', 5, 'Yourself', """
            Choose a subtype of \\glossterm<energy damage>: cold, electricity, or fire.
            You become immune to damage of the chosen type.
            Attacks that deal damage of multiple types still inflict damage normally unless you are immune to all types of damage dealt.

            \\rankline
            \\rank<7> You may attune to this spell any number of times, choosing a different subtype of energy damage each time.
        """, tags=['Attune (self)']),
        Spell('Retributive Shield', 6, 'Yourself or an \\glossterm<ally> in \\rngmed range', """
            The target gains a \\glossterm<magic bonus> equal to half your \\glossterm<power> to \\glossterm<resistances> against \\glossterm<physical> damage.
            Whenever an attack that deals \\glossterm<physical damage> fails to beat the target's \\glossterm<wound resistance>, the attacker takes that damage.
            If the attacker is beyond \\rngclose range of the target, this reflection fails.
            Any effect which increases this spell's range increases the range of this effect by the same amount.

            You can cast this spell as a \\glossterm<minor action>.

            \\rankline
            \\rank<8> The range of the spell and the range of the reflection increase to \\rngmed.
        """, tags=['Attune (target)']),
        Spell('Deflective Shield', 1, 'Yourself or an \\glossterm<ally> in \\rngmed range', """
            The target gains a +1 \\glossterm<magic bonus> to Armor defense and Reflex defense.

            You can cast this spell as a \\glossterm<minor action>.

            \\rankline
            \\rank<3> The bonus to Reflex defense increases to +2.
            \\rank<5> The bonus to Armor defense increases to +2.
            \\rank<7> The bonus to Reflex dfense increases to +3.
        """, tags=['Attune (target)']),
        Spell('Antilife Shell', 6, '\\glossterm<Enemies> that enter the area (see text)', """
            This spell creates a repulsive field in a \\areamed radius \\glossterm<zone> from your location.
            When an enemy makes physical contact with the spell's area for the first time, you make an attack vs. Mental against it.
            You gain a +10 bonus to \\glossterm<accuracy> against living creatures.
            \\hit The target is unable to enter the spell's area with any part of its body.
            The rest of its movement in the current phase is cancelled.

            Creatures in the area at the time that the spell is cast are unaffected by the spell.

            \\rankline
            \\rank<8> The area increases to a \\arealarge radius.
        """, tags=['Sustain (minor)']),
    ],
    rituals=[
        Spell('Endure Elements', 1, 'Yourself or an \\glossterm<ally> or unattended object within \\rngmed range', """
            The target suffers no harm from being in a hot or cold environment.
            It can exist comfortably in conditions between \minus50 and 140 degrees Fahrenheit.
            Its equipment, if any, is also protected.
            This does not protect the target from fire or cold damage.

            This ritual takes one minute to perform.
        """, tags=['Attune (ritual)']),
        Spell('Mystic Lock', 3, 'One large or smaller closable, nonmagical object within \\rngclose range, such as a door or box', """
            The target object becomes magically locked.
            It can be unlocked with a Devices check against a \\glossterm<difficulty rating> equal to 20 \\add your \\glossterm<power>.
            The \\glossterm<difficulty rating> to break it open forcibly increases by 10.

            You can freely pass your own \\ritual<mystic lock> as if the object were not locked.
            This effect lasts as long as you \\glossterm<attune> to it.
            If you use this ability multiple times, you can attune to it each time.

            This ritual takes one minute to perform.
        """, tags=['Attune (ritual)']),
        Spell('Resilient Lock', 5, 'One large or smaller closable, nonmagical object within \\rngclose range, such as a door or box', f"""
            This ritual functions like the \\ritual<mystic lock> ritual, except that the \\glossterm<difficulty rating> to unlock the target with a Devices check is instead equal to 30 + your \\glossterm<power>.
            In addition, the \\glossterm<difficulty rating> to break it open increases by 20 instead of by 10.
        """, tags=['Attune (ritual)']),
        Spell('Explosive Runes', 4, 'One Small or smaller unattended object with writing on it within \\rngclose range', """
            % TODO: clarify how to identify that this is Explosive Runes instead of bad handwriting
            The writing on the target is altered by the runes in subtle ways, making it more difficult to read.
            It becomes a \\glossterm<trap>.
            To read the writing, a creature must concentrate on reading it, which requires a standard action.
            If a creature reads the target, the target explodes.
            You make an attack vs. Reflex against everything within a \\areamed radius from the target.
            Each struck target takes energy \\glossterm<standard damage> from the explosion.

            After the target object explodes in this way, the ritual is \\glossterm<dismissed>.
            If the target is destroyed or rendered illegible, the ritual is dismissed without exploding.
            This ritual takes one hour to perform.
        """, tags=['Attune (ritual)']),
        Spell('Scryward', 3, None, """
            This ritual creates a ward against scrying in a \\arealarge radius \\glossterm<zone> centered on your location.
            All \\glossterm<Scrying> effects fail to function in the area.
            This effect is permanent.

            This ritual takes 24 hour to perform, and requires 8 action points from its participants.
        """, tags=['AP']),
        Spell('Private Sanctum', 5, None, """
            This ritual creates a ward against any external perception in a \\arealarge radius \\glossterm<zone> centered on your location.
            This effect is permanent.
            Everything in the area is completely imperceptible from outside the area.
            Anyone observing the area from outside sees only a dark, silent void, regardless of darkvision and similar abilities.
            In addition, all \\glossterm<Scrying> effects fail to function in the area.
            Creatures inside the area can see within the area and outside of it without any difficulty.

            This ritual takes 24 hours to perform, and requires 32 action points from its participants.
        """, tags=['AP']),
    ],
    category='buff, defense',
)
