gift_names = input().split()
none_count = 0

while True:
    command = input().split()

    if command[1] == 'Money':
        break

    if command[0] == 'OutOfStock':
        if command[1] in gift_names:
            for i in range(len(gift_names)):
                if gift_names[i] == command[1]:
                    gift_names[i] = 'None'

    elif command[0] == 'Required':
        if int(command[2]) <= len(gift_names) - 1:
            gift_names[int(command[2])] = command[1]

    elif command[0] == 'JustInCase':
        gift_names[-1] = command[1]

result = [gift for gift in gift_names if gift != 'None']
print(' '.join(result))
