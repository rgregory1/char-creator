# List of minor powers

Armor = {
  'power_name': 'Armor',
  'power_type': 'minor',
  'description': 'You possess damage resistance from super-thick skin or some kind of worn armor.',
  'stat_changes': {},
  'notes': 'Armor - Ignore the first lost Body damage from each attack. No knockback unless foe possess Super-Strength. \n'
}

Burrowing = {
  'power_name': 'Burrowing',
  'power_type': 'minor',
  'description': 'You can travel underground at your normal Move rate.',
  'stat_changes': {},
  'notes': 'Burrowing - It costs a free action to submerge and start burrowing, or stop burrowing and re-surface, but once you’ve surfaced, you cannot burrow again until next turn. You can burrow through or under any intervening terrain as if it were normal ground. You cannot resurface within a solid object. Instead of attacking when you surface, you can create fissures and tremors. Use your special action to create these tremors; any enemies within 5in of you must make a TN3 check or be knocked down. \n'
}

Damage_Field = {
  'power_name': 'Damage Field',
  'power_type': 'minor',
  'description': 'Spend a free action to activate or deactivate this power. You surround yourself with a deadly field. Anyone touching you (successful attacks or knockbacks) suffers a 4D[1] Body damage attack. No knockback. Resolve this after resolving any successful attack action.',
  'stat_changes': {},
  'notes': 'Damage Field - Spend a free action to activate or deactivate this power. You surround yourself with a deadly field. Anyone touching you (successful attacks or knockbacks) suffers a 4D[1] Body damage attack. No knockback. Resolve this after resolving any successful attack action. \n'
}

Density_Increase = {
  'power_name': 'Density Increase',
  'power_type': 'minor',
  'description': 'With a thought you become super-dense.',
  'stat_changes': {},
  'notes': 'Density Increase - At the start of your turn, before any movement, spend a free action to activate. While active, you can charge at your base Move value only. While super dense you gain +1 Re-roll on melee attack checks and +1D to melee and ranged defense checks against Body damaging attacks. You’re also immune to all knockback. \n'
}
Enhance_Minor = {
  'power_name': 'Enhance (Minor)',
  'power_type': 'minor',
  'description': 'You can increase the capabilities of characters within 5” of you.',
  'stat_changes': {},
  'notes': 'Enhance (Minor) - Special action 5D check. Every two goals you score grant your target, within 5in, +1 Re-roll to his re-roll pool. You can split Re-rolls between multiple targets within 5in of you. \n'
}

Enhanced_Senses = {
  'power_name' : 'Enhanced Senses',
  'power_type': 'minor',
  'description' :  'You possess heightened physical and/or psionic senses that allow you to ignore environmental conditions like darkness.',
  'stat_changes': {},
  'notes': 'Enhanced Senses - +2D on perception checks to spot hidden, invisible, or obscured characters, team gains +1 Re-roll on initiative checks \n'
}

Explosion = {
  'power_name': 'Explosion',
  'power_type': 'minor',
  'description': 'This counts as a Radius Attack. Make a 4D[1] attack check. Anyone within 5in of you must roll to resist the attack. Anyone within the next 5in is also affected but resists with +1 Re-roll. You reform at the end of your next turn. Until then you can not be targeted by Physical attacks.',
  'stat_changes': {},
  'notes': 'Explosion - Radius Attack. 4D[1] first 5in, 4D[2] next 5in. You reform at the end of your next turn. Until then you can not be targeted by Physical attacks. \n'
}

Entangle = {
  'power_name': 'Entangle',
  'power_type': 'minor',
  'description': 'description here',
  'stat_changes': {},
  'notes': 'Entangle - 10in Range, 5D Body-based entangle attack that does no damage'
}

Flight = {
  'power_name': 'Flight',
  'power_type': 'minor',
  'description': 'You can fly up to 20in per turn, ignoring any grounded models or obstacles in your path. You may choose to land on an object or piece of terrain, or hover in place. When you do hover you float 15in above the tabletop.',
  'stat_changes': {},
  'notes': 'Flight - 20in per turn, ignoring any grounded models or obstacles. May choose to land on an object or piece of terrain, or hover in place. When you do hover you float 15in above the tabletop. \n'
}

