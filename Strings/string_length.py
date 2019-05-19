#Write a Python program to calculate the length of a string.

def str_length(user_inp):
    count = 0
    for char in user_inp:
        count += 1
    return count

def main():
    user_inp = input('Enter the string: ')
    print('The length of string is:', str_length(user_inp))

main()

