def extract_digits_from_string(string):
    numbers = []
    new_string = ''
    final_string = []

    for char in string:
        for element in char:
            if element.isdigit():
                numbers.append(int(element))
            else:
                new_string += element

        number_str = ''.join(map(str, numbers))
        number = int(number_str)

        character = chr(number)

        new_string = character + new_string
        new_string_list = list(new_string)
        new_string_list[1], new_string_list[-1] = new_string_list[-1], new_string_list[1]

        current_string_list = [''.join(new_string_list)]

        final_string.extend(current_string_list)

        numbers = []
        new_string = ''

    return final_string


characters = input().split()

result = extract_digits_from_string(characters)
print(' '.join(result))
