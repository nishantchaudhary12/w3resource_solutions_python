# Write a Python program to count the number of even and odd numbers from a series of numbers.


def even_odd(numbers):
    even = 0
    odd = 0
    for each in numbers:
        if each % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Odd:", odd, "Even:", even)


def main():
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    even_odd(numbers)


main()