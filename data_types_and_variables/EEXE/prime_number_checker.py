number = int(input())

is_prime = True

for num in range(2, number):
    if number % num == 0:
        is_prime = False

print(is_prime)
