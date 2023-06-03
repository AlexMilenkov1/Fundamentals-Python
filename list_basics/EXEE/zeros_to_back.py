numbers_string = input().split(', ')

numbers = []
count = 0

for string in numbers_string:
    number = int(string)
    numbers.append(number)

while 0 in numbers:
    numbers.remove(0)
    count += 1

for _ in range(count):
    numbers.append(0)

print(numbers)
