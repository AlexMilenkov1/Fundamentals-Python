def check_presence(key, info):
    substring = info[1]

    if substring in key:
        return f"{key} contains {substring}"
    else:
        return "Substring not found!"

def flip_the_key(key, info):
    upper_or_lower = info[1]
    start_index = int(info[2])
    end_index = int(info[3])

    if upper_or_lower == 'Upper':
        before_substring = key[:start_index]
        after_substring = key[end_index:]
        substring = key[start_index:end_index]

        changed_substring = substring.upper()

        key = before_substring + changed_substring + after_substring
    else:
        before_substring = key[:start_index]
        after_substring = key[end_index:]
        substring = key[start_index:end_index]

        changed_substring = substring.lower()

        key = before_substring + changed_substring + after_substring

    return key
def slicing_the_key(key, info):
    start_index = int(info[1])
    end_index = int(info[2])

    first_string = key[:start_index]
    second_string = key[end_index:]

    key = first_string + second_string

    return key


def control_panel(activation_key):
    while True:
        information = input().split('>>>')

        command = information[0]

        if command == 'Generate':
            break

        if command == 'Contains':
            print(check_presence(activation_key, information))

        elif command == 'Flip':
            activation_key = flip_the_key(activation_key, information)

            print(activation_key)

        elif command == 'Slice':
            activation_key = slicing_the_key(activation_key, information)

            print(activation_key)

    return activation_key


raw_activation_key = input()
result_key =  control_panel(raw_activation_key)

print(f'Your activation key is: {result_key}')
