def extract_digits_from_string(string):
    numbers = []

    for char in string:
        for element in char:
            if element.isdigit():
                numbers.append(int(element))

        number_str = ''.join(map(str, numbers))
        number = int(number_str)

        character = chr(number)

        char.replace(number_str, character)
        print(char)
        # list_char = list(char)
        # for index, item in list_char:
        #     if index == 1:
        #         list_char[index] = list_char[-1]
        #     elif index == len(list_char) - 1:
        #         list_char[index] = list_char[1]
        #
        # print(list_char)


characters = input().split()

digits = extract_digits_from_string(characters)
print(digits)
# number = int(digits)
# print(number)
