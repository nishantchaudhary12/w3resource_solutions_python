#Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.


def update_string(sample_string):
    if len(sample_string) > 2:
        end_string = sample_string[-3:]
        if end_string == 'ing':
            new_string = sample_string + 'ly'
        else:
            new_string = sample_string + 'ing'
    else:
        new_string = sample_string

    return new_string


def main():
    sample_string = 'string'
    print(update_string(sample_string))


main()