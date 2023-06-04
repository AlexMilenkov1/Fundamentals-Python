def is_perfect_number(num):
    sum_of_divisors = 0

    for element in range(1, num):
        if num % element == 0:
            sum_of_divisors += element

    return sum_of_divisors


number = int(input())

final_sum = is_perfect_number(number)

if final_sum == number:
    print('We have a perfect number!')
else:
    print("It's not so perfect.")
