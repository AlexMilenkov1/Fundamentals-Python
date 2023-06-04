def add_and_subtract(first, second, third):
    result_of_sum = sum_numbers(first, second)
    final_diff = subtract(result_of_sum, third)

    return final_diff


def sum_numbers(first, second):
    sum_of_numbers = first + second

    return sum_of_numbers


def subtract(result, third_num):
    diff = result - third_num

    return diff


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
