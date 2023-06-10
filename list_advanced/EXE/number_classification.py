numbers = [int(number) for number in input().split(', ')]

positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    if number % 2 != 0:
        odd_numbers.append(number)
    if number >= 0:
        positive_numbers.append(number)
    if number < 0:
        negative_numbers.append(number)


print(f'Positive: {", ".join([str(num) for num in positive_numbers])}')
print(f'Negative: {", ".join([str(num) for num in negative_numbers])}')
print(f'Even: {", ".join([str(num) for num in even_numbers])}')
print(f'Odd: {", ".join([str(num) for num in odd_numbers])}')
