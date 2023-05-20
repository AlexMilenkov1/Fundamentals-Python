number_of_orders = int(input())

total_cost = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())

    if 0.01 > price_per_capsule or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_needed < 1 or capsules_needed > 2000:
        continue

    coffe_price = price_per_capsule * days * capsules_needed
    total_cost += coffe_price
    print(f"The price for the coffee is: ${coffe_price:.2f}")

print(f"Total: ${total_cost:.2f}")
