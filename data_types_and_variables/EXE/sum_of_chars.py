number_of_lines = int(input())

total = 0

for _ in range(number_of_lines):
    letter = input()

    total += ord(letter)

print(f'The sum equals: {total}')
