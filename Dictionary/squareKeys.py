#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.


def generate_dict(n):
    dict_record = dict()
    for each in range(1, n+1):
        dict_record[each] = each * each
    return dict_record


if __name__ == '__main__':
    n = 15
    print(generate_dict(n))
