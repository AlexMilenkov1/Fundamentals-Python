sequence_of_numbers_str = input().split()
string = input()

string_list = []

for str in string:
    string_list.append(str)

msg = ''

for num in sequence_of_numbers_str:
    independent_num = []
    for value in num:
        number = int(value)
        independent_num.append(number)

    index = sum(independent_num)

    if index > len(string_list):
        index = index - len(string_list)

    msg += string_list[index]
    del string_list[index]

print(msg)
