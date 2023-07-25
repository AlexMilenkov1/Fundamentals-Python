import re

total_cal = 0
days = 0

info = input()

pattern = r'([#|\|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,4}|10000)\1'

matches = re.findall(pattern, info)

for match in matches:
    total_cal +=  int(match[3])

days = total_cal // 2000

print(f"You have food to last you for: {days} days!")
for match in matches:
    print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")
