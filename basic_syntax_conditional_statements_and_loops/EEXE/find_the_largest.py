number = int(input())

number_str = str(number)

list_of_numbers = []

for num in number_str:
    list_of_numbers.append(num)

list_of_numbers.sort(reverse=True)

for element in list_of_numbers:
    print(element, end='')
