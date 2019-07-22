# Write a Python function to check whether a string is a pangram or not.


def check_pangram(sample_string):
    my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']
    sample_string = sample_string.lower()
    sample_string = {char for char in sample_string if char.isalpha()}
    for each in sample_string:
        if each in my_list:
            my_list.remove(each)
    if not my_list:
        print('Yes')
    else:
        print('No')


def main():
    sample_string = "The quick brown fox jumps over the lazy dog"
    check_pangram(sample_string)


main()