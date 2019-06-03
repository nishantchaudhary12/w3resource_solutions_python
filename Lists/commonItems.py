#Write a Python program to find common items from two lists.


def common_item(list_1, list_2):
    set1 = set(list_1)
    set2 = set(list_2)

    return set1 & set2


def main():
    list_1 = [1, 3, 5, 7]
    list_2 = [2, 4, 5, 7, 8]
    print(common_item(list_1, list_2))


main()