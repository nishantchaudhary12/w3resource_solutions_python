#Write a Python program that accepts a string and calculate the number of digits and letters.


def countDigitAndLetters(sampleData):
    digits = 0
    letters = 0
    for each in sampleData:
        if each.isalpha():
            letters += 1
        elif each.isdigit():
            digits += 1
    print('Letters:', letters)
    print('Digits:', digits)


sampleData = 'Python 3.2'
countDigitAndLetters(sampleData)
