import pprint
from super_data import *

Stats = {'melee_attack' : 4, 'melee_attack_rr' : 0, 'melee_defence' : 4, 'melee_defence_rr' : 0, 'ranged_attack' : 0, 'ranged_attack_rr' : 0, 'ranged_defence' : 4, 'ranged_defence_rr' : 0, 'psyche_attack' : 0, 'psyche_attack_rr' : 0, 'psyche_defence' : 4, 'psyche_defence_rr' : 0}

minor_power_options = []

active_arch = {}



# create list of archetype dictionaries
arch_list = [arch_blaster, arch_brawler, arch_brick]


# List of major powers


Archery = {'power_name': 'Archery',
           'power_type' : 'major',
           'description' : 'you can use once per turn...',
           'additional_minorp' : ['Entangle', 'Leaping', 'Melee Specialist', 'Obscurement', 'Sonic Blasts', 'Stun', 'Super-Agility'],
           'additional_minorp_prefix' : 'Trick Arrow',
           'add_p_num' : 4,
           'stat_changes': {'ranged_attack': 1, 'ranged_attack_rr': 1},
           'notes': 'Archery - 15in range, body damage  \n'}

Power_Blasts = { 'power_name' : 'Power Blasts',
                 'power_type' : 'major',
                 'description' : 'You shoot blasts of power (concussive force, cosmic energy, electricity, etc.) from your eyes or hands.  You can make 30in ranged attacks at +2D[1].  Your blasts are physical in nature and inflict Body Damage',
                 'stat_changes' : {'ranged_attack' : 2, 'ranged_attack_rr': 1},
                 'notes': 'Power Blasts - 30in range, body damage \n'}

Super_Strength = {'power_name' : 'Super-Strength',
                  'power_type': 'major',
                  'description': 'description here',
                  'stat_changes': {'melee_attack': 2, 'ranged_attack': 4},
                  'notes': 'Hurling - 10in range, body damage, +2D entangle escapes, grappling checks and breaking objects, 4in knockback, +2D on jumping and leaping  \n'}

Scrapper = { 'power_name' : 'Scrapper',
             'power_type' : 'major',
             'description' : "You're a resourceful, tenacious close-in fighter.  You possess the following abilities: +1D on melee attack rolls, +1D on melee defence rolls, reduce an melee gang-up bonus foes gain against you by -1D, and Counterattack: You posses the Reflection minor power limited to melee attacks.",
             'stat_changes': {'melee_attack': 1, 'melee_defence': 1},
             'notes': 'reduce melee gang-up by -1D, and reflection minor power \n Anytime you successfully defend against a Body-damaging attack you can choose to make a Chance roll. On a 2+, your attack- er suffers 2 Body damage. \n'}


# Create list of major powers
majp_list = [Archery, Power_Blasts, Scrapper, Super_Strength]

# List of minor powers

Damage_Field = {'power_name' : 'Damage Field', 'power_type': 'minor', 'description': 'Spend a free action to activate or deactivate this power. You surround yourself with a deadly field. Anyone touching you (successful attacks or knockbacks) suffers a 4D[1] Body damage attack. No knockback. Resolve this after resolving any successful attack action.', 'stat_changes': {}, 'notes': 'Damage Field - Spend a free action to activate or deactivate this power. You surround yourself with a deadly field. Anyone touching you (successful attacks or knockbacks) suffers a 4D[1] Body damage attack. No knockback. Resolve this after resolving any successful attack action. \n'}

Explosion = {'power_name' : 'Explosion', 'power_type': 'minor', 'description': 'This counts as a Radius Attack. Make a 4D[1] attack check. Anyone within 5in of you must roll to resist the attack. Anyone within the next 5in is also affected but resists with +1 Re-roll. You reform at the end of your next turn. Until then you can not be targeted by Physical attacks.', 'stat_changes': {}, 'notes': 'Explosion - Radius Attack. 4D[1] first 5in, 4D[2] next 5in. You reform at the end of your next turn. Until then you can not be targeted by Physical attacks. \n'}

Entangle = {'power_name' : 'Entangle', 'power_type': 'minor', 'description': 'description here', 'stat_changes': {}, 'notes': 'Entangle - 10in Range, 5D Body-based entangle attack that does no damage'}

