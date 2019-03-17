# Write a Python program to find the second largest number in a list.


def second_largest(list_inp):
    largest = max(list_inp)
    second_large = max([i for i in list_inp if i != largest])
    print('The second largest element in the list is:', second_large)


def main():
    list_inp = [3, 6, 4, 7, 12, 15, 10, 3]
    second_largest(list_inp)


main()