#Write a Python program to check the validity of password input by users.
#Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.


def validation(password):
    smallLetter = False
    capitalLetter = False
    digit = False
    specialChar = False
    if len(password) >= 6 and len(password) <= 16:
        for each in password:
            if each.islower():
                smallLetter = True
            elif each.isupper():
                capitalLetter = True
            elif each.isdigit():
                digit = True
            elif each in ['$', '#', '@']:
                specialChar = True
        if smallLetter and capitalLetter and digit and specialChar:
            print('Valid Password')
        else:
            print('Invalid Password')
    else:
        print('Invalid Password')




password = 'w3@Resource'
validation(password)