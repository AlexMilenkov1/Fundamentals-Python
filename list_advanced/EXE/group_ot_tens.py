def check_group(current_numbers):
    current_group = 10

    result = []

    while current_numbers:

        for number in current_numbers:
            if current_group >= number:
                result.append(number)

        for num in result:
            current_numbers.remove(num)

        print(f"Group of {current_group}'s: {result}")
        current_group += 10
        result = []


sequence_of_numbers = [int(number) for number in input().split(', ')]

check_group(sequence_of_numbers)
