text = input().split()

total_sum = 0

for characters in text:
    first_letter = characters[0]
    second_letter = characters[-1]
    number = int(characters[1:-1])

    if first_letter.isupper():
        total_sum += number / (ord(first_letter) - 64)
    else:
        total_sum += number * (ord(first_letter) - 96)

    if second_letter.isupper():
        total_sum -= ord(second_letter) - 64
    else:
        total_sum += ord(second_letter) - 96

print(f"{total_sum:.2f}")
