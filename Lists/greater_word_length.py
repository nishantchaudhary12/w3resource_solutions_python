#Write a Python program to find the list of words that are longer than n from a given list of words.


def check(user_inp, n):
    elements = list()
    for item in user_inp:
        if len(item) > n:
            elements.append(item)
    return elements


def main():
    n = 3
    user_inp = ['Matthew', 'John', 'Isaiah', 'Col', 'ABC']
    print('The list of words that have length greater than', n, check(user_inp, n))


main()

