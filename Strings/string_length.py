#Write a Python program to calculate the length of a string.

def str_length(user_inp):
    return len(user_inp)

def main():
    user_inp = input('Enter the string: ')
    print('The length of string is:', str_length(user_inp))

main()

