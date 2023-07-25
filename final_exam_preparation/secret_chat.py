def insert_space(message, index):
    message = message[:index] + ' ' + message[index:]

    return message
def reverse(message, substring):
    if substring in message:
        message = message.replace(substring, '', 1)
        new_substring = substring[::-1]
        message = message + new_substring

        return message

    else:
        return "error"

def change_all(message, substring, replacement):
    if substring in message:
        message = message.replace(substring, replacement)

        return message

def control_the_commands(message):
    while True:

        command = input().split(':|:')

        if command[0] == 'Reveal':
            break

        action, *params = command

        if action == 'InsertSpace':
            index = int(params[0])
            message = insert_space(message, index)
            print(message)

        elif action == 'Reverse':
            substring = params[0]

            if reverse(message, substring) == 'error':
                print('error')
            else:
                message = reverse(message, substring)
                print(message)

        elif action == 'ChangeAll':
            substring, replacement = params[0], params[1]


            message = change_all(message, substring, replacement)
            print(message)

    return message



concealed_message = input()

print(f'You have a new text message: {control_the_commands(concealed_message)}')
