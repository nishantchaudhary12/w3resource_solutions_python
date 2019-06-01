#Write a Python program to change a given string to a new string where the first and last chars have been exchanged.


def remove_char(sample_string):
    new_string = sample_string[-1] + sample_string[1:-1] + sample_string[0]

    return new_string


def main():
    sample_string = 'w3resource.com'
    print(remove_char(sample_string))


main()