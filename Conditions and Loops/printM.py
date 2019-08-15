#Write a Python program to print alphabet pattern 'M'.


result_str = ''
for row in range(7):
    for column in range(7):
        if (column == 1 or column == 5 or (row == 1 and (column == 2 or column == 4)) or (row == 2 and column == 3)):
            result_str = result_str + '*'
        else:
            result_str = result_str + " "
    result_str = result_str + '\n'

print(result_str)

