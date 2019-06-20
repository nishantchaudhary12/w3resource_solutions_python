#Write a Python function to reverses a string if it's length is a multiple of 4.


def reverse_str(sample_string):  #can also use reversed function directly
    new_string = ''
    if len(sample_string) % 4 == 0:
        for each in range(len(sample_string) - 1, -1, -1):
            new_string = new_string + sample_string[each]
    else:
        new_string = sample_string
    return new_string


def main():
    sample_string = 'https://www.w3resource.com//'
    print(reverse_str(sample_string))


main()