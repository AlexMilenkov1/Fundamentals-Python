sequence_of_numbers = [int(number) for number in input().split()]

removed_elements = 0

while sequence_of_numbers:
    index = int(input())

    if index < 0:
        removed_element = sequence_of_numbers.pop(0)
        sequence_of_numbers.insert(0, sequence_of_numbers[-1])

        removed_elements += removed_element

    elif index > len(sequence_of_numbers) - 1:
        removed_element = sequence_of_numbers.pop(-1)
        sequence_of_numbers.append(sequence_of_numbers[0])

        removed_elements += removed_element

    else:
        removed_element = sequence_of_numbers.pop(index)
        removed_elements += removed_element

    index = 0
    while index < len(sequence_of_numbers):
        number = sequence_of_numbers[index]

        if removed_element >= number:
            sequence_of_numbers[index] += removed_element

        elif removed_element < number:
            sequence_of_numbers[index] -= removed_element

        index += 1

print(removed_elements)
