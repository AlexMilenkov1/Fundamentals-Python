the_neighbourhood_hearts = [int(heart) for heart in input().split('@')]

index = 0

while True:
    jump = input().split()

    if jump[0] == 'Love!':
        break

    jump_length = int(jump[1])

    index += jump_length

    if index > len(the_neighbourhood_hearts) - 1:
        index = 0

    if the_neighbourhood_hearts[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        the_neighbourhood_hearts[index] -= 2

        if the_neighbourhood_hearts[index] == 0:
            print(f"Place {index} has Valentine's day." )

print(f"Cupid's last position was {index}.")

if all(element == 0 for element in the_neighbourhood_hearts):
    print("Mission was successful.")
else:
    count = len([value for value in the_neighbourhood_hearts if value != 0])
    print(f"Cupid has failed {count} places.")
