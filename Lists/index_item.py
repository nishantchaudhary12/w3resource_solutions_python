# Write a Python program to find the index of an item in a specified list.


def find_index(list_inp, element):
    index_elem = list_inp.index(element)
    return index_elem


def main():
    list_inp = [1, 4, 6, 3, 6, 3, 9, 10, 12, 45]
    element = 6
    print('Index:',find_index(list_inp, element))


main()
