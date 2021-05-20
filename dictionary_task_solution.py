"""
Задачка действительно оказалась несложной =(
"""

inv = {'gold': 10, 'axe': 1}
lootbox = ["gold", "silver", "gold"]

for loot in lootbox:
    if loot in inv.keys():
        inv[loot] += 1
    else:
        inv[loot] = 1

print(inv)