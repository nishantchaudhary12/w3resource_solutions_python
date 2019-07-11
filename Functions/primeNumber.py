# Write a Python function that takes a number as a parameter and check the number is prime or not


import math


def checkPrime(num):
    flag = True
    for each in range(2, int(math.sqrt(num)+1)):
        if num % each == 0:
            print('It is not a prime number')
            flag = False
            break
    if flag:
        print('It is a prime number')


def main():
    num = 2
    checkPrime(num)


main()