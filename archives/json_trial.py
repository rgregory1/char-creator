import json

import pprint



# Create list of minor powers


print(20 * '\n')
big_dict = {}


# crate dictionary of dictionaries with
# for power in arch_list:
#     prekey = power['power_name']
#     key = prekey.replace(" ", "_")
#     big_dict[key] = power

# create dictionary of dictionaries of archetype data -------------------------

with open('data/archetype_data.json') as f:
    data = json.load(f)

# for arch in data:
#     key = arch['archetype']
#     big_dict[key] = arch

for archs in data:
    for power in data[archs]['minor_p_list']:
        new_list = data[archs]['minor_p_list']
        # print(big_dict[archs]['minor_p_list'])
        # print(new_list)
    del data[archs]['minor_p_list']
    newest_list = []
    for old_power in new_list:
        new_power = old_power.replace(" ", "_")
        newest_list.append(new_power)
    data[archs]['minor_p_list'] = newest_list


# pprint.pprint(big_dict)

# # crate dictionary of dictionaries with ---------------------------------------
# for power in minp_list_of:
#     prekey = power['power_name']
#     print(prekey)
#     key = prekey.replace(" ", "_")
#     print(key)
#     big_dict[key] = power

# # # crate dictionary of dictionaries with ---------------------------------------
# for power in majp_list:
#     prekey = power['power_name']
#     print(prekey)
#     key = prekey.replace(" ", "_")
#     print(key)
#     big_dict[key] = power

with open('new_data.json', 'w') as f:
    json.dump(data, f, indent=2)

# grab info from JSON file and assign it to a variable -----------------------
# with open('new_data.json') as f:
#     data = json.load(f)

# pprint.pprint(data)
