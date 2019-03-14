#Write a Python program to remove duplicates from a list.


def rem_duplicates(usr_inp):
    without_dup = list()
    for item in range(len(usr_inp)):
        first = usr_inp[item]
        if first not in without_dup:
            without_dup.append(first)

    return without_dup


def main():
    usr_inp = [1, 3, 5, 2, 6, 1, 7, 8, 2, 0, 9, 5, 8, 2, 4, 5]
    print('The list after removing after all the duplicates:',rem_duplicates(usr_inp))


main()