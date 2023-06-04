def find_the_smallest(numbers):
    result = min(numbers)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

all_numbers = [first_number, second_number, third_number]

the_smallest_num = find_the_smallest(all_numbers)
print(the_smallest_num)
