number_of_strings = int(input())

for string in range(number_of_strings):
    word = input()

    if ',' in word or '.' in word or '_' in word:
        print(f"{word} is not pure!")
    else:
        print(f"{word} is pure.")
