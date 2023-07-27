def cast_spell(info, hero_dict):
    hero_name = info[1]
    mana_needed = int(info[2])
    spell_name = info[3]

    if hero_dict[hero_name]['mp'] >= mana_needed:
        hero_dict[hero_name]['mp'] -= mana_needed
        return f"{hero_name} has successfully cast {spell_name} and now has {hero_dict[hero_name]['mp']} MP!"

    return f"{hero_name} does not have enough MP to cast {spell_name}!"


def take_damage(info, hero_dict):
    hero_name = info[1]
    damage = int(info[2])
    attacker = info[3]

    hero_dict[hero_name]['hp'] -= damage

    if hero_dict[hero_name]['hp'] > 0:
        return f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero_dict[hero_name]['hp']} HP left!"

    del hero_dict[hero_name]
    return f"{hero_name} has been killed by {attacker}!"


def recharge(info, hero_dict):
    hero_name = info[1]
    amount = int(info[2])


    hero_dict[hero_name]['mp'] += amount

    check = hero_dict[hero_name]['mp']

    if hero_dict[hero_name]['mp'] > 200:
        hero_dict[hero_name]['mp'] = 200

        amount_recovered = amount - (check - 200)

        return f"{hero_name} recharged for {amount_recovered} MP!"

    return f"{hero_name} recharged for {amount} MP!"



def heal(info, hero_dict):
    hero_name = info[1]
    amount = int(info[2])

    hero_dict[hero_name]['hp'] += amount

    check = hero_dict[hero_name]['hp']

    if hero_dict[hero_name]['hp'] > 100:
        hero_dict[hero_name]['hp'] = 100

        amount_recovered = amount - (check - 100)

        return f"{hero_name} healed for {amount_recovered} HP!"

    return f"{hero_name} healed for {amount} HP!"


def heroes_management(lines):
    heroes_party = {}

    for _ in range(lines):
        hero_info = input().split()

        hero_name, hit_points, mana_points = hero_info[0], int(hero_info[1]), int(hero_info[2])

        heroes_party[hero_name] = {'hp':hit_points, 'mp':mana_points}

    while True:
        information = input().split(" - ")

        if information[0] == 'End':
            break

        action = information[0]

        if action == 'CastSpell':
            print(cast_spell(information, heroes_party))

        elif action == 'TakeDamage':
            print(take_damage(information, heroes_party))

        elif action == 'Recharge':
            print(recharge(information, heroes_party))

        elif action == 'Heal':
            print(heal(information, heroes_party))

    return heroes_party

number_of_heroes = int(input())

heroes = heroes_management(number_of_heroes)


for hero in heroes.keys():
    hit_points, mana = heroes[hero]['hp'],  heroes[hero]['mp']

    print(hero)
    print(f'HP: {hit_points}')
    print(f'MP: {mana}')

