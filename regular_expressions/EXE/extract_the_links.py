import re

emails = input()

pattern = r'((w{3})\.([A-Za-z\d\-]+)(\.[a-z]+)+)'

results = []

while emails != '':
    match = re.search(pattern, emails)

    if match:
        results.append(match.group(0))


    emails = input()

for email in results:
    print(email)
