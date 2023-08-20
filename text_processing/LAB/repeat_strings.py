string = input().split()

result = ''

for symbol in string:
    result += symbol * len(symbol)

print(result)
