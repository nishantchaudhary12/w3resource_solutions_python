#Write a Python function to multiply all the numbers in a list.


def list_multiply(num):
    mul_list = 1
    for each in num:
        mul_list *= each
    print(mul_list)


def main():
    num = [1, 2, 3, 4, 5]
    list_multiply(num)


main()
