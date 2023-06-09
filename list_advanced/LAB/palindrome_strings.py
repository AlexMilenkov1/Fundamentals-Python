def is_palindrome(current_words):
    palindromes = []

    for word in current_words:
        if word == word[::-1]:
            palindromes.append(word)

    return palindromes


words = input().split()
palindrome = input()

result = is_palindrome(words)
print(result)
print(f'Found palindrome {result.count(palindrome)} times')
