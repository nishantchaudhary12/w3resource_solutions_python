#Write a Python program to print alphabet pattern 'D'.


result_str = ''
for row in range(7):
    for column in range(5):
        if (((column == 0 or column == 4) and row != 0 and row != 6) or ((row == 0 or row == 6) and (column >= 0 and column < 4))):
            result_str = result_str + '*'
        else:
            result_str = result_str + " "
    result_str = result_str + '\n'

print(result_str)

