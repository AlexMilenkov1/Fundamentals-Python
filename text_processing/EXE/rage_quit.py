text = input().upper()

number = ''
characters_to_repeat = ''
result = ''

for i in range(len(text)):
    if not text[i].isdigit():
        characters_to_repeat += text[i]
    else:
        for index in range(i, len(text)):
            if text[index].isdigit():
                number += text[index]
            else:
                break

        result += characters_to_repeat * int(number)
        number = ''
        characters_to_repeat = ''

unique_chars = ''

for char in result:
    if char not in unique_chars:
        unique_chars += char

print(f'Unique symbols used: {len(unique_chars)}')
print(result)
