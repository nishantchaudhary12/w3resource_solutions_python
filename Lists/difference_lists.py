# Write a Python program to get the difference between the two lists.


def difference(list1, list2):
    return (set(list1) - set(list2))


def main():
    list1 = [1, 4, 5, 3, 6, 8]
    list2 = [3, 5, 2, 5, 7]
    print(difference(list1, list2))


main()

'''
#another method

def difference(list1, list2):
    list_new = list()
    for num in list1:
        if num in list1 and num not in list2:
            list_new.append(num)
    return list_new


def main():
    list1 = [1, 4, 5, 3, 6, 8]
    list2 = [3, 5, 2, 5, 7]
    print(difference(list1, list2))


main()

'''



