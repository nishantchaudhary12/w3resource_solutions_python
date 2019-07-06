#Write a Python program to convert a tuple to a string.


def main():
    x = ('w', '3', 'r', 'e', 's', 'o', 'u', 'r', 'c', 'e')
    result = ('').join(x)
    print(result)


main()