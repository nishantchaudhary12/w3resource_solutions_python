#Write a Python program to replace last value of tuples in a list.


def replaceLastVal(tup, num):
    new_tup = list()
    for x, y, z in tup:
        z = num
        new_tup.append((x, y, z))
    print(new_tup)


def main():
    tup = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    replaceWith = 100
    replaceLastVal(tup, replaceWith)
    print([each[:-1] + (100,) for each in tup])


main()