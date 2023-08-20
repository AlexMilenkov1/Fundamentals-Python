products = {}

while True:
    order = input().split()

    if order[0] == 'buy':
        break

    product, price, quantity = order[0], float(order[1]), int(order[2])

    if product not in products:
        products[product] = []
    else:
        products[product].pop(0)
        products[product].insert(0, price)
        products[product][1] += quantity
        continue
    products[product].append(price)
    products[product].append(quantity)

for product, sales in products.items():
    calculation = sales[0] * sales[1]
    print(f'{product} -> {calculation:.2f}')
