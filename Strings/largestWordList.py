#Write a Python function that takes a list of words and returns the length of the longest one.


def get_length(sample_words):
    largest = 0
    for each in sample_words:
        if len(each) > largest:
            largest = len(each)

    return largest


def main():
    sample_words = ['abc', 'abcba', 'aaa', 'abcd']
    print('Length of the largest word in the list:', get_length(sample_words))


main()