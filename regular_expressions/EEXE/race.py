import re

list_of_participants = input().split(', ')

participants = {}

while True:
    line = input()

    if line == 'end of race':
        break

    letters_pattern =  '[A-Za-z]+'
    digits_pattern = r'\d'

    matches_letters = re.findall(letters_pattern, line)
    matches_digits = re.findall(digits_pattern, line)

    name = ''
    digits = [int(digit) for digit in matches_digits]
    ran = sum(digits)

    for match in matches_letters:
        name += match


    if name in list_of_participants:
        if name not in participants.keys():
            participants[name] = [0, name]
        participants[name][0] += ran


sorted_items = sorted(participants.items(), key=lambda item: item[1], reverse=True)
sorted_dict = dict(sorted_items)

result = []

count = 0
for player in sorted_dict.keys():
    result.append(sorted_dict[player])
    count += 1

    if count == 3:
        break

print(f'''1st place: {result[0][1]}
2nd place: {result[1][1]}
3rd place: {result[2][1]}''')

