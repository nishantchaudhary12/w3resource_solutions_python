#Write a Python program to remove an item from a tuple.


def main():
    x = (1, 2, 3, 4, 5)
    x = list(x)
    x.remove(5)
    x = tuple(x)
    print(x)


main()