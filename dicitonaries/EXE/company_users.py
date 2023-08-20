companies = {}

while True:
    info = input().split(' -> ')

    if info[0] == 'End':
        break

    company, id_user = info

    if company not in companies.keys():
        companies[company] = []

    if id_user not in companies[company]:
        companies[company].append(id_user)

for company, users in companies.items():
    print(company)
    for user in users:
        print(f'-- {user}')
