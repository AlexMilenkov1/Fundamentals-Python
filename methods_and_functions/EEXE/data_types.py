def check_data_type(type, data):
    if type == 'int':
        number = float(data)

        return round(number * 2)

    elif type == 'real':
        number = float(data)

        return f"{number * 1.5:.2f}"

    elif type == 'string':
        return f'${data}$'


data_type = input()
element = input()

check_result = check_data_type(data_type, element)

print(check_result)
