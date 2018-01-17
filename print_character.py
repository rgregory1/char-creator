import pprint

def print_out_hero(hero):
    print('final results \n \n \n \n')
    print('Name:  ' + hero['hero_name'] + '\n')
    print('Archetype: ' + hero['hero_arch'])
    print('Move:  ' + str(hero['move']).rjust(5))
    print( '\n')
    print('Body Points:  ' + str(hero['body_points'] * '[ ] ') + '[KO]')
    print('Psyche Points:  ' + str(hero['psych_points'] * '[ ] ') + '[KO] \n')
# melee stat line
    if hero['melee_attack_rr'] == 0 and hero['melee_defence_rr'] == 0:
        print('Melee Att: ' + str(hero['melee_attack']) + ' \t Melee Def: ' + str(hero['melee_defence']))
    elif hero['melee_attack_rr'] == 0 and hero['melee_defence_rr'] != 0:
        print('Melee Att: ' + str(hero['melee_attack']) + ' \t Melee Def: ' + str(hero['melee_defence']) + '[' + str(hero['melee_defence_rr']) + ']')
    else:
        print('Melee Att: ' + str(hero['melee_attack']) + '[' + str(hero['melee_attack_rr']) + ']' + ' \t Melee Def: ' + str(hero['melee_defence']) + '[' + str(hero['melee_defence_rr']) + ']')
# ranged stat line
    if 'ranged_attack' not in hero:
        if hero['ranged_defence_rr'] == 0:
            print('Ranged Att: ' + str(0) + ' \t Ranged Def: ' + str(hero['ranged_defence']))
        else:
            print('Ranged Att: ' + str(0) + ' \t Ranged Def: ' + str(hero['ranged_defence']) + '[' + str(hero['ranged_defence_rr']) + ']')
    else:
        if hero['ranged_attack_rr'] == 0 and hero['ranged_defence_rr'] == 0:
            print('Ranged Att: ' + str(hero['ranged_attack']) + ' \t Ranged Def: ' + str(hero['ranged_defence']))
        elif hero['ranged_attack_rr'] == 0 and hero['ranged_defence_rr'] != 0:
            print('Ranged Att: ' + str(hero['ranged_attack']) + ' \t Ranged Def: ' + str(hero['ranged_defence']) + '[' + str(hero['ranged_defence_rr']) + ']')
        else:
            print('Ranged Att: ' + str(hero['ranged_attack']) + '[' + str(hero['ranged_attack_rr']) + ']' + ' \t Ranged Def: ' + str(hero['ranged_defence']) + '[' + str(hero['ranged_defence_rr']) + ']')

# pysche stat line
    if 'psyche_attack' not in hero:
        if hero['psyche_defence_rr'] == 0:
            print('Psyche Att: ' + str(0) + ' \t Psyche Def: ' + str(hero['psyche_defence']))
        else:
            print('Psyche Att: ' + str(0) + ' \t Psyche Def: ' + str(hero['psyche_defence']) + '[' + str(hero['psyche_defence_rr']) + ']')
    else:
        if hero['psyche_attack_rr'] == 0 and hero['psyche_defence_rr'] == 0:
            print('Psyche Att: ' + str(hero['psyche_attack']) + ' \t Psyche Def: ' + str(hero['psyche_defence']))
        elif hero['psyche_attack_rr'] == 0 and hero['psyche_defence_rr'] != 0:
            print('Psyche Att: ' + str(hero['psyche_attack']) + ' \t Psyche Def: ' + str(hero['psyche_defence']) + '[' + str(hero['psyche_defence_rr']) + ']')
        else:
            print('Psyche Att: ' + str(hero['psyche_attack']) + '[' + str(hero['psyche_attack_rr']) + ']' + ' \t Psyche Def: ' + str(hero['psyche_defence']) + '[' + str(hero['psyche_defence_rr']) + ']')
# print major power
    print('\n')
    print('Major Power: ' + hero['hero_majp'] + '\n')

    print('Notes: \n')
    print(hero['hero_notes'])
