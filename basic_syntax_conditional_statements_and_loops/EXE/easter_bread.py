budget = float(input(""))
price_per_kg_flour = float(input(""))

price_per_pack_eggs = 0.75 * price_per_kg_flour
price_per_liter_milk = 1.25 * price_per_kg_flour
price_per_250ml_milk = price_per_liter_milk / 4

loaves_count = 0
eggs_count = 0

while budget >= price_per_kg_flour + price_per_pack_eggs + price_per_250ml_milk:
    budget -= price_per_kg_flour + price_per_pack_eggs + price_per_250ml_milk
    loaves_count += 1
    eggs_count += 3

    if loaves_count % 3 == 0:
        eggs_lost = loaves_count - 2
        eggs_count -= eggs_lost

money_left = "{:.2f}".format(budget)

print(f"You made {loaves_count} loaves of Easter bread! Now you have {eggs_count} eggs and {money_left}BGN left.")
