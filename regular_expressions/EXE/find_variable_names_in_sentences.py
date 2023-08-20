import re

line = input()

pattern = r"\b_([a-zA-Z0-9]+)\b"

match = re.findall(pattern, line)

print(','.join(match))
