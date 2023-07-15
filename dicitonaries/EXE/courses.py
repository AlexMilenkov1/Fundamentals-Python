course = {}

while True:
    info = input().split(' : ')

    if info[0] == 'end':
        break

    course_name = info[0]
    person_name = info[1]

    if course_name not in course.keys():
        course[course_name] = []

    course[course_name].append(person_name)

for name, people in course.items():
    print(f'{name}: {len(course[name])}')
    for person in people:
        print(f'-- {person}')
