names_list = input().split(', ')

sorted_names = sorted(names_list, key=lambda name: (-len(name), name))

print(sorted_names)
