file_path = input().split("\\")
file = file_path[-1].split('.')

print(f'File name: {file[-2]}')
print(f'File extension: {file[-1]}')
