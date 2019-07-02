#Write a Python program to add an item in a tuple.


def main():
    x = (1, 2, 3, 4, 5)
    x = list(x)
    x.append(6)
    x = tuple(x)
    print(x)


main()