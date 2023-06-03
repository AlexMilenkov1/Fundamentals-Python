from math import ceil

sequence_of_numbers = input().split()

route = []

for string in sequence_of_numbers:
    number = int(string)
    route.append(number)

middle_of_rout = ceil(len(route) / 2)
left_side = route[:middle_of_rout - 1]
right_side = route[middle_of_rout:]
reversed_right_side = right_side[::-1]

total_time_left = 0
total_time_right = 0

for time in left_side:
    if time == 0 and total_time_left != 0:
        total_time_left = total_time_left * 0.8
    else:
        total_time_left += time

for time in reversed_right_side:
    if time == 0 and total_time_right != 0:
        total_time_right = total_time_right * 0.8
    else:
        total_time_right += time

if total_time_left < total_time_right:
    print(f"The winner is left with total time: {total_time_left:.1f}")
else:
    print(f"The winner is right with total time: {total_time_right:.1f}")
