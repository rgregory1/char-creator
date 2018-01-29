import pprint
import json
import logging
logging.basicConfig(level=logging.DEBUG)
# logging.disable(logging.CRITICAL)
from print_character import *
import time


# grab info from JSON file and assign it to a variable -----------------------

with open('data/minor_power_data.json') as f:
    min_power_dict = json.load(f)

with open('data/major_power_data.json') as f:
    maj_power_dict = json.load(f)

with open('data/archetype_data.json') as f:
    arch_dict = json.load(f)

# initiate lists and dicts for later use ---------------------------------------


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

# Initiate hero dict
hero = {
  'melee_attack': 4,
  'melee_attack_rr': 0,
  'melee_defence': 4,
  'melee_defence_rr': 0,
  'ranged_attack_rr': 0,
  'ranged_defence': 4,
  'ranged_defence_rr': 0,
  'psyche_attack_rr': 0,
  'psyche_defence': 4,
  'psyche_defence_rr': 0,
  'hero_notes': [],
  'hero_type': 'Standard',
  'hero_archetype_list': [],
  'hero_major_power_list': [],
  'hero_minor_power_list': []
}

new_arch_dict = {}

# begin all functions ----------------------------------------------------------

def assign_base_points(hero_info, new):
    """ assigns base points from archetype to main dictionary """
    hero_info['body_points'] = new['body_points']
    hero_info['psych_points'] = new['psych_points']
    hero_info['move'] = new['move']
    return(hero_info)

def assign_max_points(hero_info, new):
    """ assigns max points from archetype to main dictionary """
    hero_info['body_points'] = max(new['body_points'], hero_info['body_points'])
    hero_info['psych_points'] = max(new['psych_points'], hero_info['psych_points'])
    hero_info['move'] = max(new['move'], hero_info['move'])
    return(hero_info)

def choose_power(current_dict, power_type):
    """ enter a dictionary and create a list to choose from, return chosen dictionary """
    print(power_type + ' Choices \t \t Description \n')
    for n,a in enumerate(current_dict):
        current_dict[a]['identifier'] = n
        print(current_dict[a]['identifier'], ' - ', current_dict[a]['power_name'], ' : \t', current_dict[a]['description'])
        print()

    while True:
        #check to see if number typed is valid
        choice_range = len(current_dict)
        choice_num = int(input('Type the number of the ' + str(power_type) +' that you would like: \n'))
        if choice_num < choice_range:
            break
        else:
            print('Your typed a number not allowed, please choose again! \n \n')
    for b in current_dict:
        if choice_num == current_dict[b]['identifier']:
            # set hero archetype/power to one chosen from list
            final = current_dict.pop(b)
            break
    return(final, current_dict)

def hero_stat_adjust(base,adjusts):
    """retrun hero dict with adjusted stats"""
    for key in adjusts:
        base[key] = base.get(key, 4) + adjusts[key]
    return base

# begin building hero ----------------------------------------------------------

# Pick a name for the hero and add it to the hero dictionary
print(10 * '\n')
chosen_name = input('Choose the name of your hero: ')
hero['hero_name'] = chosen_name
print(10 * '\n')

# Display a list of archetypes to choose from ----------------------------------
current_archetype, arch_dict = choose_power(arch_dict, 'archetype')
hero['hero_archetype_list'].append(current_archetype)

# hero['hero_type'] = hero['main_archetype']['power_type']
hero['hero_type'] = hero['hero_archetype_list'][0]['power_type']

# if chosen archetype is standard, set stats
if hero['hero_archetype_list'][0]['power_type'] == 'Standard':
    hero = assign_base_points(hero, hero['hero_archetype_list'][0])
# if archetype is alt power level, start to do special stuff
elif hero['hero_archetype_list'][0]['power_type'] == 'Super' or hero['hero_archetype_list'][0]['power_type'] == 'Powerhouse':
    # creat new dict without alt power levels in it
    for d in arch_dict:
        if arch_dict[d]['power_type'] == 'Standard':
            new_arch_dict[d] = arch_dict[d].copy()
    loops = hero['hero_archetype_list'][0]['major_power_number']
    while loops > 0:
        # print new list to choose from
        # check to see how many archetypes are present, if only one, choose first arch
        if len(hero['hero_archetype_list']) == 1:
            print('\n \n')
            print('Due to your intitial Archetype choice of ' + str(hero['hero_archetype_list'][0]['archetype']) + ' you are allowed to choose ' + str(loops) + ' additional archetype/s:')
            current_archetype, new_arch_dict = choose_power(new_arch_dict, 'archetype')
            hero['hero_archetype_list'].append(current_archetype)
            hero = assign_base_points(hero, hero['hero_archetype_list'][1])
        else:
            # if first arch chose, choos third arch
            print('\n \n')
            print('Round two - Due to your intitial Archetype choice of ' + str(hero['hero_archetype_list'][0]['archetype']) + ' you are allowed to choose ' + str(loops) + ' additional archetype/s:')
            current_archetype, new_arch_dict = choose_power(new_arch_dict, 'archetype')
            hero['hero_archetype_list'].append(current_archetype)
            hero = assign_max_points(hero, hero['hero_archetype_list'][2])
        loops -= 1

