#Write a Python program to iterate over dictionaries using for loops.


def iteration(dic1):
    for x in dic1.keys():
        print(x, '-', dic1[x])


if __name__ == '__main__':
    dic1 = {1: 10, 2: 20, 3:30, 4:40}
    iteration(dic1)
    