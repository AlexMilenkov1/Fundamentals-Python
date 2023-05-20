first_sting = input()
second_string = input()

last_string = first_sting

length = len(first_sting)

for character in range(1, length + 1):
    left_part = second_string[:character]
    right_part = first_sting[character:]

    full_word = left_part + right_part

    if full_word != last_string:
        last_string = full_word
    else:
        continue

    print(last_string)
