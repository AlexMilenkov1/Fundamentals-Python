products = input().split()
searched_products = input().split()

stocks = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = int(products[index + 1])
    stocks[key] = value

for product in searched_products:
    if product in stocks.keys():
        print(f'We have {stocks[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")
