#Write a Python program to calculate the sum of a list of numbers.


def sumNumbers(i, numbers):
    if i == len(numbers):
        return 0
    else:
        curr = numbers[i]
        i += 1
        return curr + sumNumbers(i, numbers)


def sumNums(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + sumNums(numbers[1:])


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sumNumbers(0, numbers))
    print(sumNums(numbers))


main()