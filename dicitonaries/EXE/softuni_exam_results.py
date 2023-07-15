results = {}
submissions = {}

while True:
    info = input()

    if info == 'exam finished':
        break

    new_info = info.split('-')

    if new_info[1] == 'banned':
        user = new_info[0]

        del results[user]
    else:
        name, language, points = new_info[0], new_info[1], int(new_info[2])

        if name not in results.keys():
            results[name] = 0
            results[name] += points
        else:
            if results[name] < points:
                results[name] = points

        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1

print('Results:')
for name, points in results.items():
    print(f'{name} | {points}')
print('Submissions:')
for language, count in submissions.items():
    print(f'{language} - {count}')
