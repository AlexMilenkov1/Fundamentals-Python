def check_palindrome(numbers):
    for number in numbers:
        if str(number) == str(number)[::-1]:
            print(True)
        else:
            print(False)


sequence_of_numbers = input().split(', ')

check_palindrome(sequence_of_numbers)
