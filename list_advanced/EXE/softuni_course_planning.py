schedule_of_lessons = input().split(', ')

while True:
    command = input().split(':')

    if command[0] == 'course start':
        break

    action = command[0]
    lesson_title = command[1]

    if action == 'Add':
        if lesson_title not in schedule_of_lessons:
            schedule_of_lessons.append(lesson_title)

    elif action == 'Insert':
        if lesson_title not in schedule_of_lessons:
            if 0 <= int(command[2]) <= len(schedule_of_lessons) - 1:
                schedule_of_lessons.insert(int(command[2]), lesson_title)

    elif action == 'Remove':
        if lesson_title in schedule_of_lessons:
            current_index_lesson = schedule_of_lessons.index(lesson_title)
            current_index_exercise = current_index_lesson + 1

            if 0 <= current_index_exercise <= len(schedule_of_lessons) - 1:
                if schedule_of_lessons[current_index_exercise] == f'{lesson_title}-Exercise':
                    schedule_of_lessons.pop(current_index_exercise)

            schedule_of_lessons.pop(current_index_lesson)

    elif action == 'Swap':
        if lesson_title in schedule_of_lessons and command[2] in schedule_of_lessons:
            first_index = schedule_of_lessons.index(lesson_title)
            second_index = schedule_of_lessons.index(command[2])

            first_has_exercise = False
            second_has_exercise = False

            if 0 <= first_index + 1 <= len(schedule_of_lessons) - 1:
                if schedule_of_lessons[first_index + 1] == f'{lesson_title}-Exercise':
                    first_has_exercise = True

            if 0 <= second_index + 1 <= len(schedule_of_lessons) - 1:
                if schedule_of_lessons[second_index + 1] == f'{command[2]}-Exercise':
                    second_has_exercise = True

            if first_has_exercise and second_has_exercise:
                schedule_of_lessons[first_index], schedule_of_lessons[second_index] = schedule_of_lessons[second_index], schedule_of_lessons[first_index]

                schedule_of_lessons[first_index + 1], schedule_of_lessons[second_index + 1] = \
                    schedule_of_lessons[second_index + 1], schedule_of_lessons[first_index + 1]

            elif first_has_exercise:
                schedule_of_lessons[first_index], schedule_of_lessons[second_index] = schedule_of_lessons[second_index], schedule_of_lessons[first_index]
                schedule_of_lessons.remove(f'{lesson_title}-Exercise')
                get_index = schedule_of_lessons.index(lesson_title)
                schedule_of_lessons.insert(get_index + 1, f'{lesson_title}-Exercise')

            elif second_has_exercise:
                schedule_of_lessons[first_index], schedule_of_lessons[second_index] = schedule_of_lessons[second_index], schedule_of_lessons[first_index]
                schedule_of_lessons.remove(f'{command[2]}-Exercise')
                get_index = schedule_of_lessons.index(command[2])
                schedule_of_lessons.insert(get_index + 1, f'{command[2]}-Exercise')

            else:
                schedule_of_lessons[first_index], schedule_of_lessons[second_index] = schedule_of_lessons[second_index], \
                                                                                  schedule_of_lessons[first_index]

    elif action == 'Exercise':
        if lesson_title in schedule_of_lessons:
            lesson_index = schedule_of_lessons.index(lesson_title)
            if 0 <= lesson_index + 1 <= len(schedule_of_lessons):
                if schedule_of_lessons[lesson_index + 1] != f'{lesson_title}-Exercise':
                    schedule_of_lessons.insert(lesson_index + 1, f"{lesson_title}-Exercise")
        else:
            schedule_of_lessons.append(lesson_title)
            schedule_of_lessons.append(f"{lesson_title}-Exercise")

for index, lesson in enumerate(schedule_of_lessons, start=1):
    print(f'{index}.{lesson}')
