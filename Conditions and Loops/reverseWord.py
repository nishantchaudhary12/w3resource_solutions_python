#Write a Python program that accepts a word from the user and reverse it.


def main():
    word = 'w3resource'
    reverse_word = ''
    for each in range(len(word)-1, -1, -1):
        reverse_word += word[each]
    print(reverse_word)


main()
