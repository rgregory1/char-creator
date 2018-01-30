current_major_sorcery_grimoire = {'description': 'You possess brain burning, mind-controlling mental powers!',
 'identifier': 3,
 'notes': ['Mentalism - Mental Blast - This 15in range, 6D attack does Psyche damage. This attack cannot be used in melee.',
           'Mentailism - Mind Control (Recharge 2+) -  Roll 6D, 15in range. No damage, but the target immediately activates under your control and may take a free action and either a move, attack, charge, or special action.'],
 'power_name': 'Mentalism',
 'power_type': 'major',
 'stat_changes': {}}

current_major_sorcery_grimoire['power_name'] = 'Grimoire - ' + current_major_sorcery_grimoire['power_name']
for a in current_major_sorcery_grimoire['notes']:
    a = 'Grimoire - ' + a

print(current_major_sorcery_grimoire)




# quick_list = list(current_major_sorcery_grimoire['notes'])
# for a in quick_list:
#      a = 'Grimoire - ' + a
