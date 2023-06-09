wagons_number = int(input())

wagons = []

for _ in range(wagons_number):
    wagons.append(0)

while True:
    command = input().split()

    if command[0] == 'End':
        print(wagons)
        break

    if command[0] == 'add':
        wagons[-1] += int(command[1])

    if command[0] == 'insert':
        index = command[1]
        wagons[int(index)] += int(command[2])

    if command[0] == 'leave':
        index = command[1]
        wagons[int(index)] -= int(command[2])
