import re

pattern = r'(%([A-Z][a-z]+)%([^|$%.]?)<(\w+)>([^|$%.]?)\|(\d+)([^|$%.]?)\|(\d+\.\d*)\$)'

total_income = 0

while True:
    info = input()

    if info == 'end of shift':
        print(f'Total income: {total_income:.2f}')
        break

    matches = re.findall(pattern, info)


    for match in matches:
        customer, product, count, price = match[1], match[3], int(match[5]), float(match[7])

        income = count * price

        total_income += income

        print(f'{customer}: {product} - {income}')

