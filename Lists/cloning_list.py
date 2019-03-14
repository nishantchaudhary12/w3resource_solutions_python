#Write a Python program to clone or copy a list.


def clone(user_inp):
    copy = list()
    for item in user_inp:
        copy.append(item)
    return copy


def main():
    user_inp = [1,2,3,4,5]
    print('Original:',user_inp)
    print('Copy:',clone(user_inp))


main()