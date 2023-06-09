def happiness_calculation():
    numbers = input().split()
    factor = int(input())

    happiness_numbers = list(map(lambda x: int(x), numbers))

    multiplied_by_factor_happiness = list(map(lambda x: x * factor, happiness_numbers))

    average_happiness = sum(multiplied_by_factor_happiness) / len(multiplied_by_factor_happiness)

    happy_people_list = list(filter(lambda person: person >= average_happiness, multiplied_by_factor_happiness))

    if len(happiness_numbers) / 2 <= len(happy_people_list):
        return f'Score: {len(happy_people_list)}/{len(happiness_numbers)}. Employees are happy!'
    else:
        return f"Score: {len(happy_people_list)}/{len(happiness_numbers)}. Employees are not happy!"


print(happiness_calculation())
