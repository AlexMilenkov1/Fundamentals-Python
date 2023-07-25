def add_rating(plant, rating, plant_info):
    plant_info[plant].append(rating)

def update_rarity(plant, new_rarity, plant_info):
    plant_info[plant][0] = new_rarity

def remove_rating(plant, plant_info):
    plant_info[plant].pop(1)

def plant_discovery_management(lines_to_count):
    plant_dict = {}

    for _ in range(lines_to_count):
        plant, rarity = input().split('<->')

        plant_dict[plant] = [rarity]

    while True:
        command, *params = input().split()

        if command == 'Exhibition':
            break

        if command == 'Rate:':
            plant, rating = params[0], int(params[2])

            if plant in plant_dict.keys():
                add_rating(plant, rating, plant_dict)
            else:
                print('error')

        elif command == 'Update:':
            plant, new_rarity = params[0], int(params[2])

            if plant in plant_dict.keys():
                update_rarity(plant, new_rarity, plant_dict)
            else:
                print('error')

        elif command == 'Reset:':
            plant = params[0]

            if plant in plant_dict.keys():
                remove_rating(plant, plant_dict)
            else:
                print('error')

    return plant_dict


lines = int(input())
result =  plant_discovery_management(lines)

print('Plants for the exhibition:')
for plant, info in result.items():
    if len(info) > 1:
        rarity, *rating = info

        calculate_average_rating = sum(rating) / len(rating)

        print(f'- {plant}; Rarity: {rarity}; Rating: {calculate_average_rating:.2f}')
    else:
        rarity = info[0]
        print(f'- {plant}; Rarity: {rarity}; Rating: {0:.2f}')
