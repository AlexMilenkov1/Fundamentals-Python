animal_list = []

for _ in range(1, 4):
    animal_part = input()

    animal_list.append(animal_part)

animal_list[0], animal_list[2] = animal_list[2], animal_list[0]

print(animal_list)
