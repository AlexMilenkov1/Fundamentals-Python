import re

line = input()

nums = []

pattern = r'\d+'

while line != '':
    match = re.findall(pattern, line)

    for element in match:
        nums.append(element)

    line = input()

for number in nums:
    print(number, end=' ')
