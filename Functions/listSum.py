#Write a Python function to sum all the numbers in a list.


def list_sum(num):
    sum_list = 0
    for each in num:
        sum_list += each
    print('Sum:', sum_list)


def main():
    num = [1, 2, 3, 4, 5]
    list_sum(num)


main()
