#Write a Python script to concatenate following dictionaries to create a new one


def concatenate(dic1, dic2, dic3):
    dic_new = dict()
    for dic in dic1, dic2, dic3:
        dic_new.update(dic)
    print(dic_new)


if __name__ == '__main__':
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    concatenate(dic1, dic2, dic3)