sequence = input().split()
sequence = [item.lower() for item in sequence]

dictionary = {}

for element in sequence:
    if element not in dictionary.keys():
        dictionary[element] = 1
    else:
        dictionary[element] += 1

for key in dictionary.keys():
    if dictionary[key] % 2 != 0:
        print(key, end=' ')
