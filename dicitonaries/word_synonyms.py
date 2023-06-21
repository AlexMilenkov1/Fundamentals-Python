count = int(input()) * 2

synonyms_dict = {}

words = []

for _ in range(count):
    word = input()
    words.append(word)


for i in range(1, len(words), 2):
    if words[i] % 2 != 0:
        if words[i] not in synonyms_dict.keys():
            synonyms_dict[words[i]] = []
    synonyms_dict[words[i]] += words[i + 1]
