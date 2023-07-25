def move_letters(message, number_of_letters):
    message = message[number_of_letters:] + message[:number_of_letters]

    return message

def insert_value(message, index, value):
    message = message[:index] + value + message[index:]

    return message
def change_occurrences(message, substring, replacement):
    message = message.replace(substring, replacement)

    return message

def control_panel(message):
    while True:
        command = input().split('|')

        if command[0] == 'Decode':
            break

        action, *params = command

        if action == 'Move':
            number_of_letters = int(params[0])

            message = move_letters(message, number_of_letters)

        elif action == 'Insert':
            index, value = int(params[0]), params[1]

            message = insert_value(message, index, value)

        else:
            substring, replacement = params

            message = change_occurrences(message, substring, replacement)

    return message


encrypted_message = input()
decrypted_message = control_panel(encrypted_message)

print(f'The decrypted message is: {decrypted_message}')
