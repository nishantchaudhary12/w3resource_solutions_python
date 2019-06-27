#Write a Python script to check if a given key already exists in a dictionary.


def checkKey(dic1, key):
    if key in dic1:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    dic1 = {1: 10, 2: 20}
    key = 2
    checkKey(dic1, key)