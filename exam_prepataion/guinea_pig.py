food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000

for day in range(1, 31):
    food -= 300

    if day % 2 == 0:
        consumed_hay = 0.05 * food
        hay -= consumed_hay
    if day % 3 == 0:
       cover_to_put = 1 / 3 * weight
       cover -= cover_to_put

if food <= 0 or hay <= 0 or cover <= 0:
    print('Merry must go to the pet store!')
else:
    food = food / 1000
    cover = cover / 1000
    hay = hay / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
