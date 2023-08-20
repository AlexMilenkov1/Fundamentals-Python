phonebook = {}

count = 0

while True:
    contact = input().split('-')

    if contact[0].isdigit():
        count = int(contact[0])
        break

    name, number = contact[0], contact[1]

    phonebook[name] = number

for _ in range(count):
    searched_name = input()

    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
