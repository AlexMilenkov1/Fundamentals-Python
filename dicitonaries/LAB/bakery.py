products = input().split()

bakery = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = int(products[index + 1])
    bakery[key] = value

print(bakery)
