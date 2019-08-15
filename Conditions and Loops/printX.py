#Write a Python program to print alphabet pattern 'X'.


result_str = ''
for row in range(7):
    for column in range(7):
        if (((column == 1 or column == 5) and (row > 4 or row < 2)) or row == column and column > 0 and column < 6 or (column == 2 and row == 4) or (column == 4 and row == 2)):
            result_str = result_str + '*'
        else:
            result_str = result_str + " "
    result_str = result_str + '\n'

print(result_str)
print ("testing_git")
