def find_the_wealthiest(people, wealth):
    equal_wealth__list = []
    the_wealthiest_people = []

    for wealthy_person in people:
        if wealthy_person >= wealth:
            the_wealthiest_people.append(wealthy_person)

    poor_people = [person for person in people if person not in the_wealthiest_people]

    sorted_wealthy_people = sorted(the_wealthiest_people, reverse=True)

    interation = 0

    for rich_person in sorted_wealthy_people:
            for poor_person in poor_people:
                get_money_from_rich = wealth - poor_person
                if interation == 0:
                    index = poor_people.index(poor_person)
                    get_rich_index = sorted_wealthy_people.index(rich_person)

                    if rich_person - get_money_from_rich < wealth:
                        break
                    else:
                        rich_person -= get_money_from_rich
                        sorted_wealthy_people[get_rich_index] -= get_money_from_rich
                        poor_people[index] += get_money_from_rich


    final_result = poor_people + sorted_wealthy_people[::-1]

    if all(element >= wealth for element in final_result):
        return final_result
    else:
        return 'No equal distribution possible'



population = [int(number) for number in input().split(', ')]
minimum_wealth = int(input())

print(find_the_wealthiest(population, minimum_wealth))
