strings = input().split()

total_sum = 0

word_a, word_b = strings

if len(word_a) > len(word_b):
    for index in range(len(word_b)):
        total_sum += ord(word_a[index]) * ord(word_b[index])

    for i in range(len(word_b), len(word_a)):
        total_sum += ord(word_a[i])

elif len(word_a) < len(word_b):
    for index in range(len(word_a)):
        total_sum += ord(word_a[index]) * ord(word_b[index])

    for i in range(len(word_a), len(word_b)):
        total_sum += ord(word_b[i])

else:
    for index in range(len(word_a)):
        total_sum += ord(word_a[index]) * ord(word_b[index])

print(total_sum)
