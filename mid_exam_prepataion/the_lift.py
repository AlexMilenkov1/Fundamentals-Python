people = int(input())
lift = [int(cabin) for cabin in input().split()]

MAX_PEOPLE_IN_CABIN = 4


for seat in range(len(lift)):
    free_seats = MAX_PEOPLE_IN_CABIN - lift[seat]

    if people > free_seats:
        lift[seat] += free_seats
        people -= free_seats
    else:
        lift[seat] += people
        people = 0




if people <= 0 and lift[-1] < MAX_PEOPLE_IN_CABIN:
    print('The lift has empty spots!')
    print(' '.join([str(cabin) for cabin in lift]))
elif people > 0 and lift[-1] == MAX_PEOPLE_IN_CABIN:
    print(f"There isn't enough space! {people} people in a queue!")
    print(' '.join([str(cabin) for cabin in lift]))
elif people <= 0 and lift[-1] == MAX_PEOPLE_IN_CABIN:
    print(' '.join([str(cabin) for cabin in lift]))
