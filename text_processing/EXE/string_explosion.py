sequence_of_characters = input()

result = ''
power_of_explosion = 0

for index in range(len(sequence_of_characters)):
    if power_of_explosion > 0 and sequence_of_characters[index] != ">":
        power_of_explosion -= 1

    elif sequence_of_characters[index] == '>':
        result += sequence_of_characters[index]
        power_of_explosion += int(sequence_of_characters[index + 1])

    else:
        result += sequence_of_characters[index]

print(result)
