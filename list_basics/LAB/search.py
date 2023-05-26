lines_count = int(input())
special_word = input()

lst = []

for _ in range(lines_count):
    current_string = input()

    lst.append(current_string)

print(lst)

modified_list = []

for string in lst:
    if special_word in string:
        modified_list.append(string)

print(modified_list)
