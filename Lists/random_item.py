# Write a Python program to select an item randomly from a list.


import random


def random_elem(list_inp):
    index_item = random.randint(0, len(list_inp)-1)
    return list_inp[index_item]


def main():
    list_inp = [4, 6, 4, 7, 12, 15, 10]
    print(random_elem(list_inp))


main()