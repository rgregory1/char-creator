import pprint
from super_data import *
from minor_power_data import *

Stats = {
  'melee_attack': 4,
  'melee_attack_rr': 0,
  'melee_defence': 4,
  'melee_defence_rr': 0,
  'ranged_attack': 0,
  'ranged_attack_rr': 0,
  'ranged_defence': 4,
  'ranged_defence_rr': 0,
  'psyche_attack': 0,
  'psyche_attack_rr': 0,
  'psyche_defence': 4,
  'psyche_defence_rr': 0
}

minor_power_options = []

active_arch = {}

# create list of archetype dictionaries
arch_list = [arch_blaster, arch_brawler, arch_brick, arch_mastermind, arch_mentalist]


# List of major powers


Archery = {
  'power_name': 'Archery',
  'power_type': 'major',
  'description': 'you can use once per turn...',
  'additional_minorp': ['Entangle', 'Leaping', 'Melee Specialist', 'Obscurement', 'Sonic Blasts', 'Stun', 'Super-Agility'],
  'additional_minorp_prefix': 'Trick Arrow',
  'add_p_num': 4,
  'stat_changes': {
    'ranged_attack': 1,
    'ranged_attack_rr': 1
  },
  'notes': 'Archery (Major)- 15in range, body damage  \n'
}

Enhance = {
  'power_name': 'Enhance',
  'power_type': 'major',
  'description': 'You can increase the capabilities of characters within 10in of you.',
  'stat_changes': {},
  'notes': 'Enhance - Use a free action and make a 6D check. Every two goals you score grant your target, within 10in, +1 Re-roll to his Re-roll pool. You can split Re-rolls between multiple targets within 10” of you.  \n'
}

Healing = {
  'power_name': 'Healing',
  'power_type': 'major',
  'description': 'You can heal yourself, or a char- acter in melee contact with you.',
  'stat_changes': {},
  'notes': 'Healing - Roll 6D. Every two goals you score restores one lost box of either Body or Psyche damage, or you can mix the boxes restored. You cannot restore more damage boxes than your target began with.  \n'
}

Mentalism = {
  'power_name': 'Mentalism',
  'power_type': 'major',
  'description': 'You possess brain burning, mind-controlling mental powers!',
  'stat_changes': {},
  'notes': 'Mentalism - Mental Blast - This 15in range, 6D attack does Psyche damage. This attack cannot be used in melee.  \n Mentailism - Mind Control (Recharge 2+) -  Roll 6D, 15” range. No damage, but the target immediately activates under your control and may take a free action and either a move, attack, charge, or special action. \n'
}

Power_Blasts = {
  'power_name': 'Power Blasts',
  'power_type': 'major',
  'description': 'You shoot blasts of power (concussive force, cosmic energy, electricity, etc.) from your eyes or hands.  You can make 30in ranged attacks at +2D[1].  Your blasts are physical in nature and inflict Body Damage',
  'stat_changes': {
    'ranged_attack': 2,
    'ranged_attack_rr': 1
  },
  'notes': 'Power Blasts (Major)- 30in range, body damage \n'
}

Super_Strength = {
  'power_name': 'Super-Strength',
  'power_type': 'major',
  'description': 'description here',
  'stat_changes': {
    'melee_attack': 2,
    'ranged_attack': 4
  },
  'notes': 'Super-Strength (Major) - Hurling - 10in range, body damage, +2D entangle escapes, grappling checks and breaking objects, 4in knockback, +2D on jumping and leaping  \n'
}

Scrapper = {
  'power_name': 'Scrapper',
  'power_type': 'major',
  'description': "You're a resourceful, tenacious close-in fighter.  You possess the following abilities: +1D on melee attack rolls, +1D on melee defence rolls, reduce an melee gang-up bonus foes gain against you by -1D, and Counterattack: You posses the Reflection minor power limited to melee attacks.",
  'stat_changes': {
    'melee_attack': 1,
    'melee_defence': 1
  },
  'notes': 'reduce melee gang-up by -1D, and reflection minor power \n Anytime you successfully defend against a Body-damaging attack you can choose to make a Chance roll. On a 2+, your attack- er suffers 2 Body damage. \n'
}

# Create list of major powers
majp_list = [Archery, Enhance, Healing, Mentalism, Power_Blasts, Scrapper, Super_Strength]

# Create list of minor powers

minp_list_of = [Armor, Burrowing, Damage_Field, Density_Increase, Enhance_Minor, Enhanced_Senses, Entangle, Explosion, Flight, Force_Field, Gadgets, Iron_Will, Leaping, Magic_Artifact, Massive, Melee_Specialist, Obscurement, Power_Blasts_Minor, Rage, Rapport, Resistance, Reflection, Savant, Shield, Sonic_Blasts, Stun, Super_Agility, Super_Strength_Minor]

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

while True:
    choice_range = len(arch_list)
    arch_choice_num = int(input('Type the number of the archetype that you would like to build: \n'))
    if arch_choice_num <= choice_range:
        break
    else:
        print('Your typed a number not allowed, please choose again! \n \n')
# print(arch_list[int(arch_choice_num)]['archetype'])


arch_choice = arch_list[int(arch_choice_num)]['archetype']

# Add archetype choice to hero dictionary
hero['hero_arch'] = arch_choice

for a in arch_list:
    if arch_choice == a['archetype']:
        active_arch = a.copy()


hero['body_points'] = active_arch['body_points']
hero['psych_points'] = active_arch['psych_points']
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

    minor_p_choice_num = input('Please type the number of the minor power you would like: \n')  # choose power

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
