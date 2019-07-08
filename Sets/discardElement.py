#Write a Python program to remove an item from a set if it is present in the set.


def main():
    x = set([1, 2, 3, 4, 5])
    x.discard(4)
    print(x)


main()