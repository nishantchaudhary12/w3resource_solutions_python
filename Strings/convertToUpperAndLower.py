#Write a Python script that takes input from the user and displays that input back in upper and lower cases.


def convert_upper(sample_string):
    return sample_string.upper()


def convert_lower(sample_string):
    return sample_string.lower()


def main():
    sample_string = 'w3resource.COM'
    print('Upper case:', convert_upper(sample_string))
    print('Lower case:', convert_lower(sample_string))


main()