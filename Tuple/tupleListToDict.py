#Write a Python program to convert a list of tuples into a dictionary.


def tupleToDict(tup):
    new_dict = dict()
    for each in tup:
        new_dict.setdefault(each[0], []).append(each[1])
    print(new_dict)


def main():
    tup = [(1, 'a'), (2, 'b'), (3, 'c'), (1, 'f'), (3, 'x')]
    tupleToDict(tup)


main()