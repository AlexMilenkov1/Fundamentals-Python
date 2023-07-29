import re

text = input()

threshold = 1

pattern_1 = r'\d'
digits = re.findall(pattern_1, text)

for digit in digits:
    threshold *= int(digit)

cool_emojis = []

pattern_2 = r'(::)([A-Z][a-z]{2,})(::)|(\*\*)([A-Z][a-z]{2,})(\*\*)'

matches = re.findall(pattern_2, text)

for match in matches:
    check = 0

    for letter in match[1]:
        check += ord(letter)

    if check >= threshold:
        if match[0] == '::':
            cool_emojis.append(f'::{match[1]}::')
        else:
            cool_emojis.append(f'**{match[1]}**')

print(f'Cool threshold: {threshold}')
print(f'{len(matches)} emojis found in the text. The cool ones are:')
for cool_emoji in cool_emojis:
    print(cool_emoji)





