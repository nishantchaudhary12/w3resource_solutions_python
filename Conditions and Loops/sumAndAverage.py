#Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.


def sumAndAverage(data):
    if data:
        print('Sum:', sum(data))
        print('Average:', sum(data)/len(data))


def main():
    num = int(input('Enter a number(0 to exit): '))
    data = list()
    while num != 0:
        data.append(num)
        num = int(input('Enter a number(0 to exit): '))
    sumAndAverage(data)


main()