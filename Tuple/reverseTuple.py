#Write a Python program to reverse a tuple.


def reverse_tuple(tup):
    tup = tuple(reversed(tup))
    print(tup)


def reverse_tup(tup):
    sorted_list = list()
    for each in range(len(tup)-1, -1, -1):
        sorted_list.append(tup[each])
    print(tuple(sorted_list))


def main():
    tup = (1, 2, 3, 4, 5, 6, 7)
    reverse_tuple(tup)
    reverse_tup(tup)


main()