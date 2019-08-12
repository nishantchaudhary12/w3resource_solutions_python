#Write a Python program to guess a number between 1 to 9.


import random


def main():
    num = random.randint(1, 9)
    guess = 0
    while guess != num:
        guess = int(input('Guess the number: '))
    print('Your Guess was right')


main()
