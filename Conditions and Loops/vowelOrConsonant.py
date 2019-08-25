#Write a Python program to check whether an alphabet is a vowel or consonant.


def checkAlphabet(alp):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if alp.isalpha():
        if alp in vowels:
            print('Vowel')
        else:
            print('Consonant')
    else:
        print('Enter an alphabet')


checkAlphabet('a')