number_of_lines = int(input())

WATER_TANK_CAPACITY = 255
liters_amount_total = 0

for _ in range(number_of_lines):
    liters = int(input())

    if liters_amount_total + liters > WATER_TANK_CAPACITY:
        print('Insufficient capacity!')
        continue

    liters_amount_total += liters

print(liters_amount_total)
