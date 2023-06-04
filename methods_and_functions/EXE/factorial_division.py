def calculate_factorial(number):
    result = 1
    for num in range(1, number + 1):
        result *= num

    return result


first_number = int(input())
second_number = int(input())

first_result = calculate_factorial(first_number)
second_result= calculate_factorial(second_number)

final_result = first_result / second_result

print(f'{final_result:.2f}')
