#Write a Python program to display formatted text (width=50) as output.


import textwrap


def main():
    sample_string = 'w3resource.com'
    print(textwrap.fill(sample_string, 50))


main()