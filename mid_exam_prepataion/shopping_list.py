initial_shopping_list = input().split("!")

while True:

    action = input().split()

    if action[0] == 'Go':
        break

    need_to_do = action[0]
    item = action[1]

    if need_to_do == 'Urgent':
        if item not in initial_shopping_list:
            initial_shopping_list.insert(0, item)

    elif need_to_do == 'Unnecessary':
        if item in initial_shopping_list:
            index = initial_shopping_list.index(item)
            initial_shopping_list.pop(index)

    elif need_to_do == 'Correct':
        new_item = action[2]

        if item in initial_shopping_list:
            get_index = initial_shopping_list.index(item)
            initial_shopping_list.pop(get_index)
            initial_shopping_list.insert(get_index, new_item)

    elif need_to_do == 'Rearrange':
        if item in initial_shopping_list:
            index = initial_shopping_list.index(item)
            initial_shopping_list.pop(index)

            initial_shopping_list.append(item)

print(', '.join(initial_shopping_list))
