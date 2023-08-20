count = int(input()) * 2

synonyms_dict = {}

words = []

for _ in range(count):
    word = input()

    words.append(word)

for i in range(0, len(words), 2):
    if words[i] not in synonyms_dict.keys():
        synonyms_dict[words[i]] = []

    synonyms_dict[words[i]].append(words[i + 1])

for key, value in synonyms_dict.items():
    print(f"{key} - {', '.join(value)}")
