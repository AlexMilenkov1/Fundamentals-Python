registered_users = {}

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()

    if command[0] == 'register':
        username = command[1]
        plate_number = command[2]

        if username not in registered_users.keys():
            registered_users[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered_users[username]}")

    else:
        username = command[1]

        if username not in registered_users.keys():
            print(f"ERROR: user {username} not found")
        else:
            del registered_users[username]
            print(f"{username} unregistered successfully")

for user, license_number in registered_users.items():
    print(f'{user} => {license_number}')
