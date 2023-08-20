people_in_queue = int(input())
lift = [int(seat) for seat in input().split()]

CAPACITY = 4

for i in range(len(lift)):
    free_seat = CAPACITY - lift[i]

    if people_in_queue >= free_seat:
        lift[i] += free_seat
    else:
        lift[i] += people_in_queue

    people_in_queue -= free_seat

print(lift)
