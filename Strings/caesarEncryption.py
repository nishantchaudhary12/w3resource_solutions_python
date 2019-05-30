#Write a Python program to create a Caesar encryption.

#using list
'''
def caesar_encp(sample_string, shift):
    new_string = ''
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    for each in sample_string:
        if each.isupper():
            index = uppercase.index(each)
            new_index = (index + shift) % 26
            new_string = new_string + uppercase[new_index]
        else:
            index = lowercase.index(each)
            new_index = (index + shift) % 26
            new_string = new_string + lowercase[new_index]

    return new_string


def main():
    sample_string = 'resource'
    shift = 3
    print(caesar_encp(sample_string, shift))


main()
'''

#using ascii value

def caesar_encp(sample_string, shift):
    new_string = ''
    for i in range(len(sample_string)):
        char = sample_string[i]
        if char.isupper():
            new = (ord(char) - (65 - shift)) % 26 + 65
        else:
            new = (ord(char) - (97 - shift)) % 26 + 97
        new_string = new_string + chr(new)
    return new_string


def main():
    sample_string = 'resource'
    shift = 3
    print(caesar_encp(sample_string, shift))


main()