Flight = {'power_name' : 'Flight', 'power_type': 'minor', 'description': 'You can fly up to 20in per turn, ignoring any grounded models or obstacles in your path. You may choose to land on an object or piece of terrain, or hover in place. When you do hover you float 15in above the tabletop.', 'stat_changes': {}, 'notes': 'Flight - 20in per turn, ignoring any grounded models or obstacles. May choose to land on an object or piece of terrain, or hover in place. When you do hover you float 15in above the tabletop. \n'}

Force_Field = {'power_name' : 'Force-Field', 'power_type': 'minor', 'description': 'You wield protective energies. Decide when you acquire this power whether it shields against Body or Psyche damage. Your Force-Field grants you a separate 4D defense goal roll against incoming attacks.', 'stat_changes': {}, 'notes': 'Force-Field - Decide when you acquire this power whether it shields against Body or Psyche damage. Your Force-Field grants you a separate 4D defense goal roll against incoming attacks. If an attack gets through, you must make a second defense goal roll against the full incoming attack. You may also protect additional characters within 10in of you. Use a special action and make a 4D check and note your goals - 2 goals = 1 character 3 goals = 2 characters 4 goals = 3 characters. Decide which characters to protect before making your check. Protected characters must remain within 10in of you to enjoy your Force-Fields benefits. Maximum Protection - You can push your Force-Field to its limits, rolling 6D instead of 4D for its protection, but succeed or fail, the power shuts down after this one enhanced use. You must decide to push your field prior to your foes attack goal roll. Recharge 2+ \n'}

Iron_Will = {'power_name' : 'Iron Will', 'power_type': 'minor', 'description': 'You can resist the effects of mental powers better than most! Gain +1D to your defense checks against any Psyche based mental attack. Also gain +1D on all KO checks.', 'stat_changes': {'psyche_defence': 1}, 'notes': 'Iron Will - You can resist the effects of mental powers better than most! Gain +1D to your defense checks against any Psyche based mental attack. Also gain +1D on all KO checks. \n'}

Leaping = {'power_name' : 'Leaping', 'power_type': 'minor', 'description': 'description here', 'stat_changes': {}, 'notes': '4D action check. Declare where you want to land. You can leap up to 10in + goals scored high and 20in + goals scored long. \n'}

Melee_Specialist = {'power_name' : 'Melee Specialist', 'power_type': 'minor', 'description': '+1 Re-roll on melee attack rolls, +1 Re-roll on melee defense rolls, and +2D on any checks to break objects or escape entangles.', 'stat_changes': {'melee_attack': 1, 'melee_defence': 1}, 'notes': 'Melee Speicialist - +2D on any checks to break objects or escape entangles \n'}

Obscurement = {'power_name' : 'Obscurement', 'power_type': 'minor', 'description': 'Anytime a foe tries to detect you, he must make a TN3 perception check. If failed you get +1 re-roll to Body Damage attacks, +1 re-roll to Body Damage defence, +1 to hide checks', 'stat_changes': {}, 'notes': 'Obscurement - Anytime a foe tries to detect you, he must make a TN3 perception check. If failed you get +1 re-roll to Body Damage attacks, +1 re-roll to Body Damage defence, +1 to hide checks, Recharge 1+ \n'}

Reflection = {'power_name' : 'Reflection', 'power_type': 'minor', 'description': 'Reflection - You can sometimes turn Body-damaging attacks back on your attacker! Anytime you successfully defend against a Body-damaging attack you can choose to make a Chance roll. On a 2+, your attacker suffers 2 Body damage.', 'stat_changes': {}, 'notes': 'Anytime you successfully defend against a Body-damaging attack you can choose to make a Chance roll. On a 2+, your attacker suffers 2 Body damage. \n'}

Resistance = {'power_name' : 'Resistance', 'power_type': 'minor', 'description': 'You are super-tough! Gain +1D on all defense checks from Body damaging attacks and +1D on KO checks.', 'stat_changes': {'melee_defence' : 1, 'ranged_defence' : 1}, 'notes': 'Resistance - +1D on KO checks \n'}

Sonic_Blasts = {'power_name' : 'Sonic Blasts', 'power_type': 'minor', 'description': 'You possess sonic powers you can direct at foes with maddening force! This is a 4D[1], 15in Psyche-damage ranged attack.', 'stat_changes': {'pysche_attack': 0, 'pysche_attack_rr': 1}, 'notes': 'Sonic Blasts - 15in Psyche-Damage ranged attack \n'}

