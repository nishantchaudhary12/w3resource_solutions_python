#Write a Python program to convert a list of multiple integers into a single integer.


def convertInterger(usr_inp):
    str_new = ''
    for each in usr_inp:
        str_new += str(each)
    print('Integer:', str_new)
    num = ''.join(map(str, usr_inp))   #using map function
    print(num)


def main():
    usr_inp = [11, 33, 50]
    convertInterger(usr_inp)


main()