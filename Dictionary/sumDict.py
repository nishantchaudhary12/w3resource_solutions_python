#Write a Python program to sum all the items in a dictionary.


def sum_dict(dic1):
    sum_dict = 0
    for each in dic1.keys():
        sum_dict += dic1[each]
    print('Sum:', sum_dict)


if __name__ == '__main__':
    dic1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    sum_dict(dic1)
