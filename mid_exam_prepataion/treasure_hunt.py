chest = input().split('|')

while True:
    action = input().split()

    if action[0] == 'Yohoho!':
        break

    if action[0] == 'Loot':
        all_loot = action[1:]

        for item in all_loot:
            if item not in chest:
                chest.insert(0, item)

    elif action[0] == 'Drop':
        index = int(action[1])

        if 0 <= index <= len(chest) - 1:
            pop_item = chest.pop(index)

            chest.append(pop_item)

    elif action[0] == "Steal":
        count = int(action[1])

        stolen_items = []

        if count > len(chest):
            for item in range(len(chest)):
                stolen_item = chest.pop(-1)
                stolen_items.insert(0, stolen_item)

        else:
            for item in range(count):
                stolen_item = chest.pop(-1)
                stolen_items.insert(0, stolen_item)

        print(', '.join(stolen_items))


if chest:
    all_items_length = 0

    for item in chest:
        all_items_length += len(item)

    average_gain = all_items_length / len(chest)

    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
