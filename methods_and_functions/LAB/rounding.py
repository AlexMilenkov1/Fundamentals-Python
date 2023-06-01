string_number = input().split()

float_numbers = []

for string in string_number:
    number = float(string)
    float_numbers.append(number)

rounded_numbers = []

for num in float_numbers:
    rounded_num = round(num)
    rounded_numbers.append(rounded_num)

print(rounded_numbers)
