#Write a Python program to iterate over dictionaries using for loops.


def iterate_dict(dic1):
    for each in dic1.keys():
        print(each, '-', dic1[each])


if __name__ == '__main__':
    dic1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    iterate_dict(dic1)
