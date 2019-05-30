#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
# except the first char itself.

def change_string(sample_string):
    first_char = sample_string[0]
    new_string = first_char
    for each in range(1, len(sample_string)):
        if sample_string[each] == first_char:
            new_string += '$'
        else:
            new_string += sample_string[each]

    return new_string


def main():
    sample_string = 'resource'
    print(change_string(sample_string))   #can also use string.replace to replace the alphabet


main()