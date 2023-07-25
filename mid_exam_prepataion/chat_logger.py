chat = []

while True:
    command = input().split()

    action = command[0]

    if action == 'end':
        break

    if action == 'Chat':
        message = command[1]

        chat.append(message)

    elif action == 'Delete':
        message = command[1]

        if message in chat:
            chat.remove(message)

    elif action == 'Edit':
        message = command[1]
        edited_version = command[2]

        if message in chat:
            message_index = chat.index(message)

            chat.pop(message_index)
            chat.insert(message_index, edited_version)

    elif action == 'Pin':
        message = command[1]

        if message in chat:
            chat.remove(message)
            chat.append(message)

    elif action == 'Spam':
        messages = command[1:]

        chat.extend(messages)

for word in chat:
    print(''.join(word))

