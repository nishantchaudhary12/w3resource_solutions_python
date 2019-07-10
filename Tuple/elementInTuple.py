#Write a Python program to check whether an element exists within a tuple.


def main():
    x = ('w', '3', 'r', 'e', 's', 'o', 'u', 'r', 'c', 'e')
    elem = '3'
    if elem in x:
        print('Yes')
    else:
        print('NO')


main()