numbers = input().split()

result = []

for value in numbers:
    inverted_num = -int(value)

    result.append(inverted_num)

print(result)
