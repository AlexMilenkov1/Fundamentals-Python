def odd_even_sum(some_number):
    sum_even = 0
    sum_odd = 0

    for num in str(number):
        if int(num) % 2 == 0:
            sum_even += int(num)
        else:
            sum_odd += int(num)

    return sum_even, sum_odd


number = int(input())

even, odd = odd_even_sum(number)

print(f'Odd sum = {odd}, Even sum = {even}')
