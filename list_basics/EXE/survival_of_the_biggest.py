all_numbers = input().split()
amount_to_remove = int(input())

all_numbers_int = []

for num in all_numbers:
    all_numbers_int.append(int(num))


for count in range(amount_to_remove):
    the_smallest_number = min(all_numbers_int)
    all_numbers_int.remove(the_smallest_number)

final_string = []

for element in all_numbers_int:
    final_string.append(str(element))

print(', '.join(final_string))
