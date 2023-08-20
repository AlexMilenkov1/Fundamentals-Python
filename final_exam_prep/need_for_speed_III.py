def drive_given_distance(cars, commands):
    car = commands[1]
    distance = int(commands[2])
    fuel = int(commands[3])

    over_mileage = False

    if cars[car]['fuel'] >= fuel:
        cars[car]['mileage'] += distance
        cars[car]['fuel'] -= fuel\

        if cars[car]['mileage'] >= 100_000:

            del cars[car]

            return [f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.", f"Time to sell the {car}!"]

        return f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."

    else:
        return "Not enough fuel to make that ride"


def refill_the_tank(cars, commands):
    car = commands[1]
    fuel = int(commands[2])

    if cars[car]['fuel'] < 75:
        cars[car]['fuel'] += fuel
    else:
        return f"{car} refueled with 0 liters"

    check =  cars[car]['fuel']

    if  cars[car]['fuel'] >= 75:
        cars[car]['fuel'] = 75

        fuel_amount = fuel - (check - 75)

        return f"{car} refueled with {fuel_amount} liters"

    return f"{car} refueled with {fuel} liters"

def decrease_the_mileage(cars, commands):
    car = commands[1]
    km = int(commands[2])

    cars[car]['mileage'] -= km

    if cars[car]['mileage'] < 10_000:
        cars[car]['mileage'] = 10_000
    else:
        return f"{car} mileage decreased by {km} kilometers"

def all_cars(lines):
    cars = {}

    for _ in range(lines):
        car_info = input().split('|')

        car_model, mileage, fuel = car_info

        cars[car_model] = {'mileage':int(mileage), 'fuel':int(fuel)}

    while True:
        commands = input().split(' : ')

        if commands[0] == 'Stop':
            break

        action = commands[0]

        if action == 'Drive':
            message = drive_given_distance(cars, commands)

            if len(message) == 2:
                mm, over_mileage_message = message

                print(mm)
                print(over_mileage_message)
            else:
                print(message)

        elif action == 'Refuel':
            message = refill_the_tank(cars, commands)

            print(message)

        elif action == 'Revert':
            message = decrease_the_mileage(cars, commands)

            if message:
                print(message)

    return cars

number_of_cars = int(input())
result =  all_cars(number_of_cars)

for model in result.keys():
    mileage, fuel = result[model]['mileage'], result[model]['fuel']

    print(f"{model} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
