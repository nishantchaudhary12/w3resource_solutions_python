#Write a Python program to sort a string lexicographically.


def lexi_sort(sample_string):
    new_string = sorted(sample_string)
    return new_string


def main():
    sample_string = 'w3resource'
    print(lexi_sort(sample_string))


main()