import math

array_of_data = input().split()

while True:
    command = input().split()

    if command[0] == '3:1':
        break

    action = command[0]
    first_index = int(command[1])
    second_index = int(command[2])

    if action == 'merge':
        if len(array_of_data) - 1 >= first_index >= 0 and len(array_of_data) - 1 >= second_index >= 0:
            merged_elements = ''.join(array_of_data[first_index + 1:second_index + 1])
            del array_of_data[first_index:second_index]
            array_of_data.insert(first_index, merged_elements)
        else:
            if first_index < 0:
                first_index = 0
            if second_index >= len(array_of_data):
                second_index = len(array_of_data) - 1
            merged_elements = ''.join(array_of_data[first_index + 1:second_index + 1])
            del array_of_data[first_index:second_index + 1]
            if merged_elements:
                array_of_data.insert(first_index, merged_elements)

    elif action == 'divide':
        list_with_new_items = []

        if len(array_of_data[first_index]) % second_index == 0:
                times_to_count = len(array_of_data[first_index]) // second_index
                string_to_change = array_of_data.pop(first_index)

                for partition in range(second_index):
                        list_with_new_items.append(string_to_change[:times_to_count])
                        string_to_change = string_to_change[times_to_count:]

                for x in list_with_new_items[::-1]:
                    array_of_data.insert(first_index, x)

        elif len(array_of_data[first_index]) % second_index != 0:
            times_to_count = len(array_of_data[first_index]) // second_index
            string_to_change = array_of_data.pop(first_index)

            for partition in range(1, second_index + 1):
                if partition == second_index:
                    list_with_new_items.append(string_to_change)
                else:
                    list_with_new_items.append(string_to_change[:times_to_count])
                    string_to_change = string_to_change[times_to_count:]

            for x in list_with_new_items[::-1]:
                array_of_data.insert(first_index, x)

print(' '.join(array_of_data))