Stun = {'power_name' : 'Stun', 'power_type': 'minor', 'description': "Body or Psyche based attack. Decide which when you acquire this power. Stun is a 5D, 15in ranged attack that inflicts no damage, but rather impairs a target's actions for a certain period of time.", 'stat_changes': {}, 'notes': 'Stun - Body or Psyche based attack. 5D, 15in ranged attack that inflicts stun. \n'}

Super_Agility = {'power_name' : 'Super Agility', 'power_type': 'minor', 'description': "You gain +2in to your move and +1 Re-roll on all defense checks against Body damaging attacks, and any check to avoid being knocked down. You can move up, hang from, and walk along vertical surfaces as if they were normal ground. You can also spend a Move action to move between structures or other vertical terrain pieces within 15in of each other.", 'stat_changes': {'move': 2, 'melee_defence_rr': 1, 'ranged_defence_rr': 1}, 'notes': 'Super-Agility - +1D on Knock down checks, move along verticle surfaces, and spend a Move action to move 15in \n'}

Super_Strength = {'power_name' : 'Super-Strength', 'power_type': 'minor', 'description': 'You possess enhanced strength greater than any normal human.', 'stat_changes': {'melee_attack' : 1}, 'notes': '+1D to entangle escapes, grappling checks, and on breaking objects, +1D on Jumping and Leaping checks, inflict knockback at 2in per body damage'}






Generic = {'power_name' : 'name', 'power_type': 'minor', 'description': 'description here', 'stat_changes': {}, 'notes': ''}

# Create list of minor powers

minp_list_of = [Entangle, Obscurement, Sonic_Blasts, Stun, Super_Agility, Leaping, Melee_Specialist, Damage_Field, Explosion, Flight, Force_Field, Iron_Will, Resistance, Reflection, Super_Strength]

# Initiate hero dict
hero = {'melee_attack' : 4, 'melee_attack_rr' : 0, 'melee_defence' : 4, 'melee_defence_rr' : 0, 'ranged_attack_rr' : 0, 'ranged_defence' : 4, 'ranged_defence_rr' : 0, 'psyche_attack_rr' : 0, 'psyche_defence' : 4, 'psyche_defence_rr' : 0, 'hero_notes': ''}


# Adjust hero dict with stats from powers
def hero_stat_adjust(base,adjusts):
    for key in adjusts:
        base[key] = base.get(key, 4) + adjusts[key]
    return base


# take state changes out of major power dictionary
def grab_stat_changes(base, choice):
    adjustments = {}
    for b in base:
        if choice == b['power_name']:
            adjustments = b['stat_changes'].copy()
    return adjustments


# take state changes out of minor power dictionary
def grab_minp_stat_changes(base, choice):
    adjustments = {}
    for b in base:
        if choice['power_name'] == b['power_name']:
            adjustments = b['stat_changes'].copy()
    return adjustments

# Pick a name for the hero and add it to the hero dictionary
chosen_name = input('Choose the name of your hero: ')
hero['hero_name'] = chosen_name

# Display a list of archetypes to choose from
print()
for n,a in enumerate(arch_list):
    print(n, ' - ', a['archetype'], ':', a['summary'])
    print()
arch_choice_num = input('Type the number of the archetype that you would like to build: \n')

# print(arch_list[int(arch_choice_num)]['archetype'])


arch_choice = arch_list[int(arch_choice_num)]['archetype']

# Add archetype choice to hero dictionary
hero['hero_arch'] = arch_choice

for a in arch_list:
    if arch_choice == a['archetype']:
        active_arch = a.copy()


hero['body_pionts'] = active_arch['body_points']
hero['psych_pionts'] = active_arch['psych_points']
hero['move'] = active_arch['move']


# Choose major power
print()
if len(active_arch['maj-p']) == 1:
    print('Your Major Power is ' + str(active_arch['maj-p'][0]))
    majp_choice = active_arch['maj-p'][0]
else:
    for n, a in enumerate(active_arch['maj-p']):
        print(n, ' - ', active_arch['maj-p'][n])
    majp_choice_num = input('Type the number of the Major Power you Choose: \n')
    majp_choice = active_arch['maj-p'][int(majp_choice_num)]

