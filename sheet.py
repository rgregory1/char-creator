from PIL import ImageFont, ImageDraw
from PIL import Image
import os
# im = Image.new('RGBA', (200,200), 'white')
# draw = ImageDraw.Draw(im)
# draw.text((20,150), 'Hello', fill='purple')
# #avegerFont = ImageFont.truetype(AMA.ttf, 15)
# fontsFolder = 'FONT_FOLDER'
# avengerFont = ImageFont.truetype("AMA.ttf", 32)
# draw.text((100,150), 'Howdy', fill='gray', font=avengerFont)
# im.save('text.png')

hero = {
'body_points': 7,
'hero_archetype_list': [{'archetype': 'Brawler',
                          'body_points': 7,
                          'description': 'You are a close in fighter who '
                                         'relies on sheer bravado,...',
                          'identifier': 1,
                          'maj-p': ['Scrapper'],
                          'min_p_num': 2,
                          'minor_p_list': ['Enhanced_Senses',
                                           'Fortune',
                                           'Iron_Will',
                                           'Melee_Specialist',
                                           'Regen',
                                           'Resistance',
                                           'Shield',
                                           'Super-Agility'],
                          'move': 7,
                          'power_name': 'Brawler',
                          'power_type': 'Standard',
                          'psych_points': 6}],
 'hero_backgrounds': ['Military', 'Public Safety'],
 'hero_major_power_list': [{'description': "You're a resourceful, tenacious "
                                           'close-in fighter.  You possess the '
                                           'following abilities: +1D on melee '
                                           'attack rolls, +1D on melee defence '
                                           'rolls, reduce an melee gang-up '
                                           'bonus foes gain against you by '
                                           '-1D, and Counterattack: You posses '
                                           'the Reflection minor power limited '
                                           'to melee attacks.',
                            'notes': ['Scrapper - reduce melee gang-up by -1D, '
                                      'and reflection minor power',
                                      'Anytime you successfully defend against '
                                      'a Body-damaging attack you can choose '
                                      'to make a Chance roll. On a 2+, your '
                                      'attack- er suffers 2 Body damage.'],
                            'power_name': 'Scrapper',
                            'power_type': 'major',
                            'stat_changes': {'melee_attack': 1,
                                             'melee_defence': 1}}],
 'hero_minor_power_list': [{'description': '+1 Re-roll on melee attack rolls, '
                                           '+1 Re-roll on melee defense rolls, '
                                           'and +2D on any checks to break '
                                           'objects or escape entangles.',
                            'identifier': 3,
                            'notes': ['Melee Speicialist - +2D on any checks '
                                      'to break objects or escape entangles.'],
                            'power_name': 'Melee Specialist',
                            'power_type': 'minor',
                            'stat_changes': {'melee_attack': 1,
                                             'melee_defence': 1}},
                           {'description': 'You possess a super-hard shield.',
                            'identifier': 6,
                            'notes': ['Shield - You can hurl it as a 3D, 5in '
                                      'ranged attack, and it always returns to '
                                      'your hand. Can also ricochet ranged '
                                      'attack to a second target within 5in of '
                                      'you. In this case you make a single '
                                      'attack goal roll, and your targets make '
                                      'separate, +1D defense goal rolls.'],
                            'power_name': 'Shield',
                            'power_type': 'minor',
                            'stat_changes': {'melee_attack_rr': 1,
                                             'melee_defence_rr': 1,
                                             'ranged_defence_rr': 1}}],
 'hero_name': 'Jim',
 'hero_notes': ['Scrapper - reduce melee gang-up by -1D, and reflection minor '
                'power',
                'Anytime you successfully defend against a Body-damaging '
                'attack you can choose to make a Chance roll. On a 2+, your '
                'attacker suffers 2 Body damage.',
                'Shield - You can hurl it as a 3D, 5in ranged attack, and it '
                'always returns to your hand. Can also ricochet ranged attack '
                'to a second target within 5in of you. In this case you make a '
                'single attack goal roll, and your targets make separate, +1D '
                'defense goal rolls.',
                'Melee Speicialist - +2D on any checks to break objects or '
                'escape entangles.'],
 'hero_type': 'Standard',
 'melee_attack': 6,
 'melee_attack_rr': 1,
 'melee_defence': 6,
 'melee_defence_rr': 1,
 'move': 7,
 'psych_points': 6,
 'psyche_attack_rr': 0,
 'psyche_defence': 4,
 'psyche_defence_rr': 0,
 'ranged_attack_rr': 0,
 'ranged_defence': 4,
 'ranged_defence_rr': 1}

im = Image.open("blank_sheet.png")
draw = ImageDraw.Draw(im)
avengerFont = ImageFont.truetype("AMA.ttf", 36)
draw.text((395,319), hero['hero_name'], fill='grey', font=avengerFont)


if len(hero['hero_archetype_list']) == 1:
    draw.text((500,400), hero['hero_archetype_list'][0]['archetype'], fill='grey', font=avengerFont)
if len(hero['hero_archetype_list']) == 2:
    draw.text((500,400), hero['hero_archetype_list'][1]['archetype'], fill='grey', font=avengerFont)
if len(hero['hero_archetype_list']) == 3:
    draw.text((500,400), hero['hero_archetype_list'][1]['archetype'], fill='grey', font=avengerFont)
    draw.text((500,400), hero['hero_archetype_list'][2]['archetype'], fill='grey', font=avengerFont)
draw.text((200,1600), hero['hero_notes'][1], fill='grey', font=avengerFont)




im.save('text.png')
