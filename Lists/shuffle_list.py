# Write a Python program to shuffle and print a specified list.


import random


def shuffle(list_inp):
    random.shuffle(list_inp)
    print(list_inp)
    

def main():
    list_inp = [1, 4, 2, 5, 6, 3, 7, 8, 9, 4]
    shuffle(list_inp)


main()