def validate_password(passwrd):
    is_valid = True

    if len(passwrd) not in range(6, 11):
        print("Password must be between 6 and 10 characters")
        is_valid = False

    if not passwrd.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False

    digits_count = 0

    for element in passwrd:
        if element.isdigit():
            digits_count += 1

    if digits_count < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    return is_valid


password = input()

validation = validate_password(password)

if validation:
    print('Password is valid')
