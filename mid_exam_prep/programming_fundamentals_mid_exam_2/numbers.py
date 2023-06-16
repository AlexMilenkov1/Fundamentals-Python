numbers = [int(number) for number in input().split()]

average_number = sum(numbers) / len(numbers)

greater_than_average = []

for num in numbers:  # find all greater than average
    if num > average_number:
        greater_than_average.append(num)


if len(greater_than_average) == 0:
    print('No')
elif len(greater_than_average) <= 5:
    sorted_result = sorted(greater_than_average, reverse=True)
    result = [str(string) for string in sorted_result]

    print(' '.join(result))

elif len(greater_than_average) > 5:
    sorted_result = sorted(greater_than_average, reverse=True)
    result = [str(string) for string in sorted_result]

    top_5 = result[:5]

    print(' '.join(top_5))
