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
        print('Melee Att: ' + str(hero['melee_attack']) + '[' + str(hero['melee_defence_rr']) + ']' + ' \t Melee Def: ' + str(hero['melee_defence']) + '[' + str(hero['melee_defence_rr']) + ']')
# ranged stat line
    if 'ranged_attack' not in hero:
        print('Ranged Att: ' + str(0) + ' \t Ranged Def: ' + str(hero['ranged_defence']))
