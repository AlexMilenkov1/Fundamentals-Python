def calculation(operator, first_num, second_num):
    if operator == 'multiply':
        return first_num * second_num
    elif operator == 'divide':
        return int(first_num / second_num)
    elif operator == 'add':
        return first_num + second_num
    else:
        return first_num - second_num


operator = input()
number_a = int(input())
number_b = int(input())

calculate = calculation(operator, number_a, number_b)
print(calculate)
