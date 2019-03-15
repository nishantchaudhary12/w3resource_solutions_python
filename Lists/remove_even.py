# Write a Python program to print the numbers of a specified list after removing even numbers from it.


def rem_even(list_inp):
    rem = [num for num in list_inp if num%2 != 0]
    print(rem)


def main():
    list_inp = [1,4,2,5,6,3,7,8,9,4]
    rem_even(list_inp)


main()