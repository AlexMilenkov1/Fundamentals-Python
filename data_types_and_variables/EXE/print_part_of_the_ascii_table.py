start_char_index = int(input())
end_char_index = int(input())

for i in range(start_char_index, end_char_index + 1):
    print(chr(i), end=' ')
