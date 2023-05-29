items = input().split('|')
budget = float(input())

TRAIN_TICKET = 150

CLOTHES_PRICE_MAX_PRICE = 50
SHOES_MAX_PRICE = 35
ACCESSORIES_MAX_PRICE = 20.50

bought_items = []

profit = 0

for item in items:
    type_of_item, price_str = item.split('->')
    price = float(price_str)

    if type_of_item == 'Clothes':
        if price <= CLOTHES_PRICE_MAX_PRICE:
            if budget >= price:
                budget -= price
                bought_items.append(price * 1.4)
                profit += (price * 1.4) - price

    elif type_of_item == 'Shoes':
        if price <= SHOES_MAX_PRICE:
            if budget >= price:
                budget -= price
                bought_items.append(price * 1.4)
                profit += (price * 1.4) - price

    elif type_of_item == 'Accessories':
        if price <= ACCESSORIES_MAX_PRICE:
            if budget >= price:
                budget -= price
                bought_items.append(price * 1.4)
                profit += (price * 1.4) - price

for item in bought_items:
    print(f'{item:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')
if budget + sum(bought_items) >= TRAIN_TICKET:
    print("Hello, France!")
else:
    print("Not enough money.")
