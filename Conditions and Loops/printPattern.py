#Write a Python program to construct the following pattern, using a nested for loop.
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*


def main():
    max_num = 5
    for each in range(1, 10):
        diff = abs(max_num - each)
        for num in range(diff, max_num):
            print('*', end=' ')
        print('')


main()
