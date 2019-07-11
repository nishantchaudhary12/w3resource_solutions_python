#Write a Python program to unpack a tuple in several variables.


def main():
    x = tuple()
    x = (1, 2, 3, 4, 5)
    a, b, c, d, e = x
    print(a, b, c, d, e)


main()