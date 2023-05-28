deck_of_card = input().split()
counts_of_shuffle = int(input())

for shuffle in range(counts_of_shuffle):
    current_deck = []

    middle_of_deck = len(deck_of_card) // 2
    left_part = deck_of_card[:middle_of_deck]
    right_part = deck_of_card[middle_of_deck:]

    for index in range(len(left_part)):
        current_deck.append(left_part[index])
        current_deck.append(right_part[index])

    deck_of_card = current_deck

print(deck_of_card)
