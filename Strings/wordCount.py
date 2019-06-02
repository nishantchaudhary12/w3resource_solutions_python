# Write a Python program to count the occurrences of each word in a given sentence.


def count_occurence(sample_string):
    words = sample_string.split()
    word_count = dict()
    for each in words:
        if each in word_count:
            word_count[each] += 1
        else:
            word_count[each] = 1

    return word_count


def main():
    sample_string = 'the quick brown fox jumps over the lazy dog'
    print('Word count of all the words in the sentence:', count_occurence(sample_string))


main()