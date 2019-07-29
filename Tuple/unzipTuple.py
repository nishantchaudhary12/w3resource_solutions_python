#Write a Python program to unzip a list of tuples into individual lists.


def unzip_tuple(tup):
    result = list(zip(*tup))
    print(result)


def unzip_tup(tup):
    tup = [[i for i, j in tup], [j for i, j in tup]]
    print(tup)


def main():
    tup = [(1, 'a'), (2, 'b'), (3, 'c')]
    unzip_tuple(tup)
    unzip_tup(tup)


main()