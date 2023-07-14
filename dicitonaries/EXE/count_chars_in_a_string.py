characters = [char for char in input() if char != ' ']

occurrences = {}

for symbol in characters:
    if symbol not in occurrences.keys():
        occurrences[symbol] = 0
    occurrences[symbol] += 1

for key, value in occurrences.items():
    print(f'{key} -> {value}')
