def loading_bar(num):
    if number == 100:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    else:
        times_to_multiply_percent = num // 10
        print(f'{num}% [{"%" * times_to_multiply_percent}{"." * (10 - times_to_multiply_percent)}]')
        print('Still loading...')


number = int(input())

loading_bar(number)
