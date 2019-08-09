#Write a Python program to print alphabet pattern 'G'.


result_str = ''
for row in range(7):
    for column in range(5):
        if (((row == 0 or row == 6) and (column > 0 and column < 4)) or (row == 3 and (column != 1)) or (row == 2 and column == 0) or ((row == 1 or row == 4 or row == 5) and (column == 0 or column == 4))):
            result_str = result_str + '*'
        else:
            result_str = result_str + " "
    result_str = result_str + '\n'

print(result_str)

