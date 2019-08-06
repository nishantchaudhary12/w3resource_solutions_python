# Write a Python function to check whether a number is perfect or not.


def perfect_number(num):
    sum = 0
    for each in range(1, num+1):
        if num % each == 0:
            sum += each
    if sum // 2 == num:
        print('Yes')
    else:
        print('No')


def main():
    num = 496
    perfect_number(num)


main()