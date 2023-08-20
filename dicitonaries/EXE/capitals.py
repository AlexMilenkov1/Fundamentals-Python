countries = input().split(', ')
capitals = input().split(', ')

info = {countries[index]: capitals[index] for index in range(len(countries))}

for country, capital in info.items():
    print(f'{country} -> {capital}')
