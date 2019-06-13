#Write a Python program to get the last part of a string before a specified character.


def last_part(sample_string, character):
    new_string = sample_string.rsplit(character, 1)
    return new_string[0]


def main():
    sample_string = 'https://www.w3resource.com/python-exercises'
    character = '-'
    print(last_part(sample_string, character))


main()