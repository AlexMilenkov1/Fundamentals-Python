word = input()

index_list = []

for index, letter in enumerate(word):
    if letter.isupper():
        index_list.append(index)

print(index_list)
