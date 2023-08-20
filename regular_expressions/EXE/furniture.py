import re

total_cost = 0
furniture = []

pattern = r'>>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)'


line = input()

while line != 'Purchase':
    match = re.search(pattern, line)

    if match:
        bought_furniture, price, quantity = match.groups()
        furniture.append(bought_furniture)
        total_cost += float(price) * int(quantity)

    line = input()

print('Bought furniture:')
for element in furniture:
    print(element)
print(f'Total money spend: {total_cost:.2f}')