Force_Field = {
  'power_name': 'Force-Field',
  'power_type': 'minor',
  'description': 'You wield protective energies. Decide when you acquire this power whether it shields against Body or Psyche damage. Your Force-Field grants you a separate 4D defense goal roll against incoming attacks.',
  'stat_changes': {},
  'notes': 'Force-Field - Decide when you acquire this power whether it shields against Body or Psyche damage. Your Force-Field grants you a separate 4D defense goal roll against incoming attacks. If an attack gets through, you must make a second defense goal roll against the full incoming attack. You may also protect additional characters within 10in of you. Use a special action and make a 4D check and note your goals - 2 goals = 1 character 3 goals = 2 characters 4 goals = 3 characters. Decide which characters to protect before making your check. Protected characters must remain within 10in of you to enjoy your Force-Fields benefits. Maximum Protection - You can push your Force-Field to its limits, rolling 6D instead of 4D for its protection, but succeed or fail, the power shuts down after this one enhanced use. You must decide to push your field prior to your foes attack goal roll. Recharge 2+ \n'
}

Fortune = {
  'power_name': 'Fortune',
  'power_type': 'minor',
  'description': 'You’re darn lucky or capable of manipulating probabilities in your favor when it counts the most.',
  'stat_changes': {},
  'notes': 'Fortune - Recharge 2+, Gain +1D[1] on a defense roll against any attack. You can decide to use this ability after you’ve made your initial defense roll!  \n'
}

Gadgets = {
  'power_name': 'Gadgets',
  'power_type': 'minor',
  'description': 'You have an array of gadgets and devices in your utility belt or bag of tricks that you can use to give you an advantage against your foes.',
  'stat_changes': {},
  'notes': 'Gadgets - Make a Chance Roll at the start of your turn. The number of goals rolled is the number of Re-rolls added to your Re-roll pool. \n Gadgets - 3D, 10in Body-damage ranged attack. \n'
}

Iron_Will = {
  'power_name': 'Iron Will',
  'power_type': 'minor',
  'description': 'You can resist the effects of mental powers better than most! Gain +1D to your defense checks against any Psyche based mental attack. Also gain +1D on all KO checks.',
  'stat_changes': {
    'psyche_defence': 1
  },
  'notes': 'Iron Will - You can resist the effects of mental powers better than most! Gain +1D to your defense checks against any Psyche based mental attack. Also gain +1D on all KO checks. \n'
}

Leaping = {
  'power_name': 'Leaping',
  'power_type': 'minor',
  'description': 'Your super-strong legs propel you high into the air with pro- digious leaps!',
  'stat_changes': {},
  'notes': 'Leaping - 4D action check. Declare where you want to land. You can leap up to 10in + goals scored high and 20in + goals scored long. \n'
}

Magic_Artifact = {
  'power_name': 'Magic Artifact',
  'power_type': 'minor',
  'description': 'You wield a powerful artifact that acts as both a melee weapon and a ranged weapon, as well as granting you other powers. All of this great stuff comes with a price, however.',
  'stat_changes': {
    'melee_attack_rr': 1,
    'ranged_attack_rr': 1,
  },
  'notes': 'Magic Artifact - 15in ranged attack. You can also employ its energies for the Flight and Force-Field minor powers. See rules for additional. Recharge 2+ (3+ if you pushed your Force-Field) \n Magic Artifact Flight - 20in per turn, ignoring any grounded models or obstacles. May choose to land on an object or piece of terrain, or hover in place. When you do hover you float 15in above the tabletop. \n Magic Artifact Force-Field - Decide when you acquire this power whether it shields against Body or Psyche damage. Your Force-Field grants you a separate 4D defense goal roll against incoming attacks. If an attack gets through, you must make a second defense goal roll against the full incoming attack. '
}

Massive = {
  'power_name': 'Massive',
  'power_type': 'minor',
  'description': 'You are up to twice the size of a normal model!',
  'stat_changes': {
    'move': 2,
    'body_points' : 2,
  },
  'notes': 'Massive - +1 Re-roll on charge attacks, Foes gain +1 Re-roll on Body-based melee and ranged attacks against you. \n'
}

