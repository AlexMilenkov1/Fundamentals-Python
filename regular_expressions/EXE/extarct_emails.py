import re

line = input()

pattern = r'\s(([a-z0-9]+[\.\-\_]?[a-z0-9]+)@([a-z\-]+)(\.[a-z]+)+)'

match = re.findall(pattern, line)

for element in match:
    print(element[0])
