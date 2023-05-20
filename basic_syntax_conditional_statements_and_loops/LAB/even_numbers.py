n = int(input())

for i in range(n):
    number = int(input())

    if number % 2 != 0:
        print(f'{number} is odd!')
        exit()

print('All numbers are even.')
