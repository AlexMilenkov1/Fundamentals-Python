number = int(input())

is_special = False

for num in range(1, number + 1):
    string_number = str(num)

    if int(string_number) <= 9:
        if int(string_number) == 5 or int(string_number) == 7:
            is_special = True
            print(f'{int(string_number)} -> {is_special}')
        else:
            is_special = False
            print(f'{int(string_number)} -> {is_special}')

    else:
        result = 0
        for index in string_number:
            result += int(index)

        if result == 5 or result == 7 or result == 11:
            is_special = True
        else:
            is_special = False

        print(f'{int(string_number)} -> {is_special}')
