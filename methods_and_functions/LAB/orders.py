def calculate_bill(product, quantity):
    if product == 'coffee':
        return quantity * 1.50
    elif product == 'water':
        return quantity * 1
    elif product == 'coke':
        return quantity * 1.40
    elif product == 'snacks':
        return quantity * 2


product_name = input()
quantity_of_product = int(input())

calculation = calculate_bill(product_name, quantity_of_product)
print(f'{calculation:.2f}')
