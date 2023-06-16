first_employee_capacity = int(input())
second_employee_capacity = int(input())
third_employee_capacity = int(input())
all_students = int(input())

max_students_answer_per_hour = first_employee_capacity + second_employee_capacity + third_employee_capacity

hours = 0

while all_students > 0:
    all_students -= max_students_answer_per_hour
    hours += 1

    if hours % 4 == 0 and hours != 0:
        hours += 1
        continue

print(f"Time needed: {hours}h.")
