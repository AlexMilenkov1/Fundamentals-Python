coffe_count = 0

while True:
    command = input()

    if command == "END":
        break

    if command.isupper():
        if command == "coding".upper():
            coffe_count += 2
        elif command == 'dog'.upper() or command == 'cat'.upper():
            coffe_count += 2
        elif command == 'movie'.upper():
            coffe_count += 2
        else:
            continue
    else:
        if command == "coding":
            coffe_count += 1
        elif command == 'dog' or command == 'cat':
            coffe_count += 1
        elif command == 'movie':
            coffe_count += 1
        else:
            continue

if coffe_count > 5:
    print('You need extra sleep')
else:
    print(coffe_count)
