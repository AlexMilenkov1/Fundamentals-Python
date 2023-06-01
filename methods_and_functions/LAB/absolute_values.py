number = input().split()

current_nums = []

for num in number:
    float_number = float(num)
    current_nums.append(float_number)

result = []

for value in current_nums:
    absolute_value = abs(value)
    result.append(absolute_value)

print(result)
