import re

lines = int(input())

pattern = r'@#+([\^A-Z][a-zA-Z\d]{4,}[A-Z\$])@#+'

digits = ''

for _ in range(lines):
    information = input()
    match = re.search(pattern, information)

    if match:
            for valid_barcode in match.group(1):
                for element in valid_barcode:
                    if element.isdigit():
                        digits += element

            if digits:
                print(f'Product group: {digits}')
                digits = ''
            else:
                print('Product group: 00')
    else:
        print('Invalid barcode')
