lines_count = int(input())

positive_nums = []
negative_nums = []

for _ in range(lines_count):
    num = int(input())

    if num >= 0:
        positive_nums.append(num)
    else:
        negative_nums.append(num)

print(positive_nums)
print(negative_nums)
print(f'Count of positives: {len(positive_nums)}')
print(f'Sum of negatives: {sum(negative_nums)}')
