# Write a Python program to remove the nth index character from a nonempty string.


def remove_char(sample_string, n):
    new_string = sample_string
    if n < len(sample_string):
        new_string = sample_string[:n] + sample_string[n+1:]
    else:
        print('Enter proper value for index')

    return new_string


def main():
    sample_string = 'w3resource.com'
    print(remove_char(sample_string, 5))


main()