#Write a Python function to find the Max of three numbers.


def max_number(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            print(num1)
        else:
            print(num3)
    elif num3 > num2:
        print(num3)
    else:
        print(num2)


def main():
    num1 = 111
    num2 = 12
    num3 = 999
    max_number(num1, num2, num3)


main()
