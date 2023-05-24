key_number = int(input())
lines = int(input())

for i in range(lines):
    current_letter = input()

    index = ord(current_letter)

    needed_char = index + key_number

    transformed_char = chr(needed_char)

    print(transformed_char, end='')
