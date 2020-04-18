from rise.latex.mystic_sphere import MysticSphere
from rise.latex.spell import Spell
from rise.latex.effects import Effects



# Primary: buff
# Secondary: utility
# None: damage, debuff
umbramancy=MysticSphere(
    name="Umbramancy",
    short_description="Manipulate shadows and darkness to conceal allies and inhibit foes",
    cantrips=[],
    lists=['Arcane', 'Pact'],
    spells=[
        Spell('Banish Light', 3, 'One \\areamed radius \\glossterm<zone> within \\rngmed range', """
            All light within the area is suppressed.
            Light within or passing through the area is snuffed out.
            Any object or effect which blocks light also blocks this spell's effect.
            Darkvision and similar abilities which do not require light still function within the area.

            \\rankline
            \\rank<5> The area increases to a \\arealarge radius \\glossterm<zone>.
            \\rank<7> The area increases to a \\areaext radius \\glossterm<zone>.
        """, tags=['Sensation', 'Sustain (minor)']),
        Spell('Darklantern', 3, 'One Small or smaller unattended object within \\rngclose range', """
            This spell suppresses light in a \\areamed radius \\glossterm<emanation> from the target.
            Light within or passing through the area is dimmed to be no brighter than shadowy illumination.
            Any object or effect which blocks light also blocks this spell's effect.

            \\rankline
            \\rank<5> The area increases to a \\arealarge radius \\glossterm<emanation>.
            \\rank<7> The area increases to a \\areahuge radius \\glossterm<emanation>.
        """, tags=['Attune (self)', 'Sensation']),
        Spell('Darkvision', 1, 'Yourself or an \\glossterm<ally> within \\rngmed range', """
            The target gains \\glossterm<darkvision> with a 50 foot radius.

            \\rankline
            \\rank<3> The radius increases to 100 feet.
            \\rank<5> The radius increases to 150 feet.
            \\rank<7> The radius increases to 200 feet.
        """, tags=['Attune (target)']),
        Spell('Clutch of Darkness', 1, 'One creature within \\rngmed range', """
            Make an attack vs. Fortitude against the target.
            You gain a +2 bonus to \\glossterm<accuracy> with the attack if the target is not in bright light.

            \\hit The target takes cold \\glossterm<standard damage>.

            \\rankline
            \\rank<3> The damage increases to \\glossterm<standard damage> +1d.
            \\rank<5> The damage increases to \\glossterm<standard damage> +2d.
            \\rank<7> The damage increases to \\glossterm<standard damage> +3d.
        """, tags=[]),
        Spell('Shadow Mantle', 1, 'Yourself or an \\glossterm<ally> within \\rngmed range', """
            The target's physical form becomes blurred and shifts in and out of existence.
            This is not a mere trick of the light, but an alteration of reality to make its existence more ambiguous.
            The target gains a +1 \\glossterm<magic bonus> to Armor defense and the Stealth skill.

            \\rankline
            \\rank<3> The defense bonus applies to all defenses.
            \\rank<5> The bonus to Armor defense and Stealth increases to +2.
            \\rank<7> The bonus to all defenses increases to +2.
        """, tags=['Attune (target)']),
        Spell('Conceal Trail', 1, 'Yourself and up to five \\glossterm<allies>', """
            At the end of each round, the footprints, scent, and other tracks left by each target during that round are magically concealed.
            This increases the \\glossterm<difficulty rating> to follow the trail by 10, but does not prevent creatures from seeing or smelling each target normally in combat.
            At the end of each round, if any target is outside of \\rnglong range from you, the effect is broken for that target and its trail is revealed.

            \\rankline
            \\rank<3> The \\glossterm<difficulty rating> increase increases to 15.
            \\rank<5> The \\glossterm<difficulty rating> increase increases to 20.
            \\rank<7> The \\glossterm<difficulty rating> increase increases to 25.
        """, tags=['Attune (self)']),
        Spell('Dark Shroud', 1, 'One creature within \\rngmed range', """
            Make an attack vs. Mental against the target.
            You gain a +2 bonus to \\glossterm<accuracy> with the attack if the target is not in bright light.
            \\hit As a \\glossterm<condition>, the target takes a -2 penalty to \\glossterm<accuracy> and visual Awareness checks.
            \\crit The target is \\glossterm<blinded> as a \\glossterm<condition>.

            \\rankline
            \\rank<3> You gain a +1 bonus to \\glossterm<accuracy> with the attack.
            \\rank<5> The accuracy bonus increases to +2.
            \\rank<7> The accuracy bonus increases to +3.
        """, tags=['Sensation', 'Visual']),
        Spell('Blinding Shroud', 6, 'One creature within \\rngmed range', """
            Make an attack vs. Mental against the target.
            You gain a +2 bonus to \\glossterm<accuracy> with the attack if the target is not in bright light.
            \\hit The target is \\glossterm<blinded> as a \\glossterm<condition>.

            \\rankline
            \\rank<8> You gain a +1 bonus to \\glossterm<accuracy> with the attack.
        """, tags=['Sensation', 'Visual']),
        Spell('Hidden Blade', 3, 'Yourself or one \\glossterm<ally> within \\rngmed range', """
            The target's weapons become shrouded in darkness, making them virtually impossible to see.
            Its next melee \\glossterm<strike> is treated as if it came from an invisible creature.
            This effect ends at the end of the next round if the target has not made a strike by that time.

            The first attack from an invisible creature generally causes a creature to be \\glossterm<unaware> of the attack, imposing a -5 penalty to Armor and Reflex defenses.
            % TODO: wording
            After a creature has been hit by a strike from an invisible creature in this way, it is generally aware of the danger.
            As a result, it is usually \\glossterm<defenseless> instead of \\glossterm<unaware>, which only imposes a -2 penalty to Armor defense.

            This effect provides no offensive benefit against creatures immune to \\glossterm<Visual> abilities.

            % TODO: this doesn't really sense narratively
            \\rankline
            \\rank<5> The target also gains a +1 bonus to \\glossterm<accuracy> with the strike.
            \\rank<7> The accuracy bonus increases to +2.
        """, tags=['Sensation', 'Visual']),
        Spell('Conceal', 1, 'Yourself or an \\glossterm<ally> within \\rngmed range', """
            The target gains a +3 \\glossterm<magic bonus> to the Stealth skill.

            \\rankline
            \\rank<3> The bonus increases to +4.
            \\rank<5> The bonus increases to +5.
            \\rank<7> The bonus increases to +6.
        """, tags=['Attune (target)', 'Sensation']),
        Spell('Shadowstep', 1, 'Yourself or up to one Medium or smaller \\glossterm<ally> within \\rngmed range', """
            The target teleports into an unoccupied destination within range.
            If the target is in bright light, this spell is \\glossterm<miscast>.

            \\rankline
            \\rank<3> The range increases to \\rnglong.
            \\rank<5> The range increases to \\rngext.
            \\rank<7> The range increases to 2,000 feet.
        """, tags=[]),
        Spell('Walk the Shadow Roads', 4, 'Yourself', """
            You can teleport horizontally between shadows instead of moving normally.
            Teleporting a given distance costs movement equal to half that distance.
            If your \\glossterm<line of effect> to your destination is blocked, or if this teleportation would somehow place you inside a solid object, your teleportation is cancelled and you remain where you are that phase.
            Bright light blocks line of effect for this spell, so you are unable to teleport into or past areas of bright light.
            You must be able to move to teleport in this way, so effects like being \\glossterm<immobilized> prevent this movement.

            \\rankline
            \\rank<6> You can also teleport vertically or diagonally in addition to horizontally.
            \\rank<8> You can teleport in this way even if you are unable to move, such as if you are \\glossterm<immobilized> or \\glossterm<paralyzed>.
        """, tags=['Attune (self)']),
        Spell('Bind Shadow', 1, 'One creature within \\rngmed range standing on the ground', """
            You pin the target's shadow to the ground, impairing its movement.
            If the target does not have a shadow and is in bright light, this spell is \\glossterm<miscast>.
            Make an attack vs. Mental against the target.
            \\hit As a \\glossterm<condition>, the target is \\glossterm<slowed> and unable to fly or otherwise leave the ground under its own power.
            This does not prevent it from being carried or forcibly removed from the ground.
            \\crit As a \\glossterm<condition>, the target is \\glossterm<immobilized>.

            \\rankline
            \\rank<3> You gain a +1 bonus to \\glossterm<accuracy> with the attack.
            \\rank<5> The accuracy bonus increases to +2.
            \\rank<7> The accuracy bonus increases to +3.
        """, tags=[]),
        Spell('Shadow Dance', 3, 'One creature within \\rngmed range standing on the ground', """
            You command the target's shadow to move differently from the target, interfering with its movement.
            If the target does not have a shadow and is in bright light, this spell is \\glossterm<miscast>.
            Make an attack vs. Mental against the target.
            \\hit The target is \\glossterm<disoriented> as a \\glossterm<condition>.
            \\crit As a \\glossterm<condition>, you can force the target to move as you choose during each \\glossterm<movement phase>.
            You can cause it to use any of its normal movement modes, but you cannot force it to make skill checks or use abilities with a cost, such as sprinting.
            If the target tries to move on its own outside of the \\glossterm<movement phase>, it is \\glossterm<disoriented>.
            The target can otherwise act normally, and this does not prohibit it from taking other actions during the movement phase, such as drawing or sheathing weapons.

            \\rankline
            \\rank<5> You gain a +1 bonus to \\glossterm<accuracy> with the attack.
            \\rank<7> The accuracy bonus increases to +2.
        """, tags=[]),
        Spell('Shadowform', 4, 'Yourself', """
            You collapse to the ground, taking the appearance and shape of a shadow.
            This has a number of effects, as described below.
            \\begin<itemize>
                \\item You are nearly flat, allowing you to pass under doors and through other narrow passages.
                    Your horizontal dimensions are unchanged, and you cannot enter spaces that are more narrow than you can normally fit through.
                \\item You can freely move through space occupied by other creatures, and other creatures can freely move through your space.
                \\item You gain a \\glossterm<climb speed> equal to your \\glossterm<base speed>, and you can climb without using any hands.
                \\item You are always treated as being \\glossterm<prone>.
                \\item You gain a +4 \\glossterm<magic bonus> to the Stealth skill.
            \\end<itemize>

            While you are in bright light, this effect is \\glossterm<suppressed>, and you return to your normal size and shape.
            If doing so is impossible, such as if you are in a space too small to contain your body, you gain a \\glossterm<vital wound> and this effect persists for the rest of the round.
            This form offers you no special immunity to damage, as creatures can simply attack the shadow.

            \\rankline
            \\rank<6> You can maintain the form in bright light for a full round before it is suppressed.
            \\rank<8> You can maintain the form in bright light for up to five minutes in a row before it is suppressed.
        """, tags=['Attune (self)']),
        Spell('Wall of Darkness', 1, None, """
            You create a wall of darkness in a 20 ft.\\ high, \\areamed line within \\rngmed range.
            If you create the wall within a space too small to hold it, it fills as much of the space as possible, allowing you to completely block off small tunnels.
            The wall is visible as a solid block of darkness that blocks sight.
            Creatures with the \\glossterm<darkvision> ability can see through the wall normally.
            It does not inhibit the passage of objects or creatures.

            \\rankline
            \\rank<3> The area increases to a \\arealarge line.
            \\rank<5> The range increases to \\rnglong.
            \\rank<7> The area increases to a \\areahuge line.
        """, tags=['Sensation', 'Sustain (minor)']),
    ],
    rituals=[
        Spell('Sunlight Ward', 3, 'Yourself or one \\glossterm<ally> within \\rngmed range', """
            The target is never considered to be in natural sunlight.
            This does not impair its vision, but protects it if it would otherwise suffer negative consequences for being in natural sunlight.

            This ritual takes one hour to perform.
        """, tags=['Attune (target)']),
    ],
    category='buff, defense',
)
