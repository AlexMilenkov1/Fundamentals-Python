some_words = input().split()

check_even_length = [word for word in some_words if len(word) % 2 == 0]

print('\n'.join(check_even_length))
