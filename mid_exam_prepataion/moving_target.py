targets = [int(target) for target in input().split()]

def check_index(x):
    return 0 <= x <= len(targets) - 1


while True:
    action = input().split()

    if action[0] == 'End':
        break

    if action[0] == 'Shoot':
        index = int(action[1])
        power = int(action[2])

        if 0 <= index <= len(targets) - 1:
            targets[index] -= power

            if targets[index] <= 0:
                targets.pop(index)

    elif action[0] == 'Add':
        index = int(action[1])
        value = int(action[2])

        if 0 <= index <= len(targets) - 1:
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action[0] == 'Strike':
        index = int(action[1])
        radius = int(action[2])

        indexes_before = []
        indexes_after = []

        for i in range(1, radius + 1):
            indexes_before.append(index - i)
            indexes_after.append(index + i)

        validation_1 = True
        validation_2 = True

        for i in indexes_before:
            if 0 <= i <= len(targets):
                validation_1 = True
            else:
                validation_1 = False
                break

        for i in indexes_after:
            if 0 <= i <= len(targets):
                validation_2 = True
            else:
                validation_2 = False
                break

        if validation_1 and validation_2 and 0 <= index <= len(targets) - 1:
            range_to_remove = targets[indexes_before[-1]:indexes_after[-1] + 1]

            for item in range_to_remove:
                targets.remove(item)
        else:
            print("Strike missed!")

result = [str(num) for num in targets]

print('|'.join(result))

