#Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters
# in the first 4 characters.


def upper_str(sample_string):
    count = 0
    new_string = ''
    for each in range(0, 4):
        if sample_string[each].isupper():
            count += 1
    if count > 1:
        new_string = sample_string.upper()
    else:
        new_string = sample_string

    return new_string


def main():
    sample_string = 'HTtp://www.w3resource.com'
    print(upper_str(sample_string))


main()