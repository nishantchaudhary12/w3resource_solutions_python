#Write a Python program to get variable unique identification number or string.


def unique_id(user_inp):
    return id(user_inp)


def main():
    user_inp = 'abc'
    print(unique_id(user_inp))


main()