trial_dict = {
  "Blaster": {
    "archetype": "Blaster",
    "power_type": "archetype",
    "summary": "You project destructive energies...",
    "move": 6,
    "body_points": 6,
    "psych_points": 6,
    "maj-p": [
      "Archery",
      "Power Blasts"
    ],
    "min_p_num": 2,
    "minor_p_list": [
      "Damage_Field",
      "Explosion",
      "Flight",
      "Force-Field",
      "Iron_Will",
      "Resistance",
      "Reaction",
      "Super-Strength"
    ]
  },
  "Brawler": {
    "archetype": "Brawler",
    "power_type": "archetype",
    "summary": "You are a close in fighter who relies on sheer bravado,...",
    "move": 7,
    "body_points": 7,
    "psych_points": 6,
    "maj-p": [
      "Scrapper"
    ],
    "min_p_num": 2,
    "minor_p_list": [
      "Enhanced_Senses",
      "Fortune",
      "Iron_Will",
      "Melee_Specialist",
      "Regen",
      "Resistance",
      "Shield",
      "Super-Agility"
    ]
  },
  "Brick": {
    "archetype": "Brick",
    "power_type": "archetype",
    "summary": "You are the bruising, super-strong fighter on your team...",
    "move": 5,
    "body_points": 8,
    "psych_points": 6,
    "maj-p": [
      "Super-Strength"
    ],
    "min_p_num": 2,
    "minor_p_list": [
      "Armor",
      "Burrowing",
      "Density_Increase",
      "Leaping",
      "Magic_Artifact",
      "Massive",
      "Rage",
      "Resistance"
    ]
  }
}

single = trial_dict.pop('Brawler')


print(trial_dict)

print(20 * '\n')

print(single)
