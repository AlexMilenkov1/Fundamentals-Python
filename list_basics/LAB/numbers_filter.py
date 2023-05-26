lines_count = int(input())

all_numbers = []

for _ in range(lines_count):
    number = int(input())

    all_numbers.append(number)

command = input()

result = []

for num in all_numbers:
    if command == 'even' and num % 2 == 0:
        result.append(num)
    elif command == 'odd' and num % 2 != 0:
        result.append(num)
    elif command == 'positive' and num >= 0:
        result.append(num)
    elif command == 'negative' and num < 0:
        result.append(num)

print(result)
