#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.


def caseCheck(sample_str):
    low_count = 0
    upper_count = 0
    for each in sample_str:
        if each.islower():
            low_count += 1
        elif each.isupper():
            upper_count += 1
    print('Lower case:', low_count, 'Upper case:', upper_count)


def main():
    sample_string = 'The quick Brow Fox'
    caseCheck(sample_string)


main()