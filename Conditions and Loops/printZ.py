#Write a Python program to print alphabet pattern 'Z'.


result_str = ''
for row in range(7):
    for column in range(7):
        if (((row == 0 or row == 6) and column >= 0 and column <= 6) or row+column==6):
            result_str = result_str + '*'
        else:
            result_str = result_str + " "
    result_str = result_str + '\n'

print(result_str)

