while True:
    string = input()

    if string == 'end':
        break

    new_string =  f"{string} = {string[::-1]}"

    print(new_string)
