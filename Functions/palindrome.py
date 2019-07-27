# Write a Python function that checks whether a passed string is palindrome or not.


def palindrome(sample_string):
    new_string = ''
    for each in range(len(sample_string) - 1, -1, -1):
        new_string += sample_string[each]
    if new_string == sample_string:
        print('Yes')
    else:
        print('No')

    start = 0
    end = len(sample_string) - 1
    while start < end:
        if sample_string[start] != sample_string[end]:
            print('False')
            break
        start += 1
        end -= 1
    print('True')


def main():
    sample_string = 'abcba'
    palindrome(sample_string)


main()