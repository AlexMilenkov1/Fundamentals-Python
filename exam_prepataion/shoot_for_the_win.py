sequence_of_integers = [int(num) for num in input().split()]

shot_targets_count = 0

while True:
    index = input()

    if index == 'End':
        print(f'Shot targets: {shot_targets_count} -> {" ".join([str(target) for target in sequence_of_integers])}')
        break

    index = int(index)

    if 0 <= index <= len(sequence_of_integers) - 1:
        if sequence_of_integers[index] != -1:
            shot_target = sequence_of_integers.pop(index)

            sequence_of_integers.insert(index, -1)
            shot_targets_count += 1

            for i in range(len(sequence_of_integers)):
                if sequence_of_integers[i] != -1:

                    if sequence_of_integers[i] > shot_target:
                        sequence_of_integers[i] -= shot_target

                    elif sequence_of_integers[i] <= shot_target:
                        sequence_of_integers[i] += shot_target
