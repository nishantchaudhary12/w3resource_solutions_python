#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).


def generate_dict(n):
    dict_record = dict()
    for each in range(1, n+1):
        dict_record[each] = each * each
    return dict_record


if __name__ == '__main__':
    n = 5
    print(generate_dict(n))
