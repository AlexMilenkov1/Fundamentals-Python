legendary_items = {'shards': 0, 'fragments': 0, 'motes': 0}

obtained = False

items = input().split()

while not obtained:
    for index in range(0, len(items), 2):
        quantity = int(items[index])
        item =  items[index + 1].lower()

        if item not in legendary_items:
            legendary_items[item] = 0
        legendary_items[item] += quantity

        if legendary_items['shards'] >= 250:
            print('Shadowmourne obtained!')
            legendary_items['shards'] -= 250
            obtained = True
            break

        elif legendary_items['fragments'] >= 250:
            print('Valanyr obtained!')
            legendary_items['fragments'] -= 250
            obtained = True
            break


        elif legendary_items['motes'] >= 250:
            print('Dragonwrath obtained!')
            legendary_items['motes'] -= 250
            obtained = True
            break
    if obtained:
        break
    else:
        items = input().split()

for item, quantity in legendary_items.items():
    print(f'{item}: {quantity}')
