#Write a Python function to get a string made of 4 copies of the last two characters of a specified string
# (length must be at least 2).


def insert_end(sample_string):
    if len(sample_string) > 1:
        return sample_string[-2:] * 4


def main():
    sample_string = 'Python'
    print(insert_end(sample_string))


main()