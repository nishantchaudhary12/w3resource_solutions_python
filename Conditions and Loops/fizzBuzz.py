# Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".


def printFizzBuzz(num):
    for each in range(num + 1):
        if each % 3 == 0 and each % 5 == 0:
            print('FizzBuzz')
        elif each % 3 == 0:
            print('Fizz')
        elif each % 5 == 0:
            print('Buzz')
        else:
            print(each)


def main():
    num = 50
    printFizzBuzz(num)


main()