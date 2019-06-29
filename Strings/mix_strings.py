#Write a Python program to get a single string from two given strings, separated by a space and swap the first two
# characters of each string.


def mix_string(sample_string_1, sample_string_2):
    first_2_str1 = sample_string_2[:2]
    first_2_str2 = sample_string_1[:2]
    new_string = first_2_str1 + sample_string_1[2:] + ' ' + first_2_str2 + sample_string_2[2:]

    return new_string


def main():
    sample_string_1 = 'abc'
    sample_string_2 = 'xyz'
    print(mix_string(sample_string_1,  sample_string_2))


main()