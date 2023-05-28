items = input().split(', ')
count_of_beggars = int(input())

money = []
final_sum = []

for item in items:
    money.append(int(item))

start_index = 0

while start_index < count_of_beggars:
    current_payment = 0
    for element in range(start_index, len(money), count_of_beggars):
        current_payment += money[element]

    final_sum.append(current_payment)
    start_index += 1

print(final_sum)
