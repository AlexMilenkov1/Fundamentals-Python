def swap_the_elements(index_1, index_2, numbers):
    numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]


def multiply_the_elements(index_1, index_2, numbers):
    calculation = numbers[index_1] * numbers[index_2]

    numbers[index_1] = calculation


def decrease_the_elements(numbers):
    decrease = list(map(lambda num:  num - 1, numbers))

    return decrease


array_with_integers = [int(number) for number in input().split()]

while True:
    command = input().split()

    if command[0] == 'end':
        break

    if len(command) == 3:
        action = command[0]
        first_index = int(command[1])
        second_index = int(command[2])
    else:
        action = command[0]
        first_index = None
        second_index = None

    if action == 'swap':
        swap_the_elements(first_index, second_index, array_with_integers)
    elif action == 'multiply':
        multiply_the_elements(first_index, second_index, array_with_integers)
    elif action == 'decrease':
        decreasement = decrease_the_elements( array_with_integers)

        array_with_integers = decreasement

numbers_result = [str(string) for string in array_with_integers]

print(', '.join(numbers_result))
