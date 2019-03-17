# Write a Python program to append a list to the second list.


def main():
    list_inp1 = [4, 6, 4, 7]
    list_inp2 = [3, 6, 9, 12, 45]
    list_inp1.extend(list_inp2)
    print(list_inp1)


main()