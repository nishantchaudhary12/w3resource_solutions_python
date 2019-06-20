#Write a Python program to remove a newline in Python.


def rem_newLine(sample_string):
    return sample_string.rstrip()


def main():
    sample_string = 'w3resource\n'
    print(rem_newLine(sample_string))


main()