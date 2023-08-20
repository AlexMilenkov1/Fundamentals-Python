unready_tickets = input().split(', ')

tickets = [ticket.strip() for ticket in unready_tickets if ticket != ' ']

for ticket in tickets:
    if len(ticket) == 20:
        left_part = ticket[0:10]
        right_part = ticket[10:]

        wining_symbols = ['@', '#', '$', '^']

        count_of_symbols = 0
        found_win = False
        match_symbol = ''

        for symbol in wining_symbols:
            for number in range(10, 5, -1):
                if number == left_part.count(symbol) and number == right_part.count(symbol):
                    count_of_symbols = number
                    found_win = True
                    match_symbol = symbol
                    break

            if found_win:
                break

        if count_of_symbols == 10:
            print(f'ticket "{ticket}" - {count_of_symbols}{match_symbol} Jackpot!')
        elif 6 <= count_of_symbols < 10:
            print(f'ticket "{ticket}" - {count_of_symbols}{match_symbol}')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")
