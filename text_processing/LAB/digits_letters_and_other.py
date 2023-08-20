text = input()

digits = ""
letters = ""
characters = ""

for symbol in text:
    if symbol.isdigit():
        digits += symbol
    elif symbol.isalpha():
        letters += symbol
    else:
        characters += symbol

print(digits)
print(letters)
print(characters)