print('\n finished with archetypes \n')
time.sleep(1)



# begin Major Power choice and adjustments -------------------------------------
# Create archetype dict that we can destroy
mutable_archetype_list = [x for x in hero['hero_archetype_list']]
# check for powerhouse and ajust for double archetype powers, first if = super power level
if len(mutable_archetype_list) == 2:
    del mutable_archetype_list[0]
# second if equals powerhouse
if len(mutable_archetype_list) == 3:
    print('Due to your Powerhouse Archetype, you will go through the Major Power and Minor Power choice process twice:')
    del mutable_archetype_list[0]


for arch in mutable_archetype_list:
    # check if only one major power available, if so set it to current
    if len(arch['maj-p']) == 1:
        print('\n')
        print('Your Major Power is ' + str(arch['maj-p'][0]) + '\n \n')
        majp_choice = arch['maj-p'][0]
    else:
        # if choice of major power exists, print list to choose from and a set choice to current
        for n, a in enumerate(arch['maj-p']):
            print(n, ' - ', arch['maj-p'][n])
        majp_choice_num = input('Type the number of the Major Power you Choose: \n')
        majp_choice = arch['maj-p'][int(majp_choice_num)]

    for majorpower in maj_power_dict:
        if majp_choice == maj_power_dict[majorpower]['power_name']:
            current_major_power = maj_power_dict[majorpower].copy()
            break
    # print()
    # print(current_major_power)
    # print()
    # assign major power choice to the hero dict
    hero['hero_major_power_list'].insert(0, current_major_power)
    # adjust stats based on major power choosen
    hero = hero_stat_adjust(hero,current_major_power['stat_changes'])
    # Add notes from Major Power
    hero['hero_notes'].extend(current_major_power['notes'])

    # print('current major power is:')
    # print(arch)
    # begin minor power Choices ------------------------------------------------


    current_minor_power_dict = {}
    for x in min_power_dict:
        for y in arch['minor_p_list']:
            if x == y:
                current_minor_power_dict[x] = min_power_dict[x].copy()
            elif min_power_dict[x]['power_type'] == 'boost':
                current_minor_power_dict[x] = min_power_dict[x].copy()

    # remove current minor powers from list for powerhouse archetype second group of minor power Choices
    if hero['hero_minor_power_list'] is not []:
        for x in hero['hero_minor_power_list']:
            for y in current_minor_power_dict.copy():
                if x['power_name'] == y:
                    del current_minor_power_dict[y]
    # set up number of looks for minor powers and boosts
    boost_loops = 1
    loops = arch['min_p_num']
    # add two minor powers to super archetypes powers, and two boost options
    if hero['hero_type'] == 'Super':
        loops = loops + 2
        boost_loops = 2
    while loops > 0:
        print(5 * '\n')
        print('\nYou may now choose ', str(loops), 'minor powers from the following list: \n' )
        current_minor_power, current_minor_power_dict = choose_power(current_minor_power_dict, 'minor power')
        # adjust stats based on major power choosen
        hero = hero_stat_adjust(hero,current_minor_power['stat_changes'])
        # Add notes from Major Power
        hero['hero_notes'].extend(current_minor_power['notes'])
        # add to list of minor powers
        hero['hero_minor_power_list'].insert(0, current_minor_power)
        # remove boosts from chooses once one is choosen (or two for supers)
        if current_minor_power['power_type'] == 'boost':
            boost_loops -= 1
            if boost_loops == 0:
                for x in current_minor_power_dict.copy():
                    if current_minor_power_dict[x]['power_type'] == 'boost':
                        del current_minor_power_dict[x]
        loops -= 1



# start checking for archery or sorcery and build in those optinos
# use the code below, it's pretty brillian if I don't say so myself :)







print(5 * '\n')
logging.debug(pprint.pformat(hero))













# -----------------------Massive section to see if there are additional powers attached to major power



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

    # print('this_minor_p_choice', this_minor_p_choice) # test to see if correct

    # print('minp_list_of', minp_list_of)
    pprint.pprint(hero)
    # Pull out adjustments from minor power dict
    active_minp_adjust = grab_minp_stat_changes(minp_list_of, this_minor_p_choice)

    print('active minor power adjust is', active_minp_adjust)

    # Adjust stats acording to major power
    hero = hero_stat_adjust(hero, active_minp_adjust)

    hero['hero_notes'] = hero['hero_notes'] + this_minor_p_choice['notes']

    minor_power_cycles -= 1

# end of new code

pprint.pprint(hero)


print_out_hero(hero)
