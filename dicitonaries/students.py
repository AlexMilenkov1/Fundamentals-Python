students_dictionary = {}

while True:
    students_info = input().split(':')

    if len(students_info) < 3:
        without_snakecase = students_info[0].replace('_', ' ')
        for key in students_dictionary.keys():
            if key == without_snakecase:
                print('\n'.join(students_dictionary[key]))

        break

    course = students_info[2]
    id_student = students_info[1]
    name_of_student = students_info[0]

    if course not in students_dictionary.keys():
        students_dictionary[course] = []

    students_dictionary[course].append(f'{name_of_student} - {int(id_student)}')



