lst = input().split()

working_list = []

for string in lst:
    number = int(string)
    working_list.append(number)

while True:
    command = input().split()

    if command[0] == 'end':
        break

    if command[0] == 'exchange':
        index = int(command[1])

        if len(working_list) >= index > 0:
            left_part = working_list[:index + 1]
            right_part = working_list[index + 1:]

            new_list = right_part + left_part
            print(new_list)

        else:
            print('Invalid index')

    elif command[0] == 'max':
        if command[1] == 'even':
            even_numbers = []
            for even in working_list:
                if even % 2 == 0:
                    even_numbers.append(even)
            max_even = max(even_numbers)
            max_even_index = working_list.index(max_even)
            print(max_even_index)
        else:
            odd_numbers = []
            for odd in working_list:
                if odd % 2 != 0:
                    odd_numbers.append(odd)
            max_odd = max(odd_numbers)
            max_odd_index = working_list.index(max_odd)
            print(max_odd_index)

    elif command[0] == 'first':
        count = int(command[1])

        count_list = []

        if command[2] == 'even':
            while count > 0:
                for even_num in working_list:
                    if even_num % 2 == 0:
                        count_list.append(even_num)
                        count -= 1
                else:
                    break
        else:
            reversed_list = working_list[::-1]
            while count > 0:
                for element in reversed_list:
                    if element % 2 != 0:
                        count_list.append(element)
                        count -= 1
                else:
                    break

        if len(count_list) > len(working_list):
            print('Invalid count')
        else:
            if len(count_list) == 0:
                print('[]')
            else:
                print(count_list)
