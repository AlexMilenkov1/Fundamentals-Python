message = input()

result = ''

for character in message:
        new_message = chr(ord(character) + 3)
        result += new_message

print(result)
