import re

travel_points = 0
locations = []

pattern = r'([=|\/])([A-Z][A-Za-z]{2,})\1'

current_locations = input()

matches = re.findall(pattern, current_locations)

for match in matches:
    locations.append(match[1])
    travel_points += len(match[1])

if matches:
    print(f"Destinations: {', '.join(locations)}")
    print(f'Travel Points: {travel_points}')

else:
    print("Destinations:")
    print("Travel Points: 0")