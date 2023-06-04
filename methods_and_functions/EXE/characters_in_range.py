def all_chars_in_between(first, second):
    all_chars = []

    for index in range(ord(first) + 1, ord(second)):
        all_chars.append(chr(index))

    return all_chars


first_char = input()
second_char = input()

result = all_chars_in_between(first_char, second_char)
print(' '.join(result))
