#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.


def make_string(sample_string):
    if len(sample_string) > 1:
        new_string = sample_string[0:2]+sample_string[-2:]
    else:
        new_string = ''
    return new_string


def main():
    sample_string = 'w3resource'
    print(make_string(sample_string))


main()