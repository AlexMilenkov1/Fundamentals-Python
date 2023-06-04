sequence_of_numbers = input().split()

numbers = []

for element in sequence_of_numbers:
    numbers.append(int(element))

min_number = min(numbers)
max_number = max(numbers)
sum_off_all_nums = sum(numbers)

print(f'The minimum number is {min_number}')
print(f'The maximum number is {max_number}')
print(f'The sum number is: {sum_off_all_nums}')
