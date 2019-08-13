#Write a Python program to print alphabet pattern 'T'.


result_str = ''
for row in range(7):
    for column in range(7):
        if (column == 3 or (row == 0 and column > 0 and column <6)):
            result_str = result_str + '*'
        else:
            result_str = result_str + " "
    result_str = result_str + '\n'

print(result_str)

