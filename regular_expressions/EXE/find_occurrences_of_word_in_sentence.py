import re

line = input()
searched_word = input()

pattern = fr'\b{searched_word}\b'

match = re.findall(pattern, line, re.IGNORECASE)

print(len(match))
