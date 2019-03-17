# Write a Python program to find the second smallest number in a list.


def second_smallest(list_inp):
    smallest = min(list_inp)
    second_small = min([i for i in list_inp if i != smallest])
    print('The second smallest element in the list is:', second_small)


def main():
    list_inp = [3, 6, 4, 7, 12, 15, 10, 3]
    second_smallest(list_inp)


main()