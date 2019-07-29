#Write a Python program to convert a tuple to a dictionary.


def main():
    x = ((1, 2), (3, 4), (5, 6))
    x = dict((i, j) for i, j in x)
    print(x)


main()