quantity_of_snowballs = int(input())

max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

for snowball in range(quantity_of_snowballs):
    weight_of_snowball = int(input())
    time_for_flight = int(input())
    quality = int(input())

    formula = (weight_of_snowball / time_for_flight) ** quality

    if formula > max_value:
        max_value = formula
        max_weight = weight_of_snowball
        max_time = time_for_flight
        max_quality = quality


print(f'{max_weight} : {max_time} = {int(max_value)} ({max_quality})')
