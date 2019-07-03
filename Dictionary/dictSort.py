#Write a Python program to sort (ascending and descending) a dictionary by value.


def asc_sort(usr_inp):
    result = sorted(usr_inp.items(), key = lambda x : x[1])
    return result


def desc_sort(usr_inp):
    result = sorted(usr_inp.items(), key = lambda x : x[1], reverse=True)
    return result


if __name__ == '__main__':
    usr_inp = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    print('Ascending:', asc_sort(usr_inp))
    print('Descending:', desc_sort(usr_inp))