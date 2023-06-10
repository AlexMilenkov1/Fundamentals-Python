number_of_rooms = int(input())

total_needed_chairs = 0
total_free_chairs = 0

for current_room in range(1, number_of_rooms + 1):
    chairs, visitors = input().split()

    if len(chairs) < int(visitors):
        needed_chairs = int(visitors) - len(chairs)
        print(f"{needed_chairs} more chairs needed in room {current_room}")
        total_needed_chairs += needed_chairs

    if len(chairs) > int(visitors):
        total_free_chairs += (len(chairs) - int(visitors))

if total_free_chairs >= total_needed_chairs:
    print(f'Game On, {total_free_chairs} free chairs left')
