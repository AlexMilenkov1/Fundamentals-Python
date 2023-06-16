def check_for_distribution(rich_people, wealth, money):
    the_richest_person = max(rich_people)

    if the_richest_person - money < wealth:
        return False
    return True


def find_the_wealthiest(people, wealth):
    equal_wealth__list = []
    the_wealthiest_people = []

    for wealthy_person in people:
        if wealthy_person >= wealth:
            the_wealthiest_people.append(wealthy_person)

    poor_people = [person for person in people if person not in the_wealthiest_people]

    sorted_wealthy_people = sorted(the_wealthiest_people, reverse=True)

    no_distribution = False

    for rich_person in sorted_wealthy_people:
            for poor_person in poor_people:

                get_money_from_rich = wealth - poor_person
                result = check_for_distribution(sorted_wealthy_people, wealth, get_money_from_rich)

                if result:
                        index = poor_people.index(poor_person)
                        poor_people[index] += get_money_from_rich
                        rich_person -= get_money_from_rich

                        if rich_person - get_money_from_rich < wealth:
                            break
                else:
                    return 'No equal distribution possible'
    
    return poor_people


population = [int(number) for number in input().split(', ')]
minimum_wealth = int(input())

print(find_the_wealthiest(population, minimum_wealth))
