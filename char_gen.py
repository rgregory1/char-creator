import pprint
import json
import logging
logging.basicConfig(level=logging.DEBUG)
# logging.disable(logging.CRITICAL)
from print_character import *
import time
import copy

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
  'hero_minor_power_list': [],
  'hero_backgrounds': []
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

def add_power_perfix(prefix, power_dict):
    """takes in a dictionary and adds prefixes for archery and sorcery """
    for a in power_dict:
        power_dict[a]['power_name'] = prefix + ' - ' + power_dict[a]['power_name']
        for b in power_dict[a]['notes']:
            power_dict[a]['notes'][b] = prefix + ' - ' + power_dict[a]['notes'][b]

def prefix_additional_powers(current_power, prefix):
    """ adds addional power prefixes to powers after they have been selected """
    current_power['power_name'] = prefix + ' - ' + current_power['power_name']
    for i in range(len(current_power['notes'])):
        current_power['notes'][i] = prefix + ' - ' + current_power['notes'][i]
    return current_power

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
    if arch['maj-p'] is True:
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

        #check to see if Sorcery is the main power, if so, choose a sorcery major power for the grimoire
        if current_major_power['power_name'] == 'Sorcery':
            #create list of major powers to choose from
            sorcery_maj_power_dict = copy.deepcopy(maj_power_dict)
            del sorcery_maj_power_dict['Sorcery']

            # create a chooser for sorcery stuff
            print('\nYou may now choose a Major Power for your Grimoire from the following list: \n' )
            current_major_sorcery_grimoire, current_minor_power_dict = choose_power(sorcery_maj_power_dict, 'Grimoire')

            current_major_sorcery_grimoire['power_name'] = 'Grimoire - ' + current_major_sorcery_grimoire['power_name']
            for i in range(len(current_major_sorcery_grimoire['notes'])):
                current_major_sorcery_grimoire['notes'][i] = 'Grimoire - ' + current_major_sorcery_grimoire['notes'][i]

            pprint.pprint(current_major_sorcery_grimoire)

            hero['hero_major_power_list'].append(current_major_sorcery_grimoire)

            # Add notes from Major Power
            hero['hero_notes'].extend(current_major_sorcery_grimoire['notes'])


        # begin minor power Choices  starting with Archery and Sorcery------------------------------------------------

        if 'add_minor_powers_number' in current_major_power:
            # create a list of minor powers for trick arrows
            if current_major_power['power_name'] == 'Archery':
                current_minor_power_dict = {}
                for x in min_power_dict:
                    for y in current_major_power['additional_minor_powers']:
                        if x == y:
                            current_minor_power_dict[x] = min_power_dict[x].copy()
            if current_major_power['power_name'] == 'Sorcery':
                current_minor_power_dict = copy.deepcopy(min_power_dict)
                del current_minor_power_dict['Magic_Artifact']
                del current_minor_power_dict['Shield']

            # Set number of loops
            loops = current_major_power['add_minor_powers_number']

            # Add additional minor power to hero dict with each pass
            while loops > 0:
                print(5 * '\n')
                print('\nYou may now choose ', str(loops), 'minor powers from the following list to add to your ', current_major_power['additional_power_prefix'], ': \n' )
                current_minor_power, current_minor_power_dict = choose_power(current_minor_power_dict, current_major_power['additional_power_prefix'])
                # Add prefix to power
                current_minor_power = prefix_additional_powers(current_minor_power, current_major_power['additional_power_prefix'])

                # Add notes from Major Power
                hero['hero_notes'].extend(current_minor_power['notes'])
                # add to list of minor powers
                hero['hero_minor_power_list'].append(current_minor_power)
                # remove boosts from chooses once one is choosen (or two for supers)

                loops -= 1


# begin regular minor power choices---------------------------------------------

    if hero['hero_type'] == 'Super':
        print('As a character with the Archetype of Super, you have the option of exchanging two of your Archetyp Minor Powers for a Minor Power from any Archetype.')
        extra_choice = input('Would you like to do this?  y/n \n')
        if extra_choice == 'y':
            current_minor_power, current_minor_power_dict = choose_power(min_power_dict, 'Bonus Power')
            # adjust stats based on major power choosen
            hero = hero_stat_adjust(hero,current_minor_power['stat_changes'])
            # Add notes from Major Power
            hero['hero_notes'].extend(current_minor_power['notes'])
            # add to list of minor powers
            hero['hero_minor_power_list'].insert(0, current_minor_power)
            hero['super_archetype_bonus'] = 'yes'

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
        if 'super_archetype_bonus' not in hero:
            loops = loops + 2
        boost_loops = 2
    while loops > 0:
        print(5 * '\n')
        print('\nYou may now choose ', str(loops), ' minor powers from the following list: \n' )
        current_minor_power, current_minor_power_dict = choose_power(current_minor_power_dict, 'Minor Power')
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

# choose a couple of backgrounds for your character
loops = 2
backgrounds = ['Alien/Dimensional', 'Arcane', 'Art', 'Athletics', 'Blue Collar', 'Business', 'Criminal', 'Espionage', 'Exploration', 'High Society', 'Journalist', 'Medicine', 'Military', 'Monarch', 'Performance', 'Public', 'Safety', 'Science', 'Social Science']
while loops > 0:
    print(5 * '\n')
    print('\nYou may now choose ', str(loops), ' backgrounds from the following list: \n' )
    for i,v in enumerate(backgrounds):
        print(i, ' - ', backgrounds[i])
    background_choice = int(input('Choose the number of the background you would like: \n'))
    current_background = backgrounds.pop(background_choice)
    # Add notes from Major Power
    hero['hero_backgrounds'].append(current_background)
    loops -= 1







print(5 * '\n')
logging.debug(pprint.pformat(hero))
