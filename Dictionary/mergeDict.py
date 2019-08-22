#Write a Python script to merge two Python dictionaries.


def merge_dict(dic1, dic2):
    dict_record = dict()
    dict_record.update(dic1)
    dict_record.update(dic2)
    return dict_record


if __name__ == '__main__':
    dic1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    dic2 = {6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
    print(merge_dict(dic1, dic2))
