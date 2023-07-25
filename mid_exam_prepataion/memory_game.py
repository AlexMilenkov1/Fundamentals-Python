sequence_of_elements = input().split()

number_of_moves = 0

while sequence_of_elements:
    indexes = input().split()

    if indexes[0] == 'end':
        print("Sorry you lose :(")
        print(' '.join(sequence_of_elements))
        break

    index_1 = int(indexes[0])
    index_2 = int(indexes[1])

    number_of_moves += 1

    if index_1 == index_2 or 0 > index_1 or index_1 > len(sequence_of_elements) - 1 or 0 > index_2 or index_2 > len(sequence_of_elements) - 1:
        middle_of_sequence = len(sequence_of_elements) // 2
        sequence_of_elements.insert(middle_of_sequence, f'-{number_of_moves}a')
        sequence_of_elements.insert(middle_of_sequence + 1, f'-{number_of_moves}a')
        print("Invalid input! Adding additional elements to the board")
    else:
        if sequence_of_elements[index_1] == sequence_of_elements[index_2]:
            print(f"Congrats! You have found matching elements - {sequence_of_elements[index_1]}!")
            if index_1 > index_2:
                sequence_of_elements.pop(index_1)
                sequence_of_elements.pop(index_2)
            elif index_2 > index_1:
                sequence_of_elements.pop(index_2)
                sequence_of_elements.pop(index_1)

        elif sequence_of_elements[index_1] != sequence_of_elements[index_2]:
            print("Try again!")

else:
    print(f"You have won in {number_of_moves} turns!")
