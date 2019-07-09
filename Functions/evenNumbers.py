# Write a Python program to print the even numbers from a given list.


def even_numbers(sample_list):
    for each in sample_list:
        if each % 2 == 0:
            yield each


def main():
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list(even_numbers(sample_list)))


main()