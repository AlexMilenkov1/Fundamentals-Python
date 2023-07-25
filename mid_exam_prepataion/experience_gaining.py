amount_of_experience = float(input())
count_of_battles = int(input())

gained_experience = 0
battles = 0

for battle in range(1, count_of_battles + 1):
    if gained_experience >= amount_of_experience:
        break

    experience = float(input())

    battles += 1

    if battle % 3 == 0:
        gained_experience += (experience + (experience * 0.15))
    elif battle % 5 == 0:
        gained_experience += (experience - (experience * 0.10))
    elif battle % 15 == 0:
        gained_experience += (experience + (experience * 0.05))
    else:
        gained_experience += experience

if gained_experience >= amount_of_experience:
    print(f'Player successfully collected his needed experience for {battles} battles.')
else:
    calculation = amount_of_experience - gained_experience
    print(f'Player was not able to collect the needed experience, {calculation:.2f} more needed.')

