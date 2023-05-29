fire_with_their_cells = input().split('#')
total_water = int(input())

high_type_fyre = range(81, 126)
medium_type_fyre = range(51, 81)
low_type_fyre = range(1, 51)

total_fire = 0
total_effort = 0

cells_to_put_out = []

for fyre in fire_with_their_cells:
    split_fyre = fyre.split(' = ')
    type_of_fyre = split_fyre[0]
    cell_value = int(split_fyre[1])

    if total_water >= cell_value:
        if type_of_fyre == 'High':
            if cell_value in high_type_fyre:
                total_water -= cell_value
                cells_to_put_out.append(cell_value)
                total_effort += (0.25 * cell_value)
                total_fire += cell_value

        elif type_of_fyre == 'Medium':
            if cell_value in medium_type_fyre:
                total_water -= cell_value
                cells_to_put_out.append(cell_value)
                total_effort += (0.25 * cell_value)
                total_fire += cell_value

        elif type_of_fyre == 'Low':
            if cell_value in low_type_fyre:
                total_water -= cell_value
                cells_to_put_out.append(cell_value)
                total_effort += (0.25 * cell_value)
                total_fire += cell_value
    else:
        continue

print('Cells:')
for cell in cells_to_put_out:
    print(f'- {cell}')
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
