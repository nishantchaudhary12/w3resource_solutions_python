#Write a Python program to remove an empty tuple(s) from a list of tuples.


def removeEmpty(tup):
    new_tup = list()
    for each in tup:
        if each:
            new_tup.append(each)
    print(new_tup)


def main():
    tup = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d',)]
    removeEmpty(tup)
    print([each for each in tup if each])


main()