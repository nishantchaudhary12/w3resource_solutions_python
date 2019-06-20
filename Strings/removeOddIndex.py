#Write a Python program to remove the characters which have odd index values of a given string.


def remove_odd_char(sample_string):
    new_string = ''
    for each in range(0, len(sample_string), 2):
        new_string = new_string + sample_string[each]

    return new_string


def main():
    sample_string = 'w3resource.com'
    print(remove_odd_char(sample_string))


main()