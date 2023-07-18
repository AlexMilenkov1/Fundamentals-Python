def is_valid(user):
    if check_length(user) and contain_certain_characters(user) and no_redundant_symbols(user):
        return True
    return False

def check_length(user):
    if 3 <= len(user) <= 16:
        return True
    return False

def contain_certain_characters(user):
    validation = True
    for character in user:
        if character.isalnum() or character == '-' or character == '_':
            validation = True
        else:
            validation = False
            break

    if validation:
        return True
    else:
        return False

def  no_redundant_symbols(user):
    if ' ' in user:
        return False
    return True


usernames = input().split(', ')

for username in usernames:
    if is_valid(username):
        print(username)
