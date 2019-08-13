#Write a Python program to print alphabet pattern 'E'.


result_str = ''
for row in range(7):
    for column in range(5):
        if ((column == 0 and row != 0 and row != 6 and row != 3) or ((row == 0 or row == 6) and (column >= 0 and column < 5)) or (row == 3 and column < 4)):
            result_str = result_str + '*'
        else:
            result_str = result_str + " "
    result_str = result_str + '\n'

print(result_str)

