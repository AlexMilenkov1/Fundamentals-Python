coffees_list = input().split()
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()

    action = command[0]

    if action == 'Include':
        coffee = command[1]

        coffees_list.append(coffee)

    elif action == 'Remove':
        first_or_last = command[1]
        number_of_coffees = int(command[2])

        if len(coffees_list) >= number_of_coffees:
            if first_or_last == 'first':
                items_to_pop = coffees_list[0:number_of_coffees]

                for item in items_to_pop:
                    coffees_list.remove(item)

            elif first_or_last == 'last':
                reversed_list = coffees_list[::-1]

                for _ in range(number_of_coffees):
                    reversed_list.pop(0)

                coffees_list = reversed_list[::-1]

    elif action == 'Prefer':
        index_1 = int(command[1])
        index_2 = int(command[2])

        if 0 <= index_1 <= len(coffees_list) - 1 and 0 <= index_2 <= len(coffees_list) - 1:
            coffees_list[index_1], coffees_list[index_2] = coffees_list[index_2], coffees_list[index_1]

    elif action == 'Reverse':
        coffees_list = coffees_list[::-1]

print('Coffees:')
print(' '.join(coffees_list))
