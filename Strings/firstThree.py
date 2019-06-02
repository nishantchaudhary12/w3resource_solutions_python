#Write a Python function to get a string made of its first three characters of a specified string.
# If the length of the string is less than 3 then return the original string.


def first_three(sample_string):
    new_string = ''
    if len(sample_string) > 2:
        new_string = sample_string[:3]
    else:
        new_string = sample_string
    return new_string


def main():
    sample_string = 'Python'
    print(first_three(sample_string))


main()