Melee_Specialist = {
  'power_name': 'Melee Specialist',
  'power_type': 'minor',
  'description': '+1 Re-roll on melee attack rolls, +1 Re-roll on melee defense rolls, and +2D on any checks to break objects or escape entangles.',
  'stat_changes': {
    'melee_attack': 1,
    'melee_defence': 1
  },
  'notes': 'Melee Speicialist - +2D on any checks to break objects or escape entangles \n'
}

Obscurement = {
  'power_name': 'Obscurement',
  'power_type': 'minor',
  'description': 'Anytime a foe tries to detect you, he must make a TN3 perception check. If failed you get +1 re-roll to Body Damage attacks, +1 re-roll to Body Damage defence, +1 to hide checks',
  'stat_changes': {},
  'notes': 'Obscurement - Anytime a foe tries to detect you, he must make a TN3 perception check. If failed you get +1 re-roll to Body Damage attacks, +1 re-roll to Body Damage defence, +1 to hide checks, Recharge 1+ \n'
}

Power_Blasts_Minor = {
  'power_name': 'Power Blasts (Minor)',
  'power_type': 'minor',
  'description': 'You shoot blasts of power (concussive force, cosmic energy, electricity, etc.) from your eyes or hands.',
  'stat_changes': {
    'ranged_attack': 1,
    'ranged_attack_rr': 1,
  },
  'notes': 'Power Blasts (Minor) - You can make 15in ranged attacks that inflict Body Damage \n'
}

Rapport = {
  'power_name': 'Rapport',
  'power_type': 'minor',
  'description': 'Choose another character on your team; you possess a special mental link with that character. This link grants you both additional strength. ',
  'stat_changes': {},
  'notes': 'Rapport - Choose a team mate, so long as both characters are not KO’ed, they can share +1D between them for any defense checks. As soon as once charter uses the +1D, it is spent until the beginning of the next round. \n'
}

Rage = {
  'power_name': 'Rage',
  'power_type': 'minor',
  'description': 'The madder you get, the tougher you get!',
  'stat_changes': {},
  'notes': 'Rage - Make a 1+ Chance roll each time you suffer Body or Psyche damage. On a success you gain a cumulative +1D to melee attack and Psyche defense rolls. This bonus maxes out at +2D. Your Rage bonuses last until the end of the battle. \n'
}

Reflection = {
  'power_name': 'Reflection',
  'power_type': 'minor',
  'description': 'Reflection - You can sometimes turn Body-damaging attacks back on your attacker! Anytime you successfully defend against a Body-damaging attack you can choose to make a Chance roll. On a 2+, your attacker suffers 2 Body damage.',
  'stat_changes': {},
  'notes': 'Anytime you successfully defend against a Body-damaging attack you can choose to make a Chance roll. On a 2+, your attacker suffers 2 Body damage. \n'
}

Regen = {
  'power_name': 'Regen',
  'power_type': 'minor',
  'description': 'You possess the potential to heal yourself! This could be from a natural mutant power, injected nanites, cosmic energy, or whatever.',
  'stat_changes': {},
  'notes': 'Regen - At the beginning of any turn you begin at less than full Body or Psyche, make a Chance roll. You regain 1 + goals scored lost damage. You can spread this healing between both of your damage tracks. If you lose the last box in either damage track, but make your KO check, your healing could slow down. Make a Chance roll for Regen, but only the goals on the throw count as your healing. This power stops working for the rest of the battle if you fail a KO check. \n'
}

Resistance = {
  'power_name': 'Resistance',
  'power_type': 'minor',
  'description': 'You are super-tough! Gain +1D on all defense checks from Body damaging attacks and +1D on KO checks.',
  'stat_changes': {
    'melee_defence': 1,
    'ranged_defence': 1
  },
  'notes': 'Resistance - +1D on KO checks \n'
}

