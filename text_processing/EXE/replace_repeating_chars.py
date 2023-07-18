string = input()

result = ''
last_char = ''

for character in string:
    if character != last_char:
        last_char = character
        result += character

print(result)
