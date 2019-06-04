#Write a Python program to create a list by concatenating a given list which range goes from 1 to n.


def concatenate_list(sample_list, n):
    new_list = list()
    for item in sample_list:
        for each in range(1, n+1):
            new_list.append(item + str(each))

    return new_list


def main():
    sample_list = ['p', 'q']
    n = 5
    print(concatenate_list(sample_list, n))


main()