Savant = {
  'power_name': 'Savant',
  'power_type': 'minor',
  'description': 'You’re brilliant and you enjoy +1 Re-roll on any checks during a battle that involve non-combat situations.',
  'stat_changes': {},
  'notes': 'Savant - You enjoy +1 Re-roll on any checks during a battle that involve non-combat situations. Including initiative, movement, objective, perception, and summoning checks, but not KO checks. At the beginning of each battle, after all models have been placed, but before the first round begins, you may take a non-charge Move action. \n'
}

Shield = {
  'power_name' : 'Shield',
  'power_type': 'minor',
  'description' :  'You possess a super-hard shield.',
  'stat_changes': {
    'melee_attack_rr' : 1,
    'melee_defence_rr' : 1,
    'ranged_defence_rr' : 1,
  },
  'notes': 'Shield - You can hurl it as a 3D, 5in ranged attack, and it always returns to your hand. Can also ricochet ranged attack to a second target within 5in of you. In this case you make a single attack goal roll, and your targets make separate, +1D defense goal rolls. \n'
}


Sonic_Blasts = {
  'power_name': 'Sonic Blasts',
  'power_type': 'minor',
  'description': 'You possess sonic powers you can direct at foes with maddening force! This is a 4D[1], 15in Psyche-damage ranged attack.',
  'stat_changes': {
    'pysche_attack': 0,
    'pysche_attack_rr': 1
  },
  'notes': 'Sonic Blasts - 15in Psyche-Damage ranged attack \n'
}

Stun = {
  'power_name': 'Stun',
  'power_type': 'minor',
  'description': "Body or Psyche based attack. Decide which when you acquire this power. Stun is a 5D, 15in ranged attack that inflicts no damage, but rather impairs a target's actions for a certain period of time.",
  'stat_changes': {},
  'notes': 'Stun - Body or Psyche based attack. 5D, 15in ranged attack that inflicts stun. \n'
}

Super_Agility = {
  'power_name': 'Super Agility',
  'power_type': 'minor',
  'description': "You gain +2in to your move and +1 Re-roll on all defense checks against Body damaging attacks, and any check to avoid being knocked down. You can move up, hang from, and walk along vertical surfaces as if they were normal ground. You can also spend a Move action to move between structures or other vertical terrain pieces within 15in of each other.",
  'stat_changes': {
    'move': 2,
    'melee_defence_rr': 1,
    'ranged_defence_rr': 1
  },
  'notes': 'Super-Agility - +1D on Knock down checks, move along verticle surfaces, and spend a Move action to move 15in \n'
}

Super_Strength_Minor = {
  'power_name': 'Super-Strength',
  'power_type': 'minor',
  'description': 'You possess enhanced strength greater than any normal human.',
  'stat_changes': {
    'melee_attack': 1
  },
  'notes': '+1D to entangle escapes, grappling checks, and on breaking objects, +1D on Jumping and Leaping checks, inflict knockback at 2in per body damage \n'
}

Telekinesis = {
  'power_name': 'Telekinesis',
  'power_type': 'minor',
  'description': 'You can move objects with your mind, grapple foes at range, and levitate yourself and others!',
  'stat_changes': {},
  'notes': 'Telekinesis - As a special or combat action lift, carry, and wield objects up to 15in away as if you had minor Super-Strength--this includes using an object as a super-club! Target must also be within 15in range. \n Telekinesis - Use a combat action to grapple a foe up to 15” away as if you possessed minor Super-Strength. \n Telekinesis - On your move action levitate yourself and one friendly character within 15” of you up to 6”, and up to 15” in height. Your friend must remain within your 15” sphere of TK in uence. You and your levitated friend must land at the end of your move. \n'
}

Teleport = {
  'power_name': 'Teleport',
  'power_type': 'minor',
  'description': 'You can move from one point to another instantaneously!',
  'stat_changes': {},
  'notes': 'Teleport - Teleporting costs a move action, and when you do so make a goal roll. You move up to 10in + 5in per goal scored. You can move to any point on the board whether you can see it or not. If you teleport out of melee combat, your foe still gets a free attack on you. If you are knocked back from a successful hit, measure your teleport distance from the point where your knockback ends. \n'
}

Generic = {
  'power_name': 'name',
  'power_type': 'minor',
  'description': 'description here',
  'stat_changes': {},
  'notes': ' \n'
}
