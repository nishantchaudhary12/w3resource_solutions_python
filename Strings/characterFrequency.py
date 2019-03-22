# Write a Python program to count the number of characters (character frequency) in a string.


def check_frequency(sample_string):
    freq_dict = {}
    string_split = list(sample_string)
    for key in string_split:
        if key not in freq_dict.keys():
            freq_dict[key] = 1
        else:
            freq_dict[key] += 1
    print(freq_dict)


def main():
    sample_string = 'google.com'
    check_frequency(sample_string)


main()