#Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.


def check(user_inp):
    elements = list()
    for item in user_inp:
        if len(item) > 1:
            if item[0] == item[-1]:
                elements.append(item)
    return len(elements)


def main():
    user_inp = ['aba', '12321', '1234', '9876', 'abc']
    print('The number of strings where the string length is 2 or more\
    and the first and last character are same:', check(user_inp))



main()

