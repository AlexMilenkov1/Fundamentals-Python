lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expenses = 0
broken_helmets_count = 0
broken_swords_count = 0
broken_shield_count = 0
broken_armor_count = 0

for lost_fight in range(1, lost_fights_count + 1):
    if lost_fight % 2 == 0:
        broken_helmets_count += 1
    if lost_fight % 3 == 0:
        broken_swords_count += 1
    if lost_fight % 6 == 0:
        broken_shield_count += 1
    if lost_fight % 12 == 0:
        broken_armor_count += 1

total_expenses = (broken_helmets_count * helmet_price) + \
                 (broken_swords_count * sword_price) + \
                 (broken_shield_count * shield_price) + \
                 (broken_armor_count * armor_price)

print(f'Gladiator expenses: {total_expenses:.2f} aureus')
