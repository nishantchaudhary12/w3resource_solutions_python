#Write a Python program that accepts a comma separated sequence of words as input and
# prints the unique words in sorted form (alphanumerically).


def get_data(sample_words):
    words = sample_words.split(',')
    for each in range(0, len(words)):
        words[each] = words[each].strip()
    return words


def sort_words(words):
    words = set(words)
    words = list(words)
    words.sort()
    return words


def main():
    sample_words = 'red, white, black, red, green, black'
    words = get_data(sample_words)
    print(sort_words(words))


main()

