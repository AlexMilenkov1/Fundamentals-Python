number_of_lines = int(input())

string_list = []
left_brackets = []
right_brackets = []

for i in range(number_of_lines):
    string = input()

    if string == '(':
        string_list.append('(')
    elif string == ')':
        string_list.append(')')
    else:
        continue

for bracket in string_list:
    if bracket == '(':
        left_brackets.append(bracket)
    else:
        right_brackets.append(bracket)

if len(left_brackets) == len(right_brackets):
    print('BALANCED')
else:
    print('UNBALANCED')
