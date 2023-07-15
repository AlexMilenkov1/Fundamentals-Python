students_grades = {}

number_of_pairs = int(input())

for _ in range(number_of_pairs):
    student = input()
    grade = float(input())

    if student not in students_grades.keys():
        students_grades[student] = []

    students_grades[student].append(grade)

for name, grade in students_grades.items():
    average = sum(students_grades[name]) / len(students_grades[name])
    if average >= 4.50:
        print(f'{name} -> {average:.2f}')
