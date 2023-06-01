repeat_string = lambda str, times_to_repeat: str * times_to_repeat

string = input()
count = int(input())

result = repeat_string(string, count)
print(result)
