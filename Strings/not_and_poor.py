#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.


def update_string(sample_string):
    not_index = sample_string.find('not')
    poor_index = sample_string.find('poor')
    if not_index != -1 and poor_index != -1:
        new_string = sample_string[:not_index] + 'good' + sample_string[poor_index+4:]
    else:
        new_string = sample_string
    return new_string


def main():
    sample_string = 'The lyrics is not that poor! The lyrics is poor!'
    print(update_string(sample_string))


main()