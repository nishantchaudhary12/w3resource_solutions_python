#Write a Python program to print alphabet pattern 'L'.


result_str = ''
for row in range(7):
    for column in range(5):
        if ((row == 6) or (column == 0)):
            result_str = result_str + '*'
        else:
            result_str = result_str + " "
    result_str = result_str + '\n'

print(result_str)

