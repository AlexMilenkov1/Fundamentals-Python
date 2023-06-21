products = {}

while True:
    items = input().split(': ')

    if items[0] == 'statistics':
        break

    product = items[0]
    value = int(items[1])

    if product not in products.keys():
        products[product] = 0

    products[product] += value

print('Products in stock:')
for key, value in products.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(products)}')
print(f'Total Quantity: {sum(products.values())}')
