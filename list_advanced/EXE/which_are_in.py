def find_substrings(first, second):
    substrings = []

    for f in first:
        for s in second:
            if f in s:
                substrings.append(f)
                break

    return substrings


first_sequence = input().split(', ')
second_sequence = input().split(', ')

print(find_substrings(first_sequence, second_sequence))
