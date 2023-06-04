def check_even(number):
    all_even_numbers = []

    if int(number) % 2 == 0:
        all_even_numbers.append(int(number))

    return all_even_numbers


sequence_of_numbers = input().split()

result = list(filter(check_even, sequence_of_numbers))

final_result = []

for string in result:
    final_result.append(int(string))

print(final_result)
