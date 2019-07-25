# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a
# hyphen-separated sequence after sorting them alphabetically.


def split_sort_string(sample_string):
    sample_string = sample_string.split('-')
    sample_string = sorted(sample_string)
    print('-'.join(sample_string))


def main():
    sample_string = 'green-red-yellow-black-white'
    split_sort_string(sample_string)


main()