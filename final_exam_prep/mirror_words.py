import re

information = input()

pattern = r'([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

matches = re.findall(pattern, information)

palindrome_words = []

for match in matches:
    first_word = match[1]
    second_word = match[2]

    if first_word == second_word[::-1]:
        palindrome_words.append(f'{first_word} <=> {second_word}')

if matches:
    print(f'{len(matches)} word pairs found!')
else:
    print("No word pairs found!")

if palindrome_words:
    print('The mirror words are:')
    print(', '.join(palindrome_words))
else:
    print("No mirror words!")
