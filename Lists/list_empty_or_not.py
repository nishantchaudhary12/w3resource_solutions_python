#Write a Python program to check a list is empty or not.

def empty_or_not(user_inp):
    if not user_inp:
        print('The list is empty')
    else:
        print('The list is not empty')


def main():
    user_inp = [1]
    empty_or_not(user_inp)


main()