hero['hero_majp'] = majp_choice
# print(hero)

# Pull out adjustments from major power dict
active_majp_adjust = grab_stat_changes(majp_list, majp_choice)

# print('active majp adjust is ', active_majp_adjust)

# Adjust stats acording to major power
hero = hero_stat_adjust(hero, active_majp_adjust)

for c in majp_list:
    if majp_choice == c['power_name']:
        active_majp = c.copy()

# print(active_majp)


# Add notes from Major Power
hero['hero_notes'] = hero['hero_notes'] + active_majp['notes']

# -----------------------Massive section to see if there are additional powers attached to major power

def minor_power_chooser(arch, min_p):
    minor_power_options = []
    for x in arch['minor_p_list']:     # create list of minor power options
        for y in min_p:
            if x == y['power_name']:
                minor_power_options.append(y)
    return minor_power_options


def choose_minor_power_from_list(options, cycles):
    active_minor_power = ''
    minor_p_choice = ''
    minor_p_choice_num = ''
    print('Minor Power Choices \t \t Description \n')
    for n,z in enumerate(options):
        print(n, ' - ', z['power_name'], '\t', z['description'], '\n')  # print powers to choose from

    print('You have', cycles, 'minor power choices remaining.')  # show number of powers remaining
    print()

    minor_p_choice_num = input('Please type the name of the minor power you would like: \n')  # choose power

    minor_p_choice = options[int(minor_p_choice_num)]['power_name']

    for c in options:
        if minor_p_choice == c['power_name']:    # attach power dict to active power
            active_minor_power = c.copy()

    for d in options:
        if minor_p_choice == d['power_name']:   # remove power from list for future choices
            options.remove(d)
    return active_minor_power, options




# check for Archery Major power, if so, choose four additional minor powers



def additional_minor_power_chooser(arch, min_p):
    minor_power_options = []
    for x in arch['additional_minorp']:     # create list of minor power options
        for y in min_p:
            if x == y['power_name']:
                y['power_name'] = arch['additional_minorp_prefix'] + ' - ' + y['power_name']
                y['notes'] = arch['additional_minorp_prefix'] + ' - ' + y['notes']
                minor_power_options.append(y)
    return minor_power_options


if 'additional_minorp' in active_majp:
    add_minor_p_cycles = active_majp['add_p_num']
    print('The ' + active_majp['power_name'] + ' Major Power has ' + str(add_minor_p_cycles) + ' additional minor powers')
    list_of_additional_minorp_options = additional_minor_power_chooser(active_majp, minp_list_of)
    while add_minor_p_cycles > 0:
        this_minor_p_choice, list_of_minorp_options = choose_minor_power_from_list(list_of_additional_minorp_options,
                                                                                   add_minor_p_cycles)

        print('this_minor_p_choice', this_minor_p_choice)  # test to see if correct

        print('minp_list_of', minp_list_of)

        # Pull out adjustments from minor power dict
        active_minp_adjust = grab_minp_stat_changes(minp_list_of, this_minor_p_choice)

        print('active minor power adjust is', active_minp_adjust)

        # Adjust stats acording to major power
        hero = hero_stat_adjust(hero, active_minp_adjust)

        hero['hero_notes'] = hero['hero_notes'] + this_minor_p_choice['notes']

        add_minor_p_cycles -= 1
    # pprint.pprint(list_of_additional_minorp_options)


# ------------------------- choose minor powers from a list ----------------------------




minor_power_cycles = active_arch['min_p_num']
list_of_minorp_options = minor_power_chooser(active_arch, minp_list_of)
while minor_power_cycles > 0:
    this_minor_p_choice, list_of_minorp_options = choose_minor_power_from_list(list_of_minorp_options,minor_power_cycles)

    print('this_minor_p_choice', this_minor_p_choice) # test to see if correct

    print('minp_list_of', minp_list_of)

    # Pull out adjustments from minor power dict
    active_minp_adjust = grab_minp_stat_changes(minp_list_of, this_minor_p_choice)

    print('active minor power adjust is', active_minp_adjust)

    # Adjust stats acording to major power
    hero = hero_stat_adjust(hero, active_minp_adjust)

    hero['hero_notes'] = hero['hero_notes'] + this_minor_p_choice['notes']

    minor_power_cycles -= 1

# end of new code

pprint.pprint(hero)
