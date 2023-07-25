price = input()

price_without_taxes = 0
taxes = 0

while price != 'special' and price != 'regular':
    price = float(price)

    if price < 0:
        print("Invalid price!")
    else:
        price_without_taxes += price
        taxes += 0.2 * price

    price = input()

total_price = price_without_taxes + taxes

if str(price) == 'special':
    total_price = total_price * 0.9

if total_price == 0:
    print('Invalid order!')
else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {price_without_taxes:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f"Total price: {total_price:.2f}$")
