first_line = input().split()
second_line = input().split()
third_line = input().split()

first_lines_lst = []
second_lines_lst = []
third_lines_lst = []

found = False

for string in first_line:
    num = int(string)
    first_lines_lst.append(num)

for string in second_line:
    num = int(string)
    second_lines_lst.append(num)

for string in third_line:
    num = int(string)
    third_lines_lst.append(num)

for player in range(1, 3):
    line = [player, player, player]

    if first_lines_lst == line or second_lines_lst == line or third_lines_lst == line:
        found = True

    for i in range(0, 3):
        if first_lines_lst[i] == player and second_lines_lst[i] == player and third_lines_lst[i] == player:
            found = True

    if first_lines_lst[0] == player and second_lines_lst[1] == player and third_lines_lst[2] == player:
        found = True
    elif first_lines_lst[2] == player and second_lines_lst[1] == player and third_lines_lst[0] == player:
        found = True

    if found:
        if player == 1:
            print('First player won')
        else:
            print('Second player won')
        break
else:
    print('Draw!')
