#Write a Python program to print a tuple with string formatting.


def formatting(tup):
    print('This is a list of tuples: {}'.format(tup))


def main():
    tup = [(1, 'a'), (2, 'b'), (3, 'c'), (1, 'f'), (3, 'x')]
    formatting(tup)


main()