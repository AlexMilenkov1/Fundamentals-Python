def take_odd_letters(string):
    result = ''
    for index in range(len(string)):
        if index % 2 != 0:
            result += string[index]

    return result

def cut_the_string(string, commands):
    index = int(commands[1])
    length = int(commands[2])

    before_substring = string[:index]
    after_substring = string[index+length:]

    string = before_substring + after_substring

    return string


def substitute_elements(string, commands):
    substring = commands[1]
    substitute = commands[2]

    if substring in string:
        string = string.replace(substring, substitute)
        return string
    return "Nothing to replace!"

def control_panel(current_string):
    while True:
        commands = input().split()

        if commands[0] == 'Done':
            break

        action = commands[0]

        if action == 'TakeOdd':
            current_string = take_odd_letters(current_string)

            print(current_string)

        elif action == 'Cut':
            current_string = cut_the_string(current_string, commands)

            print(current_string)

        elif action == 'Substitute':
            if substitute_elements(current_string, commands) == 'Nothing to replace!':
                print("Nothing to replace!")
            else:
                current_string = substitute_elements(current_string, commands)

                print(current_string)

    return current_string

raw_string = input()
password = control_panel(raw_string)

print(f"Your password is: {password}")
