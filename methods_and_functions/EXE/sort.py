sequence_of_numbers = input().split()

numbers = []

for element in sequence_of_numbers:
    numbers.append(int(element))

print(sorted(numbers))
