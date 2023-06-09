def is_even(x):
    return x % 2 == 0


numbers = input().split(', ')

integer_numbers = list(map(lambda x: int(x), numbers))

filtered_numbers = list(filter(is_even, integer_numbers))

result = []

for num in filtered_numbers:
    result.append(integer_numbers.index(num))
    index = integer_numbers.index(num)
    integer_numbers[index] = 1

print(result)
