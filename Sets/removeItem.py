#Write a Python program to remove item(s) from set


def main():
    x = set([1, 2, 3, 4, 5])
    x.remove(5)
    x.discard(4)
    y = x.pop()
    print(x, y)


main()