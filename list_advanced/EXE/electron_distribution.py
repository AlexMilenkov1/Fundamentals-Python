def filling_shells(current_electrons):
    list_of_shells = []

    index = 1

    while current_electrons > 0:
        maximum_electrons_in_shell = 2 * (index ** 2)

        if maximum_electrons_in_shell > current_electrons:
            list_of_shells.append(current_electrons)
        else:
            list_of_shells.append(maximum_electrons_in_shell)

        current_electrons -= maximum_electrons_in_shell

        index += 1

    return list_of_shells


electrons = int(input())

all_shells = filling_shells(electrons)

print(all_shells)
