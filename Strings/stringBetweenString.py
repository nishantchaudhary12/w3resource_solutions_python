#Write a Python function to insert a string in the middle of a string.


def insert_string_middle(string2, string1):
    half_len_str2 = len(string2)//2
    new_string = string2[:half_len_str2] + string1 + string2[half_len_str2:]
    return new_string


def main():
    string1 = 'Python'
    string2 = '[[]]'
    print(insert_string_middle(string2, string1))


main()