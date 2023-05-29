events = input().split('|')

is_open = True

initial_energy = 100
coins = 100

for element in events:
    event, value_str = element.split('-')
    value = int(value_str)

    gained_energy = 0
    earned_coins = 0

    if event == 'rest':
        current_energy = initial_energy
        initial_energy += value
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif event == 'order':
        if initial_energy >= 30:
            coins += value
            earned_coins += value
            initial_energy -= 30
            print(f"You earned {earned_coins} coins.")
        else:
            print('You had to rest!')
            initial_energy += 50

    else:
        if coins >= value:
            coins -= value
            print(f'You bought {event}.')
        else:
            print(f"Closed! Cannot afford {event}.")
            is_open = False
            break

if is_open:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {initial_energy}")
